__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"


class select:

    def chain(self, chains):
        from pymol import cmd
        for chain in chains:
            cmd.select(
                name='prot_' + chain,
                selection='c. ' + chain
            )
        cmd.select(
            name='sm',
            selection='hetatm'
        )

    def pocket(self, ):
        from pymol import cmd
        cmd.select(
            name='pocket',
            selection='byres(sm around 8)'
        )