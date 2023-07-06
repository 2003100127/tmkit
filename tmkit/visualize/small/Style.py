__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import Optional


def Style(sm_style: Optional[str] = "sticks") -> None:
    """
    Change the representation style of the 'sm' selection in PyMOL.

    Parameters
    ----------
    sm_style : str, optional
        The representation style to use for the 'sm' selection. Default is 'sticks'.

    Returns
    -------
    None
    """
    from pymol import cmd

    cmd.hide(representation="spheres", selection="sm")
    cmd.show(representation=sm_style, selection="sm")
