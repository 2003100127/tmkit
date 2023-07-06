__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from tmkit.chain.PDB import pdb as cpdb
from tmkit.chain.Collate import collate as coll
from tmkit.chain.CollateBatch import collateBatch as collb


def chain(
        pdb_fp,
        prot_name,
):
    chains = cpdb(
        pdb_fp=pdb_fp,
        prot_name=prot_name,
    ).chains()
    print('======>protein has chains {}'.format(chains))
    return chains


def single(
        prot_name,
        chain_focus,
        pdb_rcsb_fp,
        pdb_pdbtm_fp,
        symbol='.',
):
    """

    Parameters
    ----------
    prot_name
    chain_focus
    pdb_rcsb_fp
    pdb_pdbtm_fp
    symbol

    Returns
    -------

    """
    coll_sgl = coll(
        prot_name=prot_name,
        chain_focus=chain_focus,
        pdb_rcsb_fp=pdb_rcsb_fp,
        pdb_pdbtm_fp=pdb_pdbtm_fp,
    )

    return coll_sgl.df, coll_sgl.throwback(symbol=symbol)


def batch(
        prot_df,
        prot_pdbtm_df,
        prot_rcsb_df,
        pdb_rcsb_fp,
        pdb_pdbtm_fp,
        strategy='diff',
        symbol='.'
):
    """

    Parameters
    ----------
    prot_df
    prot_pdbtm_df
    prot_rcsb_df
    pdb_rcsb_fp
    pdb_pdbtm_fp
    strategy

    Returns
    -------

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
        prot_collated_df=coll_batch.prot_collated_df,
        symbol=symbol
    )