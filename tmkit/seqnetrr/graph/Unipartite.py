__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2022"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import sys
import time
import itertools
import numpy as np
sys.path.append('../../')
from tmkit.seqnetrr.Path import to
from tmkit.seqnetrr.window.base import Pair as ecabPair
from tmkit.seqnetrr.net.Reader import reader as prrcreader
from tmkit.seqnetrr.util.Console import console


class unipartite(ecabPair.pair):
    """

    Notes
    -----
       make(), assign().
    reflexive class offers methods to assign CI to reflexive pairs.

    References
    ----------
       It has been built since April, 2018.
       Change Log:
       1>. It has been revised since the end of June, 2018.
       2>. It has been revised since Oct. 11th, 2018.

    """

    def __init__(
            self,
            sequence,
            window_size,
            window_m_ids,
            verbose=True,
            input_kind='general',
    ):
        super(unipartite, self).__init__(sequence, window_size, window_m_ids)
        self.prrcreader = prrcreader(
            seq_sep_inferior=None,
            seq_sep_superior=None
        )
        self.console = console()
        self.console.verbose = verbose
        self.input_kind = input_kind
        if self.input_kind == 'general':
            self.file_initiator = self.prrcreader.general
        elif self.input_kind == 'freecontact':
            self.file_initiator = self.prrcreader.freecontact
        elif self.input_kind == 'mutual information':
            self.file_initiator = self.prrcreader.mi
        elif self.input_kind == 'gdca':
            self.file_initiator = self.prrcreader.gdca
        elif self.input_kind == 'ccmpred':
            self.file_initiator = self.prrcreader.ccmpred
        elif self.input_kind == 'plmc':
            self.file_initiator = self.prrcreader.plmc
        elif self.input_kind == 'simulate':
            self.file_initiator = self.prrcreader.simulate
        else:
            self.file_initiator = self.prrcreader.general

    def pairids(self):
        """

        Methods
        -------
            1>. In this method, we constituted all reflexive pairs commbinations complying
               with the concept of localEVfold, which means we eliminate all symmetric pairs,
               like [a, b] or [b, a]. Because those two values equal with each other.
               It is noted that the action below we haven't done yet: let a be first and b
               be second if a < b.
            2>. a. 1st dimension is also an ensemble of all pairs being in contact or not.
               Length of first dimension is, for example, 119 (or first 800 that we specify)
               for contact pairs in protein sequence 1atz A chain.
               b. 2nd dimension includes the combinations of all pairs regularized by windows.
               An example is that window size is 5, the length of second dimension is
               [(5*2+1)(5*2)/2]*2 = 110. The correct understanding of number 2 outside square
               bracket is that we have two residues, so we have to multipy 2 outside the
               square bracket.
               c. 3rd dimension is two residues serving as a pair.
            3>. block 1: pairs[i][0] (e.g. [1, 2, 5]) is a residues ensemble that has been windowed by left
                        residue of a pair. pairs[i][1] is a residues ensemble that has been
                        windowed by right residue of a pair. itertools.combinations() perfroms
                        any two residues combination from pairs[i][0] or pairs[i][1].
               |------- block 1.1: l1 is any two residues combination from side_of_pair1, e.g.
                                   [1, 2], [2, 5], [1, 5].
               |------- block 1.2: l2 is any two residues combination from side_of_pair2.

        Raises
        ------
            1>. It has been revised since the end of June, 2018.
            2>. It has been revised since Oct. 10th, 2018.
            3>. It has been revised since Sep. 19th, 2019.

        Returns
        -------
            3d array

        """
        start_time = time.time()
        local_pairs = [[] for _ in range(self.num_pairs)]
        # #/*** block 1 ***/
        for i in range(self.num_pairs):
            # #/*** block 1.1 ***/
            t1 = self.combo2x2(self.window_m_ids[i][0])
            # print('win',self.window_m_ids[i][0])
            # print(t1)
            # for l1 in t1:
            #     if l1[0] is not None and l1[1] is not None and l1[0] < l1[1]:
            #         local_pairs[i].append([l1[0], l1[1]])
            #     else:
            #         local_pairs[i].append([l1[1], l1[0]])
            for l1 in t1:
                if l1[0] is not None and l1[1] is None:
                    local_pairs[i].append([l1[0], None])
                elif l1[0] is None and l1[1] is not None:
                    local_pairs[i].append([None, l1[1]])
                elif l1[0] is not None and l1[1] is not None:
                    if l1[0] < l1[1]:
                        local_pairs[i].append([l1[0], l1[1]])
                    else:
                        local_pairs[i].append([l1[1], l1[0]])
                else:
                    local_pairs[i].append([None, None])
            # #/*** block 1.2 ***/
            t2 = self.combo2x2(self.window_m_ids[i][1])
            # for l2 in t2:
            #     if l2[0] is not None and l2[1] is not None and l2[0] < l2[1]:
            #         local_pairs[i].append([l2[0], l2[1]])
            #     else:
            #         local_pairs[i].append([l2[1], l2[0]])
            for l2 in t2:
                if l2[0] is not None and l2[1] is None:
                    local_pairs[i].append([l2[0], None])
                elif l2[0] is None and l2[1] is not None:
                    local_pairs[i].append([None, l2[1]])
                elif l2[0] is not None and l2[1] is not None:
                    if l2[0] < l2[1]:
                        local_pairs[i].append([l2[0], l2[1]])
                    else:
                        local_pairs[i].append([l2[1], l2[0]])
                else:
                    local_pairs[i].append([None, None])
        end_time = time.time()
        self.console.print('======>unipartite pair generation: {time}s.'.format(time=end_time - start_time))
        return local_pairs

    def combo2x2(self, array):
        """

        Notes
        -----
            nonrepeated 2x2 combination of elements of an array.

        Parameters
        ----------
        array
            amount of combo2x2: L*(L-1)/2.

        Returns
        -------

        """
        combo = []
        ob = itertools.combinations(array, 2)
        for i in ob:
            combo.append(list(i))
        return combo

    def assign(self, list_2d, fpn=None, simu_seq_len=100, mode='hash'):
        """

        Notes
        -----
            assign() uses a fast algorithm to generate CI features for given reflexive pairs.

        Methods
        -------
            1>. We provide a very fast data generation method for CIs. Typically this algorithm
            can speed up around 5-10 times than the general method shown in the example below.
            2>. The input dataset is a 2d dataset, like a stack, because we will do a stack op
            later on. Data will be constantly fed into this stack.
            The length of each contact pair or noncontact pair is [(5*2+1)(5*2)/2]*2 = 110
            if we specify for a window size 5. Let's say:
                          number: [(window_size * 2 + 1)(window_size * 2)/2]*2.
            supp: Another fast retrieval way:
            >>># list_2d[j-1].append(
            >>># np.array(ccmpred.loc[(ccmpred['id_1'] == inf) &
            >>># (ccmpred['id_2'] == sup)]['score'])[0])
            3>. :arg [a, b] or [inf, sup]: the inferior(inf) and superior(sup) in a protein
                                      sequence, separately.
            :arg k: k = (a - 1) * length_sequence - {[a * (a + 1)] / 2} + b can be an index
                   of pairwise residue in any CI file.
            4>. block 1: assign CIs and FCj is a vernier of residue pairs to mark which pair we reach.
            |------- block 1.1: read freecontact file
            |------- block 1.2: assign CI from freecontact file
                    |--------- block 1.2.1: i % (2 * self.stretch_window) means the completion
                                            of all pairs in a window for first central pair,
                                            where i is current residue in pair_left. This
                                            sub-block means that assigning CIs will be finished
                                            for each central pair until all residue pairs
                                            combination in this window have been traversed
                                            only once. And then it is next turn (execute
                                            FCj + 1 op) for second central pair and so on.
            block 2: assign CI from ccmpred file
            |------- block 2.1: read ccmpred file
            |------- block 2.2: assign CI from ccmpred file
            block 3: assign CI from plmc file
            |------- block 3.1: read plmc file
            |------- block 3.2: assign CI from plmc file
            block 4: assign CI from gdca file
            |------- block 4.1: read gdca file
            |------- block 4.2: assign CI from gdca file

        Examples
        --------
            The time complexity of an example below is o(n^3)'''
            >>># for i in range(len(local_pair_ids)):
            >>>#     for j in range(len(local_pair_ids[0])):
            >>>#         if local_pair_ids[i][j][0] is None or local_pair_ids[i][j][1] is None:
            >>>#             trainning_data[i].append(0)
            >>>#         else:
            >>>#             for k in range(len(ccmpred_np)):
            >>>#                 if ccmpred_np[k][0] == local_pair_ids[i][j][0] \
            >>>#                         and ccmpred_np[k][1] == local_pair_ids[i][j][1] \
            >>>#                         or ccmpred_np[k][0] == local_pair_ids[i][j][1] \
            >>>#                         and ccmpred_np[k][1] == local_pair_ids[i][j][0]:
            >>>#                     trainning_data[i].append(ccmpred_np[k][2])

        Raises
        ------
            It has been built since April, 2018.
            1>. It has been revised since the end of June, 2018.
            2>. It has been revised since Oct. 10th, 2018.
            3>. It has been revised since Sep. 19th, 2019.
            3>. It has been revised since Sep. 23th, 2019.

        Parameters
        ----------
        list_2d
        fpn
        simu_seq_len
        mode

        Returns
        -------
            2d array - list

        """
        start_time = time.time()
        list_2d_ = list_2d
        if mode == 'hash_rl':
            local_pair_ids = self.pairids()
            # print(local_pair_ids[0])
            # print(len(local_pair_ids))
            # print(len(local_pair_ids[0]))
            # print(len(local_pair_ids[0][0]))
            pairs_left = []
            pairs_right = []
            for i in range(self.num_pairs):
                for j in range(2 * self.stretch_window):
                    pairs_left.append(local_pair_ids[i][j][0])
                    pairs_right.append(local_pair_ids[i][j][1])
            # print('Left Pairs: {}'.format(pairs_left))
            # print('Right Pairs: {}'.format(pairs_right))
            # #/*** block 1 ***/
            FCj = 0
            # #/*** block 1.1 ***/
            evfold_dict = self.file_initiator(
                fpn=simu_seq_len if self.input_kind == 'simulate' else fpn,
                sort_=5,
            )
            # #/*** block 1.2 ***/
            for i in range(len(pairs_left)):
                # #/*** block 1.2.1 ***/
                if i % (2 * self.stretch_window) == 0:
                    FCj += 1
                if pairs_left[i] is None or pairs_right[i] is None:
                    list_2d_[FCj - 1].append(0)
                else:
                    inf = pairs_left[i]
                    sup = pairs_right[i]
                    # print([inf, sup])
                    list_2d_[FCj-1].append(evfold_dict[inf][sup])
        elif mode == 'hash_ori':
            evfold_dict = self.file_initiator(
                fpn=simu_seq_len if self.input_kind == 'simulate' else fpn,
                sort_=5,
            )
            local_pair_ids = self.pairids()
            # #/*** block 1 ***/
            for i in range(self.num_pairs):
                # #/*** block 1.1 ***/
                for j in range(2 * self.stretch_window):
                    inf = local_pair_ids[i][j][0]
                    sup = local_pair_ids[i][j][1]
                    if inf is None or sup is None:
                        list_2d_[i].append(0)
                    else:
                        list_2d_[i].append(evfold_dict[inf][sup])
        elif mode == 'hash':
            evfold_dict = self.file_initiator(
                fpn=simu_seq_len if self.input_kind == 'simulate' else fpn,
                sort_=5,
            )
            # #/*** block 1 ***/
            for i in range(self.num_pairs):
                # #/*** block 1.1 ***/
                t1 = self.combo2x2(self.window_m_ids[i][0])
                # print(self.window_m_ids[i][0])
                # print(self.combo2x2(self.window_m_ids[i][0]))
                for l1 in t1:
                    if l1[0] is not None and l1[1] is None:
                        list_2d_[i].append(0)
                    elif l1[0] is None and l1[1] is not None:
                        list_2d_[i].append(0)
                    elif l1[0] is not None and l1[1] is not None:
                        if l1[0] < l1[1]:
                            list_2d_[i].append(evfold_dict[l1[0]][l1[1]])
                        else:
                            list_2d_[i].append(evfold_dict[l1[1]][l1[0]])
                    else:
                        list_2d_[i].append(0)
                # #/*** block 1.2 ***/
                t2 = self.combo2x2(self.window_m_ids[i][1])
                for l2 in t2:
                    if l2[0] is not None and l2[1] is None:
                        list_2d_[i].append(0)
                    elif l2[0] is None and l2[1] is not None:
                        list_2d_[i].append(0)
                    elif l2[0] is not None and l2[1] is not None:
                        if l2[0] < l2[1]:
                            list_2d_[i].append(evfold_dict[l2[0]][l2[1]])
                        else:
                            list_2d_[i].append(evfold_dict[l2[1]][l2[0]])
                    else:
                        list_2d_[i].append(0)
        elif mode == 'pandas':
            evfold_df = self.file_initiator(
                fpn=simu_seq_len if self.input_kind == 'simulate' else fpn,
                is_sort=True,
                sort_=3,
            )
            evfold_df = evfold_df.set_index(['id_1', 'id_2'])
            # #/*** block 1 ***/
            for i in range(self.num_pairs):
                # #/*** block 1.1 ***/
                t1 = self.combo2x2(self.window_m_ids[i][0])
                for l1 in t1:
                    if l1[0] is not None and l1[1] is None:
                        list_2d_[i].append(0)
                    elif l1[0] is None and l1[1] is not None:
                        list_2d_[i].append(0)
                    elif l1[0] is not None and l1[1] is not None:
                        if l1[0] < l1[1]:
                            # print(evfold_df.at[(l1[0], l1[1]), 'score'])
                            list_2d_[i].append(evfold_df.at[(l1[0], l1[1]), 'score'])
                        else:
                            # print(evfold_df.at[(l1[1], l1[0]), 'score'])
                            list_2d_[i].append(evfold_df.at[(l1[1], l1[0]), 'score'])
                    else:
                        list_2d_[i].append(0)
                # #/*** block 1.2 ***/
                t2 = self.combo2x2(self.window_m_ids[i][1])
                for l2 in t2:
                    if l2[0] is not None and l2[1] is None:
                        list_2d_[i].append(0)
                    elif l2[0] is None and l2[1] is not None:
                        list_2d_[i].append(0)
                    elif l2[0] is not None and l2[1] is not None:
                        if l2[0] < l2[1]:
                            list_2d_[i].append(evfold_df.at[(l2[0], l2[1]), 'score'])
                        else:
                            list_2d_[i].append(evfold_df.at[(l2[1], l2[0]), 'score'])
                    else:
                        list_2d_[i].append(0)
        elif mode == 'numpy':
            evfold_df = self.file_initiator(
                fpn=simu_seq_len if self.input_kind == 'simulate' else fpn,
                is_sort=True,
                sort_=3,
            )
            evfold_np = np.array(evfold_df).T
            # #/*** block 1 ***/
            for i in range(self.num_pairs):
                # #/*** block 1.1 ***/
                t1 = self.combo2x2(self.window_m_ids[i][0])
                for l1 in t1:
                    if l1[0] is not None and l1[1] is None:
                        list_2d_[i].append(0)
                    elif l1[0] is None and l1[1] is not None:
                        list_2d_[i].append(0)
                    elif l1[0] is not None and l1[1] is not None:
                        if l1[0] < l1[1]:
                            list_2d_[i].append(evfold_np[2][(evfold_np[0] == l1[0]) & (evfold_np[1] == l1[1])][0])
                        else:
                            list_2d_[i].append(evfold_np[2][(evfold_np[0] == l1[1]) & (evfold_np[1] == l1[0])][0])
                    else:
                        list_2d_[i].append(0)
                # #/*** block 1.2 ***/
                t2 = self.combo2x2(self.window_m_ids[i][1])
                for l2 in t2:
                    if l2[0] is not None and l2[1] is None:
                        list_2d_[i].append(0)
                    elif l2[0] is None and l2[1] is not None:
                        list_2d_[i].append(0)
                    elif l2[0] is not None and l2[1] is not None:
                        if l2[0] < l2[1]:
                            list_2d_[i].append(evfold_np[2][(evfold_np[0] == l2[0]) & (evfold_np[1] == l2[1])][0])
                        else:
                            list_2d_[i].append(evfold_np[2][(evfold_np[0] == l2[1]) & (evfold_np[1] == l2[0])][0])
                    else:
                        list_2d_[i].append(0)
        self.console.print('======>unipartite pair assignment: {time}s.'.format(time=time.time() - start_time))
        return list_2d_


if __name__ == "__main__":
    from tmkit.seqnetrr.window.Pair import pair
    from tmkit.seqnetrr.sequence.Fasta import fasta as sfasta
    from tmkit.seqnetrr.combo.Position import position as pfasta
    from tmkit.seqnetrr.combo.Length import length as plength

    DEFINE = {
        'prot_name': '1aig',
        'file_chain': 'L',
        'seq_chain': 'L',

        # 'prot_name': '5lki',
        # 'file_chain': 'A',
        # 'seq_chain': 'A',

        'cutoff': 5.5,
        'seq_sep_inferior': 4,
        'seq_sep_superior': None,
        'fasta_path': to('data/example/'),
    }

    # /* sequence */
    fasta_path = to('data/example/1aigL.fasta')
    # sequence = sfasta().get(fasta_path)
    sequence = sfasta().simulate(seq_len=100)

    # /* scenario of position */
    pos_list = plength(seq_sep_inferior=0).topair(len(sequence))

    # /* position */
    position = pfasta(sequence).pair(pos_list=pos_list)

    # /* window */
    window_size = 3
    window_m_ids = pair(
        sequence=sequence,
        position=position,
        window_size=window_size,
    ).mid()
    print(np.array(window_m_ids).shape)
    print(window_m_ids[-1])

    # /* unipartite ec values */
    p = unipartite(
        sequence=sequence,
        window_size=window_size,
        window_m_ids=window_m_ids,
        # input_kind='general',
        # input_kind='freecontact',
        input_kind='simulate',
    )

    result = p.assign(
        list_2d=position,
        fpn=to('data/example/') + DEFINE['prot_name'] + DEFINE['file_chain'] + '.evfold',
        # mode='hash_rl',
        # mode='hash_ori',
        mode='hash',
        # mode='pandas',
        # mode='numpy',
    )
    # print(result)
    print(result[0])
    print(len(result[0]))