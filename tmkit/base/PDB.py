__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import List, Tuple

import warnings

from Bio.PDB.PDBParser import PDBParser
from Bio.PDB.Polypeptide import PPBuilder


class Sequence:
    """
    Class representing a protein sequence from a PDB file.

    Attributes
    ----------
    pdb_fp : str
        The file path to the PDB file.
    prot_name : str
        The name of the protein.
    seq_chain : str
        The chain ID of the protein sequence.
    file_chain : str
        The chain ID of the PDB file.
    pdb_fpn : str
        The full file path to the PDB file.
    bio_parser : PDBParser
        The PDB parser object.
    structure : Structure
        The structure object.
    model : Model
        The model object.
    pdb_chain : Chain
        The chain object corresponding to the protein sequence.
    ppb : PPBuilder
        The polypeptide builder object.
    """

    def __init__(
        self, pdb_fp: str, prot_name: str, seq_chain: str, file_chain: str
    ) -> None:
        from Bio import BiopythonWarning

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", BiopythonWarning)
            self.pdb_fp = pdb_fp
            self.prot_name = prot_name
            self.file_chain = file_chain
            self.seq_chain = seq_chain
            self.pdb_fpn = self.pdb_fp + self.prot_name + self.file_chain + ".pdb"

            self.bio_parser = PDBParser()
            self.structure = self.bio_parser.get_structure(self.prot_name, self.pdb_fpn)
            self.model = self.structure[0]
            self.pdb_chain = self.model[self.seq_chain]
            self.ppb = PPBuilder()


class ID:
    """
    Class representing a protein ID from a PDB file.

    Attributes
    ----------
    pdb_fp : str
        The file path to the PDB file.
    prot_name : str
        The name of the protein.
    seq_chain : str
        The chain ID of the protein sequence.
    file_chain : str
        The chain ID of the PDB file.
    pdb_fpn : str
        The full file path to the PDB file.
    bio_parser : PDBParser
        The PDB parser object.
    structure : Structure
        The structure object.
    model : Model
        The model object.
    pdb_chain : Chain
        The chain object corresponding to the protein sequence.
    """

    def __init__(
        self, pdb_fp: str, prot_name: str, seq_chain: str, file_chain: str
    ) -> None:
        self.pdb_fp = pdb_fp
        self.prot_name = prot_name
        self.file_chain = file_chain
        self.seq_chain = seq_chain
        self.pdb_fpn = self.pdb_fp + self.prot_name + self.file_chain + ".pdb"

        self.bio_parser = PDBParser()
        self.structure = self.bio_parser.get_structure(self.prot_name, self.pdb_fpn)
        self.model = self.structure[0]
        self.pdb_chain = self.model[self.seq_chain]
        self.three_to_one = {
            'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
            'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N',
            'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W',
            'ALA': 'A', 'VAL':'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M',
        }


class Structure:
    """
    Class representing a protein structure from a PDB file.

    Attributes
    ----------
    pdb_fp : str
        The file path to the PDB file.
    prot_name : str
        The name of the protein.
    seq_chain : str
        The chain ID of the protein sequence.
    file_chain : str
        The chain ID of the PDB file.
    pdb_fpn : str
        The full file path to the PDB file.
    bio_parser : PDBParser
        The PDB parser object.
    structure : Structure
        The structure object.
    model : Model
        The model object.
    pdb_chain : Chain
        The chain object corresponding to the protein sequence.
    """

    def __init__(
        self, pdb_fp: str, prot_name: str, seq_chain: str, file_chain: str
    ) -> None:
        self.pdb_fp = pdb_fp
        self.prot_name = prot_name
        self.file_chain = file_chain
        self.seq_chain = seq_chain
        self.pdb_fpn = self.pdb_fp + self.prot_name + self.file_chain + ".pdb"

        self.bio_parser = PDBParser()
        self.structure = self.bio_parser.get_structure(self.prot_name, self.pdb_fpn)
        self.model = self.structure[0]
        if self.seq_chain != "":
            self.pdb_chain = self.model[self.seq_chain]

    @property
    def name(self) -> str:
        """
        The name of the protein structure.

        Returns
        -------
        str
            The name of the protein structure.
        """
        return self.structure.header["name"]

    @property
    def rez(self) -> float:
        """
        The resolution of the protein structure.

        Returns
        -------
        float
            The resolution of the protein structure.
        """
        return self.structure.header["resolution"]

    @property
    def met(self) -> str:
        """
        The structure method used to determine the protein structure.

        Returns
        -------
        str
            The structure method used to determine the protein structure.
        """
        return self.structure.header["structure_method"]

    @property
    def head(self) -> str:
        """
        The header of the protein structure.

        Returns
        -------
        str
            The header of the protein structure.
        """
        return self.structure.header["head"]

    @property
    def head_keys(self) -> List[str]:
        """
        The keys of the header of the protein structure.

        Returns
        -------
        List[str]
            The keys of the header of the protein structure.
        """
        return self.structure.header.keys()

    @property
    def psi_phi(self) -> List[Tuple[float, float]]:
        """
        The phi-psi angles of the protein structure.

        Returns
        -------
        List[Tuple[float, float]]
            The phi-psi angles of the protein structure.
        """
        for pp in PPBuilder().build_peptides(self.structure):
            print(pp.get_phi_psi_list())
        return PPBuilder().build_peptides(self.structure).get_phi_psi_list()


class Chain:
    """
    Class representing a protein chain from a PDB file.

    Attributes
    ----------
    pdb_fp : str
        The file path to the PDB file.
    prot_name : str
        The name of the protein.
    pdb_fpn : str
        The full file path to the PDB file.
    bio_parser : PDBParser
        The PDB parser object.
    structure : Structure
        The structure object.
    model : Model
        The model object.
    """

    def __init__(self, pdb_fp: str, prot_name: str) -> None:
        self.pdb_fp = pdb_fp
        self.prot_name = prot_name
        self.pdb_fpn = self.pdb_fp + self.prot_name + ".pdb"
        self.bio_parser = PDBParser(QUIET=True)
        self.structure = self.bio_parser.get_structure(self.prot_name, self.pdb_fpn)
        self.model = self.structure[0]
