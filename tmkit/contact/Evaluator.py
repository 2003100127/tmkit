__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import numpy as np
import pandas as pd
from sklearn import metrics
from tmkit.contact.Reader import reader as rrcreader


class evaluator:

    def __init__(
            self,
            prot_name,
            file_chain,
            dist_df,
            pair_list,
            dist_limit=None,
            tool=None,
            tool_fp=None,
            sort_=None,
            seq_sep_inferior=None,
            seq_sep_superior=None,
    ):
        self.tool_fp = tool_fp
        self.prot_name = prot_name
        self.file_chain = file_chain
        self.dist_limit = dist_limit
        self.pair_list = pair_list
        self.tool = tool
        self.sort_ = sort_
        self.seq_sep_inferior = seq_sep_inferior
        self.seq_sep_superior = seq_sep_superior
        self.rrcreader = rrcreader(
            seq_sep_inferior=self.seq_sep_inferior,
            seq_sep_superior=self.seq_sep_superior
        )
        self.dist_df = dist_df
        self.dist_df.columns = [
            'fasta_id_1',
            'aa_1',
            'pdb_id_1',
            'fasta_id_2',
            'aa_2',
            'pdb_id_2',
            'dist',
            'is_contact'
        ]
        self.row_real_dist = self.dist_df.shape[0]

        print('======>Evaluating protein {}'.format(prot_name + file_chain))

    def fetch(self):
        switch = {
            'psicov': self.psicov,
            'freecontact': self.freecontact,
            'ccmpred': self.ccmpred,
            'gremlin': self.gremlin,
            'gdca': self.gdca,
            'plmc': self.plmc,
            'memconp':self.memconp,
            'membrain2':self.membrain2,
            'tma165': self.tma165,
        }
        return switch[self.tool]()

    def compare(self, target, cut_off):
        # #/*** block fetch target results ***/
        res_sorted = target.sort_values(['score'], ascending=False)
        # self.pfwwriter.generic(res_sorted, sv_fpn='./cheers')
        res_cutoff = res_sorted.iloc[0:cut_off, :]
        new_index = np.arange(res_cutoff.shape[0])
        res_cutoff = res_cutoff.set_index(new_index, inplace=False, drop=True)
        # print(res_cutoff)
        row_cutoff = res_cutoff.shape[0]
        row_offset = target.shape[0] - row_cutoff
        # #/*** block y_true_cutoff ***/
        y_true_cutoff = []
        for i in range(row_cutoff):
            conid1 = self.dist_df['fasta_id_1'] == res_cutoff['fasta_id_1'][i]
            conid2 = self.dist_df['fasta_id_2'] == res_cutoff['fasta_id_2'][i]
            juery = (conid1) & (conid2)
            tmp = self.dist_df.loc[juery]
            y_true_cutoff.append(tmp['is_contact'].sum())
        # #/*** block y_true_all ***/
        y_true_all = list(res_sorted['is_contact'])
        # #/*** block y_pred_all ***/
        y_pred_all = list(
            np.concatenate(
                [np.zeros([row_cutoff]) + 1, np.zeros([row_offset])],
                axis=0
            ).astype(np.int64)
        )
        # #/*** block precision ***/
        precision = metrics.precision_score(y_true=y_true_all, y_pred=y_pred_all)
        print('=========>precision: {}'.format(precision))
        # #/*** block recall ***/
        recall = metrics.recall_score(y_true=y_true_all, y_pred=y_pred_all)
        print('=========>recall: {}'.format(recall))
        # #/*** block mcc ***/
        mcc = metrics.matthews_corrcoef(y_true=y_true_all, y_pred=y_pred_all)
        print('=========>mcc: {}'.format(mcc))
        # #/*** block f1score ***/
        f1score = metrics.f1_score(y_true=y_true_all, y_pred=y_pred_all)
        print('=========>f1score: {}'.format(f1score))
        # #/*** block accuracy ***/
        accuracy = metrics.accuracy_score(y_true=y_true_all, y_pred=y_pred_all)
        print('=========>accuracy: {}'.format(accuracy))
        metrics_summary = {
            'precision': precision,
            'recall': recall,
            'f1score': f1score,
            'mcc': mcc,
            'accuracy': accuracy,
        }
        return metrics_summary

    def psicov(self):
        pcv_dist, chain_dist_all = self.rrcreader.psicov(
            pcv_path=self.tool_fp,
            file_name=self.prot_name,
            file_chain=self.file_chain,
            pair_list=self.pair_list,
            dist_df=self.dist_df,
            sort_=self.sort_
        )
        return pd.concat([pcv_dist, chain_dist_all], axis=1)

    def freecontact(self):
        fc_dist, chain_dist_all = self.rrcreader.freecontact(
            fc_path=self.tool_fp,
            file_name=self.prot_name,
            file_chain=self.file_chain,
            pair_list=self.pair_list,
            dist_df=self.dist_df,
            sort_=self.sort_
        )
        return pd.concat([fc_dist, chain_dist_all], axis=1)

    def ccmpred(self):
        cp_dist, chain_dist_all = self.rrcreader.ccmpred(
            cp_path=self.tool_fp,
            file_name=self.prot_name,
            file_chain=self.file_chain,
            pair_list=self.pair_list,
            dist_df=self.dist_df,
            sort_=self.sort_
        )
        return pd.concat([cp_dist, chain_dist_all], axis=1)

    def gremlin(self):
        gl_dist, chain_dist_all = self.rrcreader.gremlin(
            gl_path=self.tool_fp,
            file_name=self.prot_name,
            file_chain=self.file_chain,
            pair_list=self.pair_list,
            dist_df=self.dist_df,
            sort_=self.sort_
        )
        return pd.concat([gl_dist, chain_dist_all], axis=1)

    def gdca(self):
        gdca_dist, chain_dist_all = self.rrcreader.gdca(
            gdca_path=self.tool_fp,
            file_name=self.prot_name,
            file_chain=self.file_chain,
            pair_list=self.pair_list,
            dist_df=self.dist_df,
            sort_=self.sort_
        )
        return pd.concat([gdca_dist, chain_dist_all], axis=1)

    def plmc(self):
        plmc_dist, chain_dist_all = self.rrcreader.plmc(
            plmc_path=self.tool_fp,
            file_name=self.prot_name,
            file_chain=self.file_chain,
            pair_list=self.pair_list,
            dist_df=self.dist_df,
            sort_=self.sort_
        )
        return pd.concat([plmc_dist, chain_dist_all], axis=1)

    def memconp(self):
        memconp_dist, chain_dist_all = self.rrcreader.memconp(
            mcp_path=self.tool_fp,
            file_name=self.prot_name,
            file_chain=self.file_chain,
            pair_list=self.pair_list,
            dist_df=self.dist_df,
            sort_=self.sort_
        )
        return pd.concat([memconp_dist, chain_dist_all], axis=1)

    def membrain2(self):
        membrain2_dist, chain_dist_all = self.rrcreader.membrain2(
            mb_path=self.tool_fp,
            file_name=self.prot_name,
            file_chain=self.file_chain,
            pair_list=self.pair_list,
            dist_df=self.dist_df,
            sort_=self.sort_
        )
        return pd.concat([membrain2_dist, chain_dist_all], axis=1)

    def tma165(self):
        tma165_dist, chain_dist_all = self.rrcreader.tma165(
            tma165_path=self.tool_fp,
            file_name=self.prot_name,
            file_chain=self.file_chain,
            pair_list=self.pair_list,
            dist_df=self.dist_df,
            sort_=self.sort_
        )
        return pd.concat([tma165_dist, chain_dist_all], axis=1)