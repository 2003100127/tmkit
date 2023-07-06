__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import Dict, List, Union

import json

import pandas as pd
import requests

from tmkit.util.Kit import tactic7
from tmkit.util.Reader import Reader as greader
from tmkit.util.Writer import Writer


class Reader:
    def __init__(
        self,
    ) -> None:
        self.greader = greader()
        self.writer = Writer()

    def api(self, identifier: str) -> Dict[str, str]:
        """
        Get the API endpoints (links) for the given identifier.

        Parameters
        ----------
        identifier : str
            The complex name + chain ID + domain ID; e.g., 1h2sB00.

        Returns
        -------
        Dict[str, str]
            A dictionary containing the API endpoints for the given identifier.
        """
        return {
            "domain": "http://www.cathdb.info/version/v4_2_0/api/rest/domain_summary/"
            + identifier,
            "funfam": "http://www.cathdb.info/version/v4_2_0/api/rest/superfamily/1.10.8.10/funfam/"
            + identifier,
            "superfamily": "http://www.cathdb.info/version/v4_2_0/api/rest/superfamily/"
            + identifier,
        }

    def download(self, sv_fp: str, version: str = "newest") -> str:
        """
        Download the CATH database of the given version.

        Parameters
        ----------
        sv_fp : str
            File path to save the downloaded file.
        version : str, optional
            Version of the CATH database to download, by default "newest".

        Returns
        -------
        str
            A message indicating that the download is finished.
        """
        from tmkit.util.Kit import urlliby

        print("===>The CATH database of version " + version + " is being downloaded...")
        urlliby(
            url="ftp://orengoftp.biochem.ucl.ac.uk/cath/releases/daily-release/"
            + version
            + "/cath-b-"
            + version
            + "-all.gz",
            fpn=sv_fp + "cath-b-" + version + "-all.gz",
        )
        print(
            "===>The CATH database of version "
            + version
            + " is successfully downloaded!"
        )
        print(
            "===>The CATH database of version " + version + " is being decompressed..."
        )
        from tmkit.util.Kit import ungz

        ungz(
            file_path=sv_fp,
            file_name="cath-b-" + version + "-all",
            sv_fp=sv_fp,
            new_suffix=".txt",
        )
        print(
            "===>The CATH database of version "
            + version
            + " is successfully decompressed!"
        )
        return "Finished!"

    def fetch(self, domain_id: str, sort: str) -> Dict[str, Union[str, Dict[str, str]]]:
        """
        Fetch the data for the given domain ID and the sort type.

        Parameters
        ----------
        domain_id : str
            The domain ID to fetch data for.
        sort : str
            The sort type to use, in the current version (TMKit 0.0.2), we have only "domain".

        Returns
        -------
        Dict[str, Union[str, Dict[str, str]]]
            A dictionary containing the fetched data according to the CATH database.
        """
        json_data = requests.get(self.api(domain_id)[sort]).json()
        if "data" in json_data:
            # this is to avoid a domain in the file
            # exist but the domain via api does not exist.
            return json_data["data"]
        else:
            return {}

    def domain(
        self, cath_fpn: str, groupby: str = "version", group: str = "v4_2_0"
    ) -> pd.DataFrame:
        """
        Read the CATH database and return the domain information.

        Parameters
        ----------
        cath_fpn : str
            The file path to the CATH database.
        groupby : str, optional
            The column to group by, by default "version".
        group : str, optional
            The value to group by, by default "v4_2_0".

        Returns
        -------
        pd.DataFrame
            A DataFrame containing the domain information, including
            'domain', 'version', 'superfamily', and 'bound'.
        """
        print("======>reading CATH...")
        df_domain = self.greader.generic(df_fpn=cath_fpn, df_sep=r"\s+")
        df_domain = df_domain.rename(
            columns={
                0: "domain",
                1: "version",
                2: "superfamily",
                3: "bound",
            }
        )
        print(f"======>CATH features are: ")
        for i, e in enumerate(df_domain.columns):
            print(f"=========>No.{i + 1}: {e}")
        domain_info_grouped = df_domain.groupby(by=[groupby]).get_group(group)
        return domain_info_grouped

    def funfamsToJson(
        self,
        df_prot: pd.DataFrame,
        df_domain: pd.DataFrame,
        sv_fpn: str = "./results.json",
        targets: List[str] = ["funfam_number"],
    ) -> Dict[str, Dict[str, Dict[str, Dict[str, str]]]]:
        """
        Convert the given protein and domain DataFrame to
        a JSON file containing funfam information.

        Parameters
        ----------
        df_prot : pd.DataFrame
            The protein DataFrame.
        df_domain : pd.DataFrame
            The domain DataFrame.
        sv_fpn : str, optional
            The file path to save the resulting JSON file, by default "./results.json".
        targets : List[str], optional
            The targets to fetch data for, by default ["funfam_number"].

        Returns
        -------
        Dict[str, Dict[str, Dict[str, Dict[str, str]]]]
            A dictionary containing the funfam information.
        """
        complex_ids = df_domain["domain"].apply(lambda x: x[:4])
        chain_ids = df_domain["domain"].apply(lambda x: x[4])
        domain_ids = df_domain["domain"].apply(lambda x: x[5:])
        complex_info = pd.concat(
            [complex_ids, chain_ids, domain_ids], axis=1
        ).values.tolist()
        domain_dict = tactic7(complex_info)
        # print(domain_dict)
        cands = {}
        for i in df_prot.index:
            prot_name = df_prot.loc[i, "prot"]
            # seq_chain = self.df_prot.loc[i, 1]
            # print('----> No.{} protein {} chain {}'.format(i + 1, prot_name, seq_chain))
            print(f"======>No.{i + 1} protein complex: {prot_name}")
            if prot_name in domain_dict.keys():
                cands[prot_name] = {}
                # if seq_chain in domain_dict[prot_name].keys():
                for seq_chain in domain_dict[prot_name].keys():
                    cands[prot_name][seq_chain] = {}
                    for domain_id in domain_dict[prot_name][seq_chain]:
                        print(
                            "=========>domain id is: {}".format(
                                prot_name + seq_chain + domain_id
                            )
                        )
                        domain_data = self.fetch(
                            domain_id=prot_name + seq_chain + domain_id, sort="domain"
                        )
                        cands[prot_name][seq_chain][domain_id] = {}
                        for target in targets:
                            if target in domain_data.keys():
                                cands[prot_name][seq_chain][domain_id][
                                    target
                                ] = domain_data[target]
        with open(sv_fpn, "w") as fp:
            json.dump(cands, fp)
        print("======>The file is saved.")
        return cands
