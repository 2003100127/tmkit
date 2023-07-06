from typing import List, Tuple
import pandas as pd

__author__: str = "Jianfeng Sun"
__version__: str = "v1.0"
__copyright__: str = "Copyright 2023"
__license__: str = "GPL v3.0"
__email__: str = "jianfeng.sunmt@gmail.com"
__maintainer__: str = "Jianfeng Sun"


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
) -> pd.DataFrame:
    """
    Read data from files and return a pandas DataFrame.

    Parameters
    ----------
    prot_name : str
        Name of the protein.
    seq_chain : str
        Chain ID of the protein.
    fasta_fp : str
        File path of the fasta file.
    pdb_fp : str
        File path of the pdb file.
    dist_fp : str
        File path of the distance file.
    xml_fp : str
        File path of the xml file.
    tool : str
    the tool to use.
    tool_fp : str
        File path of the tool.
    seq_sep_superior : int
        Superior sequence separation.
    seq_sep_inferior : int, optional
        Inferior sequence separation, by default 0.

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
    pair_arr = ppssegment().toPair(fasta_lower_tmh, fasta_upper_tmh)

    sdist, _ = m(
        tool_fp,
        file_name=prot_name,
        file_chain=seq_chain,
        pair_list=pair_arr,
        dist_df=dist_df,
        sort_=2,
    )
    return sdist


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
        Name of the protein.
    seq_chain : str
        Chain ID of the protein.
    fasta_fp : str
        File path of the fasta file.
    pdb_fp : str
        File path of the pdb file.
    dist_fp : str
        File path of the distance file.
    xml_fp : str
        File path of the xml file.
    cutoff : float
        Cutoff value.
    tool_fp : str
        File path of the tool.
    tool : str
        Name of the tool to use.
    seq_sep_inferior : int
        Inferior sequence separation.
    seq_sep_superior : int
        Superior sequence separation.
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
        sort_=sort,
    )
    tool_results = p.fetch()
    p.compare(target=tool_results, cut_off=110)
    # TODO: add return
