__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2022"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from pymol import cmd


def palette(chains, prot_c='rainbow', sm_c='blue_green'):
    for chain in chains:
        cmd.spectrum(
            palette=prot_c,
            selection="prot_" + chain
        )
    cmd.spectrum(
        palette=sm_c,
        selection="sm"
    )