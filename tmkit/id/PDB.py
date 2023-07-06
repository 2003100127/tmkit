__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from tmkit.base import PDB
from Bio.PDB.Polypeptide import three_to_one


class pdb(PDB.id):

    def __init__(self, pdb_fp, prot_name, seq_chain, file_chain=''):
        """

        Parameters
        ----------
        pdb_fp
            structure path
        prot_name
            structure name
        file_chain
            file chain
        seq_chain
            sequence chain
        """
        super(pdb, self).__init__(pdb_fp, prot_name, seq_chain, file_chain)

    def chain(self):
        """

        Returns
        -------
            dict: pdb id -> aa symbol

        """
        ids = {}
        for i, residue in enumerate(self.pdb_chain):
            res_name = three_to_one(residue.get_resname())
            ids[residue.id[1]] = res_name
        # print([*ids.keys()])
        return ids