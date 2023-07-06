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

from tmkit.sequence.PDB import PDB as spdb
from tmkit.util.Kit import seqchainid, tactic5


class CollateBatch:
    """
    Class for collating protein data from PDBTM and RCSB databases.

    Parameters
    ----------
    prot_df : pd.DataFrame
        DataFrame containing protein data.
    pdb_rcsb_fp : str
        Filepath for RCSB PDB file.
    pdb_pdbtm_fp : str
        Filepath for PDBTM PDB file.
    prot_pdbtm_df : pd.DataFrame
        DataFrame containing PDBTM protein data.
    prot_rcsb_df : pd.DataFrame
        DataFrame containing RCSB protein data.
    strategy : str, optional
        Strategy for collating data. Default is "diff".

    Attributes
    ----------
    prot_df : pd.DataFrame
        DataFrame containing protein data.
    pdb_rcsb_fp : str
        Filepath for RCSB PDB file.
    pdb_pdbtm_fp : str
        Filepath for PDBTM PDB file.
    prot_collated_df : pd.DataFrame
        DataFrame containing collated protein data.
    """

    def __init__(
        self,
        prot_df: pd.DataFrame,
        pdb_rcsb_fp: str,
        pdb_pdbtm_fp: str,
        prot_pdbtm_df: pd.DataFrame,
        prot_rcsb_df: pd.DataFrame,
        strategy: str = "diff",
    ) -> None:
        self.prot_df = prot_df
        self.pdb_rcsb_fp = pdb_rcsb_fp
        self.pdb_pdbtm_fp = pdb_pdbtm_fp

        self.prot_collated_df = self.rcsb(
            prot_pdbtm_df=prot_pdbtm_df,
            prot_rcsb_df=prot_rcsb_df,
            strategy=strategy,
        )

        print(f"======>basic info: \n{self.prot_collated_df}")

    def rcsb(
        self, prot_pdbtm_df: pd.DataFrame, prot_rcsb_df: pd.DataFrame, strategy: str
    ) -> pd.DataFrame:
        """
        Collates protein data from PDBTM and RCSB databases.

        Notes
        -----
            It contains 6 columns:
                1> 0
                2> 1
                3> pdbtm
                4> rcsb
                5> diff
                6> source

            The protein chain composed of col 0 and 1 comes from a complex
            containing chains in cols 'pdbtm' and 'rcsb'.

            The different chains are stored in col 'diff'.

            The column 'source' means whether a chain(s) in PDBTM exists in
            the chains in RCSB, which means if this chain(s) in PDBTM
            is transformed using the BIOMAT 350 records.

            If strategy='diff' is selected and values in column 'source' are
            shown 'rcsb', which means all chains of a self.prot_df in PDBTM
            can be found in RCSB.

            strategy_dict stores the same or different chains between PDBTM and RCSB.

        Parameters
        ----------
        prot_pdbtm_df : pd.DataFrame
            DataFrame containing PDBTM protein data.
        prot_rcsb_df : pd.DataFrame
            DataFrame containing RCSB protein data.
        strategy : str
            Strategy for collating data.

        Returns
        -------
        pd.DataFrame
            DataFrame containing collated protein data.
        """
        prot_pdbtm_dict: Dict[str, List[str]] = tactic5(prot_pdbtm_df.values)
        prot_rcsb_dict: Dict[str, List[str]] = tactic5(prot_rcsb_df.values)
        strategy_dict: Dict[str, List[str]] = {}
        for prot_name in prot_pdbtm_dict.keys():
            A = prot_pdbtm_dict[prot_name]
            B = prot_rcsb_dict[prot_name]
            if strategy == "diff":
                strategy_dict[prot_name] = list(set(A).difference(set(B)))
            else:
                strategy_dict[prot_name] = list(set(A).intersection(set(B)))
        self.prot_df["pdbtm"] = "NaN"
        self.prot_df["rcsb"] = "NaN"
        if strategy == "diff":
            self.prot_df["diff"] = "NaN"
        else:
            self.prot_df["same"] = "NaN"
        self.prot_df["source"] = "NaN"
        # print(strategy_dict)
        for i in self.prot_df.index:
            self.prot_df.loc[i, "pdbtm"] = "".join(
                prot_pdbtm_dict[self.prot_df.iloc[i, 0]]
            )
            self.prot_df.loc[i, "rcsb"] = "".join(
                prot_rcsb_dict[self.prot_df.iloc[i, 0]]
            )
            if strategy == "diff":
                self.prot_df.loc[i, "diff"] = "".join(
                    strategy_dict[self.prot_df.iloc[i, 0]]
                )
            else:
                self.prot_df.loc[i, "same"] = "".join(
                    strategy_dict[self.prot_df.iloc[i, 0]]
                )
            if self.prot_df.iloc[i, 1] not in prot_rcsb_dict[self.prot_df.iloc[i, 0]]:
                self.prot_df.loc[i, "source"] = "pdbtm"
            else:
                self.prot_df.loc[i, "source"] = "rcsb"
        # print(self.prot_df)
        return self.prot_df

    def throwback(
        self, prot_collated_df: pd.DataFrame, symbol: str = "."
    ) -> Dict[str, str]:
        """
        Throws back collated protein data.

        Notes
        -----
            throw_backs is a dict with keys being the collated protein chains
            corresponding to the chains in RCSB mapped from PDBTM, with the
            values 'untransformed' or 'collated' being whether protein chains
            are untransformed or collated, respectively.

        Parameters
        ----------
        prot_collated_df : pd.DataFrame
            DataFrame containing collated protein data.
        symbol : str, optional
            Symbol to use for chain ID. Default is ".".

        Returns
        -------
        Dict[str, str]
            Dictionary containing throwback data.
        """
        throw_backs: Dict[str, str] = {}
        for id in self.prot_df.index:
            prot_name = self.prot_df.loc[id, 0]
            prot_chain = self.prot_df.loc[id, 1]
            if prot_collated_df.loc[id, "source"] == "rcsb":
                throw_backs[prot_name + symbol + prot_chain] = "untransformed"
            else:
                chain_collated_dict = self.are_same_seqs(
                    prot_name=prot_name,
                    chain_to_be_collated=[prot_chain],
                    rcsb_chains=list(prot_collated_df["rcsb"][id]),
                    symbol=".",
                )
                if len([*chain_collated_dict.values()]) > 0:
                    print(
                        "======>master is collated: {} ".format(
                            [*chain_collated_dict.values()][0]
                        )
                    )
                    throw_backs[[*chain_collated_dict.values()][0]] = "collated"
                else:
                    throw_backs[[*chain_collated_dict]] = "transformed"
        return throw_backs

    def are_same_seqs(
        self,
        prot_name: str,
        chain_to_be_collated: List[str],
        rcsb_chains: List[str],
        symbol: str = ".",
    ) -> Dict[str, List[str]]:
        """
        Checks if protein sequences are the same.

        Parameters
        ----------
        prot_name : str
            Name of protein.
        chain_to_be_collated : List[str]
            List of chains to be collated.
        rcsb_chains : List[str]
            List of RCSB chains.
        symbol : str, optional
            Symbol to use for chain ID. Default is ".".

        Returns
        -------
        Dict[str, List[str]]
            Dictionary containing chain collation data.
        """
        chain_collated_dict: Dict[str, List[str]] = {}
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", BiopythonWarning)
            for chain_pdbtm in chain_to_be_collated:
                chain_collated_dict[prot_name + symbol + seqchainid(chain_pdbtm)] = []
                seq_pdbtm = spdb(
                    pdb_fp=self.pdb_pdbtm_fp,
                    prot_name=prot_name,
                    seq_chain=seqchainid(chain_pdbtm),
                    file_chain="",
                ).chain()
                for chain_rcsb in rcsb_chains:
                    seq_rcsb = spdb(
                        pdb_fp=self.pdb_rcsb_fp,
                        prot_name=prot_name,
                        seq_chain=seqchainid(chain_rcsb),
                        file_chain="",
                    ).chain()
                    if seq_pdbtm == seq_rcsb:
                        print(
                            "=========>{}.{} in PDBTM corresponds to {}.{} in RCSB.".format(
                                prot_name,
                                seqchainid(chain_pdbtm),
                                prot_name,
                                seqchainid(chain_rcsb),
                            )
                        )
                        chain_collated_dict[
                            prot_name + symbol + seqchainid(chain_pdbtm)
                        ].append(prot_name + symbol + seqchainid(chain_rcsb))
        return chain_collated_dict
