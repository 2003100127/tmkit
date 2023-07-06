__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import subprocess

import numpy as np
import pandas as pd

from tmkit.util.Kit import chainid, tactic5, tactic6


import subprocess
from typing import Optional
import pandas as pd


class HelixSurface:
    def __init__(
        self,
        msa_path: Optional[str] = None,
        lips_fpn: Optional[str] = None,
        prot_name: Optional[str] = None,
        file_chain: Optional[str] = None,
        sv_fp: Optional[str] = None,
        df_prot: Optional[pd.DataFrame] = None,
    ) -> None:
        """
        Initialize the helixSurface object.

        Parameters
        ----------
        msa_path : str, optional
            The path to the MSA file, by default None.
        lips_fpn : str, optional
            The file path to the LIPS script, by default None.
        prot_name : str, optional
            The name of the protein, by default None.
        file_chain : str, optional
            The chain identifier of the protein, by default None.
        sv_fp : str, optional
            The file path to store the output, by default None.
        df_prot : pd.DataFrame, optional
            The protein dataframe, by default None.
        """
        self.msa_path = msa_path
        self.lips_fpn = lips_fpn
        self.sv_fp = sv_fp
        self.df_prot = df_prot
        self.prot_name = prot_name
        self.file_chain = file_chain

    def generate(self) -> int:
        """
        Generate the helix surface.

        Returns
        -------
        int
            A status code indicating the success of the operation (0 indicates success).
        """
        msa_fpn = self.msa_path + self.prot_name + self.file_chain + ".aln"
        sv_fpn = self.sv_fp + self.prot_name + self.file_chain + "/"
        self.surf = subprocess.call(
            [
                "perl",
                self.lips_fpn,
                msa_fpn,
                sv_fpn,
            ],
            shell=True,
        )
        return 0

    def bgenerate(self) -> int:
        """
        Generate the helix surface for multiple proteins.

        Returns
        -------
        int
            A status code indicating the success of the operation (0 indicates success).
        """
        for i, prot_name in enumerate(self.df_prot["prot"]):
            prot_chain = self.df_prot["chain"][i]
            file_chain = chainid(prot_chain)
            print(f"=========>No.{i} protein {prot_name + file_chain}")
            self.msa_fpn = self.msa_path + prot_name + file_chain + ".aln"
            sv_fpn = self.sv_fp + prot_name + file_chain + "/"
            self.surf = subprocess.call(
                [
                    "perl",
                    self.lips_fpn,
                    self.msa_fpn,
                    sv_fpn,
                ],
                shell=True,
            )
        return 0

    def surface(self, i: int) -> pd.DataFrame:
        """
        Read a surface file and return the data as a DataFrame.

        Parameters
        ----------
        i : int
            The index of the surface file to read.

        Returns
        -------
        pd.DataFrame
            The surface data with columns 'aa_ids', 'aa_names', 'lipos', 'ents', and 'surf'.
        """
        surf_fpn = self.sv_fp + self.prot_name + \
            self.file_chain + "/" + str(i) + ".txt"
        with open(surf_fpn) as f:
            surf_x = [[str(digit) for digit in line.split()] for line in f]
            surf_x = pd.DataFrame(
                surf_x,
                columns=[
                    "aa_ids",
                    "aa_names",
                    "lipos",
                    "ents",
                ],
            )
            surf_x["aa_ids"] = surf_x["aa_ids"].apply(int)
            surf_x["lipos"] = surf_x["lipos"].apply(float)
            surf_x["ents"] = surf_x["ents"].apply(float)
            surf_x["surf"] = int(i)
        return surf_x

    def transformToRosseta(self, df_surf_lips: pd.DataFrame) -> pd.DataFrame:
        """
        Transform surface and lips data to a combined DataFrame in Rosseta format.

        Parameters
        ----------
        df_surf_lips : pd.DataFrame
            The surface and lips data with columns 'surfs', 'lipos', 'ents', and 'lxe'.

        Returns
        -------
        pd.DataFrame
            The transformed data with columns 'aa_ids', 'mean_lipo', 'lipos', and 'ents'.
        """
        d = []
        for i in df_surf_lips.index:
            o = df_surf_lips["surfs"][i]
            b = self.surface(o)
            print(f"======>reading surface {o}")
            b["mean_lipo"] = df_surf_lips.loc[o]["lxe"]
            b = b[
                [
                    "aa_ids",
                    "mean_lipo",
                    "lipos",
                    "ents",
                ]
            ]
            d.append(b)
        return pd.concat(d, axis=0).reset_index(drop=True)

    def lips(self) -> pd.DataFrame:
        """
        Read the lips file and return the data as a DataFrame.

        Returns
        -------
        pd.DataFrame
            The lips data with columns 'surfs', 'lipos', 'ents', and 'lxe'.
        """
        lips_fpn = self.sv_fp + self.prot_name + self.file_chain + "/LIPS.txt"
        with open(lips_fpn) as f:
            lips_ = [[digit for digit in line.split()] for line in f]
            lips_surf = pd.DataFrame(
                lips_, columns=["surfs", "lipos", "ents", "lxe"])
            lips_surf["surfs"] = lips_surf["surfs"].apply(int)
            lips_surf["lipos"] = lips_surf["lipos"].apply(float)
            lips_surf["ents"] = lips_surf["ents"].apply(float)
            lips_surf["lxe"] = lips_surf["lxe"].apply(float)
        return lips_surf

    def read(self) -> Tuple[Dict[int, int], Dict[int, float], Dict[int, float], Dict[int, float]]:
        """
        Read and process surface, lips, and entropy data.

        Returns
        -------
        Tuple[Dict[int, int], Dict[int, float], Dict[int, float], Dict[int, float]]
            A tuple containing dictionaries:
            - aa_surf_rank: Dictionary mapping amino acid IDs to the most relevant surface index.
            - lipos_dict: Dictionary mapping amino acid IDs to lipophilicity values.
            - entropy_dict: Dictionary mapping amino acid IDs to entropy values.
            - lips_dict: Dictionary mapping amino acid IDs to lips values.
        """
        surfs = pd.DataFrame()
        surf_lipos = pd.DataFrame()
        surf_ents = pd.DataFrame()
        for i in range(7):
            # print(self.surface(i)['lipos'].mean()*2)
            # print(self.surface(i)['ents'].mean())
            surfs = pd.concat(
                [surfs, self.surface(i)[["aa_ids", "surf"]]], axis=0
            )
            surfs = surfs.reset_index(drop=True)
            surf_lipos = pd.concat(
                [surf_lipos, self.surface(i)[["aa_ids", "lipos"]]], axis=0
            )
            surf_lipos = surf_lipos.reset_index(drop=True)
            surf_ents = pd.concat(
                [surf_ents, self.surface(i)[["aa_ids", "ents"]]], axis=0
            )
            surf_ents = surf_ents.reset_index(drop=True)

        surfs_dict = tactic5(surfs.values.tolist())
        lipos_dict = tactic6(surf_lipos.values.tolist())
        entropy_dict = tactic6(surf_ents.values.tolist())
        lips_dict = tactic6(self.lips().values.tolist())

        aa_surf_rank = {}
        for k, v in surfs_dict.items():
            compare = []
            for s in v:
                compare.append(lips_dict[s][2])
            aa_surf_rank[k] = v[np.argmax(compare)]
            # print(compare)
            # print(np.argmax(compare))
            # print(v[np.argmax(compare)])
        return aa_surf_rank, lipos_dict, entropy_dict, lips_dict

    def boolean(self, aa_surf_rank: Dict[int, int], key: int) -> np.ndarray:
        """
        Create a boolean array based on the amino acid's surface rank.

        Parameters
        ----------
        aa_surf_rank : Dict[int, int]
            Dictionary mapping amino acid IDs to the most relevant surface index.
        key : int
            The amino acid ID.

        Returns
        -------
        np.ndarray
            Boolean array with 1 indicating the surface rank and 0 elsewhere.
        """
        bool_ = np.zeros(7)
        bool_[aa_surf_rank[key]] = 1
        return bool_

    def boolean_(self, list_2d: List[List[Optional[float]]], window_aa_ids: List[List[Optional[int]]], aa_surf_rank: Dict[int, int]) -> List[List[float]]:
        """
        Update the 2D list with boolean values based on surface ranks.

        Parameters
        ----------
        list_2d : List[List[Optional[float]]]
            The 2D list to be updated.
        window_aa_ids : List[List[Optional[int]]]
            The window amino acid IDs.
        aa_surf_rank : Dict[int, int]
            Dictionary mapping amino acid IDs to the most relevant surface index.

        Returns
        -------
        List[List[float]]
            The updated 2D list with boolean values.
        """
        list_2d_ = list_2d
        for i, aa_win_ids in enumerate(window_aa_ids):
            for j in aa_win_ids:
                if j is None:
                    for k in range(7):
                        list_2d_[i].append(0)
                else:
                    r = aa_surf_rank[j]
                    bool_ = [0] * 7
                    bool_[r] = 1
                    for k in range(7):
                        list_2d_[i].append(bool_[k])
        return list_2d_

    def lipos_(self, list_2d: List[List[Optional[float]]], window_aa_ids: List[List[Optional[int]]], lipos_dict: Dict[int, float]) -> List[List[float]]:
        """
        Update the 2D list with lipophilicity values based on amino acid IDs.

        Parameters
        ----------
        list_2d : List[List[Optional[float]]]
            The 2D list to be updated.
        window_aa_ids : List[List[Optional[int]]]
            The window amino acid IDs.
        lipos_dict : Dict[int, float]
            Dictionary mapping amino acid IDs to lipophilicity values.

        Returns
        -------
        List[List[float]]
            The updated 2D list with lipophilicity values.
        """
        list_2d_ = list_2d
        for i, aa_win_ids in enumerate(window_aa_ids):
            for j in aa_win_ids:
                if j is None:
                    list_2d_[i].append(0)
                else:
                    list_2d_[i].append(lipos_dict[j])
        return list_2d_

    def entropy_(self, list_2d: List[List[float]], window_aa_ids: List[List[Optional[int]]],
                 entropy_dict: Dict[int, float]) -> List[List[float]]:
        """
        Calculate entropy values and append them to the 2D list.

        Parameters
        ----------
        list_2d : List[List[float]]
            The input 2D list to be modified.
        window_aa_ids : List[List[Optional[int]]]
            The window amino acid IDs for each element in `list_2d`.
        entropy_dict : Dict[int, float]
            A dictionary mapping amino acid IDs to entropy values.

        Returns
        -------
        List[List[float]]
            The modified 2D list with entropy values appended.
        """
        list_2d_ = list_2d
        for i, aa_win_ids in enumerate(window_aa_ids):
            for j in aa_win_ids:
                if j is None:
                    list_2d_[i].append(0)
                else:
                    list_2d_[i].append(entropy_dict[j])
        return list_2d_

    def avlipos_(self, list_2d: List[List[float]], window_aa_ids: List[List[Optional[int]]],
                 aa_surf_rank: Dict[int, int], lips_dict: Dict[int, List[float]]) -> List[List[float]]:
        """
        Calculate average lipos values and append them to the 2D list.

        Parameters
        ----------
        list_2d : List[List[float]]
            The input 2D list to be modified.
        window_aa_ids : List[List[Optional[int]]]
            The window amino acid IDs for each element in `list_2d`.
        aa_surf_rank : Dict[int, int]
            A dictionary mapping amino acid IDs to surface ranks.
        lips_dict : Dict[int, List[float]]
            A dictionary mapping surface ranks to lipos values.

        Returns
        -------
        List[List[float]]
            The modified 2D list with average lipos values appended.
        """
        list_2d_ = list_2d
        for i, aa_win_ids in enumerate(window_aa_ids):
            for j in aa_win_ids:
                if j is None:
                    list_2d_[i].append(0)
                else:
                    r = aa_surf_rank[j]
                    list_2d_[i].append(lips_dict[r][0])
        return list_2d_

    def aventropy_(self, list_2d: List[List[float]], window_aa_ids: List[List[Optional[int]]],
                   aa_surf_rank: Dict[int, int], lips_dict: Dict[int, List[float]]) -> List[List[float]]:
        """
        Calculate average entropy values and append them to the 2D list.

        Parameters
        ----------
        list_2d : List[List[float]]
            The input 2D list to be modified.
        window_aa_ids : List[List[Optional[int]]]
            The window amino acid IDs for each element in `list_2d`.
        aa_surf_rank : Dict[int, int]
            A dictionary mapping amino acid IDs to surface ranks.
        lips_dict : Dict[int, List[float]]
            A dictionary mapping surface ranks to lipos values.

        Returns
        -------
        List[List[float]]
            The modified 2D list with average entropy values appended.
        """
        list_2d_ = list_2d
        for i, aa_win_ids in enumerate(window_aa_ids):
            for j in aa_win_ids:
                if j is None:
                    list_2d_[i].append(0)
                else:
                    r = aa_surf_rank[j]
                    list_2d_[i].append(lips_dict[r][1])
        return list_2d_

    def avlips_(self, list_2d: List[List[float]], window_aa_ids: List[List[Optional[int]]],
                aa_surf_rank: Dict[int, int], lips_dict: Dict[int, List[float]]) -> List[List[float]]:
        """
        Calculate average lips values and append them to the 2D list.

        Parameters
        ----------
        list_2d : List[List[float]]
            The input 2D list to be modified.
        window_aa_ids : List[List[Optional[int]]]
            The window amino acid IDs for each element in `list_2d`.
        aa_surf_rank : Dict[int, int]
            A dictionary mapping amino acid IDs to surface ranks.
        lips_dict : Dict[int, List[float]]
            A dictionary mapping surface ranks to lipos values.

        Returns
        -------
        List[List[float]]
            The modified 2D list with average lips values appended.
        """
        list_2d_ = list_2d
        for i, aa_win_ids in enumerate(window_aa_ids):
            for j in aa_win_ids:
                if j is None:
                    list_2d_[i].append(0)
                else:
                    r = aa_surf_rank[j]
                    list_2d_[i].append(lips_dict[r][2])
        return list_2d_
