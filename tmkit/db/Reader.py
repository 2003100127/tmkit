__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import numpy as np
import pandas as pd

from tmkit.util.Reader import Reader as greader


class Reader:
    """
    A class for reading various types of interaction data files.

    Attributes
    ----------
    sort_ : int
        The sorting method to use when reading the data files.
    greader : tmkit.util.Reader.reader
        The generic reader object used to read the data files.

    Methods
    -------
    mbpred(mbp_path: str, file_name: str, file_chain: str, sort_: int = 0) -> pd.DataFrame
        Reads an mbpred file and returns a DataFrame with the interact_id and score columns.
    delphi(delphi_path: str, file_name: str, file_chain: str, sort_: int = 0) -> pd.DataFrame
        Reads a delphi file and returns a DataFrame with the interact_id and score columns.
    graphppis(graphppis_path: str, file_name: str, file_chain: str, sort_: int = 0) -> pd.DataFrame
        Reads a graphppis file and returns a DataFrame with the interact_id and score columns.
    tma300(tma300_path: str, file_name: str, file_chain: str, sort_: int = 0) -> pd.DataFrame
        Reads a tma300 file and returns a DataFrame with the interact_id and score columns.
    """

    def __init__(self):
        self.__sort_: int = -1
        self.greader: greader = greader()

    @property
    def sort_(self) -> int:
        return self.__sort_

    @sort_.setter
    def sort_(self, value: int) -> None:
        if value > 7 or value < 0:
            raise ValueError(
                "`sort_` has yet to reach there.",
            )
        else:
            self.__sort_ = value

    def mbpred(
        self, mbp_path: str, file_name: str, file_chain: str, sort_: int = 0
    ) -> pd.DataFrame:
        """
        Reads an mbpred file and returns a DataFrame with the interact_id and score columns.

        Parameters
        ----------
        mbp_path : str
            The path to the directory containing the mbpred file.
        file_name : str
            The name of the file.
        file_chain : str
            The chain identifier for the file.
        sort_ : int, optional
            The sorting method to use when reading the file, by default 0.

        Returns
        -------
        pd.DataFrame
            A DataFrame with the interact_id and score columns.
        """
        self.__sort_ = sort_
        results = self.greader.generic(
            mbp_path + file_name + file_chain + ".mbpred",
            df_sep=",",
            header=0,
            is_utf8=True,
        )
        results.columns = ["index", "aa", "interact_id", "score"]
        results["aa"] = results["aa"].astype(str)
        recombine = results[["interact_id", "score"]]
        return recombine

    def delphi(
        self, delphi_path: str, file_name: str, file_chain: str, sort_: int = 0
    ) -> pd.DataFrame:
        """
        Reads a delphi file and returns a DataFrame with the interact_id and score columns.

        Parameters
        ----------
        delphi_path : str
            The path to the directory containing the delphi file.
        file_name : str
            The name of the file.
        file_chain : str
            The chain identifier for the file.
        sort_ : int, optional
            The sorting method to use when reading the file, by default 0.

        Returns
        -------
        pd.DataFrame
            A DataFrame with the interact_id and score columns.
        """
        self.__sort_ = sort_
        delphi_fpn = delphi_path + file_name + file_chain + ".txt"
        with open(delphi_fpn) as file:
            cues = []
            for line in file:
                if line.split()[0] == "#":
                    continue
                else:
                    cues.append(line.split())
            results = pd.DataFrame(cues)
        results.columns = ["interact_id", "aa", "score"]
        results["aa"] = results["aa"].astype(str)
        results["interact_id"] = results["interact_id"].astype(np.int)
        results["score"] = results["score"].astype(np.float)
        recombine = results[["interact_id", "score"]]
        return recombine

    def graphppis(
        self, graphppis_path: str, file_name: str, file_chain: str, sort_: int = 0
    ) -> pd.DataFrame:
        """
        Reads a graphppis file and returns a DataFrame with the interact_id and score columns.

        Parameters
        ----------
        graphppis_path : str
            The path to the directory containing the graphppis file.
        file_name : str
            The name of the file.
        file_chain : str
            The chain identifier for the file.
        sort_ : int, optional
            The sorting method to use when reading the file, by default 0.

        Returns
        -------
        pd.DataFrame
            A DataFrame with the interact_id and score columns.
        """
        self.__sort_ = sort_
        results = self.greader.generic(
            graphppis_path + file_name + file_chain + ".txt",
            df_sep="\t",
            header=0,
            is_utf8=True,
            comment="#",
        )
        results.columns = [
            "aa",
            "score",
            "label",
        ]
        results["interact_id"] = np.arange(len(results)) + 1
        results = results[["interact_id", "score"]]
        recombine = results[
            [
                "interact_id",
                "score",
            ]
        ]
        return recombine

    def tma300(
        self, tma300_path: str, file_name: str, file_chain: str, sort_: int = 0
    ) -> pd.DataFrame:
        """
        Reads a tma300 file and returns a DataFrame with the interact_id and score columns.

        Parameters
        ----------
        tma300_path : str
            The path to the directory containing the tma300 file.
        file_name : str
            The name of the file.
        file_chain : str
            The chain identifier for the file.
        sort_ : int, optional
            The sorting method to use when reading the file, by default 0.

        Returns
        -------
        pd.DataFrame
            A DataFrame with the interact_id and score columns.
        """
        self.__sort_ = sort_
        results = self.greader.generic(
            tma300_path + file_name + file_chain + ".tma300",
            df_sep="\t",
            header=None,
            is_utf8=True,
        )
        results.columns = [
            "interact_id",
            "aa",
            "score",
        ]
        results["aa"] = results["aa"].astype(str)
        recombine = results[
            [
                "interact_id",
                "score",
            ]
        ]
        return recombine
