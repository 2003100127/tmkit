__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2022"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import sys
sys.path.append('../../../')
import pandas as pd
from tmkit.base.Position import position
from tmkit.position.scenario.Separation import separation


class segment(position):

    def __init__(self, seq_sep_inferior=None, seq_sep_superior=None):
        super(segment, self).__init__(seq_sep_inferior, seq_sep_superior)

    def toPair(self, fas_lower, fas_upper):
        """
        ..  summary:
            --------
            get fasta ids of residue pairs of a protein regulated
            by seq_sep_inferior and (or) seq_sep_superior

        :param fas_lower: fasta 1d list
        :param fas_upper: fasta 1d list
        :return:
        """
        if fas_lower == [] and fas_upper == []:
            return []
        else:
            df_ = pd.DataFrame(self.interv2combi(fas_lower, fas_upper))
            pairs = separation(
                df=df_,
                first=0,
                second=1,
                is_sort=False,
                seq_sep_inferior=self.seq_sep_inferior,
                seq_sep_superior=self.seq_sep_superior
            ).extract().values.tolist()
            return pairs

    def toSingle(self, fas_lower, fas_upper):
        """
        ..  summary:
            --------
            get fasta ids of residue pairs of a protein regulated
            by seq_sep_inferior and (or) seq_sep_superior

        :param fas_lower: fasta 1d list
        :param fas_upper: fasta 1d list
        :return:
        """
        return self.asp.interv2single(fas_lower, fas_upper)

