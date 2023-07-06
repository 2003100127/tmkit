__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import List, Tuple

import pandas as pd

from tmkit.base.Position import Position
from tmkit.position.scenario.Separation import Separation


class Segment(Position):
    def __init__(
        self, seq_sep_inferior: int = None, seq_sep_superior: int = None
    ) -> None:
        super().__init__(seq_sep_inferior, seq_sep_superior)

    def to_pair(
        self, fas_lower: List[str], fas_upper: List[str]
    ) -> List[Tuple[str, str]]:
        """
        Get fasta ids of residue pairs of a protein regulated
        by seq_sep_inferior and (or) seq_sep_superior

        Parameters
        ----------
        fas_lower : List[str]
            Fasta 1d list
        fas_upper : List[str]
            Fasta 1d list

        Returns
        -------
        List[Tuple[str, str]]
            List of residue pairs
        """
        if fas_lower == [] and fas_upper == []:
            return []
        else:
            df_ = pd.DataFrame(self.interv2combi(fas_lower, fas_upper))
            pairs = (
                Separation(
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
            return pairs
