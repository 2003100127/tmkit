__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"


from typing import List


def Palette(
    chains: List[str], prot_c: str = "rainbow", sm_c: str = "blue_green"
) -> None:
    """
    Apply color palettes to protein chains and small molecules.

    Parameters
    ----------
    chains : List[str]
        A list of chain identifiers.
    prot_c : str, optional
        The color palette for protein chains, by default "rainbow".
    sm_c : str, optional
        The color palette for small molecules, by default "blue_green".

    Returns
    -------
    None
    """
    from pymol import cmd

    for chain in chains:
        cmd.spectrum(palette=prot_c, selection="prot_" + chain)
    cmd.spectrum(palette=sm_c, selection="sm")
