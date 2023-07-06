__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from tmkit.visualize.small.Palette import palette as pppmpalette
from tmkit.visualize.small.Select import select as pppmselect
from tmkit.visualize.small.Style import style as pppmstyle
from tmkit.visualize.small.Label import label as pppmlabel
from tmkit.chain.PDB import pdb as cpdb


class local:

    def __init__(
            self,
            prot_name,
            pdb_complex_fp,
            prot_c,
            sm_c,
            sm_rep,
            nby_rep,
            pocket_rep='surface',
    ):
        """

        Parameters
        ----------
        prot_name
            '6feq',
        pdb_complex_fp
            to('data/example/pymol/'),
        sm_rep
            "sticks",
        nby_rep
            'spheres',
        prot_c
            'blue_white_magenta', # 'blue_magenta' rainbow
        sm_c
            'blue_green',
        """
        from pymol import cmd
        from pymol import finish_launching
        from pymol import preset
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
            filename=pdb_complex_fp + prot_name + '.pdb',
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
        preset.ball_and_stick(selection='sm', mode=1)
        preset.ligand_sites_mesh(selection='sm')

        cmd.select(
            name='nby',
            selection='n. CA and br. all within 5 of organic'
        )

        cmd.show(
            selection='nby',
            representation=nby_rep,
        )
        cmd.show(
            selection='pocket',
            representation=pocket_rep,
        )
        pppmlabel().putup(select='nby', )

        cmd.set(name='sphere_scale', value=1.5, selection='nby')