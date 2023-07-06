__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import time


class Pair:
    """
    window.pair class offers methods to perform a sliding
    window op for each of central residue pairs for a
    given sequence.

    """

    def __init__(
        self,
        sequence,
        position,
        window_size,
    ):
        self.sequence = sequence
        self.m_pairs = position
        self.window_size = window_size
        self.len_seq = len(self.sequence)
        self.num_pairs = len(self.m_pairs)

    def mid(self):
        """
        Gets all of residues around central residues with a window size.

        Methods
        -------
            1>. This function generates all residues with a sliding
                window for m pairs.
                self.window_size * 4 means all amino acids except for
                two central amino acids.
            2>. block 1:
                --------
                return [al1, al2, al3, ar1, ar2, ar3, bl1, bl2, bl3,
                br1, br2, br3] for one pair a and b. Each of 2 central
                residues is added to the end in each sub-array,
                respectively.
                block 2:
                --------
                assign None to window_m_ids.
            3>. array specification:
                i.  1st dimension includes all pairs being in contact
                    or not in a protein sequence.
                ii. 2nd dimension represents one pair, say 2 central
                    residues, and consists of 2-sub array, each of
                    which stores all residues windowed by one of 2
                    residues.
                iii.3rd dimension will store all residues regulated in
                    a given window size.

        Returns
        -------
        List
            oder number of pairs and name of pairs.

        """
        start_time = time.time()
        window_m_ids = [[[] for _ in range(2)] for _ in range(self.num_pairs)]
        # ###/*** block 1 ***/ ###
        # ###/*** block 1.1 ***/ ###
        for i in range(self.num_pairs):
            left = [
                self.m_pairs[i][0] - (m1_left_id + 1)
                for m1_left_id in range(self.window_size)
            ]
            left.reverse()
            right = [
                self.m_pairs[i][0] + (m1_right_id + 1)
                for m1_right_id in range(self.window_size)
            ]
            window_m_ids[i][0] = (
                window_m_ids[i][0] + left + [self.m_pairs[i][0]] + right
            )
        # print(window_m_ids)
        # ###/*** block 1.2 ***/ ###
        for i in range(self.num_pairs):
            left = [
                self.m_pairs[i][3] - (m2_left_id + 1)
                for m2_left_id in range(self.window_size)
            ]
            left.reverse()
            right = [
                self.m_pairs[i][3] + (m2_right_id + 1)
                for m2_right_id in range(self.window_size)
            ]
            window_m_ids[i][1] = (
                window_m_ids[i][1] + left + [self.m_pairs[i][3]] + right
            )
        # print(window_m_ids)
        # #/*** block 2 ***/
        for i in range(self.num_pairs):
            for j in range(self.window_size * 2 + 1):
                if window_m_ids[i][0][j] < 1 or window_m_ids[i][0][j] > self.len_seq:
                    window_m_ids[i][0][j] = None
                if window_m_ids[i][1][j] < 1 or window_m_ids[i][1][j] > self.len_seq:
                    window_m_ids[i][1][j] = None
        end_time = time.time()
        print(
            "=========>Window molecule generation: {time}s.".format(
                time=end_time - start_time
            )
        )
        return window_m_ids

    def mname(self, window_m_ids):
        """
        Gets all residues names corresponding to mid().

        Methods
        -------
            It will assgin residues in the window with amino acids
            name and assign residues in the window but beyond the
            sequence boundary with None.

            What kind of residues and how many residues the window
            includes, see method mid().

        Returns
        -------
        List
            name of pairs.

        """
        num_pairs = len(window_m_ids)
        window_m_names = [[] for _ in range(num_pairs)]
        for i in range(self.num_pairs):
            for j in range(self.window_size * 4):
                if window_m_ids[i][j] is None:
                    window_m_names[i].append(None)
                # print(window_m_names)
                else:
                    for k, character in enumerate(self.sequence):
                        if window_m_ids[i][j] == k + 1:
                            # print(character)
                            window_m_names[i].append(character)
        return window_m_names
