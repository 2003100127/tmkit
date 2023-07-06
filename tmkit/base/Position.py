__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import List, Tuple, Union

import numpy as np


class Position:
    def __init__(
        self, seq_sep_inferior: Union[int, float] = None, seq_sep_superior: Union[int, float] = None
    ) -> None:
        """
        Parameters
        ----------
        seq_sep_inferior : int or None, optional
            The inferior sequence separation, by default None.
        seq_sep_superior : int or None, optional
            The superior sequence separation, by default None.
        """
        self.seq_sep_inferior = seq_sep_inferior
        self.seq_sep_superior = seq_sep_superior

    def interv2combi(
        self, inf_arr: List[int], sup_arr: List[int]
    ) -> List[Tuple[int, int]]:
        """
        Convert two arrays of inferior and superior sequence separations into a list of tuples representing all possible combinations.

        Parameters
        ----------
        inf_arr : List[int]
            The array of inferior sequence separations.
        sup_arr : List[int]
            The array of superior sequence separations.

        Returns
        -------
        List[Tuple[int, int]]
            A list of tuples representing all possible combinations.
        """
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
                            combi.append((tmp_2d[i][p], tmp_2d[j][q]))
        return combi
