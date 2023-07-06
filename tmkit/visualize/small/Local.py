__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import List, Tuple

from tmkit.chain.PDB import PDB as cpdb
from tmkit.visualize.small.Label import Label as pppmlabel
from tmkit.visualize.small.Palette import Palette as pppmpalette
from tmkit.visualize.small.Select import Select as pppmselect
from tmkit.visualize.small.Style import Style as pppmstyle


class Local:
    def __init__(
        self,
        prot_name: str,
        pdb_complex_fp: str,
        prot_c: str,
        sm_c: str,
        sm_rep: str,
        nby_rep: str,
        pocket_rep: str = "surface",
    ) -> None:
        """
        Initialize a local object.

        Parameters
        ----------
        prot_name : str
            The name of the protein.
        pdb_complex_fp : str
            The filepath of the pdb complex.
        prot_c : str
            The color of the protein.
        sm_c : str
            The color of the small molecule.
        sm_rep : str
            The representation of the small molecule.
        nby_rep : str
            The representation of the nearby atoms.
        pocket_rep : str, optional
            The representation of the pocket, by default "surface".
        """
        from pymol import cmd, finish_launching, preset

        from tmkit.chain.PDB import PDB as cpdb
        from tmkit.visualize.small.Label import Label as pppmlabel
        from tmkit.visualize.small.Palette import Palette as pppmpalette
        from tmkit.visualize.small.Select import Select as pppmselect
        from tmkit.visualize.small.Style import Style as pppmstyle

        finish_launching()

        cmd.bg_color(
            color="black"
            # color="white"
        )

        chains = cpdb(
            pdb_fp=pdb_complex_fp,
            prot_name=prot_name,
        ).chains()

        cmd.load(
            filename=pdb_complex_fp + prot_name + ".pdb",
        )

        sel_op = pppmselect()
        sel_op.chain(chains)
        sel_op.pocket()

        pppmpalette(
            chains,
            prot_c=prot_c,
            sm_c=sm_c,
        )
        pppmstyle(
            sm_style=sm_rep,
        )
        preset.ball_and_stick(selection="sm", mode=1)
        preset.ligand_sites_mesh(selection="sm")

        cmd.select(name="nby", selection="n. CA and br. all within 5 of organic")

        cmd.show(
            selection="nby",
            representation=nby_rep,
        )
        cmd.show(
            selection="pocket",
            representation=pocket_rep,
        )
        pppmlabel().putup(
            select="nby",
        )

        cmd.set(name="sphere_scale", value=1.5, selection="nby")
