__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import List

import pandas as pd

from tmkit.seqnetrr.combo.Param import Param
from tmkit.seqnetrr.combo.Separation import Separation


class length(Param):
    def __init__(
        self, seq_sep_inferior: int = None, seq_sep_superior: int = None
    ) -> None:
        """
        Parameters
        ----------
        seq_sep_inferior : int, optional
            inferior separation, by default None
        seq_sep_superior : int, optional
            superior separation, by default None
        """
        super().__init__(seq_sep_inferior, seq_sep_superior)

    def to_pair(self, length: int, kind: str = "standard") -> List:
        """
        Given length of a protein sequence, it gets fasta
        ids of residue pairs of a protein controlled by
        seq_sep_inferior and (or) seq_sep_superior.

        Parameters
        ----------
        length : int
            the length of a molecular sequence
        kind : str, optional
            type of output, by default "standard"

        Returns
        -------
        List
            2d list
        """
        df_ = pd.DataFrame(self.computlib.num2arr(length))
        if kind == "standard":
            return (
                Separation(
                    df=df_,
                    first=0,
                    second=1,
                    is_sort=False,
                    seq_sep_inferior=self.seq_sep_inferior,
                    seq_sep_superior=self.seq_sep_superior,
                ).extract().values.tolist()
            )
        elif kind == "triangular":
            return self.computlib.num2triangular(length)
        elif kind == "under_triangular":
            return self.computlib.num2arr(length)

    def tosgl(self, length: int) -> List:
        """
        Given length of a protein sequence, it gets fasta
        ids of residue pairs of a protein controlled by
        seq_sep_inferior and (or) seq_sep_superior.

        Parameters
        ----------
        length : int
            the length of a molecular sequence

        Returns
        -------
        List
            2d list
        """
        return self.computlib.num2arr2d(1, length)
