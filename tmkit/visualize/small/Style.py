__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"


def style(sm_style="sticks"):
    from pymol import cmd
    cmd.hide(
        representation="spheres",
        selection='sm'
    )
    cmd.show(
        representation=sm_style,
        selection='sm'
    )