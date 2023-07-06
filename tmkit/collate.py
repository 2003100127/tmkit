__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import List, Tuple, Dict

import pandas as pd

from tmkit.chain.Collate import Collate as coll
from tmkit.chain.CollateBatch import CollateBatch as collb
from tmkit.chain.PDB import PDB as cpdb


def chain(
    pdb_fp: str,
    prot_name: str,
) -> List[str]:
    """
    Extracts the chains from a PDB file.

    Parameters
    ----------
    pdb_fp : str
        Filepath of the PDB file.
    prot_name : str
        Name of a protein in the prefix of a PDB file name (e.g., 1xqf in 1xqfA.pdb).

    Returns
    -------
    List[str]
        A list of chains in the protein.
    """
    chains = cpdb(
        pdb_fp=pdb_fp,
        prot_name=prot_name,
    ).chains()
    print(f"======>protein has chains {chains}")
    return chains


def single(
    prot_name: str,
    chain_focus: str,
    pdb_rcsb_fp: str,
    pdb_pdbtm_fp: str,
    symbol: str = ".",
) -> Tuple[pd.DataFrame, Dict]:
    """
    Collates a single protein chain.
    Check if the chain of focus is transformed by another chain from a RCSB PDB structure.
    'untransformed' means it is not transformed by another chain.

    Parameters
    ----------
    prot_name : str
        Name of a protein in the prefix of a PDB file name (e.g., 1xqf in 1xqfA.pdb).
    chain_focus : str
        Chain of a protein in the prefix of a PDB file name (e.g., A in 1xqfA.pdb).
    pdb_rcsb_fp : str
        Path where protein complexes from RCSB are placed.
    pdb_pdbtm_fp: str
        Path where protein complexes from PDBTM are placed.
    symbol : str, optional
        The symbol to use for missing residues, by default "."

    Returns
    -------
    Tuple[pd.DataFrame, str]
        A tuple containing the collated dataframe and a collated dictionary.
        The dataframe: the protein chain composed of col 0 and 1 comes from
        a complex containing chains in cols pdbtm and rcsb.
        The different chains are stored in col diff.
        The column source means whether a chain(s) in PDBTM exists
        in the chains in RCSB, which means if this chain(s) in PDBTM
        is transformed using the BIOMAT 350 records.
        If strategy='diff' is selected and values in column source
        are shown rcsb, which means all chains of a self.prot_df in PDBTM can be found in RCSB.
        strategy_dict stores the same or different chains between PDBTM and RCSB.

        The collated dictionary: protein name -> 'transformed' or 'untransformed' (can be a list).
    """
    coll_sgl = coll(
        prot_name=prot_name,
        chain_focus=chain_focus,
        pdb_rcsb_fp=pdb_rcsb_fp,
        pdb_pdbtm_fp=pdb_pdbtm_fp,
    )

    return coll_sgl.df, coll_sgl.throwback(symbol=symbol)


def batch(
    prot_df: pd.DataFrame,
    prot_pdbtm_df: pd.DataFrame,
    prot_rcsb_df: pd.DataFrame,
    pdb_rcsb_fp: str,
    pdb_pdbtm_fp: str,
    strategy: str = "diff",
    symbol: str = ".",
) -> Tuple[pd.DataFrame, Dict]:
    """
    Collates multiple protein chains.

    Parameters
    ----------
    prot_df : pd.DataFrame
        The protein dataframe.
    prot_pdbtm_df : pd.DataFrame
        Tab-delimiter Pandas dataframe containing protein names and all of the chains of the protein (from PDBTM) in two columns, respectively.
    prot_rcsb_df : pd.DataFrame
        Tab-delimiter Pandas dataframe containing protein names and all of the chains of the protein (from RCSB) in two columns, respectively.
    pdb_rcsb_fp : str
        Path where protein complexes from RCSB are placed.
    pdb_pdbtm_fp: str
        Path where protein complexes from PDBTM are placed.
    strategy : str, optional
        The collation strategy to use, by default "diff".
    symbol : str, optional
        The symbol to use for missing residues, by default "."

    Returns
    -------
    Tuple[pd.DataFrame, str]
        A tuple containing the collated dataframe and a collated dictionary.
        The dataframe: the protein chain composed of col 0 and 1 comes from
        a complex containing chains in cols pdbtm and rcsb.
        The different chains are stored in col diff.
        The column source means whether a chain(s) in PDBTM exists
        in the chains in RCSB, which means if this chain(s) in PDBTM
        is transformed using the BIOMAT 350 records.
        If strategy='diff' is selected and values in column source
        are shown rcsb, which means all chains of a self.prot_df in PDBTM can be found in RCSB.
        strategy_dict stores the same or different chains between PDBTM and RCSB.

        The collated dictionary: protein name -> 'transformed' or 'untransformed' (can be a list).    """
    coll_batch = collb(
        prot_df=prot_df,
        pdb_rcsb_fp=pdb_rcsb_fp,
        pdb_pdbtm_fp=pdb_pdbtm_fp,
        prot_pdbtm_df=prot_pdbtm_df,
        prot_rcsb_df=prot_rcsb_df,
        strategy=strategy,
    )
    return coll_batch.prot_collated_df, coll_batch.throwback(
        prot_collated_df=coll_batch.prot_collated_df, symbol=symbol
    )
