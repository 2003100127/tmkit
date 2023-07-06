__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"


from typing import List, Dict

import numpy as np

import pandas as pd

from tmkit.db.biogrid.Reader import Reader as biogridreader
from tmkit.db.Connectivity import Connectivity as ppiconn
from tmkit.db.intact.Reader import Reader as intactreader


def download_biogrid_db(
    sv_fp: str,
    version: str = "4.4.212",
) -> str:
    """
    Download BioGRID database.

    Parameters
    ----------
    sv_fp : str
        File path to save the downloaded file.
    version : str, optional
        Version of the BioGRID database to download, by default "4.4.212".

    Returns
    -------
    str
        A message indicating that the download and decompression is finished.
    """
    return biogridreader().fetch(
        version=version,
        sv_fp=sv_fp,
    )


def read_biogrid_db(
    biogrid_fpn: str,
    sv_fpn: str,
    extract_ids: List[str] = [
        "SWISS-PROT Accessions Interactor A",
        "SWISS-PROT Accessions Interactor B",
    ],
) -> pd.DataFrame:
    """
    Read BioGRID database.

    Parameters
    ----------
    biogrid_fpn : str
        File path to the BioGRID database.
    sv_fpn : str
        File path to the saved file.
    extract_ids : List[str], optional
        List of column names to extract, by default ["SWISS-PROT Accessions Interactor A", "SWISS-PROT Accessions Interactor B"].

    Returns
    -------
    pd.DataFrame
        A dataframe containing the extracted columns.
    """
    return biogridreader().tab3(
        biogrid_fpn=biogrid_fpn,
        sv_fpn=sv_fpn,
        extract_ids=extract_ids,
    )


def download_intact_db(
    sv_fp: str,
    version: str = "4.4.212",
) -> str:
    """
    Download IntAct database.

    Parameters
    ----------
    sv_fp : str
        File path to save the downloaded file.
    version : str, optional
        Version of the IntAct database to download, by default "4.4.212".

    Returns
    -------
    str
        A message indicating the completion of the download and decompression.
    """
    return intactreader().fetch(
        version=version,
        sv_fp=sv_fp,
    )


def read_intact_db(
    intact_fpn: str,
    sv_fpn: str,
    extract_ids: List[str] = [
        "#ID(s) interactor A",
        "ID(s) interactor B",
    ],
) -> pd.DataFrame:
    """
    Read IntAct database.

    Parameters
    ----------
    intact_fpn : str
        File path to the IntAct database.
    sv_fpn : str
        File path to the saved file.
    extract_ids : List[str], optional
        List of column names to extract, by default ["#ID(s) interactor A", "ID(s) interactor B"].

    Returns
    -------
    pd.DataFrame
        The extracted data as a pandas DataFrame.
    """
    return intactreader().full(
        intact_fpn=intact_fpn,
        sv_fpn=sv_fpn,
        extract_ids=extract_ids,
    )


def get_network(
    prot_name: str,
    seq_chain: str,
    prot_idmap: Dict,
    interacting_partner_idmap: Dict,
    pdb_rcsb_fp: str,
    pdb_pdbtm_fp: str,
    sv_fpn: str,
    ppi_db_fpns: Dict,
) -> np.ndarray:
    """
    Get protein-protein interaction network.

    Parameters
    ----------
    prot_name : str
        Protein name.
    seq_chain : str
        Sequence chain.
    prot_idmap : str
        Protein ID map.
    interacting_partner_idmap : str
        Interacting partner ID map.
    pdb_rcsb_fp : str
        File path to the PDB RCSB file.
    pdb_pdbtm_fp : str
        File path to the PDB PDBTM file.
    sv_fpn : str
        File path to the saved file.
    ppi_db_fpns : List[str]
        List of file paths to the PPI databases.

    Returns
    -------
    np.ndarray
        protein-protein interactions.
    """
    return ppiconn(
        prot_name=prot_name,
        seq_chain=seq_chain,
        prot_idmap=prot_idmap,
        interacting_partner_idmap=interacting_partner_idmap,
        pdb_rcsb_fp=pdb_rcsb_fp,
        pdb_pdbtm_fp=pdb_pdbtm_fp,
        sv_fpn=sv_fpn,
    ).strategy(
        ppi_db_fpns=ppi_db_fpns,
        uniprot_id=prot_name + "." + seq_chain,
        is_del_reflexive=False,
        is_del_repeated=False,
        overlap=True,
    )


def connectivity(
    prot_name: str,
    seq_chain: str,
    prot_idmap: Dict,
    interacting_partner_idmap: Dict,
    pdb_rcsb_fp: str,
    pdb_pdbtm_fp: str,
    sv_fpn: str,
    ppi_db_fpns: Dict,
) -> pd.DataFrame:
    """
    Get protein-protein interaction connectivity.

    Parameters
    ----------
    prot_name : str
        Protein name.
    seq_chain : str
        Sequence chain.
    prot_idmap : str
        Protein ID map.
    interacting_partner_idmap : str
        Interacting partner ID map.
    pdb_rcsb_fp : str
        File path to the PDB RCSB file.
    pdb_pdbtm_fp : str
        File path to the PDB PDBTM file.
    sv_fpn : str
        File path to the saved file.
    ppi_db_fpns : List[str]
        List of file paths to the PPI databases.

    Returns
    -------
    pd.DataFrame
        List of protein-protein interactions.
    """
    return ppiconn(
        prot_name=prot_name,
        seq_chain=seq_chain,
        prot_idmap=prot_idmap,
        interacting_partner_idmap=interacting_partner_idmap,
        pdb_rcsb_fp=pdb_rcsb_fp,
        pdb_pdbtm_fp=pdb_pdbtm_fp,
        sv_fpn=sv_fpn,
    ).extract(
        ppi_db_fpns=ppi_db_fpns,
    )
