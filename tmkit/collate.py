__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2022"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from tmkit.chain.PDB import pdb as cpdb
from tmkit.chain.Collate import collate as coll
from tmkit.chain.CollateBatch import collateBatch as collb
from tmkit.util.Console import console


def chain(
        pdb_fp,
        prot_name,
        verbose=True,
):
    c = console()
    c.verbose = verbose
    chains = cpdb(
        pdb_fp=pdb_fp,
        prot_name=prot_name,
    ).chains()
    c.print('======>protein has chains {}'.format(chains))
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


if __name__ == "__main__":
    from tmkit.Path import to
    from tmkit.util.Reader import reader as reader

    pdb_rcsb_fp = to('data/example/pdb/indepdata/rcsb/')
    pdb_pdbtm_fp = to('data/example/pdb/indepdata/pdbtm/')
    prot_fpn = to('data/example/pdb/indepdata/prot_n30.txt')
    prot_pdbtm_fpn = to('data/example/pdb/indepdata/prot_n30_complex_pdbtm_full.txt')
    prot_rcsb_fpn = to('data/example/pdb/indepdata/prot_n30_complex_rcsb_full.txt')

    print(chain(
        prot_name='3pux',
        pdb_fp=pdb_pdbtm_fp,
        # pdb_fp=pdb_rcsb_fp,
    ))

    print(single(
        prot_name='3pux',
        chain_focus='G',
        pdb_rcsb_fp=pdb_rcsb_fp,
        pdb_pdbtm_fp=pdb_pdbtm_fp,
    ))

    prot_df = reader().generic(prot_fpn)
    prot_pdbtm_df = reader().generic(prot_pdbtm_fpn)
    prot_rcsb_df = reader().generic(prot_rcsb_fpn)

    print(batch(
        prot_df=prot_df,
        prot_pdbtm_df=prot_pdbtm_df,
        prot_rcsb_df=prot_rcsb_df,
        pdb_rcsb_fp=pdb_rcsb_fp,
        pdb_pdbtm_fp=pdb_pdbtm_fp,
        strategy='diff',
        symbol='.'
    ))