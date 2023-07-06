__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from tmkit.visualize.isite.ProtocolDeepTMInter import protocolDeepTMInter
from tmkit.visualize.func.Coloring import coloring as func_coloring
from tmkit.visualize.small.Local import local


def protoc_deeptminter(
        prot_name,
        prot_chain,
        pdb_chain_fp,
        pdb_complex_fp,
        tool,
        isite_fp,
        dist_fp,
        sv_bfactor_fp,
        pymol_bg_chain_ids,
        draw_type,
        bg_chain_color='raspberry',  # chromium, xenon, technetium, germanium
        color_list='white smudge',
):
    """

    Parameters
    ----------
    prot_name
    prot_chain
    pdb_chain_fp
    pdb_complex_fp
    tool
    isite_fp
    dist_fp
    sv_bfactor_fp
    pymol_bg_chain_ids
    draw_type
    bg_chain_color
    color_list

    Returns
    -------

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
        pdb_fp,
        prot_name,
        seq_chain,
        prot_c,
        names=['n1', 'n2', 'n3', 'n4', 'n5'],
        actions=['resi 1-4', 'resi 58-61', 'resi 5-57', 'i. 62-81', 'i. 62+78+81'],
        colors=['red', 'red', 'orange', 'br4', 'violet',],
        forms=['lines', 'lines', 'lines', 'lines', 'lines', ],
):
    """

    Parameters
    ----------
    pdb_fp
    prot_name
    seq_chain
    prot_c
    names
    actions
    colors
    forms

    Returns
    -------

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
        prot_name,
        pdb_complex_fp,
        sm_rep,
        nby_rep,
        prot_c,
        sm_c,
        pocket_rep,
):
    """

    Parameters
    ----------
    prot_name
    pdb_complex_fp
    sm_rep
    nby_rep
    prot_c
    sm_c
    pocket_rep

    Returns
    -------

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