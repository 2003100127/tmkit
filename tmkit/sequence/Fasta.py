__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2022"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import sys
sys.path.append('../../')
from Bio import SeqIO


class fasta():

    def __init__(self):
        pass

    def get(self, fasta_fpn):
        sequence = []
        for seq in SeqIO.parse(fasta_fpn, "fasta"):
            # print(seq.seq)
            sequence.append(str(seq.seq))
        sequence = ''.join(sequence)
        if sequence == '':
            print('The sequence is empty.')
        return sequence
