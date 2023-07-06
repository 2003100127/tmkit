__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import time


class Single:
    """It offers methods to perform a sliding window op for each of central
       residue pairs for a given sequence."""

    def __init__(
        self,
        sequence,
        position,
        window_size,
    ):
        self.sequence = sequence
        self.m_sgls = position
        self.window_size = window_size
        self.len_seq = len(self.sequence)

    def mid(self):
        """
        Gets all of residues around central residues with a window size.

        Methods
        -------
           > This function generates all residues with a sliding window for all pairs being in
             contact or not. The ensemble of final data doesn't include the pair residues
             themselves, which means
             [al1, al2, al3, ar1, ar2, ar3, bl1, bl2, bl3, br1, br2, br3]
             for one pair a and b (the 2 dimension of the dataset) but please notice that it
             does not include a and b themselves inside.
           > block 1: assigning central residues to residues around them.
           > block 2: assigning only None for window_m_id.

        Returns
        -------
        List
            oder number of residues

        """
        start_time = time.time()
        num_m = len(self.m_sgls)
        window_m_id = [[] for _ in range(num_m)]
        # #/*** block 1 ***/
        for i in range(num_m):
            for index_left in range(self.window_size):
                window_m_id[i].append(
                    self.m_sgls[i][0] - (self.window_size - index_left)
                )
            window_m_id[i].append(self.m_sgls[i][0])
            for index_right in range(self.window_size):
                window_m_id[i].append(self.m_sgls[i][0] + (index_right + 1))
        # print(window_m_id)
        # #/*** block 2 ***/
        for i in range(len(window_m_id)):
            for j in range(len(window_m_id[0])):
                if window_m_id[i][j] < 1 or window_m_id[i][j] > len(self.sequence):
                    window_m_id[i][j] = None
        # print(window_m_id)
        print(
            "=========>Window molecule generation: {time}s.".format(
                time=time.time() - start_time
            )
        )
        return window_m_id

    def mname(self, m_idices):
        """
        Gets all residues names corresponding to mid().

        Methods
        -------
           It will assgin residues in the window with amino acids name and assign residues
           in the window but beyond the sequence boundary with None.

        See Also
        --------
           what kind of residues and how many residues the window includes, see method
           mid().

        Parameters
        ----------
        m_idices

        Returns
        -------
        List
            names of residues

        """
        num_m = len(m_idices)
        window_m_name = [[] for _ in range(num_m)]
        for i in range(len(m_idices)):
            for j in range(len(m_idices[0])):
                if m_idices[i][j] is None:
                    window_m_name[i].append(None)
                # print(window_m_name)
                for k, character in enumerate(self.sequence):
                    if m_idices[i][j] == k + 1:
                        # print(character)
                        window_m_name[i].append(character)
        # print(len(m_idices), len(window_m_name[92]))
        return window_m_name
