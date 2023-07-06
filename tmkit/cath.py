from pandas import DataFrame
__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import Any
from tmkit.db.cath.Reader import reader as cathreader


def summary_by_id(
    id: str,
) -> Any:
    """_summary_

    Parameters
    ----------
    id : str
        _description_

    Returns
    -------
    Any
        _description_
    """
    return cathreader().api(identifier=id)


def fetch_by_id(
    id: str,
) -> Any:
    """_summary_

    Parameters
    ----------
    id : str
        _description_

    Returns
    -------
    Any
        _description_
    """
    return cathreader().fetch(domain_id=id, sort="domain")


def download(
    sv_fp: str,
    version: str = "newest",
) -> Any:
    """_summary_

    Parameters
    ----------
    sv_fp : str
        _description_
    version : str, optional
        _description_, by default "newest"

    Returns
    -------
    Any
        _description_
    """
    return cathreader().download(
        version=version,
        sv_fp=sv_fp,
    )


def read(
    cath_fpn: str,
    groupby: str,
    group: str,
) -> Any:
    """
    Parameters
    ----------
    cath_fpn : str
    groupby : str
    group : str

    Returns
    -------
    Any
    """
    return cathreader().domain(cath_fpn, groupby=groupby, group=group)


def fftojson(
    df_prot: DataFrame,
    df_cath_domain: DataFrame,
    sv_fpn: str,
    targets: list = [
        "funfam_number",
        "superfamily_id",
        "pdb_segments",
    ],
) -> Any:
    """
    Parameters
    ----------
    df_prot : DataFrame
    df_cath_domain : DataFrame
    sv_fpn : str
    targets : list, optional

    Returns
    -------
    Any
    """
    return cathreader().funfamsToJson(
        df_prot=df_prot,
        df_domain=df_cath_domain,
        sv_fpn=sv_fpn,
        targets=targets,
    )
