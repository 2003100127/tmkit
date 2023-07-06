__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"


def Color(color, sel_name):
    """PyMOL color a chain"""

    from pymol import cmd

    cmd.color(color=color, selection=sel_name)
    # cmd.spectrum(
    #     palette=sm_c,
    #     selection="sm"
    # )
