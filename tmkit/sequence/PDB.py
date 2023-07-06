__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import List

from tmkit.base import PDB as bpdb


class PDB(bpdb.Sequence):
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

    def chain(self) -> str:
        """
        Get whole protein sequence from a PDB file.

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
        str
            A sequence.
        """
        seq: List[str] = []
        for pp in self.ppb.build_peptides(self.pdb_chain):
            seq_tmp: str = str(pp.get_sequence())
            seq.append(seq_tmp)
        return "".join(seq)
