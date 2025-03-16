__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from tmkit.seqnetrr.combo.Param import Param


class Segment(Param):
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

    def tosgl(self, fas_lower, fas_upper):
        """
        ..  summary:
            --------
            get fasta ids of residue pairs of a protein regulated
            by seq_sep_inferior and (or) seq_sep_superior

        :param fas_lower: fasta 1d list
        :param fas_upper: fasta 1d list
        :return:
        """
        return self.computlib.interv2single(fas_lower, fas_upper)
