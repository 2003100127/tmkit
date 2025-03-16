__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import Dict

# from Bio.PDB.Polypeptide import three_to_one

from tmkit.base import PDB as bpdb


class PDB(bpdb.ID):
    def __init__(
        self, pdb_fp: str, prot_name: str, seq_chain: str, file_chain: str = ""
    ) -> None:
        """
        Parameters
        ----------
        pdb_fp : str
            structure path
        prot_name : str
            structure name
        file_chain : str, optional
            file chain, by default ""
        seq_chain : str
            sequence chain
        """
        super().__init__(pdb_fp, prot_name, seq_chain, file_chain)

    def chain(self) -> Dict[int, str]:
        """
        get a dictionary for mapping residue IDs to amino acid symbols

        Returns
        -------
        Dict[int, str]
            Dictionary mapping residue IDs to amino acid symbols.
        """
        ids: Dict[int, str] = {}
        for i, residue in enumerate(self.pdb_chain):
            res_name: str = self.three_to_one[residue.get_resname()]
            ids[residue.id[1]] = res_name
            # print([*ids.keys()])
        return ids
