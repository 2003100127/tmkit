__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2022"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import sys
sys.path.append('../../')
from Bio import SeqIO


class fasta(object):

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

    def _get(self, gap=False, universal=False):
        if universal:
            if gap:
                return ['A', 'C', 'G', 'T', '-']
            else:
                return ['A', 'C', 'G', 'T']
        else:
            if gap:
                return ['A', 'T', 'C', 'G', '-']
            else:
                return ['A', 'T', 'C', 'G']

    def todict(self, nucleotides):
        aa_dict = {}
        for k, v in enumerate(nucleotides):
            aa_dict[v] = k
        return {v: k for k, v in aa_dict.items()}

    def uniform(self, low, high, num, use_seed=True, seed=1):
        import numpy as np
        if use_seed:
            state = np.random.RandomState(seed)
            return state.randint(
                low=low,
                high=high,
                size=num
            )
        else:
            return np.random.randint(
                low=low,
                high=high,
                size=num
            )

    def simulate(self, seq_len, use_seed=False, id=0):
        nucleotides = self._get(universal=True)
        nucleotide_dict = self.todict(nucleotides)
        ran_num = self.uniform(
            low=0,
            high=4,
            num=seq_len,
            use_seed=use_seed,
            seed=id,
        )
        return ''.join([nucleotide_dict[i] for i in ran_num])