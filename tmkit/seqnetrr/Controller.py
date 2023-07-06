__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import time
import argparse
from tmkit.seqnetrr.window.Pair import pair
from tmkit.seqnetrr.window.Single import single
from tmkit.util.Writer import writer as pfwriter
from tmkit.seqnetrr.combo.Length import length as plength
from tmkit.sequence import Fasta as sfasta
from tmkit.seqnetrr.combo.Position import position as pfasta
from tmkit.seqnetrr.graph.Bipartite import bipartite as bigraph
from tmkit.seqnetrr.graph.Unipartite import unipartite as unigraph
from tmkit.seqnetrr.graph.Cumulative import cumulative as cumugraph


class controller:

    def __init__(
            self,
            method,
            fasta_fpn,
            net_fpn,
            window_size=2,
            seq_sep_inferior=0,
            seq_sep_superior=None,
            mode='internal',
            pair_mode='patch',
            assign_mode='hash',
            input_kind='general',
            list_2d=None,
            cumu_ratio=None,
            is_sv=False,
            sv_fpn=None,
    ):
        self.pfwriter = pfwriter()

        if mode == 'internal':
            self.method = method
            self.net_fpn = net_fpn
            self.fasta_fpn = fasta_fpn
            self.window_size = window_size
            self.seq_sep_inferior = seq_sep_inferior
            self.seq_sep_superior = seq_sep_superior

            self.pair_mode = pair_mode
            self.assign_mode = assign_mode
            self.input_kind = input_kind
            self.cumu_ratio = cumu_ratio
            self.list_2d = list_2d
            self.is_sv = is_sv
            self.sv_fpn = sv_fpn
        else:
            self.parser = argparse.ArgumentParser(
                description='The dedupGene module'
            )
            self.parser.add_argument(
                "--method", "-m",
                metavar='method',
                dest='m',
                required=True,
                type=str,
                help='str - a method can be: unipartite | bipartite | cumulative',
            )
            self.parser.add_argument(
                "--fasta_fpn", "-mol_f",
                metavar='fasta_fpn',
                dest='mol_f',
                required=True,
                type=str,
                help='str - molecule sequence full file path',
            )
            self.parser.add_argument(
                "--net_fpn", "-net_f",
                metavar='net_fpn',
                dest='net_f',
                required=True,
                type=str,
                help='str - full file path of relationships between any two molecules',
            )
            self.parser.add_argument(
                "--window_size", "-ws",
                metavar='window_size',
                dest='ws',
                default=2,
                type=int,
                help='int - window size',
            )
            self.parser.add_argument(
                "--seq_sep_inferior", "-ssinf",
                metavar='seq_sep_inferior',
                dest='ssinf',
                default=0,
                type=int,
                help='int - sequence separation inferior',
            )
            self.parser.add_argument(
                "--seq_sep_superior", "-sssup",
                metavar='seq_sep_superior',
                dest='sssup',
                default=None,
                type=str,
                help='str - sequence separation superior',
            )
            self.parser.add_argument(
                "--pair_mode", "-pmode",
                metavar='pair_mode',
                dest='pmode',
                default='patch',
                type=str,
                help='str - mode of global pairs: patch | memconp | cross | unchanged',
            )
            self.parser.add_argument(
                "--assign_mode", "-amode",
                metavar='assign_mode',
                dest='amode',
                default='hash',
                type=str,
                help='str - mode of assignment: hash | hash_ori | hash_rl | pandas | numpy',
            )
            self.parser.add_argument(
                "--input_kind", "-ikind",
                metavar='input_kind',
                dest='ikind',
                default='general',
                type=str,
                help='str - input kind for relationships of a network file: general | simulate | freecontact | gdca | cmmpred | plmc',
            )
            self.parser.add_argument(
                "--cumu_ratio", "-cr",
                metavar='cumu_ratio',
                dest='cr',
                default=1.,
                type=float,
                help='float - cumulative ratio',
            )
            self.parser.add_argument(
                "--is_sv", "-issv",
                metavar='is_sv',
                dest='issv',
                default=True,
                type=bool,
                help='bool - to make sure if save to a file',
            )
            self.parser.add_argument(
                "--output_net", "-o",
                metavar='output_net',
                dest='o',
                default=None,
                type=str,
                help='str - output net to a file.',
            )
            args = self.parser.parse_args()
            self.method = args.m
            self.fasta_fpn = args.mol_f
            self.net_fpn = args.net_f
            self.window_size = args.ws
            self.seq_sep_inferior = args.ssinf
            self.seq_sep_superior = None if args.sssup == 'None' else args.sssup
            self.pair_mode = args.pmode
            self.assign_mode = args.amode
            self.input_kind = args.ikind
            self.cumu_ratio = args.cr
            self.is_sv = args.issv
            self.sv_fpn = args.o
            self.list_2d = None

        self.sequence = sfasta.get(fasta_fpn=self.fasta_fpn)
        self.len_seq = len(self.sequence)

        print('===>Molecular sequence: {}'.format(self.sequence))
        print('===>Molecule length: {}'.format(self.len_seq))
        print('===>Window size: {}'.format(self.window_size))
        print('===>Sequence separation inferior: {}'.format(self.seq_sep_inferior))
        print('===>Sequence separation superior: {}'.format(self.seq_sep_superior))
        print('===>Mode: {}'.format(mode))
        print('===>Input kind: {}'.format(self.input_kind))

        if self.method == 'unipartite':
            self.unipartite()
        elif self.method == 'bipartite':
            self.bipartite()
        elif self.method == 'cumulative':
            self.cumulative()

    def unipartite(self, ):
        stime = time.time()
        # /* scenario of position */
        pos_list = plength(
            seq_sep_superior=self.seq_sep_superior,
            seq_sep_inferior=self.seq_sep_inferior,
        ).topair(self.len_seq)
        # print(pos_list[:10])

        print('===>pair number: {}'.format(len(pos_list)))

        # /* position */
        position = pfasta(self.sequence).pair(pos_list=pos_list)
        # print(position[:10])

        # /* window */
        window_m_ids = pair(
            sequence=self.sequence,
            position=position,
            window_size=self.window_size,
        ).mid()
        # print(window_m_ids[:10])

        p = unigraph(
            sequence=self.sequence,
            window_size=self.window_size,
            window_m_ids=window_m_ids,
            input_kind=self.input_kind,
        )
        # /* local ec scores */
        list_2d = position if self.list_2d == None else self.list_2d
        p.assign(
            fpn=self.net_fpn,
            list_2d=list_2d,
            mode=self.assign_mode,
        )
        # print(list_2d[:10])
        print('===>total time: {time}s.'.format(time=time.time() - stime))
        if self.is_sv:
            print('===>saving...')
            self.pfwriter.generic(
                df=list_2d,
                sv_fpn=self.sv_fpn,
                header=None,
                index=None,
            )
            print('===>saved!')
        return list_2d

    def bipartite(self, ):
        stime = time.time()
        print('===>Pair mode: {}'.format(self.pair_mode))
        # /* scenario of position */
        pos_list = plength(
            seq_sep_superior=self.seq_sep_superior,
            seq_sep_inferior=self.seq_sep_inferior,
        ).topair(self.len_seq)
        print('===>pair number: {}'.format(len(pos_list)))

        # /* position */
        position = pfasta(self.sequence).pair(pos_list=pos_list)

        # /* window */
        window_m_ids = pair(
            sequence=self.sequence,
            position=position,
            window_size=self.window_size,
        ).mid()

        p = bigraph(
            sequence=self.sequence,
            window_size=self.window_size,
            window_m_ids=window_m_ids,
            kind=self.pair_mode,
            patch_size=2,
            input_kind=self.input_kind,
        )
        # /* global ec scores */
        list_2d = position if self.list_2d == None else self.list_2d
        p.assign(
            fpn=self.net_fpn,
            list_2d=list_2d,
            mode=self.assign_mode,
        )
        # print(list_2d[-5:])

        print('===>total time: {time}s.'.format(time=time.time() - stime))
        if self.is_sv:
            print('===>saving...')
            self.pfwriter.generic(
                df=list_2d,
                sv_fpn=self.sv_fpn,
                header=None,
                index=None,
            )
            print('===>saved!')
        return list_2d

    def cumulative(self, ):
        print('cumulative ratio: {}'.format(self.cumu_ratio))
        stime = time.time()
        # /* scenario of position */
        pos_list = plength(
            seq_sep_superior=None,
            seq_sep_inferior=None,
        ).tosgl(self.len_seq)
        print('===>pair number: {}'.format(len(pos_list)))

        # /* position */
        position = pfasta(self.sequence).single(pos_list=pos_list)

        # /* window */
        window_m_ids = single(
            sequence=self.sequence,
            position=position,
            window_size=self.window_size,
        ).mid()

        p = cumugraph(
            sequence=self.sequence,
            window_size=self.window_size,
            window_m_ids=window_m_ids,
            input_kind=self.input_kind,
        )
        # /* global ec scores */
        list_2d = position if self.list_2d == None else self.list_2d
        p.assign(
            list_2d=list_2d,
            fpn=self.net_fpn,
            L=int(self.len_seq * self.cumu_ratio),
            simu_seq_len=None,
        )

        print('===>total time: {time}s.'.format(time=time.time() - stime))
        if self.is_sv:
            print('===>saving...')
            self.pfwriter.generic(
                df=list_2d,
                sv_fpn=self.sv_fpn,
                header=None,
                index=None,
            )
            print('===>saved!')
        return list_2d