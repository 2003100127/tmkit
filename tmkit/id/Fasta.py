__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import Any, Dict

from Bio import SeqIO


class Fasta:
    def get(self, fasta_fpn: str) -> Dict[int, str]:
        """
        Read a FASTA file and return a dictionary of sequence IDs and their corresponding sequences.

        Parameters
        ----------
        fasta_fpn : str
            The file path of the FASTA file.

        Returns
        -------
        Dict[int, str]
            A dictionary of sequence IDs and their corresponding sequences.
        """
        sequence = []
        for seq in SeqIO.parse(fasta_fpn, "fasta"):
            sequence.append(str(seq.seq))
        sequence = "".join(sequence)
        ids: Dict[int, str] = {}
        for i, aa in enumerate(sequence):
            ids[i + 1] = aa
        return ids
