__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import requests as r
from Bio import SeqIO
from io import StringIO

import pandas as pd

from tmkit.util.Writer import Writer


class Fasta:
    def __init__(
        self,
        prot_series: pd.Series,
    ) -> None:
        """
        Parameters
        ----------
        prot_series : pd.Series
            A pandas series containing protein names.
        """
        self.write = Writer()
        self.prot_dedup = prot_series.unique()

    def uniprot(
        self,
        sv_fp: str = './uniprot/',
        baseUrl = "http://www.uniprot.org/uniprot/"
    ) -> str:
        for i, prot_name in enumerate(self.prot_dedup):
            print(prot_name)
            print(cID)
            url = baseUrl + cID + ".fasta"
            try:
                response = r.post(url)
                cData = ''.join(response.text)
                Seq=StringIO(cData)
                pSeq=list(SeqIO.parse(Seq,'fasta'))
                sequence = ''.join(list(pSeq[0]))
                # print(sequence)
                save(cID, sequence, sv_fp=sv_fp)
            except:
                continue
        return 'Finished'
