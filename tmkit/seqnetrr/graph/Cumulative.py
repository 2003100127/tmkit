__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import Dict, List, Union

import time

import numpy as np

from tmkit.seqnetrr.net.Reader import Reader as prrcreader
from tmkit.seqnetrr.window.base import Single as ecabSgl


class Cumulative(ecabSgl.Single):
    """A class used to represent cumulative scores for a given sequence."""

    def __init__(
        self,
        sequence: str,
        window_size: int,
        window_m_ids: List[List[Union[int, None]]],
        input_kind: str = "general",
    ) -> None:
        """
        Parameters
        ----------
        sequence : str
            A string representing the amino acid sequence.
        window_size : int
            An integer representing the size of the window.
        window_m_ids : List[List[Union[int, None]]]
            A list of lists containing integers or None (beyond residue IDs) values representing the window indices.
        input_kind : str
            Input kind for relationships of a network file: general | simulate | freecontact | gdca | cmmpred | plmc
        """
        super().__init__(sequence, window_size, window_m_ids)
        self.prrcreader = prrcreader()
        self.window_size = window_size
        self.window_m_ids = window_m_ids
        self.num_aas = len(self.window_m_ids)
        self.sequence = sequence
        self.len_seq = len(self.sequence)
        self.input_kind = input_kind
        if self.input_kind == "general":
            self.file_initiator = self.prrcreader.general
        elif self.input_kind == "freecontact":
            self.file_initiator = self.prrcreader.freecontact
        elif self.input_kind == "mutual information":
            self.file_initiator = self.prrcreader.mi
        elif self.input_kind == "gdca":
            self.file_initiator = self.prrcreader.gdca
        elif self.input_kind == "ccmpred":
            self.file_initiator = self.prrcreader.ccmpred
        elif self.input_kind == "plmc":
            self.file_initiator = self.prrcreader.plmc
        elif self.input_kind == "simulate":
            self.file_initiator = self.prrcreader.simulate
        else:
            self.file_initiator = self.prrcreader.general

    def sigmoid(self, value: float) -> float:
        """
        Returns the sigmoid value of the input.

        Parameters
        ----------
        value : float
            A float value.

        Returns
        -------
        float
            The sigmoid value of the input.
        """
        return 1 / (1 + np.exp(-value))

    def assign(
        self,
        list_2d: List[List[float]],
        L: int,
        simu_seq_len: int = 100,
        fpn: str = None,
        is_activate: bool = False,
    ) -> List[List[float]]:
        """
        Assigns cumulative scores to a 2D list of floats.

        Parameters
        ----------
        list_2d : List[List[float]]
            A 2D list.
        L : int
            An integer representing the length of the sequence.
        simu_seq_len : int, optional
            An integer representing the length of the simulated sequence, by default 100.
        fpn : str, optional
            A string representing the file path name, by default None.
        is_activate : bool, optional
            A boolean value representing whether to activate the sigmoid function, by default False.

        Returns
        -------
        List[List[float]]
            A 2D list.
        """
        start_time = time.time()
        list_2d_ = list_2d
        mm_sum = self.file_initiator(
            fpn=simu_seq_len if self.input_kind == "simulate" else fpn,
            sort_=3,
            is_sort=True,
        )["score"].sum()
        mm_ave = mm_sum / self.len_seq
        mm_dict = self.file_initiator(
            fpn=simu_seq_len if self.input_kind == "simulate" else fpn,
            sort_=7,
            len_seq=self.len_seq,
            L=L,
        )
        for i, m_win_ids in enumerate(self.window_m_ids):
            for j in m_win_ids:
                if j is None:
                    list_2d_[i].append(0)
                else:
                    if is_activate:
                        list_2d_[i].append(self.sigmoid(mm_dict[j] / mm_ave))
                    else:
                        list_2d_[i].append(mm_dict[j] / mm_ave)
        print(
            "======>cumulative assignment: {time}s.".format(
                time=time.time() - start_time
            )
        )
        return list_2d_
