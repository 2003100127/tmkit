__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2022"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import sys
import warnings
sys.path.append('../../')
import pandas as pd
from Bio.PDB import *
from Bio import BiopythonWarning
from tmkit.topology.pdbtm.TMH import tmh as tmhseg
from tmkit.sequence.Fasta import fasta as sfasta
from tmkit.util.Kit import chainid
from tmkit.util.Reader import reader
from tmkit.util.Writer import writer
from tmkit.base import PDB
from tmkit.util.Console import console


class workbench():

    def __init__(
            self,
            df_prot,
            pdb_cplx_fp,
            fasta_fp,
            xml_fp=None,
            sv_fp=None,
            verbose=True,
    ):
        self.df_prot = df_prot
        self.pdb_cplx_fp = pdb_cplx_fp
        self.fasta_fp = fasta_fp
        self.xml_fp = xml_fp
        self.sv_fp = sv_fp

        self.parser = PDBParser()
        self.reader = reader()
        self.writer = writer()
        self.console = console()

        self.num_pc = self.df_prot.shape[0]

        self.df_prot_uniq = pd.DataFrame(pd.unique(self.df_prot['prot']), columns=['prot'])
        # print(self.df_prot_uniq)

        self.console.verbose = verbose

    def template(
            self,
            metric,
    ):
        """

        Parameters
        ----------
        metric

        Returns
        -------

        """
        fail_list = []
        fail_count = 0
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', BiopythonWarning)
            for i in range(self.num_pc):
                prot_name = self.df_prot.loc[i, 'prot']
                seq_chain = self.df_prot.loc[i, 'chain']
                try:
                    if metric == 'rez' or metric == 'met':
                        prot_name_pre = self.df_prot.loc[i - 1 if i > 0 else i, 'prot']
                        if i > 0 and prot_name_pre == prot_name:
                            self.df_prot.loc[i, 'rez'] = self.df_prot.loc[i-1, 'rez']
                        else:
                            struct = PDB.structure(
                                pdb_fp=self.pdb_cplx_fp,
                                prot_name=prot_name,
                                seq_chain=seq_chain,
                                file_chain='',
                            )
                            if metric == 'rez':
                                self.df_prot.loc[i, metric] = struct.rez
                            elif metric == 'met':
                                self.df_prot.loc[i, metric] = struct.met
                    else:
                        if metric == 'bio_name':
                            struct = PDB.structure(
                                pdb_fp=self.pdb_cplx_fp,
                                prot_name=prot_name,
                                seq_chain=seq_chain,
                                file_chain='',
                            )
                            self.df_prot.loc[i, metric] = struct.name
                        elif metric == 'head':
                            struct = PDB.structure(
                                pdb_fp=self.pdb_cplx_fp,
                                prot_name=prot_name,
                                seq_chain=seq_chain,
                                file_chain='',
                            )
                            self.df_prot.loc[i, metric] = struct.head
                        # elif metric == 'psi_phi':
                        #     self.df_prot.loc[i, metric] = struct.psi_phi
                        elif metric == 'desc':
                            for line in open(self.pdb_cplx_fp + prot_name + '.pdb'):
                                list = line.split()
                                id = list[0]
                                if id == 'HEADER':
                                    self.df_prot.loc[i, metric] = ' '.join(list[1:-2])
                        elif metric == 'mthm':
                            tmh_beg, tmh_last = tmhseg(
                                xml_fp=self.xml_fp,
                                prot_name=prot_name,
                                seq_chain=seq_chain,
                            ).get()
                            self.df_prot.loc[i, metric] = len(tmh_beg)
                        elif metric == 'seq':
                            seq = sfasta().get(
                                fasta_fpn=self.fasta_fp + prot_name + chainid(seq_chain) + '.fasta'
                            )
                            self.df_prot.loc[i, metric + '_aa'] = seq
                            self.df_prot.loc[i, metric + '_len'] = len(seq)

                    self.console.print('=========>protein {} chain {} with {} {}'.format(
                        self.df_prot.loc[i, 'prot'],
                        self.df_prot.loc[i, 'chain'],
                        metric,
                        self.df_prot.loc[i, metric],
                    ))
                except:
                    self.console.print('=========>File failed: {} {}'.format(
                        self.df_prot.loc[i, 'prot'],
                        self.df_prot.loc[i, 'chain'],
                    ))
                    fail_list.append([self.df_prot.loc[i, 'prot'], self.df_prot.loc[i, 'chain']])
                    fail_count = fail_count + 1
                    continue
        self.console.print('======>{} extraction items failed using {}.'.format(fail_count, metric))
        self.writer.generic(df=self.df_prot, sv_fpn=self.sv_fp + 'wb_' + metric + '_c.txt')
        return self.df_prot

    def integrate(self, metrics):
        """

        Parameters
        ----------
        metrics

        Returns
        -------

        """
        self.df_prot['prot_mark'] = self.df_prot['prot'] + self.df_prot['chain']
        for i, metric in enumerate(metrics):
            self.console.print('======>metric: {}'.format(metric))
            self.template(metric=metric)
        # self.writer.generic(df=self.df_prot, sv_fpn=self.sv_fp + 'wb_integrate.txt', header=True,)
        self.writer.excel(
            df=self.df_prot,
            sv_fpn=self.sv_fp + 'integrate.xlsx',
            sheet_name='Sheet1',
            header=True,
            index=False
        )
        return self.df_prot


if __name__ == "__main__":
    from tmkit.Path import to

    DEFINE = {
        'list_fpn': to('data/example/pdb/indepdata/prot_n30.txt'),
        'pdb_cplx_fp': to('data/example/pdb/indepdata/pdbtm/'),
        'fasta_fp': to('data/example/fasta/indepdata/'),
        'xml_fp': to('data/example/xml/indepdata/'),
        'sv_fp': to('data/example/pdb/indepdata/'),
    }

    df_prot = reader().generic(DEFINE['list_fpn'])
    df_prot = df_prot.rename(columns={
        0: 'prot',
        1: 'chain',
    })

    p = workbench(
        df_prot=df_prot,
        pdb_cplx_fp=DEFINE['pdb_cplx_fp'],
        fasta_fp=DEFINE['fasta_fp'],
        xml_fp=DEFINE['xml_fp'],
        sv_fp=DEFINE['sv_fp']
    )

    # print(p.template(
    #     # metric='rez',
    #     # metric='met',
    #     # metric='bio_name',
    #     # metric='head',
    #     # metric='desc',
    #     # metric='mthm',
    #     metric='seq',
    # ))

    print(p.integrate(
        metrics=['rez', 'met', 'bio_name', 'head', 'mthm', 'seq']
    ))