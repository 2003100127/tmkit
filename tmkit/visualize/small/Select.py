__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import List


class Select:
    """
    A class for selecting chains and pockets in PyMOL.

    Attributes
    ----------
    None

    Methods
    -------
    chain(chains: List[str]) -> None:
        Selects chains in PyMOL.

    pocket() -> None:
        Selects pockets in PyMOL.
    """

    def chain(self, chains: List[str]) -> None:
        """
        Selects chains in PyMOL.

        Parameters
        ----------
        chains : List[str]
            A list of chain IDs.

        Returns
        -------
        None
        """
        from pymol import cmd

        for chain in chains:
            cmd.select(name="prot_" + chain, selection="c. " + chain)
        cmd.select(name="sm", selection="hetatm")

    def pocket(self) -> None:
        """
        Selects pockets in PyMOL.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        from pymol import cmd

        cmd.select(name="pocket", selection="byres(sm around 8)")
