__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import List, Union
import numpy as np
from tmkit.channel.Workbench import workbench


def obtain_single(
    df_prot: np.ndarray,
    pdb_cplx_fp: str,
    fasta_fp: str,
    xml_fp: str,
    sv_fp: str,
    metric: str = "rez",
) -> np.ndarray:
    """
    Obtain a single metric for a given protein.

    Parameters
    ----------
    df_prot : np.ndarray
        A numpy array of protein data.
    pdb_cplx_fp : str
        The file path of the PDB complex.
    fasta_fp : str
        The file path of the FASTA file.
    xml_fp : str
        The file path of the XML file.
    sv_fp : str
        The file path of the SV file.
    metric : str, optional
        The metric to calculate. Can be "rez", "met", "bio_name", "head", "desc", "mthm", or "seq".

    Returns
    -------
    np.ndarray
        A numpy array of the calculated metric.
    """
    return workbench(
        df_prot=df_prot,
        pdb_cplx_fp=pdb_cplx_fp,
        fasta_fp=fasta_fp,
        xml_fp=xml_fp,
        sv_fp=sv_fp,
    ).template(metric=metric)


def integrate(
    df_prot: np.ndarray,
    pdb_cplx_fp: str,
    fasta_fp: str,
    xml_fp: str,
    sv_fp: str,
    metrics: List[str],
) -> np.ndarray:
    """
    Integrate multiple metrics for a given protein.

    Parameters
    ----------
    df_prot : np.ndarray
        A numpy array of protein data.
    pdb_cplx_fp : str
        The file path of the PDB complex.
    fasta_fp : str
        The file path of the FASTA file.
    xml_fp : str
        The file path of the XML file.
    sv_fp : str
        The file path of the SV file.
    metrics : List[str]
        A list of metrics to calculate. Can include "rez", "met", "bio_name", "head", "desc", "mthm", and "seq".

    Returns
    -------
    np.ndarray
        A numpy array of the calculated metrics.
    """
    return workbench(
        df_prot=df_prot,
        pdb_cplx_fp=pdb_cplx_fp,
        fasta_fp=fasta_fp,
        xml_fp=xml_fp,
        sv_fp=sv_fp,
    ).integrate(metrics=metrics)
