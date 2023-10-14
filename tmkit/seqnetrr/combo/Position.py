__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import List, Tuple


class Position:
    def __init__(self, sequence: str):
        """
        Initialize Position object.

        Parameters
        ----------
        sequence : str
            A string representing the sequence.

        Returns
        -------
        None
        """
        self.sequence = sequence
        self.len_seq = len(self.sequence)

    def single(
        self, pos_list: List,
    ) -> List[List[int]]:
        """
        Calculate the distance matrix for a single position.

        Parameters
        ----------
        pos_list : List[int]
            A list of positions.

        Returns
        -------
        List[List[int]]
            A list of lists representing the distance matrix.
        """
        seq_dict = self.todict(self.sequence)
        len_pairs = len(pos_list)
        dist_matrix = []
        for id in range(len_pairs):
            fas_id1 = pos_list[id][0]
            dist_matrix.append([fas_id1, seq_dict[fas_id1], fas_id1, 0])
        return dist_matrix

    def pair(
        self,
        pos_list: List,
    ) -> List[List[int]]:
        """
        Calculate the distance matrix for a pair of positions.

        Parameters
        ----------
        pos_list : List[Tuple[int, int]]
            A list of tuples representing pairs of positions.

        Returns
        -------
        List[List[int]]
            A list of lists representing the distance matrix.
        """
        seq_dict = self.todict(self.sequence)
        len_pairs = len(pos_list)
        dist_matrix = []
        for id in range(len_pairs):
            fas_id1 = pos_list[id][0]
            fas_id2 = pos_list[id][1]
            dist_matrix.append(
                [
                    fas_id1,
                    seq_dict[fas_id1],
                    fas_id1,
                    fas_id2,
                    seq_dict[fas_id2],
                    fas_id2,
                    0,
                ]
            )
        return dist_matrix

    def todict(self, seq: str) -> dict:
        """
        Convert a sequence string to a dictionary.

        Parameters
        ----------
        seq : str
            A string representing the sequence.

        Returns
        -------
        dict
            A dictionary representing the sequence.
        """
        seq_dict = {}
        len_seq = len(seq)
        for i in range(len_seq):
            seq_dict[i + 1] = seq[i]
        return seq_dict
