__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import List, Tuple
from tmkit.chain.Collate import collate as coll
from tmkit.chain.CollateBatch import collateBatch as collb
from tmkit.chain.PDB import pdb as cpdb
import pandas as pd


def chain(
    pdb_fp: str,
    prot_name: str,
) -> List[str]:
    """
    Extracts the chains from a PDB file.

    Parameters
    ----------
    pdb_fp : str
        The filepath of the PDB file.
    prot_name : str
        The name of the protein.

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
) -> Tuple[pd.DataFrame, str]:
    """
    Collates a single protein chain.

    Parameters
    ----------
    prot_name : str
        The name of the protein.
    chain_focus : str
        The chain to focus on.
    pdb_rcsb_fp : str
        The filepath of the RCSB PDB file.
    pdb_pdbtm_fp : str
        The filepath of the PDBTM file.
    symbol : str, optional
        The symbol to use for missing residues, by default "."

    Returns
    -------
    Tuple[pd.DataFrame, str]
        A tuple containing the collated dataframe and the throwback string.
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
) -> Tuple[pd.DataFrame, str]:
    """
    Collates multiple protein chains.

    Parameters
    ----------
    prot_df : pd.DataFrame
        The protein dataframe.
    prot_pdbtm_df : pd.DataFrame
        The PDBTM dataframe.
    prot_rcsb_df : pd.DataFrame
        The RCSB PDB dataframe.
    pdb_rcsb_fp : str
        The filepath of the RCSB PDB file.
    pdb_pdbtm_fp : str
        The filepath of the PDBTM file.
    strategy : str, optional
        The collation strategy to use, by default "diff".
    symbol : str, optional
        The symbol to use for missing residues, by default "."

    Returns
    -------
    Tuple[pd.DataFrame, str]
        A tuple containing the collated dataframe and the throwback string.
    """
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
