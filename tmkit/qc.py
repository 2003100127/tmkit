__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import List

import pandas as pd

from tmkit.channel.Workbench import Workbench


def obtain_single(
    df_prot: pd.DataFrame,
    pdb_cplx_fp: str,
    fasta_fp: str,
    xml_fp: str,
    sv_fp: str,
    metric: str = "rez",
) -> pd.DataFrame:
    """
    Obtain a single metric for a list of proteins.

    Parameters
    ----------
    df_prot : pd.DataFrame
        Pandas dataframe storing protein names and chain names.
    pdb_cplx_fp : str
        path where a protein complex file from PDBTM is placed.
    fasta_fp : str
        path where a protein Fasta file is placed.
    xml_fp : str
        path where a protein XML file from PDBTM is placed.
    sv_fp : str
        path to save files.
    metric : str, optional
        The metric to calculate. Can be "rez", "met", "bio_name", "head", "desc", "mthm", or "seq".

    Returns
    -------
    pd.DataFrame
        A dataframe of the calculated metric.
    """
    return Workbench(
        df_prot=df_prot,
        pdb_cplx_fp=pdb_cplx_fp,
        fasta_fp=fasta_fp,
        xml_fp=xml_fp,
        sv_fp=sv_fp,
    ).template(metric=metric)


def integrate(
    df_prot: pd.DataFrame,
    pdb_cplx_fp: str,
    fasta_fp: str,
    xml_fp: str,
    sv_fp: str,
    metrics: List[str],
) -> pd.DataFrame:
    """
    Generate multiple metrics for a list proteins.

    Parameters
    ----------
    df_prot : pd.DataFrame
        Pandas dataframe storing protein names and chain names.
    pdb_cplx_fp : str
        path where a protein complex file from PDBTM is placed.
    fasta_fp : str
        path where a protein Fasta file is placed.
    xml_fp : str
        path where a protein XML file from PDBTM is placed.
    sv_fp : str
        path to save files.
    metrics : List[str]
        A list of metrics to calculate. Can include "rez", "met", "bio_name", "head", "desc", "mthm", and "seq".

    Returns
    -------
    pd.DataFrame
        A dataframe of the calculated metrics.
    """
    return Workbench(
        df_prot=df_prot,
        pdb_cplx_fp=pdb_cplx_fp,
        fasta_fp=fasta_fp,
        xml_fp=xml_fp,
        sv_fp=sv_fp,
    ).integrate(metrics=metrics)
