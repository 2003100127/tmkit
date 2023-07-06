__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from tmkit.seqnetrr.Controller import controller


from typing import Optional


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
    method : str
        _description_
    fasta_fpn : str
        _description_
    net_fpn : str
        _description_
    window_size : int
        _description_
    pair_mode : str
        _description_
    seq_sep_inferior : int, optional
        _description_, by default 0
    seq_sep_superior : Optional[int], optional
        _description_, by default None
    assign_mode : str, optional
        _description_, by default "hash"
    input_kind : str, optional
        _description_, by default "freecontact"
    cumu_ratio : float, optional
        _description_, by default 1.0
    sv_fpn : Optional[str], optional
        _description_, by default None
    is_sv : bool, optional
        _description_, by default False

    Returns
    -------
    _type_
        _description_
    """
    return controller(
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
