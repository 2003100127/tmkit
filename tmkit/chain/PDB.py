__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from tmkit.base import PDB


class pdb(PDB.chain):

    def __init__(self, pdb_fp, prot_name):
        """

        Parameters
        ----------
        pdb_fp
            structure path
        prot_name
            structure name
        """
        super(pdb, self).__init__(pdb_fp, prot_name)

    def chains(self, ):
        return [chain.get_id() for chain in self.structure.get_chains()]