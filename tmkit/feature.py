__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from tmkit.property.HelixSurface import helixSurface as hs


def generate_helix_surfaces(
        msa_path,
        prot_name,
        file_chain,
        lips_fpn,
        sv_fp,
):
    """"""
    return hs(
        msa_path=msa_path,
        prot_name=prot_name,
        file_chain=file_chain,
        lips_fpn=lips_fpn,
        sv_fp=sv_fp,
    ).generate()


def bgenerate_helix_surfaces(
        msa_path,
        lips_fpn,
        sv_fp,
        df_prot,
):
    """"""
    return hs(
        msa_path=msa_path,
        lips_fpn=lips_fpn,
        sv_fp=sv_fp,
        df_prot=df_prot
    ).bgenerate()


def read(
        fp,
        prot_name,
        file_chain,
):
    """"""
    aa_surf_rank, lipos_dict, entropy_dict, lips_dict = hs(
        prot_name=prot_name,
        file_chain=file_chain,
        sv_fp=fp,
    ).read()
    return aa_surf_rank, lipos_dict, entropy_dict, lips_dict


def read_helix_surf(
        fp,
        prot_name,
        file_chain,
        id=0,
):
    """"""
    return hs(
        prot_name=prot_name,
        file_chain=file_chain,
        sv_fp=fp,
    ).surface(i=id)


def read_helix_all_surf(
        fp,
        prot_name,
        file_chain,
):
    """"""
    return hs(
        prot_name=prot_name,
        file_chain=file_chain,
        sv_fp=fp,
    ).lips()


def get_helix_all_surf_entropy(
        fp,
        prot_name,
        file_chain,
):
    """"""
    return hs(
        prot_name=prot_name,
        file_chain=file_chain,
        sv_fp=fp,
    ).lips()[['surfs', 'ents']]


def get_helix_all_surf_lips(
        fp,
        prot_name,
        file_chain,
):
    """"""
    return hs(
        prot_name=prot_name,
        file_chain=file_chain,
        sv_fp=fp,
    ).lips()[['surfs', 'lipos']]


def get_helix_all_surf_avelips(
        fp,
        prot_name,
        file_chain,
):
    """"""
    return hs(
        prot_name=prot_name,
        file_chain=file_chain,
        sv_fp=fp,
    ).lips()[['surfs', 'lxe']]


def torosseta(
        fp,
        prot_name,
        file_chain,
        df_surf_lips,
):
    """"""
    return hs(
        sv_fp=fp,
        prot_name=prot_name,
        file_chain=file_chain,
    ).transformToRosseta(
        df_surf_lips=df_surf_lips,
    )


def get_surf_entropy(
        fp,
        prot_name,
        file_chain,
        id=0,
):
    """"""
    return hs(
        prot_name=prot_name,
        file_chain=file_chain,
        sv_fp=fp,
    ).surface(i=id)[['aa_ids', 'ents']]


def get_surf_lips(
        fp,
        prot_name,
        file_chain,
        id=0,
):
    """"""
    return hs(
        prot_name=prot_name,
        file_chain=file_chain,
        sv_fp=fp,
    ).surface(i=id)[['aa_ids', 'lipos']]