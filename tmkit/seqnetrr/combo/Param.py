__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import Optional

from tmkit.seqnetrr.ComputLib import ComputLib


class Param:
    """
    A class representing a parameter.

    Attributes
    ----------
    seq_sep_inferior : int, optional
        The inferior sequence separation.
    seq_sep_superior : int, optional
        The superior sequence separation.
    computlib : ComputLib
        The computlib object.

    Methods
    -------
    __init__(seq_sep_inferior=None, seq_sep_superior=None)
        Initializes a new instance of the Param class.
    """

    def __init__(
        self,
        seq_sep_inferior: Optional[int] = None,
        seq_sep_superior: Optional[int] = None,
    ) -> None:
        """
        Initializes a new instance of the Param class.

        Parameters
        ----------
        seq_sep_inferior : int, optional
            The inferior sequence separation.
        seq_sep_superior : int, optional
            The superior sequence separation.
        """
        self.seq_sep_inferior = seq_sep_inferior
        self.seq_sep_superior = seq_sep_superior
        self.computlib = ComputLib()
