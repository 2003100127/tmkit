__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from tmkit.id.Mapping import mapping as idmap


from typing import List


def pdb2uniprot(
    id: str,
    ref_fpn: str = "",
) -> List[str]:
    """_summary_

    Parameters
    ----------
    id : str
        _description_
    ref_fpn : str, optional
        _description_, by default ""

    Returns
    -------
    List[str]
        _description_
    """
    return idmap().entryConvert(id=id, ref_fpn=ref_fpn, mode="pdb -> uniprot")


def uniprot2pdb(
    id: str,
    ref_fpn: str = "",
) -> List[str]:
    """_summary_

    Parameters
    ----------
    id : str
        _description_
    ref_fpn : str, optional
        _description_, by default ""

    Returns
    -------
    List[str]
        _description_
    """
    return idmap().entryConvert(id=id, ref_fpn=ref_fpn, mode="uniprot -> pdb")
