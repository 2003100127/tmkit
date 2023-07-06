__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import List, Union

import re

import pandas as pd

from tmkit.util.Reader import Reader as greader
from tmkit.util.Writer import Writer


class Reader:
    def __init__(
        self,
    ) -> None:
        self.greader = greader()
        self.writer = Writer()

    def decorate(self, x: str) -> str:
        """
        Remove "uniprotkb:" and "-" from the given string.

        Parameters
        ----------
        x : str
            The string to be decorated.

        Returns
        -------
        str
            The decorated string.
        """
        c = re.sub(r"^uniprotkb:", "", x)
        return re.sub(r".\-", "", c)

    def fetch(self, sv_fp: str, version: str = "current") -> str:
        """
        Download and decompress the IntAct database of the given version.

        Parameters
        ----------
        sv_fp : str
            The file path to save the downloaded database.
        version : str, optional
            The version of the IntAct database to download, by default "current".

        Returns
        -------
        str
            A message indicating the completion of the download and decompression.
        """
        from tmkit.util.Kit import urlliby

        print(
            "===>The IntAct database of version " + version + " is being downloaded..."
        )
        urlliby(
            url="https://ftp.ebi.ac.uk/pub/databases/intact/"
            + version
            + "/psimitab/intact.zip",
            fpn=sv_fp + "intact.zip",
        )
        print("===>The database of version " + version + " is successfully downloaded!")
        print("===>The database of version " + version + " is being decompressed...")
        import zipfile

        with zipfile.ZipFile(sv_fp + "intact.zip", "r") as zip_ref:
            zip_ref.extractall(sv_fp)
        print(
            "===>The database of version " + version + " is successfully decompressed!"
        )
        return "Finished!"

    def full(
        self,
        intact_fpn: str,
        extract_ids: List[str] = [
            "#ID(s) interactor A",
            "ID(s) interactor B",
        ],
        sv_fpn: Union[str, None] = None,
    ) -> pd.DataFrame:
        """
        Read the IntAct database and extract the specified columns.

        Parameters
        ----------
        intact_fpn : str
            The file path of the IntAct database.
        extract_ids : List[str], optional
            The list of column names to extract, by default ["#ID(s) interactor A", "ID(s) interactor B"].
        sv_fpn : Union[str, None], optional
            The file path to save the extracted data, by default None.

        Returns
        -------
        pd.DataFrame
            The extracted data as a pandas DataFrame.
        """
        print("======>reading IntAct...")

        all = self.greader.generic(intact_fpn, header=0, comment=None)

        print(f"======>IntAct features are: ")
        for i, e in enumerate(all.columns):
            print(f"=========>No.{i + 1}: {e}")

        df = pd.DataFrame()
        df["#ID(s) interactor A"] = all[extract_ids]["#ID(s) interactor A"].apply(
            lambda x: self.decorate(x)
        )
        df["ID(s) interactor B"] = all[extract_ids]["ID(s) interactor B"].apply(
            lambda x: self.decorate(x)
        )
        if sv_fpn:
            self.writer.generic(df=df, sv_fpn=sv_fpn, header=True)
        print("======>The file is saved.")
        return df
