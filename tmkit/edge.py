__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import Optional

from tmkit.seqnetrr.Controller import Controller


def extract(
    method: str,
    fasta_fpn: str,
    net_fpn: str,
    window_size: int,
    pair_mode: str,
    seq_sep_inferior: int = 0,
    seq_sep_superior: Optional[int] = None,
    assign_mode: str = "hash",
    input_kind: str = "freecontact",
    cumu_ratio: float = 1.0,
    sv_fpn: Optional[str] = None,
    is_sv: bool = False,
):
    """_summary_

    Parameters
    ----------
    method: str
        name of a contact prediction method. It can be one of PSICOV, FreeContact, CCMPred, Gremlin, GDCA, PlmDCA, MemConP, Membrain2, and DeepHelicon.
    fasta_fpn: str
        path where a target Fasta file is placed.
    net_fpn: str
        path to a protein residue contact map file.
    window_size: int
        window size
    seq_sep_inferior: int
        The lower bounds of how far any two residues are in pairs.
    seq_sep_superior: int
        The upper bounds of how far any two residues are in pairs.
    mode: str
        internal or external
    pair_mode: str
        mode of global pairs: patch | memconp | cross | unchanged
    assign_mode: str
        mode of assignment: hash | hash_ori | hash_rl | pandas | numpy
    input_kind: str
        input kind for relationships of a network file: general | simulate | freecontact | gdca | cmmpred | plmc
    list_2d: List
        2d list.
    cumu_ratio: float
        cumulative ratio.
    is_sv: bool
         if save files.
    sv_fpn: str
        path to where you want to save files.

    Returns
    -------
    List
        2D list
    """
    return Controller(
        mode="internal",
        method=method,
        assign_mode=assign_mode,
        fasta_fpn=fasta_fpn,
        net_fpn=net_fpn,
        window_size=window_size,
        seq_sep_inferior=seq_sep_inferior,
        seq_sep_superior=seq_sep_superior,
        pair_mode=pair_mode,
        input_kind=input_kind,
        cumu_ratio=cumu_ratio,
        is_sv=is_sv,
        sv_fpn=sv_fpn,
    )
