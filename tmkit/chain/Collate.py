__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2022"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import sys
import warnings
import pandas as pd
sys.path.append('../../')
from tmkit.Path import to
from tmkit.sequence.PDB import pdb as spdb
from tmkit.chain.PDB import pdb as cpdb
from tmkit.util.Kit import seqchainid
from Bio import BiopythonWarning
from tmkit.util.Console import console


class collate(object):

    def __init__(
            self,
            prot_name,
            chain_focus,
            pdb_pdbtm_fp,
            pdb_rcsb_fp,
            verbose=True,
    ):
        self.prot_name = prot_name
        self.chain_focus = chain_focus
        self.pdb_pdbtm_fp = pdb_pdbtm_fp
        self.pdb_rcsb_fp = pdb_rcsb_fp

        self.chains_pdbtm = cpdb(
            pdb_fp=self.pdb_pdbtm_fp,
            prot_name=self.prot_name,
        ).chains()

        self.chains_rcsb = cpdb(
            pdb_fp=self.pdb_rcsb_fp,
            prot_name=self.prot_name,
        ).chains()

        self.df = pd.DataFrame(
            [[self.prot_name, self.chain_focus, ''.join(self.chains_pdbtm), ''.join(self.chains_rcsb)]],
            columns=['prot_name', 'chain', 'pdbtm_chains', 'rcsb_chains'],
        )

        if self.chain_focus not in self.chains_rcsb:
            self.df['source'] = 'pdbtm_tr'
        else:
            self.df['source'] = 'rcsb'

        self.df['diff'] = ''.join(list(set(self.chains_pdbtm).difference(set(self.chains_rcsb))))
        self.df['same'] = ''.join(list(set(self.chains_pdbtm).intersection(set(self.chains_rcsb))))

        self.console = console()
        self.console.verbose = verbose

        self.console.print('======>basic info: \n{}'.format(self.df))

    def throwback(self, symbol):
        """

        Notes
        -----
            throw_backs is a dict with keys being the collated protein chains
            corresponding to the chains in RCSB mapped from PDBTM, with the
            values 'untransformed' or 'collated' being whether protein chains
             are untransformed or collated, respectively.

        Parameters
        ----------
        prot_df
        prot_collated_df
        pdb_chain_path
        symbol

        Returns
        -------
            dict - throw_backs

        """
        throw_backs = {}
        if self.df.loc[0, 'source'] == 'rcsb':
            throw_backs[self.prot_name + symbol + self.chain_focus] = 'untransformed'
        else:
            pdbtm_to_rcsb_dict = self.isSameSeq(symbol=symbol)
            if len([*pdbtm_to_rcsb_dict.values()]) > 0:
                self.console.print('======>master is collated: {} '.format([*pdbtm_to_rcsb_dict.values()][0]))
                throw_backs[self.prot_name + symbol + self.chain_focus] = [*pdbtm_to_rcsb_dict.values()][0]
            else:
                throw_backs[self.prot_name + symbol + self.chain_focus] = 'transformed & uncollated'
        return throw_backs

    def isSameSeq(self, symbol='.'):
        """

        Parameters
        ----------
        symbol

        Returns
        -------

        """
        pdbtm_to_rcsb_dict = {}

        with warnings.catch_warnings():
            warnings.simplefilter('ignore', BiopythonWarning)

            pdbtm_to_rcsb_dict[self.prot_name + symbol + self.chain_focus] = []

            seq_pdbtm = spdb(
                pdb_fp=self.pdb_pdbtm_fp,
                prot_name=self.prot_name,
                seq_chain=self.chain_focus,
                file_chain='',
            ).chain()

            for chain_rcsb in self.chains_rcsb:
                seq_rcsb = spdb(
                    pdb_fp=self.pdb_rcsb_fp,
                    prot_name=self.prot_name,
                    seq_chain=seqchainid(chain_rcsb),
                    file_chain='',
                ).chain()
                if seq_pdbtm == seq_rcsb:
                    self.console.print('=========>{}.{} in PDBTM corresponds to {}.{} in RCSB.'.format(
                        self.prot_name, self.chain_focus, self.prot_name, chain_rcsb)
                    )
                    pdbtm_to_rcsb_dict[self.prot_name + symbol + self.chain_focus].append(
                        self.prot_name + symbol + chain_rcsb
                    )
        return pdbtm_to_rcsb_dict


if __name__ == "__main__":
    from tmkit.util.Reader import reader

    DEFINE = {
        'pdb_rcsb_fp': to('data/example/pdb/indepdata/rcsb/'),
        'pdb_pdbtm_fp': to('data/example/pdb/indepdata/pdbtm/'),
        'prot_fpn': to('data/example/pdb/indepdata/prot_n30.txt'),
        'prot_pdbtm_fpn': to('data/example/pdb/indepdata/prot_n30_complex_pdbtm_full.txt'),
        'prot_rcsb_fpn': to('data/example/pdb/indepdata/prot_n30_complex_rcsb_full.txt'),
    }

    prot_df = reader().generic(DEFINE['prot_fpn'])
    prot_pdbtm_df = reader().generic(DEFINE['prot_pdbtm_fpn'])
    prot_rcsb_df = reader().generic(DEFINE['prot_rcsb_fpn'])

    p = collate(
        prot_name='3pux',
        chain_focus='G',
        pdb_rcsb_fp=DEFINE['pdb_rcsb_fp'],
        pdb_pdbtm_fp=DEFINE['pdb_pdbtm_fp'],
    )

    print(p.throwback(symbol='.'))