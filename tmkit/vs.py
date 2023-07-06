__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from tmkit.visualize.func.Coloring import coloring as func_coloring
from tmkit.visualize.isite.ProtocolDeepTMInter import protocolDeepTMInter
from tmkit.visualize.small.Local import local


from typing import List, Tuple


def protoc_deeptminter(
    prot_name: str,
    prot_chain: str,
    pdb_chain_fp: str,
    pdb_complex_fp: str,
    tool: str,
    isite_fp: str,
    dist_fp: str,
    sv_bfactor_fp: str,
    pymol_bg_chain_ids: List[str],
    draw_type: str,
    bg_chain_color: str = "raspberry",  # chromium, xenon, technetium, germanium
    color_list: str = "white smudge",
) -> None:
    """
    Parameters
    ----------
    prot_name : str
    prot_chain : str
    pdb_chain_fp : str
    pdb_complex_fp : str
    tool : str
    isite_fp : str
    dist_fp : str
    sv_bfactor_fp : str
    pymol_bg_chain_ids : List[str]
    draw_type : str
    bg_chain_color : str, optional
        Default is "raspberry".
    color_list : str, optional
        Default is "white smudge".

    Returns
    -------
    None
    """
    protocolDeepTMInter(
        prot_name=prot_name,
        prot_chain=prot_chain,
        pdb_chain_fp=pdb_chain_fp,
        pdb_complex_fp=pdb_complex_fp,
        tool=tool,
        isite_fp=isite_fp,
        sv_bfactor_fp=sv_bfactor_fp,
        dist_fp=dist_fp,
        pymol_bg_chain_ids=pymol_bg_chain_ids,
        draw_type=draw_type,
        bg_chain_color=bg_chain_color,
        color_list=color_list,
    )


def coloring(
    pdb_fp: str,
    prot_name: str,
    seq_chain: str,
    prot_c: str,
    names: List[str] = ["n1", "n2", "n3", "n4", "n5"],
    actions: List[str] = ["resi 1-4", "resi 58-61",
                          "resi 5-57", "i. 62-81", "i. 62+78+81"],
    colors: List[str] = ["red", "red", "orange", "br4", "violet"],
    forms: List[str] = ["lines", "lines", "lines", "lines", "lines"],
) -> None:
    """
    Parameters
    ----------
    pdb_fp : str
    prot_name : str
    seq_chain : str
    prot_c : str
    names : List[str], optional
        Default is ["n1", "n2", "n3", "n4", "n5"].
    actions : List[str], optional
        Default is ["resi 1-4", "resi 58-61", "resi 5-57", "i. 62-81", "i. 62+78+81"].
    colors : List[str], optional
        Default is ["red", "red", "orange", "br4", "violet"].
    forms : List[str], optional
        Default is ["lines", "lines", "lines", "lines", "lines"].

    Returns
    -------
    None
    """
    func_coloring(
        pdb_fp=pdb_fp,
        prot_name=prot_name,
        seq_chain=seq_chain,
        prot_c=prot_c,
        names=names,
        actions=actions,
        colors=colors,
        forms=forms,
    )


def sm_local(
    prot_name: str,
    pdb_complex_fp: str,
    sm_rep: str,
    nby_rep: str,
    prot_c: str,
    sm_c: str,
    pocket_rep: str,
) -> None:
    """
    Parameters
    ----------
    prot_name : str
    pdb_complex_fp : str
    sm_rep : str
    nby_rep : str
    prot_c : str
    sm_c : str
    pocket_rep : str

    Returns
    -------
    None
    """
    local(
        prot_name=prot_name,
        pdb_complex_fp=pdb_complex_fp,
        sm_rep=sm_rep,
        nby_rep=nby_rep,
        prot_c=prot_c,
        sm_c=sm_c,
        pocket_rep=pocket_rep,
    )
