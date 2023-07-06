from typing import Any, Dict, List, Tuple
from tmkit.db.muthtp.Reader import reader as muthtpreader
from tmkit.db.predmuthtp.Reader import reader as predmuthtpreader


def download_muthtp_db(
    sv_fp: str,
    version: str = "2020",
) -> Dict[str, Any]:
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
    Dict[str, Any]
        A dictionary containing the downloaded database.
    """
    return muthtpreader().fetch(
        version=version,
        sv_fp=sv_fp,
    )


def read_muthtp_db(muthtp_fpn: str) -> Dict[str, Any]:
    """
    Read the MutHTP database.

    Parameters
    ----------
    muthtp_fpn : str
        The path to the MutHTP database file.

    Returns
    -------
    Dict[str, Any]
        A dictionary containing the MutHTP database.
    """
    return muthtpreader().full(muthtp_fpn)


def download_predmuthtp_db(
    sv_fp: str,
) -> Dict[str, Any]:
    """
    Download the PredMutHTP database.

    Parameters
    ----------
    sv_fp : str
        The path to the directory where the database will be saved.

    Returns
    -------
    Dict[str, Any]
        A dictionary containing the downloaded database.
    """
    return predmuthtpreader().fetch(
        sv_fp=sv_fp,
    )


def read_predmuthtp_db(pred_muthtp_fpn: str) -> List[Dict[str, Any]]:
    """
    Read the PredMutHTP database.

    Parameters
    ----------
    pred_muthtp_fpn : str
        The path to the PredMutHTP database file.

    Returns
    -------
    List[Dict[str, Any]]
        A list of dictionaries containing the PredMutHTP database.
    """
    return predmuthtpreader().readall(pred_muthtp_fpn)


def split_predmuthtp(
    pred_muthtp_df: List[Dict[str, Any]],
    sv_fp: str,
) -> List[str]:
    """
    Split the PredMutHTP database.

    Parameters
    ----------
    pred_muthtp_df : List[Dict[str, Any]]
        A list of dictionaries containing the PredMutHTP database.
    sv_fp : str
        The path to the directory where the split database will be saved.

    Returns
    -------
    List[str]
        A list of paths to the split PredMutHTP database files.
    """
    return predmuthtpreader().split(pred_muthtp_df=pred_muthtp_df, sv_fp=sv_fp)


def read_split_predmuthtp(
    pred_split_muthtp_fpn: str,
) -> List[Dict[str, Any]]:
    """
    Read the split PredMutHTP database.

    Parameters
    ----------
    pred_split_muthtp_fpn : str
        The path to the split PredMutHTP database file.

    Returns
    -------
    List[Dict[str, Any]]
        A list of dictionaries containing the split PredMutHTP database.
    """
    return predmuthtpreader().readsingle(
        pred_split_muthtp_fpn=pred_split_muthtp_fpn,
    )
