__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"


from typing import List


class Index:
    """
    Class for generating index of a sequence.

    Parameters
    ----------
    sequence : List
        A list of elements representing the sequence.

    Attributes
    ----------
    sequence : List
        A list of elements representing the sequence.
    len_seq : int
        The length of the sequence.

    Methods
    -------
    get() -> List[int]
        Returns a list of integers representing the index of the sequence.
    """

    def __init__(self, sequence: List) -> None:
        """
        Constructs all the necessary attributes for the Index object.

        Parameters
        ----------
        sequence : List
            A list of elements representing the sequence.
        """
        self.sequence = sequence
        self.len_seq = len(self.sequence)

    def get(self) -> List[int]:
        """
        Returns a list of integers representing the index of the sequence.

        Returns
        -------
        List[int]
            A list of integers representing the index of the sequence.
        """
        ids = []
        for id in range(self.len_seq):
            ids.append(id + 1)
        return ids
