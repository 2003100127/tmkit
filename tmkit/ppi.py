__author__: str = "Jianfeng Sun"
__version__: str = "v1.0"
__copyright__: str = "Copyright 2023"
__license__: str = "GPL v3.0"
__email__: str = "jianfeng.sunmt@gmail.com"
__maintainer__: str = "Jianfeng Sun"


from typing import List, Tuple
from tmkit.db.biogrid.Reader import reader as biogridreader
from tmkit.db.Connectivity import connectivity as ppiconn
from tmkit.db.intact.Reader import reader as intactreader


def download_biogrid_db(
    sv_fp: str,
    version: str = "4.4.212",
) -> None:
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
    None
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
) -> Tuple[List[str], List[Tuple[str, str]]]:
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
    Tuple[List[str], List[Tuple[str, str]]]
        List of extracted column names and a list of extracted interactions.
    """
    return biogridreader().tab3(
        biogrid_fpn=biogrid_fpn,
        sv_fpn=sv_fpn,
        extract_ids=extract_ids,
    )


def download_intact_db(
    sv_fp: str,
    version: str = "4.4.212",
) -> None:
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
    None
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
) -> Tuple[List[str], List[Tuple[str, str]]]:
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
    Tuple[List[str], List[Tuple[str, str]]]
        List of extracted column names and a list of extracted interactions.
    """
    return intactreader().full(
        intact_fpn=intact_fpn,
        sv_fpn=sv_fpn,
        extract_ids=extract_ids,
    )


def get_network(
    prot_name: str,
    seq_chain: str,
    prot_idmap: str,
    interacting_partner_idmap: str,
    pdb_rcsb_fp: str,
    pdb_pdbtm_fp: str,
    sv_fpn: str,
    ppi_db_fpns: List[str],
) -> List[Tuple[str, str]]:
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
    List[Tuple[str, str]]
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
    prot_idmap: str,
    interacting_partner_idmap: str,
    pdb_rcsb_fp: str,
    pdb_pdbtm_fp: str,
    sv_fpn: str,
    ppi_db_fpns: List[str],
) -> List[Tuple[str, str]]:
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
    List[Tuple[str, str]]
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
