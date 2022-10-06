__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2022"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from tmkit.feature.HelixSurface import helixSurface as hs


def generate_helix_surfaces(
        msa_path,
        prot_name,
        file_chain,
        lips_fpn,
        sv_fp,
        df_prot,
):
    """

    Parameters
    ----------
    msa_path
    prot_name
    file_chain
    lips_fpn
    sv_fp
    df_prot

    Returns
    -------

    """
    return hs(
        msa_path=msa_path,
        prot_name=prot_name,
        file_chain=file_chain,
        lips_fpn=lips_fpn,
        sv_fp=sv_fp,
        df_prot=df_prot
    ).generate()


def bgenerate_helix_surfaces(
        msa_path,
        prot_name,
        file_chain,
        lips_fpn,
        sv_fp,
        df_prot,
):
    """

    Parameters
    ----------
    msa_path
    prot_name
    file_chain
    lips_fpn
    sv_fp
    df_prot

    Returns
    -------

    """
    return hs(
        msa_path=msa_path,
        prot_name=prot_name,
        file_chain=file_chain,
        lips_fpn=lips_fpn,
        sv_fp=sv_fp,
        df_prot=df_prot
    ).bgenerate()


def read(
        msa_path,
        prot_name,
        file_chain,
        lips_fpn,
        sv_fp,
        df_prot,
):
    """

    Parameters
    ----------
    msa_path
    prot_name
    file_chain
    lips_fpn
    sv_fp
    df_prot

    Returns
    -------

    """
    aa_surf_rank, lipos_dict, entropy_dict, lips_dict = hs(
        msa_path=msa_path,
        prot_name=prot_name,
        file_chain=file_chain,
        lips_fpn=lips_fpn,
        sv_fp=sv_fp,
        df_prot=df_prot
    ).read()
    return aa_surf_rank, lipos_dict, entropy_dict, lips_dict


def read_helix_surf(
        msa_path,
        prot_name,
        file_chain,
        lips_fpn,
        sv_fp,
        df_prot,
        id=0,
):
    """

    Parameters
    ----------
    msa_path
    prot_name
    file_chain
    lips_fpn
    sv_fp
    df_prot
    id

    Returns
    -------

    """
    return hs(
        msa_path=msa_path,
        prot_name=prot_name,
        file_chain=file_chain,
        lips_fpn=lips_fpn,
        sv_fp=sv_fp,
        df_prot=df_prot
    ).surface(i=id)


def read_helix_all_surf(
        msa_path,
        prot_name,
        file_chain,
        lips_fpn,
        sv_fp,
        df_prot,
):
    """

    Parameters
    ----------
    msa_path
    prot_name
    file_chain
    lips_fpn
    sv_fp
    df_prot

    Returns
    -------

    """
    return hs(
        msa_path=msa_path,
        prot_name=prot_name,
        file_chain=file_chain,
        lips_fpn=lips_fpn,
        sv_fp=sv_fp,
        df_prot=df_prot
    ).lips()


def get_helix_all_surf_entropy(
        msa_path,
        prot_name,
        file_chain,
        lips_fpn,
        sv_fp,
        df_prot,
):
    """

    Parameters
    ----------
    msa_path
    prot_name
    file_chain
    lips_fpn
    sv_fp
    df_prot

    Returns
    -------

    """
    return hs(
        msa_path=msa_path,
        prot_name=prot_name,
        file_chain=file_chain,
        lips_fpn=lips_fpn,
        sv_fp=sv_fp,
        df_prot=df_prot
    ).lips()[['surfs', 'ents']]


def get_helix_all_surf_lips(
        msa_path,
        prot_name,
        file_chain,
        lips_fpn,
        sv_fp,
        df_prot,
):
    """

    Parameters
    ----------
    msa_path
    prot_name
    file_chain
    lips_fpn
    sv_fp
    df_prot

    Returns
    -------

    """
    return hs(
        msa_path=msa_path,
        prot_name=prot_name,
        file_chain=file_chain,
        lips_fpn=lips_fpn,
        sv_fp=sv_fp,
        df_prot=df_prot
    ).lips()[['surfs', 'lipos']]


def get_helix_all_surf_avelips(
        msa_path,
        prot_name,
        file_chain,
        lips_fpn,
        sv_fp,
        df_prot,
):
    """

    Parameters
    ----------
    msa_path
    prot_name
    file_chain
    lips_fpn
    sv_fp
    df_prot

    Returns
    -------

    """
    return hs(
        msa_path=msa_path,
        prot_name=prot_name,
        file_chain=file_chain,
        lips_fpn=lips_fpn,
        sv_fp=sv_fp,
        df_prot=df_prot
    ).lips()[['surfs', 'lxe']]


def torosseta(
        msa_path,
        prot_name,
        file_chain,
        lips_fpn,
        sv_fp,
        df_prot,
        df_surf_lips,
):
    """

    Parameters
    ----------
    msa_path
    prot_name
    file_chain
    lips_fpn
    sv_fp
    df_prot
    df_surf_lips

    Returns
    -------

    """
    return hs(
        msa_path=msa_path,
        prot_name=prot_name,
        file_chain=file_chain,
        lips_fpn=lips_fpn,
        sv_fp=sv_fp,
        df_prot=df_prot
    ).transformToRosseta(
        df_surf_lips=df_surf_lips,
    )


def get_surf_entropy(
        msa_path,
        prot_name,
        file_chain,
        lips_fpn,
        sv_fp,
        df_prot,
        id=0,
):
    """

    Parameters
    ----------
    msa_path
    prot_name
    file_chain
    lips_fpn
    sv_fp
    df_prot
    id

    Returns
    -------

    """
    return hs(
        msa_path=msa_path,
        prot_name=prot_name,
        file_chain=file_chain,
        lips_fpn=lips_fpn,
        sv_fp=sv_fp,
        df_prot=df_prot
    ).surface(i=id)[['aa_ids', 'ents']]


def get_surf_lips(
        msa_path,
        prot_name,
        file_chain,
        lips_fpn,
        sv_fp,
        df_prot,
        id=0,
):
    """

    Parameters
    ----------
    msa_path
    prot_name
    file_chain
    lips_fpn
    sv_fp
    df_prot
    id

    Returns
    -------

    """
    return hs(
        msa_path=msa_path,
        prot_name=prot_name,
        file_chain=file_chain,
        lips_fpn=lips_fpn,
        sv_fp=sv_fp,
        df_prot=df_prot
    ).surface(i=id)[['aa_ids', 'lipos']]


if __name__ == "__main__":
    from tmkit.Path import to
    import pandas as pd

    # df_prot = pd.DataFrame([['1xqf', 'A'],], columns=['prot', 'chain'])
    df_prot = None

    # print(generate_helix_surfaces(
    #     msa_path=to('data/example/'),
    #     prot_name='1xqf',
    #     file_chain='A',
    #     lips_fpn=to('feature/lips/lips.pl'),
    #     sv_fp=to('data/example/'),
    #     df_prot=df_prot,
    # ))

    # print(bgenerate_helix_surfaces(
    #     msa_path=to('data/example/'),
    #     prot_name='1xqf',
    #     file_chain='A',
    #     lips_fpn=to('feature/lips/lips.pl'),
    #     sv_fp=to('data/example/'),
    #     df_prot=df_prot,
    # ))

    # print(read_helix_surf(
    #     msa_path=to('data/example/'),
    #     prot_name='1xqf',
    #     file_chain='A',
    #     lips_fpn=to('feature/lips/lips.pl'),
    #     sv_fp=to('data/example/'),
    #     df_prot=df_prot,
    #     id=1,
    # ))

    # print(get_surf_entropy(
    #     msa_path=to('data/example/'),
    #     prot_name='1xqf',
    #     file_chain='A',
    #     lips_fpn=to('feature/lips/lips.pl'),
    #     sv_fp=to('data/example/'),
    #     df_prot=df_prot,
    #     id=1,
    # ))

    print(get_surf_lips(
        msa_path=to('data/example/'),
        prot_name='1xqf',
        file_chain='A',
        lips_fpn=to('feature/lips/lips.pl'),
        sv_fp=to('data/example/'),
        df_prot=df_prot,
        id=1,
    ))

    # df_surf_lips = read_helix_all_surf(
    #     msa_path=to('data/example/'),
    #     prot_name='1xqf',
    #     file_chain='A',
    #     lips_fpn=to('feature/lips/lips.pl'),
    #     sv_fp=to('data/example/'),
    #     df_prot=df_prot,
    # )
    # print(df_surf_lips)

    print(get_helix_all_surf_lips(
        msa_path=to('data/example/'),
        prot_name='1xqf',
        file_chain='A',
        lips_fpn=to('feature/lips/lips.pl'),
        sv_fp=to('data/example/'),
        df_prot=df_prot,
    ))

    # print(get_helix_all_surf_entropy(
    #     msa_path=to('data/example/'),
    #     prot_name='1xqf',
    #     file_chain='A',
    #     lips_fpn=to('feature/lips/lips.pl'),
    #     sv_fp=to('data/example/'),
    #     df_prot=df_prot,
    # ))

    print(get_helix_all_surf_avelips(
        msa_path=to('data/example/'),
        prot_name='1xqf',
        file_chain='A',
        lips_fpn=to('feature/lips/lips.pl'),
        sv_fp=to('data/example/'),
        df_prot=df_prot,
    ))

    aa_surf_rank, lipos_dict, entropy_dict, lips_dict = read(
        msa_path=to('data/example/'),
        prot_name='1xqf',
        file_chain='A',
        lips_fpn=to('feature/lips/lips.pl'),
        sv_fp=to('data/example/'),
        df_prot=df_prot,
    )
    # print(aa_surf_rank)
    print(lipos_dict)
    # print(entropy_dict)
    # print(lips_dict)

    # print(torosseta(
    #     msa_path=to('data/example/'),
    #     prot_name='1xqf',
    #     file_chain='A',
    #     lips_fpn=to('feature/lips/lips.pl'),
    #     sv_fp=to('data/example/'),
    #     df_prot=df_prot,
    #     df_surf_lips=df_surf_lips,
    # ))