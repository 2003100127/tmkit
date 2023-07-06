__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import warnings
from Bio.PDB.PDBParser import PDBParser
from Bio.PDB.Polypeptide import PPBuilder


class sequence:

    def __init__(self, pdb_fp, prot_name, seq_chain, file_chain):
        from Bio import BiopythonWarning
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', BiopythonWarning)
            self.pdb_fp = pdb_fp
            self.prot_name = prot_name
            self.file_chain = file_chain
            self.seq_chain = seq_chain
            self.pdb_fpn = self.pdb_fp + self.prot_name + self.file_chain + '.pdb'

            self.bio_parser = PDBParser()
            self.structure = self.bio_parser.get_structure(self.prot_name, self.pdb_fpn)
            self.model = self.structure[0]
            self.pdb_chain = self.model[self.seq_chain]
            self.ppb = PPBuilder()


class id:

    def __init__(self, pdb_fp, prot_name, seq_chain, file_chain):
        self.pdb_fp = pdb_fp
        self.prot_name = prot_name
        self.file_chain = file_chain
        self.seq_chain = seq_chain
        self.pdb_fpn = self.pdb_fp + self.prot_name + self.file_chain + '.pdb'

        self.bio_parser = PDBParser()
        self.structure = self.bio_parser.get_structure(self.prot_name, self.pdb_fpn)
        self.model = self.structure[0]
        self.pdb_chain = self.model[self.seq_chain]


class structure:

    def __init__(self, pdb_fp, prot_name, seq_chain, file_chain):
        self.pdb_fp = pdb_fp
        self.prot_name = prot_name
        self.file_chain = file_chain
        self.seq_chain = seq_chain
        self.pdb_fpn = self.pdb_fp + self.prot_name + self.file_chain + '.pdb'

        self.bio_parser = PDBParser()
        self.structure = self.bio_parser.get_structure(self.prot_name, self.pdb_fpn)
        self.model = self.structure[0]
        if self.seq_chain != '':
            self.pdb_chain = self.model[self.seq_chain]

    @property
    def name(self, ):
        return self.structure.header['name']

    @property
    def rez(self, ):
        return self.structure.header['resolution']

    @property
    def met(self, ):
        return self.structure.header['structure_method']

    @property
    def head(self, ):
        return self.structure.header['head']

    @property
    def head_keys(self, ):
        return self.structure.header.keys()

    @property
    def psi_phi(self, ):
        for pp in PPBuilder().build_peptides(self.structure):
            print(pp.get_phi_psi_list())
        return PPBuilder().build_peptides(self.structure).get_phi_psi_list()


class chain:

    def __init__(self, pdb_fp, prot_name):
        self.pdb_fp = pdb_fp
        self.prot_name = prot_name
        self.pdb_fpn = self.pdb_fp + self.prot_name + '.pdb'
        self.bio_parser = PDBParser(QUIET=True)
        self.structure = self.bio_parser.get_structure(self.prot_name, self.pdb_fpn)
        self.model = self.structure[0]