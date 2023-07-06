__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import List

import argparse
import time

from tmkit.seqnetrr.combo.Length import length as plength
from tmkit.seqnetrr.combo.Position import Position as pfasta
from tmkit.seqnetrr.graph.Bipartite import Bipartite as bigraph
from tmkit.seqnetrr.graph.Cumulative import Cumulative as cumugraph
from tmkit.seqnetrr.graph.Unipartite import Unipartite as unigraph
from tmkit.seqnetrr.window.Pair import Pair
from tmkit.seqnetrr.window.Single import Single
from tmkit.sequence import Fasta as sfasta
from tmkit.util.Writer import Writer as pfwriter


class Controller:
    def __init__(
        self,
        method: str,
        fasta_fpn: str,
        net_fpn: str,
        window_size: int=2,
        seq_sep_inferior: int=0,
        seq_sep_superior: int=None,
        mode: str="internal",
        pair_mode: str="patch",
        assign_mode: str="hash",
        input_kind: str="general",
        list_2d: List=None,
        cumu_ratio: float=None,
        is_sv: bool=False,
        sv_fpn: str=None,
    ):
        """

        Parameters
        ----------
        method: str
            name of a contact prediction method. It can be one of PSICOV, FreeContact, CCMPred, Gremlin, GDCA, PlmDCA, MemConP, Membrain2, and DeepHelicon.
        fasta_fpn: str
            path where a target Fasta file is placed.
        net_fpn: str
            path to a protein residue contact map file.
        window_size: int
            window size
        seq_sep_inferior: int
            The lower bounds of how far any two residues are in pairs.
        seq_sep_superior: int
            The upper bounds of how far any two residues are in pairs.
        mode: str
            internal or external
        pair_mode: str
            mode of global pairs: patch | memconp | cross | unchanged
        assign_mode: str
            mode of assignment: hash | hash_ori | hash_rl | pandas | numpy
        input_kind: str
            input kind for relationships of a network file: general | simulate | freecontact | gdca | cmmpred | plmc
        list_2d: List
            2d list.
        cumu_ratio: float
            cumulative ratio.
        is_sv: bool
             if save files.
        sv_fpn: str
            path to where you want to save files.
        """
        self.pfwriter = pfwriter()

        if mode == "internal":
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
            self.parser = argparse.ArgumentParser(description="The dedupGene module")
            self.parser.add_argument(
                "--method",
                "-m",
                metavar="method",
                dest="m",
                required=True,
                type=str,
                help="str - a method can be: unipartite | bipartite | cumulative",
            )
            self.parser.add_argument(
                "--fasta_fpn",
                "-mol_f",
                metavar="fasta_fpn",
                dest="mol_f",
                required=True,
                type=str,
                help="str - molecule sequence full file path",
            )
            self.parser.add_argument(
                "--net_fpn",
                "-net_f",
                metavar="net_fpn",
                dest="net_f",
                required=True,
                type=str,
                help="str - full file path of relationships between any two molecules",
            )
            self.parser.add_argument(
                "--window_size",
                "-ws",
                metavar="window_size",
                dest="ws",
                default=2,
                type=int,
                help="int - window size",
            )
            self.parser.add_argument(
                "--seq_sep_inferior",
                "-ssinf",
                metavar="seq_sep_inferior",
                dest="ssinf",
                default=0,
                type=int,
                help="int - sequence separation inferior",
            )
            self.parser.add_argument(
                "--seq_sep_superior",
                "-sssup",
                metavar="seq_sep_superior",
                dest="sssup",
                default=None,
                type=str,
                help="str - sequence separation superior",
            )
            self.parser.add_argument(
                "--pair_mode",
                "-pmode",
                metavar="pair_mode",
                dest="pmode",
                default="patch",
                type=str,
                help="str - mode of global pairs: patch | memconp | cross | unchanged",
            )
            self.parser.add_argument(
                "--assign_mode",
                "-amode",
                metavar="assign_mode",
                dest="amode",
                default="hash",
                type=str,
                help="str - mode of assignment: hash | hash_ori | hash_rl | pandas | numpy",
            )
            self.parser.add_argument(
                "--input_kind",
                "-ikind",
                metavar="input_kind",
                dest="ikind",
                default="general",
                type=str,
                help="str - input kind for relationships of a network file: general | simulate | freecontact | gdca | cmmpred | plmc",
            )
            self.parser.add_argument(
                "--cumu_ratio",
                "-cr",
                metavar="cumu_ratio",
                dest="cr",
                default=1.0,
                type=float,
                help="float - cumulative ratio",
            )
            self.parser.add_argument(
                "--is_sv",
                "-issv",
                metavar="is_sv",
                dest="issv",
                default=True,
                type=bool,
                help="bool - to make sure if save to a file",
            )
            self.parser.add_argument(
                "--output_net",
                "-o",
                metavar="output_net",
                dest="o",
                default=None,
                type=str,
                help="str - output net to a file.",
            )
            args = self.parser.parse_args()
            self.method = args.m
            self.fasta_fpn = args.mol_f
            self.net_fpn = args.net_f
            self.window_size = args.ws
            self.seq_sep_inferior = args.ssinf
            self.seq_sep_superior = None if args.sssup == "None" else args.sssup
            self.pair_mode = args.pmode
            self.assign_mode = args.amode
            self.input_kind = args.ikind
            self.cumu_ratio = args.cr
            self.is_sv = args.issv
            self.sv_fpn = args.o
            self.list_2d = None

        self.sequence = sfasta.get(fasta_fpn=self.fasta_fpn)
        self.len_seq = len(self.sequence)

        print(f"===>Molecular sequence: {self.sequence}")
        print(f"===>Molecule length: {self.len_seq}")
        print(f"===>Window size: {self.window_size}")
        print(f"===>Sequence separation inferior: {self.seq_sep_inferior}")
        print(f"===>Sequence separation superior: {self.seq_sep_superior}")
        print(f"===>Mode: {mode}")
        print(f"===>Input kind: {self.input_kind}")

        if self.method == "unipartite":
            self.unipartite()
        elif self.method == "bipartite":
            self.bipartite()
        elif self.method == "cumulative":
            self.cumulative()

    def unipartite(
        self,
    ) -> List:
        """
        Unipartite pipeline.

        Returns
        -------
        2D list

        """
        stime = time.time()
        # /* scenario of position */
        pos_list = plength(
            seq_sep_superior=self.seq_sep_superior,
            seq_sep_inferior=self.seq_sep_inferior,
        ).to_pair(self.len_seq)
        # print(pos_list[:10])

        print(f"===>pair number: {len(pos_list)}")

        # /* position */
        position = pfasta(self.sequence).pair(pos_list=pos_list)
        # print(position[:10])

        # /* window */
        window_m_ids = Pair(
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
        print(f"===>total time: {time.time() - stime}s.")
        if self.is_sv:
            print("===>saving...")
            self.pfwriter.generic(
                df=list_2d,
                sv_fpn=self.sv_fpn,
                header=None,
                index=None,
            )
            print("===>saved!")
        return list_2d

    def bipartite(
        self,
    ) -> List:
        """
        Bipartite pipeline.

        Returns
        -------
            2D list

        """
        stime = time.time()
        print(f"===>Pair mode: {self.pair_mode}")
        # /* scenario of position */
        pos_list = plength(
            seq_sep_superior=self.seq_sep_superior,
            seq_sep_inferior=self.seq_sep_inferior,
        ).to_pair(self.len_seq)
        print(f"===>pair number: {len(pos_list)}")

        # /* position */
        position = pfasta(self.sequence).pair(pos_list=pos_list)

        # /* window */
        window_m_ids = Pair(
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

        print(f"===>total time: {time.time() - stime}s.")
        if self.is_sv:
            print("===>saving...")
            self.pfwriter.generic(
                df=list_2d,
                sv_fpn=self.sv_fpn,
                header=None,
                index=None,
            )
            print("===>saved!")
        return list_2d

    def cumulative(
        self,
    ) -> List:
        """
        Cumulative pipeline.

        Returns
        -------
            2D list

        """
        print(f"cumulative ratio: {self.cumu_ratio}")
        stime = time.time()
        # /* scenario of position */
        pos_list = plength(
            seq_sep_superior=None,
            seq_sep_inferior=None,
        ).tosgl(self.len_seq)
        print(f"===>pair number: {len(pos_list)}")

        # /* position */
        position = pfasta(self.sequence).single(pos_list=pos_list)

        # /* window */
        window_m_ids = Single(
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

        print(f"===>total time: {time.time() - stime}s.")
        if self.is_sv:
            print("===>saving...")
            self.pfwriter.generic(
                df=list_2d,
                sv_fpn=self.sv_fpn,
                header=None,
                index=None,
            )
            print("===>saved!")
        return list_2d
