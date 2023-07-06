__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import List

from tmkit.id.Mapping import Mapping as idmap


def pdb2uniprot(
    id: str,
    ref_fpn: str = "",
) -> str:
    """
    Convert from an PDB ID to a UniProt accession code

    Parameters
    ----------
    id : str
        A PDB ID (e.g., 1qxf.A) or a UniProt accession code (e.g., O28935).
    ref_fpn : str, optional
        Reference file for conversion between PDB IDs and UniProt accession codes.

    Returns
    -------
    str
        A UniProt accession code
    """
    return idmap().entry_convert(id=id, ref_fpn=ref_fpn, mode="pdb -> uniprot")


def uniprot2pdb(
    id: str,
    ref_fpn: str = "",
) -> str:
    """
    Convert from an UniProt accession code to a PDB ID

    Parameters
    ----------
    id : str
        A PDB ID (e.g., 1qxf.A) or a UniProt accession code (e.g., O28935).
    ref_fpn : str, optional
        Reference file for conversion between PDB IDs and UniProt accession codes.

    Returns
    -------
    str
        A PDB ID
    """
    return idmap().entry_convert(id=id, ref_fpn=ref_fpn, mode="uniprot -> pdb")
