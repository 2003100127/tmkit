__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from tmkit.chain.PDB import pdb as cpdb


class coloring:

    def __init__(
            self,
            pdb_fp,
            prot_name,
            seq_chain,
            prot_c='sulfur',
            names=['n1', 'n2', 'n3', 'n4', 'n5'],
            actions=['resi 1-4', 'resi 58-61', 'resi 5-57', 'i. 62-81', 'i. 62+78+81'],
            colors=['red', 'red', 'orange', 'br4', 'violet',],
            forms=['lines', 'lines', 'lines', 'lines', 'lines',],
    ):
        """

        Parameters
        ----------
        pdb_fp
            protein PDB file
        names
            pymol select name
        actions
            residues that pymol selects
        colors
            colors
        forms
            representation of the selected residues
        """
        from pymol import finish_launching
        from pymol import cmd
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
            filename=pdb_fp + prot_name + seq_chain + '.pdb',
        )
        for chain in chains:
            cmd.select(
                name='prot_' + chain,
                selection='c. ' + chain,
            )
            cmd.color(
                color=prot_c,
                selection='prot_' + chain,
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