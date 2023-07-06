__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import List

from tmkit.chain.PDB import PDB as cpdb


class Coloring:
    def __init__(
        self,
        pdb_fp: str,
        prot_name: str,
        seq_chain: str,
        prot_c: str = "sulfur",
        names: List[str] = ["n1", "n2", "n3", "n4", "n5"],
        actions: List[str] = [
            "resi 1-4",
            "resi 58-61",
            "resi 5-57",
            "i. 62-81",
            "i. 62+78+81",
        ],
        colors: List[str] = ["red", "red", "orange", "br4", "violet"],
        forms: List[str] = ["lines", "lines", "lines", "lines", "lines"],
    ) -> None:
        """
        Visualize and color protein segments.

        Parameters
        ----------
        prot_name : str
            name of a protein in the prefix of a PDB file name (e.g., 1xqf in 1xqfA.pdb).
        seq_chain : str
            chain of a protein in the prefix of a PDB file name (e.g., A in 1xqfA.pdb).
        pdb_fp : str
            path where a target PDB file is place.
        prot_c : str
            color of the entire protein.
        names : List[str], optional
            names of segments. Default is ["n1", "n2", "n3", "n4", "n5"].
        actions : List[str], optional
            which segments. Default is ["resi 1-4", "resi 58-61", "resi 5-57", "i. 62-81", "i. 62+78+81"].
        colors : List[str], optional
            colors selected for the segments. Default is ["red", "red", "orange", "br4", "violet"].
        forms : List[str], optional
            representation. Default is ["lines", "lines", "lines", "lines", "lines"].
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
