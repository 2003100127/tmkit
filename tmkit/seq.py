__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from tmkit.id.Fasta import fasta as idfas
from tmkit.id.PDB import pdb as idpdb
from tmkit.retrieve.PDB import pdb as repdb
from tmkit.retrieve.XML import xml as rexml
from tmkit.sequence import Fasta as sfasta
from tmkit.sequence.PDB import pdb as spdb
from tmkit.sequence.XML import xml as sxml
from tmkit.structure.PDB import pdb as stpdb


from typing import List, Tuple


def retrieve_pdb_from_rcsb(prot_series: List[str], sv_fp: str, route: str = "biopython") -> None:
    """
    Retrieve PDB files from RCSB.

    Parameters
    ----------
    prot_series : List[str]
        List of protein series.
    sv_fp : str
        File path to save the retrieved PDB files.
    route : str, optional
        Route to retrieve the PDB files, by default "biopython".
    """
    return repdb(prot_series=prot_series).rcsb(
        sv_fp=sv_fp,
        route=route,
    )


def retrieve_pdb_from_pdbtm(
    prot_series: List[str],
    sv_fp: str,
    kind: str = "tr",
) -> None:
    """
    Retrieve PDB files from PDBTM.

    Parameters
    ----------
    prot_series : List[str]
        List of protein series.
    sv_fp : str
        File path to save the retrieved PDB files.
    kind : str, optional
        Kind of PDB files to retrieve, by default "tr".
    """
    return repdb(prot_series=prot_series).pdbtm(
        sv_fp=sv_fp,
        kind=kind,
    )


def retrieve_xml_from_pdbtm(
    prot_series: List[str],
    sv_fp: str,
) -> None:
    """
    Retrieve XML files from PDBTM.

    Parameters
    ----------
    prot_series : List[str]
        List of protein series.
    sv_fp : str
        File path to save the retrieved XML files.
    """
    return rexml(
        prot_series=prot_series,
    ).pdbtm(
        sv_fp=sv_fp,
        is_cmd=False,
    )


def retrieve_pdb_alphafold(
    prot_series: List[str],
    sv_fp: str,
) -> None:
    """
    Retrieve PDB files from AlphaFold.

    Parameters
    ----------
    prot_series : List[str]
        List of protein series.
    sv_fp : str
        File path to save the retrieved PDB files.
    """
    return repdb(prot_series=prot_series).alphafold(
        sv_fp=sv_fp,
    )


def retrieve_foldseek(
    pdb_fp: str,
    prot_name: str,
    sv_fp: str,
    file_chain: str = "",
) -> None:
    """
    Retrieve FoldSeek files from PDB.

    Parameters
    ----------
    pdb_fp : str
        File path to the PDB file.
    prot_name : str
        Name of the protein.
    sv_fp : str
        File path to save the retrieved FoldSeek files.
    file_chain : str, optional
        Chain of the PDB file, by default "".
    """
    return stpdb(
        pdb_fp=pdb_fp,
        prot_name=prot_name,
        file_chain=file_chain,
    ).search_foldseek(
        sv_fp=sv_fp,
    )


def read_from_fasta(
    fasta_fpn: str,
) -> Tuple[str, str]:
    """
    Read sequence from FASTA file.

    Parameters
    ----------
    fasta_fpn : str
        File path to the FASTA file.

    Returns
    -------
    Tuple[str, str]
        Tuple containing the sequence ID and the sequence.
    """
    return sfasta.get(fasta_fpn=fasta_fpn)


def read_from_xml(
    xml_fp: str,
    xml_name: str,
    seq_chain: str,
) -> Tuple[str, str]:
    """
    Read sequence from XML file.

    Parameters
    ----------
    xml_fp : str
        File path to the XML file.
    xml_name : str
        Name of the XML file.
    seq_chain : str
        Chain of the sequence.

    Returns
    -------
    Tuple[str, str]
        Tuple containing the sequence ID and the sequence.
    """
    return sxml().get(
        xml_fp=xml_fp,
        xml_name=xml_name,
        seq_chain=seq_chain,
    )


def read_from_pdb(
    pdb_fp: str,
    prot_name: str,
    seq_chain: str,
    file_chain: str = "",
) -> str:
    """
    Read sequence from PDB file.

    Parameters
    ----------
    pdb_fp : str
        File path to the PDB file.
    prot_name : str
        Name of the protein.
    seq_chain : str
        Chain of the sequence.
    file_chain : str, optional
        Chain of the PDB file, by default "".

    Returns
    -------
    str
        The sequence.
    """
    return spdb(
        pdb_fp=pdb_fp,
        prot_name=prot_name,
        seq_chain=seq_chain,
        file_chain=file_chain,
    ).chain()


def fasid(
    fasta_fpn: str,
) -> str:
    """
    Get the ID of a sequence from a FASTA file.

    Parameters
    ----------
    fasta_fpn : str
        File path to the FASTA file.

    Returns
    -------
    str
        The sequence ID.
    """
    return idfas().get(fasta_fpn=fasta_fpn)


def pdbid(
    pdb_fp: str,
    prot_name: str,
    seq_chain: str,
    file_chain: str = "",
) -> str:
    """
    Get the ID of a sequence from a PDB file.

    Parameters
    ----------
    pdb_fp : str
        File path to the PDB file.
    prot_name : str
        Name of the protein.
    seq_chain : str
        Chain of the sequence.
    file_chain : str, optional
        Chain of the PDB file, by default "".

    Returns
    -------
    str
        The sequence ID.
    """
    return idpdb(
        pdb_fp=pdb_fp,
        prot_name=prot_name,
        seq_chain=seq_chain,
        file_chain=file_chain,
    ).chain()
