__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2022"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import sys
import time
import numpy as np
sys.path.append('../../../')
from tmkit.seqnetrr.Path import to
from tmkit.seqnetrr.window.base import Pair as ecabPair
from tmkit.seqnetrr.net.Reader import reader as prrcreader
from tmkit.seqnetrr.util.Console import console


class bipartite(ecabPair.pair):
    """
    Methods
    -------
        pairids(), assign()

    Notes
    -----
        bipartite class offers methods to assign ECA to global pairs.

    """

    def __init__(
            self,
            sequence,
            window_size,
            window_m_ids,
            kind='memconp',
            patch_size=None,
            verbose=True,
            input_kind='general',
    ):
        """

        Parameters
        ----------
        sequence
        window_size
        window_m_ids
        kind
        patch_size
        """
        super(bipartite, self).__init__(sequence, window_size, window_m_ids)
        self.prrcreader = prrcreader(
            seq_sep_inferior=None,
            seq_sep_superior=None
        )
        if kind == 'memconp':
            self.bigraph = [
                # self.num_to_dos types in MemConP
                [4, -4], [4, 4], [3, -4], [-4, 3], [3, 4],
                [4, 3], [0, -4], [0, 4], [0, -3], [0, 3],
                [-1, 0], [1, 0], [0, 0], [0, -1], [0, 1],
                [3, 0], [-3, 0], [4, 0], [-4, 0], [-3, -4],
                [-4, -3], [-3, 4], [4, -3], [-4, -4], [-4, 4],
            ]
        if kind == 'patch':
            self.bigraph = self.computlib.patch(length=patch_size)
            # print(self.bigraph)
        if kind == 'cross':
            self.bigraph = [
                [-1, 0], [1, 0], [0, 0], [0, 1], [0, -1],
            ]
        if kind == 'unchanged':
            self.bigraph = [
                [0, 0],
            ]
        self.num_to_dos = len(self.bigraph)
        self.num_to_dos_in_window = self.num_to_dos * self.aa_in_window_size
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
        Notes
        -----
            pairids() constitutes all global pairs.

        Methods
        -------
            1>. pairids
                1st dimension: all pairs number
                2nd dimension: (2 * window_size + 1) * length of bigraph list
                3rd dimension: 2 (a pair)
            1>. block 1:    traversing all pairs to be processed.
                |--->block 1.1: traversing all amino acids in a window.
                    |--->block 1.1.1:
                        assigning None to those amino acids whose index
                        beyond sequence length.
                    |--->block 1.1.2:
                        assigning calc results to rest of amino acids.
                            |--->block 1.1.2.1:
                                assigning None to those indices (original
                                amino acid index minus number in bigraph
                                list) beyond sequence length.
                            |--->block 1.1.2.2:
                                assigning results to array global_pair_ids.
            block 2: assign ECA from ccmpred file
                |--->block 2.1: read ccmpred file
                |--->block 2.2: assign ECA from ccmpred file
            block 3: assign ECA from plmc file
                |--->block 3.1: read plmc file
                |--->block 3.2: assign ECA from plmc file
            block 4: assign ECA from gdca file
                |--->block 4.1: read gdca file
                |--->block 4.2: assign ECA from gdca file

        Returns
        -------
        3d array,list

        """
        start_time = time.time()
        n = len(self.sequence)
        num_pending = len(self.bigraph)
        num_aa_in_window = len(self.window_m_ids[0][0])
        global_pair_ids = [[] for _ in range(self.num_pairs)]
        # #/*** block 1 ***/
        for i in range(self.num_pairs):
            # #/*** block 1.1 ***/
            for j in range(num_aa_in_window):
                # #/*** block 1.1.1 ***/
                if self.window_m_ids[i][0][j] is None or self.window_m_ids[i][1][j] is None:
                    for k in range(num_pending):
                        global_pair_ids[i].append([None, None])
                # #/*** block 1.1.2 ***/
                else:
                    for k in range(num_pending):
                        # #/*** block 1.1.2.1 ***/
                        left = self.window_m_ids[i][0][j] - self.bigraph[k][0]
                        right = self.window_m_ids[i][1][j] - self.bigraph[k][1]
                        left_inf = left < 1
                        left_sup = left > n
                        right_inf = right < 1
                        right_sup = right > n
                        reflexive = left == right
                        if left_inf or left_sup or right_inf or right_sup or reflexive:
                            global_pair_ids[i].append([None, None])
                        # #/*** block 1.1.2.2 ***/
                        else:
                            if left < right:
                                global_pair_ids[i].append([left, right])
                            else:
                                global_pair_ids[i].append([right, left])
        end_time = time.time()
        self.console.print('======>bipartite pair generation: {time}s.'.format(time=end_time - start_time))
        # print(global_pair_ids)
        # print(len(global_pair_ids))
        # print(len(global_pair_ids[0]))
        # print(global_pair_ids[0])
        # print(len(global_pair_ids[0][0]))
        # print(global_pair_ids[0][0])
        return global_pair_ids

    def assign(self, list_2d, fpn=None, simu_seq_len=100, mode='hash'):
        start_time = time.time()
        list_2d_ = list_2d
        if mode == 'hash_rl':
            global_pair_ids = self.pairids()
            pairs_left = []
            pairs_right = []
            for i in range(self.num_pairs):
                for j in range(self.num_to_dos * (2 * self.window_size + 1)):
                    pairs_left.append(global_pair_ids[i][j][0])
                    pairs_right.append(global_pair_ids[i][j][1])
            # print('Left pairs {}: {}'.format(len(pairs_right), len(pairs_left)))
            # print('Right pairs {}: {}'.format(len(pairs_left), len(pairs_right)))
            mark = len(pairs_left)
            # #/*** block 1 ***/
            # #/*** block 1.1 ***/
            evfold_dict = self.file_initiator(
                fpn=simu_seq_len if self.input_kind == 'simulate' else fpn,
                sort_=5,
            )
            # print(evfold_dict)
            # #/*** block 1.2 ***/
            FCj = 0
            for i in range(mark):
                if i % (self.num_to_dos * (2 * self.window_size + 1)) == 0:
                    FCj += 1
                if pairs_left[i] is None or pairs_right[i] is None:
                    list_2d_[FCj - 1].append(0)
                else:
                    inf = pairs_left[i]
                    sup = pairs_right[i]
                    # print([inf, sup])
                    list_2d_[FCj - 1].append(evfold_dict[inf][sup])
        elif mode == 'hash_ori':
            evfold_dict = self.file_initiator(
                fpn=simu_seq_len if self.input_kind == 'simulate' else fpn,
                sort_=5,
            )
            global_pair_ids = self.pairids()
            # #/*** block 1 ***/
            for i in range(self.num_pairs):
                # #/*** block 1.1 ***/
                for j in range(self.num_to_dos_in_window):
                    inf = global_pair_ids[i][j][0]
                    sup = global_pair_ids[i][j][1]
                    if inf is None or sup is None:
                        list_2d_[i].append(0)
                    else:
                        list_2d_[i].append(evfold_dict[inf][sup])
        elif mode == 'hash':
            n = len(self.sequence)
            num_pending = len(self.bigraph)
            num_aa_in_window = len(self.window_m_ids[0][0])
            evfold_dict = self.file_initiator(
                fpn=simu_seq_len if self.input_kind == 'simulate' else fpn,
                sort_=5,
            )
            # #/*** block 1 ***/
            for i in range(self.num_pairs):
                # #/*** block 1.1 ***/
                for j in range(num_aa_in_window):
                    # #/*** block 1.1.1 ***/
                    if self.window_m_ids[i][0][j] is None or self.window_m_ids[i][1][j] is None:
                        for k in range(num_pending):
                            # global_pair_ids[i].append([None, None])
                            list_2d_[i].append(0)
                    # #/*** block 1.1.2 ***/
                    else:
                        for k in range(num_pending):
                            # #/*** block 1.1.2.1 ***/
                            left = self.window_m_ids[i][0][j] - self.bigraph[k][0]
                            right = self.window_m_ids[i][1][j] - self.bigraph[k][1]
                            left_inf = left < 1
                            left_sup = left > n
                            right_inf = right < 1
                            right_sup = right > n
                            reflexive = left == right
                            if left_inf or left_sup or right_inf or right_sup or reflexive:
                                # global_pair_ids[i].append([None, None])
                                list_2d_[i].append(0)
                            # #/*** block 1.1.2.2 ***/
                            else:
                                if left < right:
                                    list_2d_[i].append(evfold_dict[left][right])
                                else:
                                    list_2d_[i].append(evfold_dict[right][left])
        elif mode == 'pandas':
            n = len(self.sequence)
            num_pending = len(self.bigraph)
            num_aa_in_window = len(self.window_m_ids[0][0])
            evfold_df = self.file_initiator(
                fpn=simu_seq_len if self.input_kind == 'simulate' else fpn,
                is_sort=True,
                sort_=3,
            )
            evfold_df = evfold_df.set_index(['id_1', 'id_2'])
            # print(evfold_df)
            # evfold_df_gp = evfold_df.groupby(by=['id_1', 'id_2'])
            # evfold_df_gp_keys = evfold_df_gp.groups.keys()
            # print(evfold_df_gp_keys)
            # #/*** block 1 ***/
            for i in range(self.num_pairs):
                # #/*** block 1.1 ***/
                for j in range(num_aa_in_window):
                    # #/*** block 1.1.1 ***/
                    if self.window_m_ids[i][0][j] is None or self.window_m_ids[i][1][j] is None:
                        for k in range(num_pending):
                            # global_pair_ids[i].append([None, None])
                            list_2d_[i].append(0)
                    # #/*** block 1.1.2 ***/
                    else:
                        for k in range(num_pending):
                            # #/*** block 1.1.2.1 ***/
                            left = self.window_m_ids[i][0][j] - self.bigraph[k][0]
                            right = self.window_m_ids[i][1][j] - self.bigraph[k][1]
                            left_inf = left < 1
                            left_sup = left > n
                            right_inf = right < 1
                            right_sup = right > n
                            reflexive = left == right
                            if left_inf or left_sup or right_inf or right_sup or reflexive:
                                # global_pair_ids[i].append([None, None])
                                list_2d_[i].append(0)
                            # #/*** block 1.1.2.2 ***/
                            else:
                                if left < right:
                                    # print(evfold_df.at[(left, right), 'score'])
                                    list_2d_[i].append(evfold_df.at[(left, right), 'score'])
                                    # list_2d_[i].append(evfold_df.loc[(evfold_df['id_1'] == left) & (evfold_df['id_2'] == right)])
                                    # list_2d_[i].append(evfold_df.ix[(left, right), 'score'])
                                    # list_2d_[i].append(evfold_df_gp.get_group((left, right))['score'].values[0])
                                else:
                                    # print(evfold_df.at[(right, left), 'score'])
                                    list_2d_[i].append(evfold_df.at[(right, left), 'score'])
                                    # list_2d_[i].append(evfold_df.loc[(evfold_df['id_1'] == right) & (evfold_df['id_2'] == left)])
                                    # list_2d_[i].append(evfold_np[2][(evfold_np[0] == right) & (evfold_np[1] == left)])
                                    # list_2d_[i].append(evfold_df.ix[(right, left), 'score'])
                                    # list_2d_[i].append(evfold_df_gp.get_group((right, left))['score'].values[0])
        elif mode == 'numpy':
            n = len(self.sequence)
            num_pending = len(self.bigraph)
            num_aa_in_window = len(self.window_m_ids[0][0])
            evfold_df = self.file_initiator(
                fpn=simu_seq_len if self.input_kind == 'simulate' else fpn,
                is_sort=True,
                sort_=3,
            )
            evfold_np = np.array(evfold_df).T
            # print(evfold_np)
            # #/*** block 1 ***/
            for i in range(self.num_pairs):
                # #/*** block 1.1 ***/
                for j in range(num_aa_in_window):
                    # #/*** block 1.1.1 ***/
                    if self.window_m_ids[i][0][j] is None or self.window_m_ids[i][1][j] is None:
                        for k in range(num_pending):
                            # global_pair_ids[i].append([None, None])
                            list_2d_[i].append(0)
                    # #/*** block 1.1.2 ***/
                    else:
                        for k in range(num_pending):
                            # #/*** block 1.1.2.1 ***/
                            left = self.window_m_ids[i][0][j] - self.bigraph[k][0]
                            right = self.window_m_ids[i][1][j] - self.bigraph[k][1]
                            left_inf = left < 1
                            left_sup = left > n
                            right_inf = right < 1
                            right_sup = right > n
                            reflexive = left == right
                            if left_inf or left_sup or right_inf or right_sup or reflexive:
                                # global_pair_ids[i].append([None, None])
                                list_2d_[i].append(0)
                            # #/*** block 1.1.2.2 ***/
                            else:
                                if left < right:
                                    # print(evfold_np[2][(evfold_np[0] == left) & (evfold_np[1] == right)][0])
                                    list_2d_[i].append(evfold_np[2][(evfold_np[0] == left) & (evfold_np[1] == right)][0])
                                else:
                                    list_2d_[i].append(evfold_np[2][(evfold_np[0] == right) & (evfold_np[1] == left)][0])
        end_time = time.time()
        self.console.print('======>bipartite pair assignment: {time}s.'.format(time=end_time - start_time))
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
    # fasta_path = to('data/example/5lkiA.fasta')
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
    # print(window_m_ids)
    # print(len(window_m_ids))
    # print(len(window_m_ids[0]))
    #
    # print(window_m_ids[0])
    # print(len(window_m_ids[0][0]))
    # print(window_m_ids[0][0])

    # /* global pairs */
    p = bipartite(
        sequence=sequence,
        window_size=window_size,
        window_m_ids=window_m_ids,
        kind='patch',
        # kind='cross',
        # kind='memconp',
        # kind='unchanged',
        patch_size=2,
        # input_kind='general',
        # input_kind='freecontact',
        input_kind='simulate',
    )

    # /* global ec scores */
    vec = p.assign(
        list_2d=position,
        fpn=to('data/example/') + DEFINE['prot_name'] + DEFINE['file_chain'] + '.evfold',
        # mode='hash_rf',
        # mode='hash_ori',
        mode='hash',
        # mode='pandas',
        # mode='numpy',
    )
    # print(vec)
