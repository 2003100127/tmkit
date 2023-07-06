__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import List
from tmkit.chain.PDB import pdb as cpdb


class Coloring:
    def __init__(
        self,
        pdb_fp: str,
        prot_name: str,
        seq_chain: str,
        prot_c: str = "sulfur",
        names: List[str] = ["n1", "n2", "n3", "n4", "n5"],
        actions: List[str] = ["resi 1-4", "resi 58-61",
                              "resi 5-57", "i. 62-81", "i. 62+78+81"],
        colors: List[str] = ["red", "red", "orange", "br4", "violet"],
        forms: List[str] = ["lines", "lines", "lines", "lines", "lines"],
    ) -> None:
        """
        Initialize the Coloring class.

        Parameters
        ----------
        pdb_fp : str
            The protein PDB file.
        prot_name : str
            The name of the protein.
        seq_chain : str
            The sequence chain of the protein.
        prot_c : str, optional
            The color of the protein, by default "sulfur".
        names : List[str], optional
            The pymol select name, by default ["n1", "n2", "n3", "n4", "n5"].
        actions : List[str], optional
            The residues that pymol selects, by default ["resi 1-4", "resi 58-61", "resi 5-57", "i. 62-81", "i. 62+78+81"].
        colors : List[str], optional
            The colors, by default ["red", "red", "orange", "br4", "violet"].
        forms : List[str], optional
            The representation of the selected residues, by default ["lines", "lines", "lines", "lines", "lines"].
        """
        from pymol import cmd, finish_launching

        finish_launching()

        cmd.bg_color(
            color="black",
            # color="white",
        )

        chains = cpdb(
            pdb_fp=pdb_fp,
            prot_name=prot_name + seq_chain,
        ).chains()

        cmd.load(
            filename=pdb_fp + prot_name + seq_chain + ".pdb",
        )
        for chain in chains:
            cmd.select(
                name="prot_" + chain,
                selection="c. " + chain,
            )
            cmd.color(
                color=prot_c,
                selection="prot_" + chain,
            )

        for i in range(len(names)):
            cmd.select(
                name=names[i],
                selection=actions[i],
            )
            cmd.color(
                color=colors[i],
                selection=names[i],
            )
            cmd.show(
                selection=names[i],
                representation=forms[i],
            )
