__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import Dict, List, Union

import warnings

import pandas as pd
from Bio import BiopythonWarning

from tmkit.chain.PDB import PDB as cpdb
from tmkit.sequence.PDB import PDB as spdb
from tmkit.util.Kit import seqchainid


class Collate:
    def __init__(
        self,
        prot_name: str,
        chain_focus: str,
        pdb_pdbtm_fp: str,
        pdb_rcsb_fp: str,
    ) -> None:
        """
        Collate chains between PDBTM and RCSB.

        Parameters
        ----------
        prot_name : str
            Name of a protein in the prefix of a PDB file name (e.g., 1xqf in 1xqfA.pdb).
        chain_focus : str
            Chain of a protein in the prefix of a PDB file name (e.g., A in 1xqfA.pdb)..
        pdb_rcsb_fp : str
            Path where protein complexes from RCSB are placed.
        pdb_pdbtm_fp: str
            Path where protein complexes from PDBTM are placed.
        """
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
            [
                [
                    self.prot_name,
                    self.chain_focus,
                    "".join(self.chains_pdbtm),
                    "".join(self.chains_rcsb),
                ]
            ],
            columns=["prot_name", "chain", "pdbtm_chains", "rcsb_chains"],
        )

        if self.chain_focus not in self.chains_rcsb:
            self.df["source"] = "pdbtm_tr"
        else:
            self.df["source"] = "rcsb"

        self.df["diff"] = "".join(
            list(set(self.chains_pdbtm).difference(set(self.chains_rcsb)))
        )
        self.df["same"] = "".join(
            list(set(self.chains_pdbtm).intersection(set(self.chains_rcsb)))
        )

        print(f"======>basic info: \n{self.df}")

    def throwback(self, symbol: str) -> Dict[str, Union[str, List[str]]]:
        """
        Return a dict with keys being the collated protein chains
        corresponding to the chains in RCSB mapped from PDBTM, with the
        values 'untransformed' or 'collated' being whether protein chains
         are untransformed or collated, respectively.

        Parameters
        ----------
        symbol : str
            The symbol to use for missing residues, by default "."

        Returns
        -------
        Dict[str, Union[str, List[str]]]
            The collated dictionary: protein name -> 'transformed' or 'untransformed' (can be a list).
        """
        throw_backs = {}
        if self.df.loc[0, "source"] == "rcsb":
            throw_backs[self.prot_name + symbol + self.chain_focus] = "untransformed"
        else:
            pdbtm_to_rcsb_dict = self.is_same_seq(symbol=symbol)
            if len([*pdbtm_to_rcsb_dict.values()]) > 0:
                print(
                    "======>master is collated: {} ".format(
                        [*pdbtm_to_rcsb_dict.values()][0]
                    )
                )
                throw_backs[self.prot_name + symbol + self.chain_focus] = [
                    *pdbtm_to_rcsb_dict.values()
                ][0]
            else:
                throw_backs[
                    self.prot_name + symbol + self.chain_focus
                ] = "transformed & uncollated"
        return throw_backs

    def is_same_seq(self, symbol: str) -> Dict[str, List[str]]:
        """
        Check if sequences are the same.

        Parameters
        ----------
        symbol : str
            The symbol to use for missing residues, by default "."

        Returns
        -------
        Dict[str, List[str]]
            Dictionary of PDBTM to RCSB mappings.
        """
        pdbtm_to_rcsb_dict = {}

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", BiopythonWarning)

            pdbtm_to_rcsb_dict[self.prot_name + symbol + self.chain_focus] = []

            seq_pdbtm = spdb(
                pdb_fp=self.pdb_pdbtm_fp,
                prot_name=self.prot_name,
                seq_chain=self.chain_focus,
                file_chain="",
            ).chain()

            for chain_rcsb in self.chains_rcsb:
                seq_rcsb = spdb(
                    pdb_fp=self.pdb_rcsb_fp,
                    prot_name=self.prot_name,
                    seq_chain=seqchainid(chain_rcsb),
                    file_chain="",
                ).chain()
                if seq_pdbtm == seq_rcsb:
                    print(
                        "=========>{}.{} in PDBTM corresponds to {}.{} in RCSB.".format(
                            self.prot_name, self.chain_focus, self.prot_name, chain_rcsb
                        )
                    )
                    pdbtm_to_rcsb_dict[
                        self.prot_name + symbol + self.chain_focus
                    ].append(self.prot_name + symbol + chain_rcsb)
        return pdbtm_to_rcsb_dict
