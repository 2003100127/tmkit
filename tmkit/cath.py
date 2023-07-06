__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

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


def download(
        sv_fp,
        version='newest',
):
    return cathreader().download(
        version=version,
        sv_fp=sv_fp,
    )


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