__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import List

from tmkit.visualize.func.Coloring import Coloring as func_coloring
from tmkit.visualize.isite.ProtocolDeepTMInter import ProtocolDeepTMInter
from tmkit.visualize.small.Local import Local


def protoc_deeptminter(
    prot_name: str,
    prot_chain: str,
    pdb_chain_fp: str,
    pdb_complex_fp: str,
    tool: str,
    isite_fp: str,
    dist_fp: str,
    sv_bfactor_fp: str,
    pymol_bg_chain_ids: str,
    draw_type: str,
    bg_chain_color: str = "raspberry",  # chromium, xenon, technetium, germanium
    color_list: str = "white smudge",
) -> None:
    """
    Parameters
    ----------
    prot_name : str
        name of a protein in the prefix of a PDB file name (e.g., 1xqf in 1xqfA.pdb).
    prot_chain : str
        chain of a protein in the prefix of a PDB file name (e.g., A in 1xqfA.pdb).
    pdb_chain_fp : str
        path where a target PDB file is place.
    dist_fp : str
        path where a file containing real distances between residues is placed (please check the file at ./data/rrc in the example dataset).
    pdb_complex_fp : str
        path where a PDB file showing a protein complex is placed.
    tool : str
        tool name. Currently, the reading of DeepTMInter, DELPHI, and MBPred files is supported.
    isite_fp : str
        path where a file showing interaction sites and the interaction likelihoods is placed.
    sv_bfactor_fp : str
        path to save a bfactor file.
    bg_chain_ids : str
        interaction chains in a protein complex.
    bg_chain_color : str
        color of interaction chains in a protein complex.
    draw_type : str
        label_actual, # label_actual, label_predicted, probability

    Returns
    -------
    None
    """
    ProtocolDeepTMInter(
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
    actions: List[str] = [
        "resi 1-4",
        "resi 58-61",
        "resi 5-57",
        "i. 62-81",
        "i. 62+78+81",
    ],
    colors: List[str] = ["red", "red", "orange", "br4", "violet"],
    forms: List[str] = ["lines", "lines", "lines", "lines", "lines"],
) -> None:
    """
    Identification of protein-protein interaction (PPI) interfaces
    of proteins is critical to understand the biological processes
    governed by them. Direct visualization of the PPI interfaces on
     3D structures can facilitate their localization at the atomic
     coordinate level. TMKit is an open-source toolkit that enables
    access to the PPI interfaces by taking as input the structure
    of a protein of interest (POI) and a list of probabilities
    of residue sites to be involved in interactions. The program
    can automatically generate the label- or propensity-based
    PPI interfaces in between a POI and its interacting proteins
     (or its larger complex), which can be visualised in PyMOL.

    Parameters
    ----------
    prot_name : str
        name of a protein in the prefix of a PDB file name (e.g., 1xqf in 1xqfA.pdb).
    seq_chain : str
        chain of a protein in the prefix of a PDB file name (e.g., A in 1xqfA.pdb).
    pdb_fp : str
        path where a target PDB file is place.
    prot_c : str
        color of the entire protein.
    names : List[str], optional
        names of segments. Default is ["n1", "n2", "n3", "n4", "n5"].
    actions : List[str], optional
        which segments. Default is ["resi 1-4", "resi 58-61", "resi 5-57", "i. 62-81", "i. 62+78+81"].
    colors : List[str], optional
        colors selected for the segments. Default is ["red", "red", "orange", "br4", "violet"].
    forms : List[str], optional
        representation. Default is ["lines", "lines", "lines", "lines", "lines"].

    Returns
    -------
    None
        The PyMOL window showing the structure.

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
        name of a protein in the prefix of a PDB file name (e.g., 1xqf in 1xqfA.pdb).
    pdb_complex_fp : str
        path where a target protein complex file is place.
    prot_c : str
        color of the entire protein.
    sm_rep : str
        representation of a ligand.
    nby_rep : str
        representation of amino acid residues surrounding a ligand.
    sm_c : str
        color of a ligand.

    Returns
    -------
    None
        The PyMOL window showing the structure.
    """
    Local(
        prot_name=prot_name,
        pdb_complex_fp=pdb_complex_fp,
        sm_rep=sm_rep,
        nby_rep=nby_rep,
        prot_c=prot_c,
        sm_c=sm_c,
        pocket_rep=pocket_rep,
    )
