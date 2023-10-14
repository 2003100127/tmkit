__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import subprocess
import urllib.request

import pandas as pd

from tmkit.util.Writer import Writer


class XML:
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

    def pdbtm(self, sv_fp: str, is_cmd: bool = False) -> str:
        """
        Download PDBTM XML files for each protein in the series.

        Parameters
        ----------
        sv_fp : str
            The file path to save the downloaded XML files.
        is_cmd : bool, optional
            Whether to use command line to download the files, by default False.

        Returns
        -------
        str
            'Finished' if a XML file is successfully retrieved.
        """
        count = 0
        fails = []
        for i, prot_name in enumerate(self.prot_dedup):
            print(f"===>No.{i} protein name: {prot_name}")
            try:
                url = (
                    # "http://pdbtm.enzim.hu/data/database/"
                    # + str(prot_name[1])
                    # + str(prot_name[2])
                    # + "/"
                    "http://pdbtm.unitmp.org/api/v1/entry/"
                    + str(prot_name)
                    + ".xml"
                )
                if is_cmd:
                    subprocess.Popen(
                        "wget " + url,
                        stderr=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        shell=True,
                    ).communicate()
                else:
                    urllib.request.urlretrieve(
                        url=url, filename=sv_fp + str(prot_name) + ".xml"
                    )
            except:
                count = count + 1
                fails.append(prot_name)
                print(f"===>number of xml that cannot be downloaded {count}")
                continue
        self.write.generic(fails, sv_fp + "log_fail_ids.txt")
        return 'Finished'
