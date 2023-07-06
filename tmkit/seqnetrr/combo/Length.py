__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import pandas as pd
import numpy as np

from tmkit.seqnetrr.combo.Param import param
from tmkit.seqnetrr.combo.Separation import separation


class length(param):
    def __init__(self, seq_sep_inferior: int = None, seq_sep_superior: int = None) -> None:
        """
        Parameters
        ----------
        seq_sep_inferior : int, optional
            inferior separation, by default None
        seq_sep_superior : int, optional
            superior separation, by default None
        """
        super().__init__(seq_sep_inferior, seq_sep_superior)

    def topair(self, length: int, kind: str = "standard") -> np.ndarray:
        """
        Given length of a protein sequence, it gets fasta
        ids of residue pairs of a protein regulated by
        seq_sep_inferior and (or) seq_sep_superior.

        Parameters
        ----------
        length : int
            the length of a molecular sequence
        kind : str, optional
            type of output, by default "standard"

        Returns
        -------
        np.ndarray
            2d array
        """
        df_ = pd.DataFrame(self.computlib.num2arr(length))
        if kind == "standard":
            return (
                separation(
                    df=df_,
                    first=0,
                    second=1,
                    is_sort=False,
                    seq_sep_inferior=self.seq_sep_inferior,
                    seq_sep_superior=self.seq_sep_superior,
                )
                .extract()
                .values.tolist()
            )
        elif kind == "triangular":
            return self.computlib.num2triangular(length)
        elif kind == "under_triangular":
            return self.computlib.num2arr(length)

    def tosgl(self, length: int) -> np.ndarray:
        """
        Given length of a protein sequence, it gets fasta
        ids of residue pairs of a protein regulated by
        seq_sep_inferior and (or) seq_sep_superior.

        Parameters
        ----------
        length : int
            the length of a molecular sequence

        Returns
        -------
        np.ndarray
            2d array
        """
        return self.computlib.num2arr2d(1, length)
