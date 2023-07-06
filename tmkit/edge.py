__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from tmkit.seqnetrr.Controller import controller


def extract(
        method,
        fasta_fpn,
        net_fpn,
        window_size,
        pair_mode,
        seq_sep_inferior=0,
        seq_sep_superior=None,
        assign_mode='hash',
        input_kind='freecontact',
        cumu_ratio=1.,
        sv_fpn=None,
        is_sv=False,
):
    return controller(
        mode='internal',
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