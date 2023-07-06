__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from tmkit.contact.Reader import reader as rrcreader
from tmkit.contact.Evaluator import evaluator
from tmkit.id.Fasta import fasta as idfasta
from tmkit.id.PDB import pdb as idpdb
from tmkit.util.Kit import chainid
from tmkit.topology.pdbtm.ToFastaId import toFastaId
from tmkit.position.scenario.Segment import segment as ppssegment
from tmkit.structure.rrc.Label import label as dlable


def read(
        prot_name,
        seq_chain,
        fasta_fp,
        pdb_fp,
        dist_fp,
        xml_fp,
        tool,
        tool_fp,
        seq_sep_superior,
        seq_sep_inferior=0,
):
    """

    Parameters
    ----------
    prot_name
    seq_chain
    fasta_fp
    pdb_fp
    dist_fp
    xml_fp
    tool
    tool_fp
    seq_sep_superior
    seq_sep_inferior

    Returns
    -------

    """
    if tool == 'psicov':
        m = rrcreader().psicov
    elif tool == 'mi':
        m = rrcreader().mi
    elif tool == 'freecontact':
        m = rrcreader().freecontact
    elif tool == 'ccmpred':
        m = rrcreader().ccmpred
    elif tool == 'gremlin':
        m = rrcreader().gremlin
    elif tool == 'gdca':
        m = rrcreader().gdca
    elif tool == 'plmc':
        m = rrcreader().plmc
    elif tool == 'memconp':
        m = rrcreader().memconp
    elif tool == 'membrain2':
        m = rrcreader().membrain2
    else:
        m = rrcreader().deephelicon

    dist_df = dlable(
        dist_path=dist_fp,
        prot_name=prot_name,
        file_chain=chainid(seq_chain),
        seq_sep_inferior=seq_sep_inferior,
        seq_sep_superior=seq_sep_superior
    ).attach()

    pdbids = idpdb(
        pdb_fp=pdb_fp,
        prot_name=prot_name,
        seq_chain=seq_chain,
        file_chain=chainid(seq_chain),
    ).chain()

    fasids = idfasta().get(fasta_fpn=fasta_fp + prot_name + chainid(seq_chain) + '.fasta')
    fasta_lower_tmh, fasta_upper_tmh = toFastaId().tmh(
        pdbid_map=pdbids,
        fasid_map=fasids,
        xml_fp=xml_fp,
        prot_name=prot_name,
        seq_chain=seq_chain,
    )
    pair_arr = ppssegment().toPair(fasta_lower_tmh, fasta_upper_tmh)

    sdist = m(
        tool_fp,
        file_name=prot_name,
        file_chain=seq_chain,
        pair_list=pair_arr,
        dist_df=dist_df,
        sort_=2
    )
    return sdist


def evaluate(
        prot_name,
        seq_chain,
        fasta_fp,
        pdb_fp,
        dist_fp,
        xml_fp,
        cutoff,
        tool_fp,
        tool,
        seq_sep_inferior,
        seq_sep_superior,
        sort=2,
):
    """

    Parameters
    ----------
    prot_name
    seq_chain
    fasta_fp
    pdb_fp
    dist_fp
    xml_fp
    cutoff
    tool_fp
    tool
    seq_sep_inferior
    seq_sep_superior
    sort

    Returns
    -------

    """
    dist_df = dlable(
        dist_path=dist_fp,
        prot_name=prot_name,
        file_chain=chainid(seq_chain),
        seq_sep_inferior=0,
        seq_sep_superior=seq_sep_superior
    ).attach()

    pdbids = idpdb(
        pdb_fp=pdb_fp,
        prot_name=prot_name,
        seq_chain=seq_chain,
        file_chain=chainid(seq_chain),
    ).chain()

    fasids = idfasta().get(fasta_fpn=fasta_fp + prot_name + chainid(seq_chain) + '.fasta')
    fasta_lower_tmh, fasta_upper_tmh = toFastaId().tmh(
        pdbid_map=pdbids,
        fasid_map=fasids,
        xml_fp=xml_fp,
        prot_name=prot_name,
        seq_chain=seq_chain,
    )
    pair_arr = ppssegment().toPair(fasta_lower_tmh, fasta_upper_tmh)

    p = evaluator(
        prot_name=prot_name,
        file_chain=chainid(seq_chain),
        dist_df=dist_df,
        pair_list=pair_arr,
        dist_limit=cutoff,
        tool_fp=tool_fp,
        tool=tool,
        seq_sep_inferior=seq_sep_inferior,
        seq_sep_superior=seq_sep_superior,
        sort_=sort
    )
    tool_results = p.fetch()
    p.compare(target=tool_results, cut_off=110)
    return