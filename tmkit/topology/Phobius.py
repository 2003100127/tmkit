__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import Any, Dict, List, Tuple

import os
import subprocess

import numpy as np
import pandas as pd

from tmkit.interface import Topology


class Phobius(Topology.Topology):
    """
    Phobius topology class for running Phobius prediction on protein sequences.

    Parameters
    ----------
    Topology : tmkit.interface.Topology
        Base class for all topology classes.

    Methods
    -------
    run(fasta_fpn: str, sv_fpn: str, email: str) -> str:
        Runs Phobius prediction on protein sequences.

    format(phobius_fpn: str) -> pd.DataFrame:
        Formats Phobius prediction output file.

    extract(df: pd.DataFrame) -> Dict[str, Tuple[List[int], List[int]]]:
        Extracts regions from formatted Phobius prediction output file.
    """

    def run(self, fasta_fpn: str, sv_fpn: str, email: str) -> str:
        """
        Runs Phobius prediction on protein sequences.

        Parameters
        ----------
        fasta_fpn : str
            File path to input fasta file.
        sv_fpn : str
            File path to output Phobius prediction file.
        email : str
            Email address for Phobius prediction.

        Returns
        -------
        str
            "finished." if Phobius prediction is completed.
        """
        print("===>Phobius is running python inline...")
        if sv_fpn is None:
            raise ValueError("sv_fpn has to be specified")
        fpnf = os.path.dirname(__file__) + "/lib/Phobius.py"
        order = (
            "python "
            + fpnf
            + " --email "
            + email
            + " --sequence "
            + fasta_fpn
            + " --stype protein --outfile "
            + sv_fpn
        )
        subprocess.Popen(
            order,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            shell=True,
        ).communicate()
        os.rename(
            sv_fpn + ".out.txt",
            sv_fpn + ".jphobius",
        )
        return "finished."

    @classmethod
    def format(cls, phobius_fpn: str) -> pd.DataFrame:
        """
        Formats Phobius prediction output file.

        Parameters
        ----------
        phobius_fpn : str
            File path to Phobius prediction output file.

        Returns
        -------
        pd.DataFrame
            Formatted Phobius prediction output file.
        """
        f = open(phobius_fpn)
        content = [[str(e) for e in line.split()] for line in f]
        df = pd.DataFrame(content)
        row_mark = df.loc[(df[0] == "ID")].index[0]
        df = df.drop(index=np.arange(row_mark + 1))
        row_mark = df.loc[(df[0] == "//")].index[0]
        try:
            df = df.drop(index=[row_mark, row_mark + 1])
        except:
            df = df.drop(index=[row_mark])
        df = df.reset_index(drop=True)
        df["type"] = ""
        if 4 not in df.columns:
            df[4] = None
        if 5 not in df.columns:
            df[5] = None
        for i in range(df.shape[0]):
            if df.iloc[i][4] is None:
                df.at[i, 4] = ""
            if df.iloc[i][5] is None:
                df.at[i, 5] = ""
            df.at[i, "type"] = df.iloc[i][4] + df.iloc[i][5]
        df[2] = df[2].astype(int)
        df[3] = df[3].astype(int)
        return df

    def extract(self, df: pd.DataFrame) -> Dict[str, Tuple[List[int], List[int]]]:
        """
        Extracts regions from formatted Phobius prediction output file.

        Parameters
        ----------
        df : pd.DataFrame
            Formatted Phobius prediction output file.

        Returns
        -------
        Dict[str, Tuple[List[int], List[int]]]
            Dictionary of extracted regions.
        """
        inside = df[[2, 3]].loc[df["type"].isin(["CYTOPLASMIC."])].values.tolist()
        tms = df[[2, 3]].loc[df[1].isin(["TRANSMEM"])].values.tolist()
        outside = df[[2, 3]].loc[df["type"].isin(["NONCYTOPLASMIC."])].values.tolist()
        signal = df[[2, 3]].loc[df[1].isin(["SIGNAL"])].values.tolist()
        cregion = df[[2, 3]].loc[df["type"].isin(["C-REGION."])].values.tolist()
        hregion = df[[2, 3]].loc[df["type"].isin(["H-REGION."])].values.tolist()
        nregion = df[[2, 3]].loc[df["type"].isin(["N-REGION."])].values.tolist()
        cytoplasmic = self.separate(inside)
        transmembrane = self.separate(tms)
        extracellular = self.separate(outside)
        signal = self.separate(signal)
        cregion = self.separate(cregion)
        hregion = self.separate(hregion)
        nregion = self.separate(nregion)
        phobius_dict = {
            "cyto_lower": cytoplasmic[0],
            "cyto_upper": cytoplasmic[1],
            "tmh_lower": transmembrane[0],
            "tmh_upper": transmembrane[1],
            "extra_lower": extracellular[0],
            "extra_upper": extracellular[1],
            "signal_lower": signal[0],
            "signal_upper": signal[1],
            "cregion_lower": cregion[0],
            "cregion_upper": cregion[1],
            "hregion_lower": hregion[0],
            "hregion_upper": hregion[1],
            "nregion_lower": nregion[0],
            "nregion_upper": nregion[1],
        }
        return phobius_dict

    def separate(self, arr: List[Tuple[int, int]]) -> Tuple[List[int], List[int]]:
        """
        Separates regions into lower and upper bounds.

        Parameters
        ----------
        arr : List[Tuple[int, int]]
            List of regions.

        Returns
        -------
        Tuple[List[int], List[int]]
            Tuple of lower and upper bounds.
        """
        lower = []
        upper = []
        for i in arr:
            lower.append(i[0])
            upper.append(i[1])
        return lower, upper
