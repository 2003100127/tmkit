__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import Dict

import pandas as pd
from pandas import DataFrame

from tmkit.db.cath.Reader import Reader as cathreader


def summary_by_id(
    id: str,
) -> Dict:
    """
    Access the information about the domains and
    families of a protein by using parameter id.
    For example, if you are interested in protein 1cuk chain A,
    we can generate the links to its domain 01.

    Parameters
    ----------
    id : str
        protein name + chain + domain, e.g., 1cukA01 (1cuk+A+01)

    Returns
    -------
    Dict
        The result is made in JSON format with domain, funfam, and superfamily information.
    """
    return cathreader().api(identifier=id)


def fetch_by_id(
    id: str,
) -> Dict:
    """
    Access the information about the domains and families of a protein
    by using parameter id. For example, if you are interested in protein
    1cuk chain A, we can see the detailed information of domain 01.

    Parameters
    ----------
    id : str
        protein name + chain + domain, e.g., 1cukA01 (1cuk+A+01)

    Returns
    -------
    Dict[str, Union[str, Dict[str, str]]]
        A dictionary containing the fetched data according to the CATH database.
    """
    return cathreader().fetch(domain_id=id, sort="domain")


def download(
    sv_fp: str,
    version: str = "newest",
) -> str:
    """
    Retrieve a Cath database.

    Parameters
    ----------
    sv_fp : str
        path to save the Cath database
    version : str, optional
        version of the Cath database

    Returns
    -------
    str
        A message indicating that the download is finished.
    """
    return cathreader().download(
        version=version,
        sv_fp=sv_fp,
    )


def read(
    cath_fpn: str,
    groupby: str,
    group: str,
) -> pd.DataFrame:
    """
    Read a CATH database file, containing information about domain', 'version', 'superfamily', and 'bound'.

    Parameters
    ----------
    cath_fpn : str
        path to the downloaded Cath database
    groupby : str
        metric used to group data, e.g., version. There are 4 metrics in total, i.e., domain, version, superfamily, and bound.
    group : str
        value of a metric. For example, if version is chosen, there are two, namely, v4_2_0 and putative.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the domain information, including
        'domain', 'version', 'superfamily', and 'bound'.
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
) -> Dict:
    """
    Convert the given protein and domain DataFrame to
        a JSON file containing funfam information.

    Parameters
    ----------
    df_prot : pd.DataFrame
        The protein DataFrame.
    df_domain : pd.DataFrame
        The domain DataFrame.
    sv_fpn : str, optional
        The file path to save the resulting JSON file, by default "./results.json".
    targets : List[str], optional
        The targets to fetch data for, by default ["funfam_number"].

    Returns
    -------
    Dict[str, Dict[str, Dict[str, Dict[str, str]]]]
        A dictionary containing the funfam information.
    """
    return cathreader().funfamsToJson(
        df_prot=df_prot,
        df_domain=df_cath_domain,
        sv_fpn=sv_fpn,
        targets=targets,
    )
