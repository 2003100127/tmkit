__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from Bio import SeqIO


class fasta:

    def get(self, fasta_fpn):
        sequence = []
        for seq in SeqIO.parse(fasta_fpn, "fasta"):
            sequence.append(str(seq.seq))
        sequence = ''.join(sequence)
        ids = {}
        for i, aa in enumerate(sequence):
            ids[i+1] = aa
        return ids
