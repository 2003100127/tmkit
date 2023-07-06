__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import linecache
import os
import re
import subprocess

import numpy as np

from tmkit.interface import Topology
from tmkit.sequence import Fasta as sfasta
from tmkit.util.Reader import Reader
from tmkit.util.Writer import Writer


class TMHMM(Topology.Topology):
    def __init__(
        self,
    ):
        self.reader = Reader()
        self.writer = Writer()

    def run(
        self,
        fasta_fpn,
        tmhmm_model_fpn,
        tag,
        sv_fpn,
    ):
        """
        Notes
        -----
        This is running python inline by installing pip install tmhmm.py.

        See Also
        --------
        https://github.com/dansondergaard/tmhmm.py
        https://pypi.org/project/tmhmm.py/1.2/

        Parameters
        ----------
        fasta_fpn
        tmhmm_model_fpn
        tag
        sv_fpn

        Returns
        -------

        """
        print("===>TMHMM is running python inline...")
        if sv_fpn is None:
            raise "sv_fpn has to be specified"
        import tmhmm as tmhmmpy

        annotation, posterior = tmhmmpy.predict(
            sequence=sfasta.get(fasta_fpn=fasta_fpn),
            header=None,
            model_or_filelike=os.path.dirname(__file__) + "/lib/TMHMM2.0.model",
            # model_or_filelike=tmhmm_model_fpn,
        )
        self.writer.save([[tag + "_tmhmm", annotation]], sv_fp=sv_fpn)
        return annotation

    def runLinux(
        self,
        fasta_fpn,
        decodeanhmm,
        options,
        modelfile,
        sv_fpn,
    ):
        """
        Notes
        -----
            This is running on Linux using the raw tmhmm executable.

        Parameters
        ----------
        fasta_fpn
            a protein fasta file path
        decodeanhmm
            e.g., './tmhmm-2.0c/bin/decodeanhmm.Linux_x86_64'
        options
            e.g., './tmhmm-2.0c/lib/TMHMM2.0.options'
        modelfile
            e.g., './tmhmm-2.0c/lib/TMHMM2.0.model'
        sv_fpn
            path to save files

        Returns
        -------
            A message string

        """
        print("===>TMHMM is running on Linux...")
        order = (
            "cat "
            + fasta_fpn
            + ".fasta | "
            + decodeanhmm
            + " -f "
            + options
            + " -modelfile "
            + modelfile
            + " -noPrintSeq -noPrintScores -noPrintID -noPrintStat > "
            + sv_fpn
        )
        # print(order)
        subprocess.Popen(
            order,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            shell=True,
        ).communicate()
        return "finished."

    def extract(self, arr_2d):
        """
        Notes
        -----
        Extract topologies.

        Parameters
        ----------
        arr_2d
            2D arr for segs, e.g.,
            [['o', 1, 9],
            ['M', 10, 32],
            ['i', 33, 38],
            ['M', 39, 61],
            ['o', 62, 95],
            ['M', 96, 118],
            ['i', 119, 124],
            ['M', 125, 147],
            ['o', 148, 181],
            ['M', 182, 204],
            ['i', 205, 210],
            ['M', 211, 233],
            ['o', 234, 261],
            ['M', 262, 284],
            ['i', 285, 290],
            ['M', 291, 313],
            ['o', 314, 327],
            ['M', 328, 350],
            ['i', 351, 362],]

        Returns
        -------
            Dict of topologies

        """
        length = len(arr_2d)
        tm_lower, tm_upper = [], []
        cyto_lower, cyto_upper = [], []
        extra_lower, extra_upper = [], []
        rest_lower, rest_upper = [], []
        for i in range(length):
            if arr_2d[i][0] == "M":
                tm_lower.append(arr_2d[i][1])
                tm_upper.append(arr_2d[i][2])
            elif arr_2d[i][0] == "i":
                cyto_lower.append(arr_2d[i][1])
                cyto_upper.append(arr_2d[i][2])
            elif arr_2d[i][0] == "o":
                extra_lower.append(arr_2d[i][1])
                extra_upper.append(arr_2d[i][2])
            else:
                rest_lower.append(arr_2d[i][1])
                rest_upper.append(arr_2d[i][2])
        tmhmm_dict = {
            "cyto_lower": cyto_lower,
            "cyto_upper": cyto_upper,
            "tmh_lower": tm_lower,
            "tmh_upper": tm_upper,
            "extra_lower": extra_lower,
            "extra_upper": extra_upper,
            "rest_lower": rest_lower,
            "rest_upper": rest_upper,
        }
        return tmhmm_dict

    @classmethod
    def formatFromLinux(cls, tmhmm_fpn):
        """
        Notes
        -----
        Reformatting a raw Linux-running tmhmm output file into a 2D arr

        Parameters
        ----------
        tmhmm_fpn
            a tmhmm output file

        Returns
        -------
            2D arr

        """
        if not os.path.exists(tmhmm_fpn):
            raise FileNotFoundError
        # lines = linecache.getlines(tmhmm_fpn)
        line = linecache.getline(tmhmm_fpn, 1)
        # print(line)
        block1 = re.split(r": ", line)
        # print(block1)
        block2 = block1[1].split(", ")
        # print(block2)
        length = len(block2)
        arr = []
        for i in range(length):
            tag = block2[i].split(" ")[0]
            beg = block2[i].split(" ")[1]
            end = block2[i].split(" ")[2]
            arr.append([tag, int(beg), int(end)])
        return arr

    @classmethod
    def formatFromInline(cls, tmhmm_fpn):
        """
        Notes
        -----
        Reformatting a tmhmm output file in fasta format into a 2D arr

        Parameters
        ----------
        tmhmm_fpn
            a tmhmm output file

        Returns
        -------
            2D arr

        """
        if not os.path.exists(tmhmm_fpn):
            raise FileNotFoundError
        annot = sfasta.get(tmhmm_fpn)
        arr = []
        flag = 1
        for i in range(len(annot)):
            if i + 1 != len(annot):
                if annot[i] == annot[i + 1]:
                    continue
                else:
                    arr.append([annot[i], flag, i + 1])
                    flag = i + 2
        arr.append([annot[-1], flag, len(annot)])
        # print(arr)
        return arr

    def totmhhcp(self, arr, sv_fpn=None):
        """
        Notes
        -----
        Working out a file as input to tmhhcp with TMHMM output

        Parameters
        ----------
        arr
            2D arr from formatFromInline or formatFromLinux
        sv_fpn
            path to save the output file

        Returns
        -------
            str

        """
        helix_orien = []
        for i in arr:
            sub = np.arange(i[1], i[2] + 1)
            for j in range(len(sub)):
                if i[0] == "o" or i[0] == "O":
                    helix_orien.append("O")
                elif i[0] == "i":
                    helix_orien.append("I")
                elif i[0] == "M":
                    helix_orien.append("H")
                else:
                    helix_orien.append("U")
        trans_helix = "".join(helix_orien)
        if sv_fpn:
            with open(sv_fpn, "w") as f:
                f.write(trans_helix)
        return trans_helix
