__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2022"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from pymol import cmd


class select(object):

    def __init__(self, ):
        pass

    def chain(self, chains):
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
        cmd.select(
            name='pocket',
            selection='byres(sm around 8)'
        )