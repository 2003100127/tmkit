__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2022"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from tmkit.sequence.PDB import pdb as spdb
from tmkit.sequence.Fasta import fasta as sfasta
from tmkit.sequence.XML import xml as sxml
from tmkit.id.Fasta import fasta as idfas
from tmkit.id.PDB import pdb as idpdb
from tmkit.retrieve.PDB import pdb as repdb
from tmkit.retrieve.XML import xml as rexml


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
    return sfasta().get(fasta_fpn=fasta_fpn)


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


if __name__ == "__main__":
    from tmkit.Path import to
    import pandas as pd

    # print(fasid(
    #     fasta_fpn=to('data/example/3puxG.fasta')
    # ))

    # print(read_from_pdb(
    #     pdb_fp=to('data/example/'),
    #     prot_name='1aig',
    #     seq_chain='L',
    #     file_chain='',
    # ))

    # print(read_from_xml(
    #     xml_fp=to('data/example/'),
    #     xml_name='1xqf',
    #     seq_chain='A',
    # ))

    # print(read_from_fasta(
    #     fasta_fpn=to('data/example/1xqfA.fasta')
    # ))

    # print(pdbid(
    #     pdb_fp=to('data/example/'),
    #     prot_name='3pux',
    #     seq_chain='G',
    #     file_chain='G',
    # ))

    # print(retrieve_pdb_from_rcsb(
    #     prot_series=pd.Series(['6e3y', '6rfq', '6t0b']),
    #     # route='biopython',
    #     sv_fp=to('data/'),
    # ))

    # print(retrieve_pdb_from_pdbtm(
    #     prot_series=pd.Series(['6e3y', '6rfq', '6t0b']),
    #     kind='tr',
    #     sv_fp=to('data/'),
    # ))

    print(retrieve_xml_from_pdbtm(
        prot_series=pd.Series(['6e3y', '6rfq', '6t0b']),
        sv_fp=to('data/'),
    ))