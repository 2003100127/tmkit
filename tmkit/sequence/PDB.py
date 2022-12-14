__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2022"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import sys
import warnings
sys.path.append('../../')
from tmkit.base import PDB
from Bio import BiopythonWarning


class pdb(PDB.sequence):

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

        Notes
        -----
            chain() can function in getting whole protein
            sequence from a PDB file given. (1). For a PDB
            file which contains many chains like A, B and C,
            you can specify a specific chain through parameter
            seq_chain. (2). For a PDB file which contains only
            one chain like A, you can specify this chain 'A'
            through parameter seq_chain. (3). For a PDB file
            which doesn't contain any chain but the fact that
            you know it contains A chain in truth, you can
            specify '' chain through parameter seq_chain. It
            is worth to mention that this function can also be
            functional in the case where in each chain you specify
            the residues are discontinuous, this function can
            also find all discontinuous residues by a for-loop.

        Returns
        -------
            a sequence

        """
        seq=[]
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', BiopythonWarning)
            for pp in self.ppb.build_peptides(self.pdb_chain):
                seq_tmp = str(pp.get_sequence())
                # print(seq_tmp)
                seq.append(seq_tmp)
        return ''.join(seq)

