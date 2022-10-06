__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2022"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import sys
import time
import numpy as np
sys.path.append('../../../')
from tmkit.seqnetrr.Path import to
from tmkit.seqnetrr.net.Reader import reader as prrcreader
from tmkit.seqnetrr.window.base import Single as ecabSgl
from tmkit.seqnetrr.util.Console import console


class cumulative(ecabSgl.single):
    
    def __init__(
            self,
            sequence,
            window_size,
            window_m_ids,
            verbose=True,
            input_kind='general',
    ):
        super(cumulative, self).__init__(sequence, window_size, window_m_ids)
        self.prrcreader = prrcreader()
        self.window_size = window_size
        self.window_m_ids = window_m_ids
        self.num_aas = len(self.window_m_ids)
        self.sequence = sequence
        self.len_seq = len(self.sequence)
        self.console = console()
        self.console.verbose = verbose
        self.input_kind = input_kind
        if self.input_kind == 'general':
            self.file_initiator = self.prrcreader.general
        elif self.input_kind == 'freecontact':
            self.file_initiator = self.prrcreader.freecontact
        elif self.input_kind == 'mutual information':
            self.file_initiator = self.prrcreader.mi
        elif self.input_kind == 'gdca':
            self.file_initiator = self.prrcreader.gdca
        elif self.input_kind == 'ccmpred':
            self.file_initiator = self.prrcreader.ccmpred
        elif self.input_kind == 'plmc':
            self.file_initiator = self.prrcreader.plmc
        elif self.input_kind == 'simulate':
            self.file_initiator = self.prrcreader.simulate
        else:
            self.file_initiator = self.prrcreader.general

    def sigmoid(self, value):
        return 1 / (1 + np.exp(-value))

    def assign(self, list_2d, L, simu_seq_len=100, fpn=None, is_activate=False):
        start_time = time.time()
        list_2d_ = list_2d
        mm_sum = self.file_initiator(
            fpn=simu_seq_len if self.input_kind == 'simulate' else fpn,
            sort_=3,
            is_sort=True,
        )['score'].sum()
        # print(mm_sum)
        mm_ave = mm_sum / self.len_seq
        # print(mm_sum)
        # print(mm_ave)
        mm_dict = self.file_initiator(
            fpn=simu_seq_len if self.input_kind == 'simulate' else fpn,
            sort_=7,
            len_seq=self.len_seq,
            L=L,
        )
        # print(mm_dict)
        for i, m_win_ids in enumerate(self.window_m_ids):
            for j in m_win_ids:
                if j is None:
                    list_2d_[i].append(0)
                else:
                    if is_activate:
                        list_2d_[i].append(self.sigmoid(mm_dict[j] / mm_ave))
                    else:
                        list_2d_[i].append(mm_dict[j] / mm_ave)
        self.console.print('======>cumulative assignment: {time}s.'.format(time=time.time() - start_time))
        return list_2d_


if __name__ == "__main__":
    from tmkit.seqnetrr.window.Single import single
    from tmkit.seqnetrr.sequence.Fasta import fasta as sfasta
    from tmkit.seqnetrr.combo.Position import position as pfasta
    from tmkit.seqnetrr.combo.Length import length as plength

    DEFINE = {
        'prot_name': '1aig',
        'file_chain': 'L',
        'seq_chain': 'L',

        # 'prot_name': '5lki',
        # 'file_chain': 'A',
        # 'seq_chain': 'A',

        'cutoff': 5.5,
        'seq_sep_inferior': 4,
        'seq_sep_superior': None,
        'fasta_path': to('data/example/'),
    }

    # /* sequence */
    fasta_path = to('data/example/1aigL.fasta')
    # sequence = sfasta().get(fasta_path)
    sequence = sfasta().simulate(seq_len=100)
    print(sequence)

    # /* scenario of position */
    pos_list = plength(seq_sep_inferior=0).tosgl(len(sequence))
    print(pos_list)

    # /* position */
    position = pfasta(sequence).single(pos_list=pos_list)
    print(position)

    window_size = 3
    window_m_ids = single(
        sequence=sequence,
        position=position,
        window_size=window_size,
    ).mid()
    # print(window_m_ids)

    p = cumulative(
        sequence=sequence,
        window_size=window_size,
        window_m_ids=window_m_ids,
        # input_kind='general',
        # input_kind='freecontact',
        input_kind='simulate',
    )
    results = p.assign(
        list_2d=position,
        L=int(len(sequence)/5),
        fpn=to('data/example/') + DEFINE['prot_name'] + DEFINE['file_chain'] + '.evfold',
        simu_seq_len=100,
    )
    print(results)
    # print(results[120])