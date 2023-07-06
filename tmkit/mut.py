__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import pandas as pd

from tmkit.db.muthtp.Reader import Reader as muthtpreader
from tmkit.db.predmuthtp.Reader import Reader as predmuthtpreader


def download_muthtp_db(
    sv_fp: str,
    version: str = "2020",
) -> str:
    """
    Download the MutHTP database.

    Parameters
    ----------
    sv_fp : str
        The path to the directory where the database will be saved.
    version : str, optional
        The version of the database to download, by default "2020".

    Returns
    -------
    str
        A message indicating the download is finished.
    """
    return muthtpreader().fetch(
        version=version,
        sv_fp=sv_fp,
    )


def read_muthtp_db(muthtp_fpn: str) -> pd.DataFrame:
    """
    Read the MutHTP database.

    Parameters
    ----------
    muthtp_fpn : str
        The path to the MutHTP database file.

    Returns
    -------
    pd.DataFrame
        A pandas DataFrame containing the MutHTP database.
    """
    return muthtpreader().full(muthtp_fpn)


def download_predmuthtp_db(
    sv_fp: str,
) -> str:
    """
    Download the Pred-MutHTP database.

    Parameters
    ----------
    sv_fp : str
        The path to the directory where the database will be saved.

    Returns
    -------
    str
        A message indicating the download is finished.
    """
    return predmuthtpreader().fetch(
        sv_fp=sv_fp,
    )


def read_predmuthtp_db(pred_muthtp_fpn: str) -> pd.DataFrame:
    """
    Read the Pred-MutHTP database.

    Parameters
    ----------
    pred_muthtp_fpn : str
        The path to the Pred-MutHTP database file.

    Returns
    -------
    pd.DataFrame
        A pandas DataFrame Pred-MutHTP the MutHTP database.
    """
    return predmuthtpreader().readall(pred_muthtp_fpn)


def split_predmuthtp(
    pred_muthtp_df: pd.DataFrame,
    sv_fp: str,
) -> str:
    """
    Split the Pred-MutHTP database.

    Parameters
    ----------
    pred_muthtp_df : pd.DataFrame
        A list of dictionaries containing the Pred-MutHTP database.
    sv_fp : str
        The path to the directory where the split database will be saved.

    Returns
    -------
    str
        A message indicating the download is finished.
    """
    return predmuthtpreader().split(pred_muthtp_df=pred_muthtp_df, sv_fp=sv_fp)


def read_split_predmuthtp(
    pred_split_muthtp_fpn: str,
) -> pd.DataFrame:
    """
    Read the split Pred-MutHTP database.

    Parameters
    ----------
    pred_split_muthtp_fpn : str
        The path to the split Pred-MutHTP database file.

    Returns
    -------
    pd.DataFrame
        A pandas DataFrame Pred-MutHTP the MutHTP database.
    """
    return predmuthtpreader().readsingle(
        pred_split_muthtp_fpn=pred_split_muthtp_fpn,
    )
