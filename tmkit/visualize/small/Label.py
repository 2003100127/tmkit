__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"


class Label:
    """
    A class for labeling residues in PyMOL.

    Attributes
    ----------
    None

    Methods
    -------
    putup(selection: str) -> None:
        Labels the residues in the given PyMOL selection with their residue name and number.
    """

    def putup(self, selection: str) -> None:
        """
        Labels the residues in the given PyMOL selection with their residue name and number.

        Parameters
        ----------
        selection : str
            The PyMOL selection to label.

        Returns
        -------
        None
        """
        from pymol import cmd

        cmd.label2(
            selection=selection,
            expression="resn, resi",
        )
        # cmd.set(name='label_font_id', selection=select, value=18)
        # cmd.set(name='label_shadow_mode', selection=select, value=1)
        cmd.set(name="label_color", selection=selection, value="orange")
        cmd.set(name="label_size", value=40, selection=selection)
