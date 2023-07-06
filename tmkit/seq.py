__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import pandas as pd

from tmkit.id.Fasta import Fasta as idfas
from tmkit.id.PDB import PDB as idpdb
from tmkit.retrieve.PDB import PDB as repdb
from tmkit.retrieve.XML import XML as rexml
from tmkit.sequence import Fasta as sfasta
from tmkit.sequence.PDB import PDB as spdb
from tmkit.sequence.XML import XML as sxml
from tmkit.structure.PDB import PDB as stpdb


def retrieve_pdb_from_rcsb(
    prot_series: pd.Series, sv_fp: str, route: str = "biopython"
) -> str:
    """
    Retrieve a PDB file from RCSB.

    Parameters
    ----------
    prot_series : pd.Series
        A Pandas Series of protein names.
    sv_fp : str
        File path to save the retrieved PDB files.
    route : str, optional
        Route to retrieve the PDB files, "biopython" by default.

    Returns
    -------
    str
        'Finished' if a PDB file is successfully retrieved.
    """
    return repdb(prot_series=prot_series).rcsb(
        sv_fp=sv_fp,
        route=route,
    )


def retrieve_pdb_from_pdbtm(
    prot_series: pd.Series,
    sv_fp: str,
    kind: str = "tr",
) -> str:
    """
    Retrieve a PDB file from PDBTM.

    Parameters
    ----------
    prot_series : pd.Series
        A Pandas Series of protein names.
    sv_fp : str
        File path to save the retrieved PDB files.
    kind : str, optional
        Kind of PDB files to retrieve, by default "tr".

    Returns
    -------
    str
        'Finished' if a PDB file is successfully retrieved.
    """
    return repdb(prot_series=prot_series).pdbtm(
        sv_fp=sv_fp,
        kind=kind,
    )


def retrieve_xml_from_pdbtm(
    prot_series: pd.Series,
    sv_fp: str,
) -> str:
    """
    Retrieve a XML file from PDBTM.

    Parameters
    ----------
    prot_series : pd.Series
        A Pandas Series of protein names.
    sv_fp : str
        File path to save the retrieved XML files.

    Returns
    -------
    str
        'Finished' if a PDB file is successfully retrieved.
    """
    return rexml(
        prot_series=prot_series,
    ).pdbtm(
        sv_fp=sv_fp,
        is_cmd=False,
    )


def retrieve_pdb_alphafold(
    prot_series: pd.Series,
    sv_fp: str,
) -> str:
    """
    Retrieve a PDB file from AlphaFold Database.

    Parameters
    ----------
    prot_series : pd.Series
        A Pandas Series of protein names.
    sv_fp : str
        File path to save the retrieved PDB files.

    Returns
    -------
    str
        'Finished' if a PDB file is successfully retrieved.
    """
    return repdb(prot_series=prot_series).alphafold(
        sv_fp=sv_fp,
    )


def retrieve_foldseek(
    pdb_fp: str,
    prot_name: str,
    sv_fp: str,
    file_chain: str = "",
) -> str:
    """
    Retrieve a FoldSeek file (*.gz) from PDB. See how to to use the compressed file
    at http://localhost:8088/tmkit-guide/public/doc/msa/foldseek.

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

    Returns
    -------
    str
        'Finished' if a PDB file is successfully retrieved.
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
) -> str:
    """
    Read a sequence from FASTA file.

    Parameters
    ----------
    fasta_fpn : str
        File path to the FASTA file.

    Returns
    -------
    str
        A protein sequence from a FASTA file.
    """
    return sfasta.get(fasta_fpn=fasta_fpn)


def read_from_xml(
    xml_fp: str,
    xml_name: str,
    seq_chain: str,
) -> str:
    """
    Read a sequence from XML file.

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
    str
        A protein sequence from a XML file.
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
    Read a sequence from a PDB file.

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
        A protein sequence from a PDB file.
    """
    return spdb(
        pdb_fp=pdb_fp,
        prot_name=prot_name,
        seq_chain=seq_chain,
        file_chain=file_chain,
    ).chain()


def fasid(
    fasta_fpn: str,
) -> dict:
    """
    Get a dictionary mapping residue FASTA IDs to amino acid symbols.

    Parameters
    ----------
    fasta_fpn : str
        File path to the FASTA file.

    Returns
    -------
    dict
        A dictionary mapping residue FASTA IDs to amino acid symbols.
    """
    return idfas().get(fasta_fpn=fasta_fpn)


def pdbid(
    pdb_fp: str,
    prot_name: str,
    seq_chain: str,
    file_chain: str = "",
) -> dict:
    """
    Get a dictionary mapping residue PDB IDs to amino acid symbols.

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
    dict
        A dictionary mapping residue FASTA IDs to amino acid symbols.
    """
    return idpdb(
        pdb_fp=pdb_fp,
        prot_name=prot_name,
        seq_chain=seq_chain,
        file_chain=file_chain,
    ).chain()
