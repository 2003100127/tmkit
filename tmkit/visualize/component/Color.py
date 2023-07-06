__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"


from typing import List

def color(color: str, sel_name: str) -> None:
    """
    Color the selection with the specified color.

    Parameters
    ----------
    color : str
        The color to use for the selection.
    sel_name : str
        The name of the selection to color.
    """
    from pymol import cmd

    cmd.color(color=color, selection=sel_name)
    # cmd.spectrum(
    #     palette=sm_c,
    #     selection="sm"
    #)
