__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2022"
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
        verbose=True,
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
        verbose=verbose,
    )


if __name__ == "__main__":
    from tmkit.Path import to
    print(extract(
        method='unipartite', # unipartite, bipartite, cumulative
        fasta_fpn=to('data/seqnetrr/example/1aigL.fasta'), # 5lkiA 1aigL
        net_fpn=to('data/seqnetrr/example/1aigL.evfold'), # 5lkiA 1aigL
        window_size=2,
        seq_sep_inferior=0,
        seq_sep_superior=None,
        verbose=True,
        pair_mode='patch',  # cross, memconp, unchanged
        assign_mode='hash',
        input_kind='freecontact',  # general, simulate
        cumu_ratio=1.,
        is_sv=True,
        sv_fpn=to('data/seqnetrr/example/') + 'output.txt',
    ))
