__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"


from typing import Any, Dict, Tuple

import pandas as pd

from tmkit.property.HelixSurface import HelixSurface as hs


def generate_helix_surfaces(
    msa_path: str,
    prot_name: str,
    file_chain: str,
    sv_fp: str,
) -> str:
    """
    Generate the helix surface.

    Parameters
    ----------
    msa_path : str, optional
        The path to the MSA file.
    prot_name : str, optional
        Name of a protein in the prefix of a PDB file name (e.g., 1xqf in 1xqfA.pdb).
    file_chain : str, optional
        Chain of a protein in the prefix of a PDB file name (e.g., A in 1xqfA.pdb).
    sv_fp : str, optional
        The file path to store the output.

    Returns
    -------
    str
        'Finished' if the success of the operation (0 indicates success).
    """
    return hs(
        msa_path=msa_path,
        prot_name=prot_name,
        file_chain=file_chain,
        sv_fp=sv_fp,
    ).generate()


def bgenerate_helix_surfaces(
    msa_path: str,
    sv_fp: str,
    df_prot: pd.DataFrame,
) -> str:
    """
    Generate the helix surface for multiple proteins.

    Parameters
    ----------
    msa_path : str, optional
        The path to the MSA file.
    sv_fp : str, optional
        The file path to store the output.
    df_prot : pd.DataFrame, optional
        Pandas dataframe storing protein names and chain names.

    Returns
    -------
    str
        'Finished' if the results are saved.
    """
    return hs(
        msa_path=msa_path, sv_fp=sv_fp, df_prot=df_prot
    ).bgenerate()


def read(
    fp: str,
    prot_name: str,
    file_chain: str,
) -> Tuple[Dict[int, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]:
    """
    Annotate all amino acids with surface ids, the entropy scores, lipophilicity scores, and mean lipophilicity scores.

    Parameters
    ----------
    fp : str, optional
            The path to a helix surface file
    prot_name : str, optional
        Name of a protein in the prefix of a PDB file name (e.g., 1xqf in 1xqfA.pdb).
    file_chain : str, optional
        Chain of a protein in the prefix of a PDB file name (e.g., A in 1xqfA.pdb).

    Returns
    -------
    Tuple[Dict[int, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]
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
) -> pd.DataFrame:
    """
    Read a surface file containing a dataframe: 5 columns, that is, aa_ids,
    aa_names, lipos, ents, and surf, corresponding to
    amino acid ID, amino acid name, the LIPOS score for the
    amino acid, entropy, and the helix surface ID.

    Parameters
    ----------
    fp : str, optional
            The path to a helix surface file
    prot_name : str, optional
        Name of a protein in the prefix of a PDB file name (e.g., 1xqf in 1xqfA.pdb).
    file_chain : str, optional
        Chain of a protein in the prefix of a PDB file name (e.g., A in 1xqfA.pdb).
    id : int
        surface id, 0-6.

    Returns
    -------
    pd.DataFrame
        5 columns, that is, aa_ids,
    aa_names, lipos, ents, and surf, corresponding to
    amino acid ID, amino acid name, the LIPOS score for the
    amino acid, entropy, and the helix surface ID
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
) -> pd.DataFrame:
    """
    Read the summary about all 7 surfaces, which shows
     the entropy, the LIPOS score, and the final LIPS
     score at the surface level.

    Parameters
    ----------
    fp : str, optional
        The path to a lips file
    prot_name : str, optional
        Name of a protein in the prefix of a PDB file name (e.g., 1xqf in 1xqfA.pdb).
    file_chain : str, optional
        Chain of a protein in the prefix of a PDB file name (e.g., A in 1xqfA.pdb).

    Returns
    -------
    pd.DataFrame
        4 columns: surfs, lipos, ents, and lxe.
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
) -> pd.DataFrame:
    """
    Read a lips file and return the surface entropy as a DataFrame.

    Parameters
    ----------
    fp : str, optional
        The path to a lips file
    prot_name : str, optional
        Name of a protein in the prefix of a PDB file name (e.g., 1xqf in 1xqfA.pdb).
    file_chain : str, optional
        Chain of a protein in the prefix of a PDB file name (e.g., A in 1xqfA.pdb).

    Returns
    -------
    pd.DataFrame
        two columns: surfs and ents
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
) -> pd.DataFrame:
    """
    Read a lips file and return the surface LIPS scores as a DataFrame.

    Parameters
    ----------
    fp : str, optional
        The path to a helix surface file
    prot_name : str, optional
        Name of a protein in the prefix of a PDB file name (e.g., 1xqf in 1xqfA.pdb).
    file_chain : str, optional
        Chain of a protein in the prefix of a PDB file name (e.g., A in 1xqfA.pdb).

    Returns
    -------
    pd.DataFrame
        two columns: surfs and lipos
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
) -> pd.DataFrame:
    """
    Read a lips file and return the average surface LIPS scores as a DataFrame.

    fp : str, optional
        The path to a helix surface file
    prot_name : str, optional
        Name of a protein in the prefix of a PDB file name (e.g., 1xqf in 1xqfA.pdb).
    file_chain : str, optional
        Chain of a protein in the prefix of a PDB file name (e.g., A in 1xqfA.pdb).

    Returns
    -------
    pd.DataFrame
        two columns: surfs and avelipos
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
    df_surf_lips: pd.DataFrame,
) -> pd.DataFrame:
    """
    Transform all surfaces files into one, containing amino acid, entropy, mean lipophilicity scores, and lipophilicity scores.

    Parameters
    ----------
    fp : str, optional
        The path to helix surface files
    prot_name : str, optional
        Name of a protein in the prefix of a PDB file name (e.g., 1xqf in 1xqfA.pdb).
    file_chain : str, optional
        Chain of a protein in the prefix of a PDB file name (e.g., A in 1xqfA.pdb).
    df_surf_lips : pd.DataFrame
        a Pandas dataframe containing helix scores and all surfuce lipophilicity scores.

    Returns
    -------
    pd.DataFrame
        4 columns, aa_ids, mean_lipo, lipos, and ents.
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
) -> pd.DataFrame:
    """
    Return all amino acid ids and their entropy scores in a helix surface.

    Parameters
    ----------
    fp : str, optional
        The path to a helix surface file.
    prot_name : str, optional
        Name of a protein in the prefix of a PDB file name (e.g., 1xqf in 1xqfA.pdb).
    file_chain : str, optional
        Chain of a protein in the prefix of a PDB file name (e.g., A in 1xqfA.pdb).
    id : int
        surface id, 0-6.

    Returns
    -------
    pd.DataFrame
        2 columns: aa_ids and ents
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
) -> pd.DataFrame:
    """
    Return all amino acid ids and their lipophilicity scores in a helix surface.

    Parameters
    ----------
    fp : str, optional
        The path to a helix surface file
    prot_name : str, optional
        Name of a protein in the prefix of a PDB file name (e.g., 1xqf in 1xqfA.pdb).
    file_chain : str, optional
        Chain of a protein in the prefix of a PDB file name (e.g., A in 1xqfA.pdb).
    id : int
        surface id, 0-6.

    Returns
    -------
    pd.DataFrame
        2 columns: aa_ids and lips
    """
    return hs(
        prot_name=prot_name,
        file_chain=file_chain,
        sv_fp=fp,
    ).surface(
        i=id
    )[["aa_ids", "lipos"]]
