__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import List

import time

import pandas as pd

from tmkit.util.Reader import Reader


class Label:
    """
    Class for labeling protein-protein interaction data based on distance cutoff.

    Parameters
    ----------
    dist_path : str
        The path to the distance file.
    prot_name : str
        The name of the protein.
    file_chain : str
        The chain of the protein.
    cutoff : int, optional
        The distance cutoff for labeling interactions, by default 6.

    Attributes
    ----------
    prot_name : str
        The name of the protein.
    file_chain : str
        The chain of the protein.
    dist_fpn : str
        The full path to the distance file.
    cutoff : int
        The distance cutoff for labeling interactions.
    read : Reader
        The reader object for reading files.

    Methods
    -------
    attach() -> pd.DataFrame
        Reads the distance file and labels interactions based on the distance cutoff.

    """

    def __init__(
        self, dist_path: str, prot_name: str, file_chain: str, cutoff: int = 6
    ) -> None:
        """
        Parameters
        ----------
        dist_path : str
            The path to the distance file.
        prot_name : str
            The name of the protein.
        file_chain : str
            The chain of the protein.
        cutoff : int, optional
            The distance cutoff for labeling interactions, by default 6.
        """
        self.prot_name: str = prot_name
        self.file_chain: str = file_chain
        self.dist_fpn: str = dist_path + self.prot_name + self.file_chain + ".dist"
        self.cutoff: int = cutoff
        self.read = Reader()

    def attach(self) -> pd.DataFrame:
        """
        Reads the distance file and labels interactions based on the distance cutoff.

        Returns
        -------
        pd.DataFrame
            The labeled distance data.
        """
        start_time: float = time.time()
        dist_df: pd.DataFrame = self.read.generic(self.dist_fpn)
        dists: pd.DataFrame = dist_df.iloc[:, 3:]
        dist_mins: pd.Series = dists.min(axis=1)
        inter_ids: List[int] = dist_mins.loc[dist_mins < self.cutoff].index.tolist()
        noninter_ids: List[int] = dist_mins.loc[dist_mins >= self.cutoff].index.tolist()
        dist_df["is_contact"] = -1
        dist_df.loc[inter_ids, "is_contact"] = 1
        dist_df.loc[noninter_ids, "is_contact"] = 0
        columns: List[str] = ["fasta_id", "aa", "pdb_id"]
        for i in range(dists.shape[1]):
            columns.append("dist_" + str(i + 1))
        columns.append("is_contact")
        dist_df.columns = columns
        end_time: float = time.time()
        print(
            "======>Time to read&label distances for {} {}: {}s.".format(
                self.prot_name, self.file_chain, end_time - start_time
            )
        )
        return dist_df
