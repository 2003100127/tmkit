__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import List

from abc import ABCMeta, abstractmethod


class Topology(metaclass=ABCMeta):
    """
    Abstract base class for topology.
    """

    @abstractmethod
    def run(self, *args: List) -> None:
        """
        Run the topology.

        Parameters
        ----------
        args : List
            List of arguments to be passed to the topology.
        """
        pass

    @abstractmethod
    def extract(self, arr_2d: List[List]) -> List:
        """
        Extract the topology.

        Parameters
        ----------
        arr_2d : List[List]
            2D list of data to be extracted.

        Returns
        -------
        List
            List of extracted data.
        """
        pass
