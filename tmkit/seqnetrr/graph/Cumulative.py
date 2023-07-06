__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import time
import numpy as np
from tmkit.seqnetrr.net.Reader import reader as prrcreader
from tmkit.seqnetrr.window.base import Single as ecabSgl


class cumulative(ecabSgl.single):
    
    def __init__(
            self,
            sequence,
            window_size,
            window_m_ids,
            input_kind='general',
    ):
        super(cumulative, self).__init__(sequence, window_size, window_m_ids)
        self.prrcreader = prrcreader()
        self.window_size = window_size
        self.window_m_ids = window_m_ids
        self.num_aas = len(self.window_m_ids)
        self.sequence = sequence
        self.len_seq = len(self.sequence)
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
        print('======>cumulative assignment: {time}s.'.format(time=time.time() - start_time))
        return list_2d_