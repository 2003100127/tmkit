__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from tmkit.seqnetrr.ComputLib import ComputLib


class Pair:
    def __init__(self, sequence, window_size, window_m_ids):
        """

        Notes
        -----
            1>. self.stretch_window is the size of all possible
                residue pairs combinations for all residues around
                central residue with a window size of 'window_size'.

            2>. self.aa_pairs can retrieve either those pairs to
                be in contact or those pairs not to be in contact,
                depending on input pair type.

        Parameters
        ----------
        sequence
            a molecular sequence
        window_size
            a window size
        window_m_ids
            molecular ids in a window
        """
        self.sequence = sequence
        self.window_size = window_size
        self.aa_in_window_size = 2 * window_size + 1
        self.window_m_ids = window_m_ids
        self.num_pairs = len(self.window_m_ids)
        self.stretch_window = int(
            (self.window_size * 2 + 1) * (self.window_size * 2) / 2
        )
        self.computlib = ComputLib()
