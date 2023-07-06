__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"


class Select:
    def chain(self, chain_name, chains="A+B+C+D+E+F+G+H+I+J+K"):
        """PyMOL select a chain"""
        from pymol import cmd

        cmd.select(name=chain_name, selection="c. " + chains)
        return
