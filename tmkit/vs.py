__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2022"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"


import sys
sys.path.append('./')
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


if __name__ == "__main__":
    from tmkit.Path import to

    protoc_deeptminter(
        # prot_name='5b0w',  # 6t0b, 5b0w, 6uiw
        # prot_chain='A',  # m, A
        # pdb_chain_fp=to('data/example/pdb/testdata/'), # indepdata, testdata
        # dist_fp=to('data/example/dist/testdata/'), # indepdata, testdata
        # pdb_complex_fp=to('data/example/pdb/testdata/pdbtm/'), # indepdata, testdata
        # tool='graphppis', # deeptminter, 'delphi', 'mbpred', 'graphppis'
        # draw_type='label_predicted', # label_actual, label_predicted, probability
        # # isite_fp=to('data/example/isite/deeptminter/testdata/'),
        # isite_fp=to('data/example/isite/graphppis/pdbtm_fast/'),
        # sv_bfactor_fp=to('data/example/bfactor/graphppis/5b0w/'),
        # # pymol_bg_chain_ids='B+C+J+K', # 6t0b
        # pymol_bg_chain_ids='c+j+k', # 5b0w

        prot_name='6e3y',  # 6t0b, 5b0w, 6uiw
        prot_chain='E',  # m, A
        pdb_chain_fp=to('data/example/pdb/indepdata/'),  # indepdata, testdata
        dist_fp=to('data/example/dist/indepdata/'),  # indepdata, testdata
        pdb_complex_fp=to('data/example/pdb/indepdata/pdbtm/'),  # indepdata, testdata
        tool='deeptminter',  # deeptminter, 'delphi', 'mbpred', 'graphppis'
        draw_type='probability',  # label_actual, label_predicted, probability
        isite_fp=to('data/example/isite/deeptminter/indepdata/'),
        # isite_fp=to('data/example/isite/graphppis/pdbtm_fast/'),
        sv_bfactor_fp=to('data/example/bfactor/deeptminter/6e3y/'),
        # pymol_bg_chain_ids='B+C+J+K', # 6t0b
        pymol_bg_chain_ids='c+j+k',  # 5b0w
    )

    # coloring(
    #     pdb_fp=to('data/example/pdb/indepdata/'),
    #     prot_name='6uiw',
    #     seq_chain='A',
    #     prot_c='chromium',
    #
    #     # names=['n1', 'n2', 'n3', 'n4', 'n5'],
    #     # actions=['resi 1-4', 'resi 58-61', 'resi 5-57', 'i. 62-81', 'i. 62+78+81'],
    #     # colors=['red', 'red', 'orange', 'br4', 'violet', ],
    #     # forms=['lines', 'lines', 'lines', 'lines', 'lines', ],
    #
    #     names=['n1', 'n2', 'n3'],
    #     actions=['i. 116+118+140+141+151+152+153+155+156+157+158+159+163+166+179+181+182+183+195+200+201+202+204', 'resi 143-149', 'resi 185-193'],
    #     colors=['violet', 'violet', 'violet', ],
    #     forms=['lines', 'lines', 'lines', ],
    # )

    # sm_local(
    #     prot_name='6feq',
    #     pdb_complex_fp=to('data/example/vs/'),
    #     sm_rep="sticks",
    #     nby_rep='sticks',
    #     prot_c='blue_white_magenta',
    #     sm_c='blue_green',
    #     pocket_rep='stick'
    # )