__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import Any, Optional

import subprocess

import numpy as np
import pandas as pd

from tmkit.util.Kit import chainid, tactic5, tactic6


class HelixSurface:
    def __init__(
        self,
        msa_path: Optional[str] = None,
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
        prot_name : str, optional
            Name of a protein in the prefix of a PDB file name (e.g., 1xqf in 1xqfA.pdb), by default None.
        file_chain : str, optional
            Chain of a protein in the prefix of a PDB file name (e.g., A in 1xqfA.pdb), by default None.
        sv_fp : str, optional
            The file path to store the output, by default None.
        df_prot : pd.DataFrame, optional
            Pandas dataframe storing protein names and chain names, by default None.
        """
        self.msa_path = msa_path
        import configparser
        config = configparser.ConfigParser()
        import os
        r_lo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        config.read(r_lo + '/.env')
        self.lips_fpn = os.path.join(
            r_lo,
            config['LIPS']['LOCATION']
        )
        # self.lips_fpn = lips_fpn
        self.sv_fp = sv_fp
        self.df_prot = df_prot
        self.prot_name = prot_name
        self.file_chain = file_chain

    def generate(self) -> str:
        """
        Generate the helix surface.

        Returns
        -------
        str
            'Finished' if the success of the operation (0 indicates success).
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
        return 'Finished'

    def bgenerate(self) -> str:
        """
        Generate the helix surface for multiple proteins.

        Returns
        -------
        str
            'Finished' if the results are saved.
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
        return 'Finished'

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
        surf_fpn = self.sv_fp + self.prot_name + self.file_chain + "/" + str(i) + ".txt"
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
            lips_surf = pd.DataFrame(lips_, columns=["surfs", "lipos", "ents", "lxe"])
            lips_surf["surfs"] = lips_surf["surfs"].apply(int)
            lips_surf["lipos"] = lips_surf["lipos"].apply(float)
            lips_surf["ents"] = lips_surf["ents"].apply(float)
            lips_surf["lxe"] = lips_surf["lxe"].apply(float)
        return lips_surf

    def read(self) -> Any:
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
            surfs = pd.concat([surfs, self.surface(i)[["aa_ids", "surf"]]], axis=0)
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
