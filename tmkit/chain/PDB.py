__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import List

from tmkit.base import PDB as bpdb


class PDB(bpdb.Chain):
    """
    A class representing a Protein Data Bank (PDB) file.

    Parameters
    ----------
    pdb_fp : str
        The file path to the PDB file.
    prot_name : str
        The name of the protein.

    Attributes
    ----------
    structure : Bio.PDB.Structure.Structure
        The structure object of the PDB file.
    """

    def __init__(self, pdb_fp: str, prot_name: str) -> None:
        super().__init__(pdb_fp, prot_name)

    def chains(self) -> List[str]:
        """
        Get a list of chain IDs in the PDB file.

        Returns
        -------
        List[str]
            A list of chain IDs.
        """
        return [chain.get_id() for chain in self.structure.get_chains()]
