__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import Tuple

import pandas as pd

from tmkit.contact.Evaluator import evaluator
from tmkit.contact.Reader import Reader as rrcreader
from tmkit.id.Fasta import Fasta as idfasta
from tmkit.id.PDB import PDB as idpdb
from tmkit.position.scenario.Segment import Segment as ppssegment
from tmkit.structure.rrc.Label import Label as dlable
from tmkit.topology.pdbtm.ToFastaId import toFastaId
from tmkit.util.Kit import chainid


def read(
    prot_name: str,
    seq_chain: str,
    fasta_fp: str,
    pdb_fp: str,
    dist_fp: str,
    xml_fp: str,
    tool: str,
    tool_fp: str,
    seq_sep_superior: int,
    seq_sep_inferior: int = 0,
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Read data from files and return a pandas DataFrame.

    Parameters
    ----------
    prot_name : str
        name of a protein in the prefix of a PDB file name (e.g., 1xqf in 1xqfA.pdb).
    seq_chain : str
        chain of a protein in the prefix of a PDB file name (e.g., A in 1xqfA.pdb). Parameter file_chain will be converted within the function.
    fasta_fp : str
        path where a target Fasta file is placed.
    pdb_fp : str
        path where a target PDB file is placed.
    dist_fp : str
        path where a file containing real distances between residues is placed (please check the file at ./data/rrc in the example dataset).
    xml_fp : str
        path where a target XML file is placed.
    cutoff : float
        distance cutoff to see whether two residues are in spatial contact (e.g., 5.5 angstrom).
    tool_fp : str
        path where a protein residue contact map file is placed.
    tool : str
        name of a contact prediction tool. It can be one of PSICOV, FreeContact, CCMPred, Gremlin, GDCA, PlmDCA, MemConP, Membrain2, and DeepHelicon.
    seq_sep_inferior : int
        The lower bounds of how far any two residues are in pairs.
    seq_sep_superior : int
        The upper bounds of how far any two residues are in pairs.
    sort : int, optional
        Sorting method, by default 2.

    Returns
    -------
    pd.DataFrame
        A pandas DataFrame containing the data.
    """
    if tool == "psicov":
        m = rrcreader().psicov
    elif tool == "mi":
        m = rrcreader().mi
    elif tool == "freecontact":
        m = rrcreader().freecontact
    elif tool == "ccmpred":
        m = rrcreader().ccmpred
    elif tool == "gremlin":
        m = rrcreader().gremlin
    elif tool == "gdca":
        m = rrcreader().gdca
    elif tool == "plmc":
        m = rrcreader().plmc
    elif tool == "memconp":
        m = rrcreader().memconp
    elif tool == "membrain2":
        m = rrcreader().membrain2
    else:
        m = rrcreader().deephelicon

    dist_df = dlable(
        dist_path=dist_fp,
        prot_name=prot_name,
        file_chain=chainid(seq_chain),
        seq_sep_inferior=seq_sep_inferior,
        seq_sep_superior=seq_sep_superior,
    ).attach()

    pdbids = idpdb(
        pdb_fp=pdb_fp,
        prot_name=prot_name,
        seq_chain=seq_chain,
        file_chain=chainid(seq_chain),
    ).chain()

    fasids = idfasta().get(
        fasta_fpn=fasta_fp + prot_name + chainid(seq_chain) + ".fasta"
    )
    fasta_lower_tmh, fasta_upper_tmh = toFastaId().tmh(
        pdbid_map=pdbids,
        fasid_map=fasids,
        xml_fp=xml_fp,
        prot_name=prot_name,
        seq_chain=seq_chain,
    )
    pair_arr = ppssegment().to_pair(fasta_lower_tmh, fasta_upper_tmh)

    sdist, sdist_true = m(
        tool_fp,
        file_name=prot_name,
        file_chain=seq_chain,
        pair_list=pair_arr,
        dist_df=dist_df,
        sort_=2,
    )
    return (sdist, sdist_true)


def evaluate(
    prot_name: str,
    seq_chain: str,
    fasta_fp: str,
    pdb_fp: str,
    dist_fp: str,
    xml_fp: str,
    cutoff: float,
    tool_fp: str,
    tool: str,
    seq_sep_inferior: int,
    seq_sep_superior: int,
    sort: int = 2,
) -> None:
    """
    Evaluate the data and print the results.

    Parameters
    ----------
    prot_name : str
        name of a protein in the prefix of a PDB file name (e.g., 1xqf in 1xqfA.pdb).
    seq_chain : str
        chain of a protein in the prefix of a PDB file name (e.g., A in 1xqfA.pdb). Parameter file_chain will be converted within the function.
    fasta_fp : str
        path where a target Fasta file is placed.
    pdb_fp : str
        path where a target PDB file is placed.
    dist_fp : str
        path where a file containing real distances between residues is placed (please check the file at ./data/rrc in the example dataset).
    xml_fp : str
        path where a target XML file is placed.
    cutoff : float
        distance cutoff to see whether two residues are in spatial contact (e.g., 5.5 angstrom).
    tool_fp : str
        path where a protein residue contact map file is placed.
    tool : str
        name of a contact prediction tool. It can be one of PSICOV, FreeContact, CCMPred, Gremlin, GDCA, PlmDCA, MemConP, Membrain2, and DeepHelicon.
    seq_sep_inferior : int
        The lower bounds of how far any two residues are in pairs.
    seq_sep_superior : int
        The upper bounds of how far any two residues are in pairs.
    sort : int, optional
        Sorting method, by default 2.
    """
    dist_df = dlable(
        dist_path=dist_fp,
        prot_name=prot_name,
        file_chain=chainid(seq_chain),
        seq_sep_inferior=0,
        seq_sep_superior=seq_sep_superior,
    ).attach()

    pdbids = idpdb(
        pdb_fp=pdb_fp,
        prot_name=prot_name,
        seq_chain=seq_chain,
        file_chain=chainid(seq_chain),
    ).chain()

    fasids = idfasta().get(
        fasta_fpn=fasta_fp + prot_name + chainid(seq_chain) + ".fasta"
    )
    fasta_lower_tmh, fasta_upper_tmh = toFastaId().tmh(
        pdbid_map=pdbids,
        fasid_map=fasids,
        xml_fp=xml_fp,
        prot_name=prot_name,
        seq_chain=seq_chain,
    )
    pair_arr = ppssegment().to_pair(fasta_lower_tmh, fasta_upper_tmh)

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
        sort_=sort,
    )
    tool_results = p.fetch()
    p.compare(target=tool_results, cut_off=110)
