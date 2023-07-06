__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from tmkit.sequence.PDB import pdb as spdb
from tmkit.sequence import Fasta as sfasta
from tmkit.sequence.XML import xml as sxml
from tmkit.id.Fasta import fasta as idfas
from tmkit.id.PDB import pdb as idpdb
from tmkit.retrieve.PDB import pdb as repdb
from tmkit.structure.PDB import pdb as stpdb
from tmkit.retrieve.XML import xml as rexml


def retrieve_pdb_from_rcsb(
        prot_series,
        sv_fp,
        route='biopython'
):
    """

    Parameters
    ----------
    prot_series
    sv_fp
    route

    Returns
    -------

    """
    return repdb(
        prot_series=prot_series
    ).rcsb(
        sv_fp=sv_fp,
        route=route,
    )


def retrieve_pdb_from_pdbtm(
        prot_series,
        sv_fp,
        kind='tr',
):
    """

    Parameters
    ----------
    prot_series
    sv_fp
    kind

    Returns
    -------

    """
    return repdb(
        prot_series=prot_series
    ).pdbtm(
        sv_fp=sv_fp,
        kind=kind,
    )


def retrieve_xml_from_pdbtm(
        prot_series,
        sv_fp,
):
    """

    Parameters
    ----------
    prot_series
    sv_fp

    Returns
    -------

    """
    return rexml(
        prot_series=prot_series,
    ).pdbtm(
        sv_fp=sv_fp,
        is_cmd=False,
    )


def retrieve_pdb_alphafold(
        prot_series,
        sv_fp,
):
    """

    Notes
    -----
        sth

    Parameters
    ----------
    prot_series
        sth
    sv_fp
        sth

    Returns
    -------
        sth

    """
    return repdb(
        prot_series=prot_series
    ).alphafold(
        sv_fp=sv_fp,
    )


def retrieve_foldseek(
        pdb_fp,
        prot_name,
        sv_fp,
        file_chain='',
):
    """"""
    return stpdb(
        pdb_fp=pdb_fp,
        prot_name=prot_name,
        file_chain=file_chain,
    ).search_foldseek(
        sv_fp=sv_fp,
    )


def read_from_fasta(
    fasta_fpn,
):
    """

    Parameters
    ----------
    fasta_fpn

    Returns
    -------

    """
    return sfasta.get(fasta_fpn=fasta_fpn)


def read_from_xml(
        xml_fp,
        xml_name,
        seq_chain,
):
    """

    Parameters
    ----------
    xml_fp
    xml_name
    seq_chain

    Returns
    -------

    """
    return sxml().get(
        xml_fp=xml_fp,
        xml_name=xml_name,
        seq_chain=seq_chain,
    )


def read_from_pdb(
        pdb_fp,
        prot_name,
        seq_chain,
        file_chain='',
):
    """

    Parameters
    ----------
    pdb_fp
    prot_name
    seq_chain
    file_chain

    Returns
    -------

    """
    return spdb(
        pdb_fp=pdb_fp,
        prot_name=prot_name,
        seq_chain=seq_chain,
        file_chain=file_chain,
    ).chain()


def fasid(
        fasta_fpn,
):
    """

    Parameters
    ----------
    fasta_fpn

    Returns
    -------

    """
    return idfas().get(fasta_fpn=fasta_fpn)


def pdbid(
        pdb_fp,
        prot_name,
        seq_chain,
        file_chain='',
):
    """

    Parameters
    ----------
    pdb_fp
    prot_name
    seq_chain
    file_chain

    Returns
    -------

    """
    return idpdb(
        pdb_fp=pdb_fp,
        prot_name=prot_name,
        seq_chain=seq_chain,
        file_chain=file_chain,
    ).chain()