__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import Optional

import sys
import warnings
from time import sleep

import pandas as pd
import requests
from Bio import BiopythonWarning

from tmkit.base import PDB as bpdb
from tmkit.util.Kit import ungz


class PDB(bpdb.Structure):
    def __init__(
        self,
        pdb_fp: str,
        prot_name: str,
        seq_chain: str = "",
        file_chain: Optional[str] = None,
    ) -> None:
        """
        Parameters
        ----------
        pdb_fp : str
            The path to the PDB file.
        prot_name : str
            The name of the protein.
        seq_chain : str, optional
            The chain of the protein sequence, by default "".
        file_chain : Optional[str], optional
            The chain of the PDB file, by default None.
        """
        super().__init__(pdb_fp, prot_name, seq_chain, file_chain)

    def read(self) -> pd.DataFrame:
        """
        Read PDB file and return a pandas DataFrame.

        Returns
        -------
        pd.DataFrame
            A pandas DataFrame containing the PDB file data.
        """
        from biopandas.pdb import PandasPdb
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", BiopythonWarning)
            df = PandasPdb().read_pdb(self.pdb_fpn).df
        return df

    def search_foldseek(self, sv_fp: str) -> str:
        """
        Search Foldseek database for a given PDB file.

        Parameters
        ----------
        sv_fp : str
            The path to save the output Foldseek file (gzip .m8 format).

        Returns
        -------
        str
            'Finished' if the results are saved.

        Examples
        --------
        >>> search_foldseek("Q5VSL9.pdb", "Q5VSL9.m8.gz")
        """

        databases = [
            "afdb50",
            "afdb-swissprot",
            "afdb-proteome",
            "cath50",
            "mgnify_esm30",
            "pdb100",
            "gmgcl_id",
        ]
        self.file_chain = "" if self.file_chain is None else self.file_chain
        with open(self.pdb_fp + self.prot_name + self.file_chain + ".pdb") as pdb_file:
            print("===>Searching databases by foldseek...")
            pdb_content = pdb_file.read()
            ticket = requests.post(
                "https://search.foldseek.com/api/ticket",
                files={"q": (pdb_content, pdb_content, "application/octet-stream")},
                data={
                    "mode": "3diaa",
                    "database[]": databases,
                },
            ).json()
        repeat = True
        while repeat:
            status = requests.get(
                "https://search.foldseek.com/api/ticket/" + ticket["id"]
            ).json()
            if status["status"] == "ERROR":
                sys.exit(0)
            # wait a short time between poll requests
            sleep(1)
            repeat = status["status"] != "COMPLETE"
        # result = requests.get(
        #     "https://search.foldseek.com/api/result/" + ticket["id"] + "/0"
        # ).json()
        download = requests.get(
            "https://search.foldseek.com/api/result/download/" + ticket["id"],
            stream=True,
        )
        with open(
            sv_fp + self.prot_name + self.file_chain + "_foldseek_result.gz", "wb"
        ) as fd:
            for chunk in download.iter_content(chunk_size=128):
                fd.write(chunk)
        ungz(
            file_path=sv_fp,
            file_name=self.prot_name + self.file_chain + "_foldseek_result",
            sv_fp=sv_fp,
            new_suffix=".csv",
        )
        print("===>Results have been saved!")
        return 'Finished'
