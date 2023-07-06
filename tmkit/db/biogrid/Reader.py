__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import List

import pandas as pd

from tmkit.util.Reader import Reader as greader
from tmkit.util.Writer import Writer


class Reader:
    """
    A class for reading and processing BioGRID database files.

    Attributes
    ----------
    greader : tmkit.util.Reader.reader
        A reader object for reading files.
    writer : tmkit.util.Writer.writer
        A writer object for writing files.

    Methods
    -------
    fetch(sv_fp: str, version: str) -> str:
        Downloads and decompresses the BioGRID database of a specified version.
    tab3(biogrid_fpn: str, sv_fpn: str, extract_ids: List[str]) -> pandas.DataFrame:
        Reads the BioGRID database file and extracts specified columns.
    """

    def __init__(
        self,
    ) -> None:
        self.greader = greader()
        self.writer = Writer()

    def fetch(self, sv_fp: str, version: str) -> str:
        """
        Downloads and decompresses the BioGRID database of a specified version.

        Parameters
        ----------
        sv_fp : str
            The file path to save the downloaded and decompressed BioGRID database.
        version : str
            The version of the BioGRID database to download.

        Returns
        -------
        str
            A message indicating that the download and decompression is finished.
        """
        from tmkit.util.Kit import urlliby

        print(
            "===>The BioGRID database of version " + version + " is being downloaded..."
        )
        urlliby(
            url="https://downloads.thebiogrid.org/Download/BioGRID/Release-Archive/BIOGRID-"
            + version
            + "/BIOGRID-ALL-"
            + version
            + ".tab3.zip",
            fpn=sv_fp + "BIOGRID-ALL-" + version + ".tab3.zip",
        )
        print("===>The database of version " + version + " is successfully downloaded!")
        print("===>The database of version " + version + " is being decompressed...")
        import zipfile

        with zipfile.ZipFile(
            sv_fp + "BIOGRID-ALL-" + version + ".tab3.zip", "r"
        ) as zip_ref:
            zip_ref.extractall(sv_fp)
        print(
            "===>The database of version " + version + " is successfully decompressed!"
        )
        return "Finished!"

    def tab3(
        self,
        biogrid_fpn: str,
        sv_fpn: str,
        extract_ids: List[str],
    ) -> pd.DataFrame:
        """
        Reads the BioGRID database file and extracts specified columns.

        Parameters
        ----------
        biogrid_fpn : str
            The file path of the BioGRID database file.
        sv_fpn : str
            The file path to save the extracted columns.
        extract_ids : List[str]
            A list of column names to extract.

        Returns
        -------
        pandas.DataFrame
            A dataframe containing the extracted columns.
        """
        print("======>reading BioGRID...")
        all = self.greader.generic(biogrid_fpn, header=0, comment=None)
        print(f"======>BioGRID features are: ")
        for i, e in enumerate(all.columns):
            print(f"=========>No.{i + 1}: {e}")
        self.writer.generic(df=all[extract_ids], sv_fpn=sv_fpn, header=True)
        print("======>The file is saved.")
        return all[extract_ids]
