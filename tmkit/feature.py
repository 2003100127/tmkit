__author__: str = "Jianfeng Sun"
__version__: str = "v1.0"
__copyright__: str = "Copyright 2023"
__license__: str = "GPL v3.0"
__email__: str = "jianfeng.sunmt@gmail.com"
__maintainer__: str = "Jianfeng Sun"


from typing import List, Tuple, Dict, Any
from tmkit.property.HelixSurface import helixSurface as hs


def generate_helix_surfaces(
    msa_path: str,
    prot_name: str,
    file_chain: str,
    lips_fpn: str,
    sv_fp: str,
) -> Dict[str, Any]:
    """_summary_

    Parameters
    ----------
    msa_path : str
        _description_
    prot_name : str
        _description_
    file_chain : str
        _description_
    lips_fpn : str
        _description_
    sv_fp : str
        _description_

    Returns
    -------
    Dict[str, Any]
        _description_
    """
    return hs(
        msa_path=msa_path,
        prot_name=prot_name,
        file_chain=file_chain,
        lips_fpn=lips_fpn,
        sv_fp=sv_fp,
    ).generate()


def bgenerate_helix_surfaces(
    msa_path: str,
    lips_fpn: str,
    sv_fp: str,
    df_prot: Dict[str, Any],
) -> Dict[str, Any]:
    """_summary_

    Parameters
    ----------
    msa_path : str
        _description_
    lips_fpn : str
        _description_
    sv_fp : str
        _description_
    df_prot : Dict[str, Any]
        _description_

    Returns
    -------
    Dict[str, Any]
        _description_
    """
    return hs(
        msa_path=msa_path, lips_fpn=lips_fpn, sv_fp=sv_fp, df_prot=df_prot
    ).bgenerate()


def read(
    fp: str,
    prot_name: str,
    file_chain: str,
) -> Tuple[List[str], Dict[str, Any], Dict[str, Any], Dict[str, Any]]:
    """_summary_

    Parameters
    ----------
    fp : str
        _description_
    prot_name : str
        _description_
    file_chain : str
        _description_

    Returns
    -------
    Tuple[List[str], Dict[str, Any], Dict[str, Any], Dict[str, Any]]
        _description_
    """
    aa_surf_rank, lipos_dict, entropy_dict, lips_dict = hs(
        prot_name=prot_name,
        file_chain=file_chain,
        sv_fp=fp,
    ).read()
    return aa_surf_rank, lipos_dict, entropy_dict, lips_dict


def read_helix_surf(
    fp: str,
    prot_name: str,
    file_chain: str,
    id: int = 0,
) -> Dict[str, Any]:
    """_summary_

    Parameters
    ----------
    fp : str
        _description_
    prot_name : str
        _description_
    file_chain : str
        _description_
    id : int, optional
        _description_, by default 0

    Returns
    -------
    Dict[str, Any]
        _description_
    """
    return hs(
        prot_name=prot_name,
        file_chain=file_chain,
        sv_fp=fp,
    ).surface(i=id)


def read_helix_all_surf(
    fp: str,
    prot_name: str,
    file_chain: str,
) -> Dict[str, Any]:
    """_summary_

    Parameters
    ----------
    fp : str
        _description_
    prot_name : str
        _description_
    file_chain : str
        _description_

    Returns
    -------
    Dict[str, Any]
        _description_
    """
    return hs(
        prot_name=prot_name,
        file_chain=file_chain,
        sv_fp=fp,
    ).lips()


def get_helix_all_surf_entropy(
    fp: str,
    prot_name: str,
    file_chain: str,
) -> Dict[str, Any]:
    """_summary_

    Parameters
    ----------
    fp : str
        _description_
    prot_name : str
        _description_
    file_chain : str
        _description_

    Returns
    -------
    Dict[str, Any]
        _description_
    """
    return hs(
        prot_name=prot_name,
        file_chain=file_chain,
        sv_fp=fp,
    ).lips()[["surfs", "ents"]]


def get_helix_all_surf_lips(
    fp: str,
    prot_name: str,
    file_chain: str,
) -> Dict[str, Any]:
    """_summary_

    Parameters
    ----------
    fp : str
        _description_
    prot_name : str
        _description_
    file_chain : str
        _description_

    Returns
    -------
    Dict[str, Any]
        _description_
    """
    return hs(
        prot_name=prot_name,
        file_chain=file_chain,
        sv_fp=fp,
    ).lips()[["surfs", "lipos"]]


def get_helix_all_surf_avelips(
    fp: str,
    prot_name: str,
    file_chain: str,
) -> Dict[str, Any]:
    """_summary_

    Parameters
    ----------
    fp : str
        _description_
    prot_name : str
        _description_
    file_chain : str
        _description_

    Returns
    -------
    Dict[str, Any]
        _description_
    """
    return hs(
        prot_name=prot_name,
        file_chain=file_chain,
        sv_fp=fp,
    ).lips()[["surfs", "lxe"]]


def torosseta(
    fp: str,
    prot_name: str,
    file_chain: str,
    df_surf_lips: Dict[str, Any],
) -> Dict[str, Any]:
    """_summary_

    Parameters
    ----------
    fp : str
        _description_
    prot_name : str
        _description_
    file_chain : str
        _description_
    df_surf_lips : Dict[str, Any]
        _description_

    Returns
    -------
    Dict[str, Any]
        _description_
    """
    return hs(
        sv_fp=fp,
        prot_name=prot_name,
        file_chain=file_chain,
    ).transformToRosseta(
        df_surf_lips=df_surf_lips,
    )


def get_surf_entropy(
    fp: str,
    prot_name: str,
    file_chain: str,
    id: int = 0,
) -> Dict[str, Any]:
    """_summary_

    Parameters
    ----------
    fp : str
        _description_
    prot_name : str
        _description_
    file_chain : str
        _description_
    id : int, optional
        _description_, by default 0

    Returns
    -------
    Dict[str, Any]
        _description_
    """
    return hs(
        prot_name=prot_name,
        file_chain=file_chain,
        sv_fp=fp,
    ).surface(
        i=id
    )[["aa_ids", "ents"]]


def get_surf_lips(
    fp: str,
    prot_name: str,
    file_chain: str,
    id: int = 0,
) -> Dict[str, Any]:
    """_summary_

    Returns
    -------
    _type_
        _description_
    """
    return hs(
        prot_name=prot_name,
        file_chain=file_chain,
        sv_fp=fp,
    ).surface(
        i=id
    )[["aa_ids", "lipos"]]
