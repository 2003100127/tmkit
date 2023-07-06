__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import numpy as np
import pandas as pd
from tmkit.db.Reader import reader as ppireader
from tmkit.structure.PDB import pdb as spdb
from tmkit.structure.ppi.Label import label as dlable
from tmkit.util.Kit import chainid, seqchainid
from tmkit.util.Kit import tactic8
from tmkit.util.Kit import create
from tmkit.util.Writer import writer


class labelling:

    def __init__(
            self,
            tool,
            prot_name,
            prot_chain,
            pdb_fp,
            isite_fp,
            sv_fp,
    ):
        self.writer = writer()
        self.ppireader = ppireader()
        self.tool = tool
        self.prot_name = prot_name
        self.prot_chain = prot_chain
        self.pdb_fp = pdb_fp
        self.isite_fp = isite_fp
        self.sv_fp = sv_fp

        self.seq_chain = seqchainid(prot_chain)
        self.file_chain = chainid(prot_chain)
        self.pdb_file = spdb(
            pdb_fp=pdb_fp,
            prot_name=prot_name,
            file_chain=self.file_chain,
            seq_chain=self.seq_chain,
        ).read()['ATOM']
        print(self.pdb_file.columns)

        self.pdb_ids = pd.unique(self.pdb_file['residue_number']).tolist()

        self.isite_pred = self.fetch()(
            isite_fp,
            prot_name,
            self.file_chain,
            sort_=0,
        ).rename(columns={
            'interact_id': 'fasta_id',
            'score': 'probability',
        })

        create(
            DIRECTORY=self.sv_fp,
            mode='dir',
        )

    def fetch(self, ):
        switch = {
            'mbpred': self.ppireader.mbpred,
            'delphi': self.ppireader.delphi,
            'deeptminter': self.ppireader.tma300,
            'graphppis': self.ppireader.graphppis,
        }
        return switch[self.tool]

    def format(self, ):
        pdb_on_use = self.pdb_file[[
            'chain_id',
            'residue_name',
            'residue_number',
            'atom_name',
        ]]
        # print(pdb_on_use)
        pdb_ids = pd.unique(pdb_on_use['residue_number'])
        # print(pdb_ids)
        self.isite_pred = self.fetch()(
            self.isite_fp,
            self.prot_name,
            self.file_chain,
            sort_=0,
        ).rename(columns={
            'interact_id': 'fasta_id',
            'score': 'probability',
        })
        fas_ids = self.isite_pred['fasta_id'].astype(np.int).values
        probs = self.isite_pred['probability'].values
        pdb_fas_map = tactic8(pdb_ids, fas_ids)
        fas_prob_map = tactic8(fas_ids, probs)
        # print(pdb_fas_map)
        # print(fas_prob_map)
        pdb_on_use['probability'] = -1
        # print(pdb_on_use)
        for i in pdb_on_use.index:
            pdb_id = pdb_on_use.loc[i, 'residue_number']
            # print(pdb_id)
            fas_id = pdb_fas_map[pdb_id]
            pdb_on_use.loc[i, 'probability'] = fas_prob_map[fas_id]
        # print(pdb_on_use)
        self.writer.generic(
            df=pdb_on_use,
            df_sep=' ',
            sv_fpn=self.sv_fp
        )
        return

    def probs(self, ):
        df = pd.concat([
                pd.DataFrame(self.pdb_ids),
                self.isite_pred['probability']
            ], axis=1)
        self.writer.generic(
            df=df,
            df_sep='\t',
            sv_fpn=self.sv_fp + 'probs_bf.txt'
        )
        return df

    def predictedLabels(self, dist_fp):
        self.isite_pred['is_interaction'] = -1
        ni_ids = self.isite_pred.loc[self.isite_pred['probability'] < 0.5].index
        i_ids = self.isite_pred.loc[self.isite_pred['probability'] >= 0.5].index
        self.isite_pred['is_interaction'].loc[ni_ids] = 0
        self.isite_pred['is_interaction'].loc[i_ids] = 1
        from sklearn import metrics
        dist_df = dlable(
            dist_path=dist_fp,
            prot_name=self.prot_name,
            file_chain=self.file_chain,
            cutoff=6
        ).attach()
        print(dist_df)
        print(self.isite_pred)
        print(metrics.accuracy_score(dist_df['is_contact'].values, np.rint(self.isite_pred['probability'].values)))
        print(metrics.average_precision_score(dist_df['is_contact'].values, np.rint(self.isite_pred['probability'].values)))
        df = pd.concat([
                pd.DataFrame(self.pdb_ids),
                self.isite_pred['is_interaction'],
            ], axis=1)
        self.writer.generic(
            df=df,
            df_sep='\t',
            sv_fpn=self.sv_fp + 'predicted_label_bf.txt'
        )
        return df

    def actualLabels(
            self,
            dist_fp,
    ):
        dist_df = dlable(
            dist_path=dist_fp,
            prot_name=self.prot_name,
            file_chain=self.file_chain,
            cutoff=6
        ).attach()
        create(
            DIRECTORY=self.sv_fp,
            mode='dir'
        )
        df = pd.concat([pd.DataFrame(self.pdb_ids), dist_df['is_contact']], axis=1)
        self.writer.generic(
            df=df,
            df_sep='\t',
            sv_fpn=self.sv_fp + 'actual_label_bf.txt'
        )
        return df