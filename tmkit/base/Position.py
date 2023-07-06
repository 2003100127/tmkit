__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import numpy as np


class position:

    def __init__(self, seq_sep_inferior=None, seq_sep_superior=None):
        self.seq_sep_inferior = seq_sep_inferior
        self.seq_sep_superior = seq_sep_superior
        # self.asp = scheme()

    def interv2combi(self, inf_arr, sup_arr):
        tmp_2d = []
        num_interv = len(inf_arr)
        for i in range(num_interv):
            tmp_2d.append(list(np.arange(inf_arr[i], sup_arr[i] + 1)))
        combi = []
        for i in range(num_interv):
            for j in range(num_interv):
                if i < j:
                    for p in range(len(tmp_2d[i])):
                        for q in range(len(tmp_2d[j])):
                            combi.append([tmp_2d[i][p], tmp_2d[j][q]])
        # print(combi)
        return combi