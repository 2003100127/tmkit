__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2022"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import pandas as pd
from tmkit.db.cath.Reader import reader as cathreader


def summary_by_id(
        id,
):
    """

    Parameters
    ----------
    id

    Returns
    -------

    """
    return cathreader().api(identifier=id)


def fetch_by_id(
        id,
):
    """

    Parameters
    ----------
    id

    Returns
    -------

    """
    return cathreader().fetch(domain_id=id, sort='domain')


def read(
        cath_fpn,
        groupby,
        group,
):
    """

    Parameters
    ----------
    cath_fpn
    groupby
    group

    Returns
    -------

    """
    return cathreader().domain(
        cath_fpn, groupby=groupby, group=group
    )


def fftojson(
        df_prot,
        df_cath_domain,
        sv_fpn,
        targets=[
            'funfam_number',
            'superfamily_id',
            'pdb_segments',
        ],
):
    """

    Parameters
    ----------
    df_prot
    df_cath_domain
    sv_fpn
    targets

    Returns
    -------

    """
    return cathreader().funfamsToJson(
        df_prot=df_prot,
        df_domain=df_cath_domain,
        sv_fpn=sv_fpn,
        targets=targets,
    )


if __name__ == "__main__":
    from tmkit.Path import to

    # print(summary_by_id(
    #     id='1cukA01'
    # ))

    # print(fetch_by_id(
    #     id='1cukA01'
    # ))

    df_cath_domain = read(
        cath_fpn=to('data/example/cath/cath_b.20200812.all'),
        groupby='version',
        group='v4_2_0',
    )
    # print(df_cath_domain)

    print(fftojson(
        df_prot=pd.DataFrame([['3udc', 'A'], ['3rko', 'A']], columns=['prot', 'chain']),
        df_cath_domain=df_cath_domain,
        sv_fpn=to('data/example/cath/compdata.json'),
        targets=[
            'funfam_number',
            'superfamily_id',
            'pdb_segments',
        ],
    ))