__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import pandas as pd

from tmkit.util.Reader import Reader as greader
from tmkit.util.Writer import Writer as gwriter


class Reader:
    def __init__(
        self,
    ):
        self.greader = greader()
        self.gwriter = gwriter()

    def fetch(
        self,
        sv_fp: str,
    ) -> str:
        """
        Download the Pred-MutHTP database.

        Parameters
        ----------
        sv_fp : str
            The path to the directory where the database will be saved.

        Returns
        -------
        str
            A message indicating the download is finished.
        """
        from tmkit.util.Kit import urlliby

        print("===>The Pred-MutHTP database is being downloaded...")
        urlliby(
            url="https://www.iitm.ac.in/bioinfo/PredMutHTP/pred_varhtp_mut.zip",
            fpn=sv_fp + "pred_varhtp_mut.zip",
        )
        print("===>The Pred-MutHTP database is successfully downloaded!")
        print("===>The Pred-MutHTP database is being decompressed...")
        import zipfile

        with zipfile.ZipFile(sv_fp + "pred_varhtp_mut.zip", "r") as zip_ref:
            zip_ref.extractall(sv_fp)
        print("===>The Pred-MutHTP database is successfully decompressed!")
        return "Finished!"

    def readall(self, pred_muthtp_fpn: str) -> pd.DataFrame:
        """
        Read the Pred-MutHTP database.

        Parameters
        ----------
        pred_muthtp_fpn : str
            The path to the Pred-MutHTP database file.

        Returns
        -------
        pd.DataFrame
            A pandas DataFrame Pred-MutHTP the MutHTP database.
        """
        print("======>reading Pred-MutHTP...")
        all = self.greader.generic(pred_muthtp_fpn, df_sep=",")
        all = all.rename(
            columns={
                0: "uniprot_id",
                1: "protein_mutation_site",
                2: "topology",
                3: "mutation_type",
                4: "mut_prob",
            }
        )
        print(f"======>Pred-MutHTP features are: ")
        for i, e in enumerate(all.columns):
            print(f"=========>No.{i + 1}: {e}")
        return all

    def readsingle(self, pred_split_muthtp_fpn: str) -> pd.DataFrame:
        """
        Read the split Pred-MutHTP database.

        Parameters
        ----------
        pred_split_muthtp_fpn : str
            The path to the split Pred-MutHTP database file.

        Returns
        -------
        pd.DataFrame
            A pandas DataFrame Pred-MutHTP the MutHTP database.
        """
        print("======>reading split Pred-MutHTP...")
        all = self.greader.generic(pred_split_muthtp_fpn, header=0)
        return all

    def split(self, pred_muthtp_df: pd.DataFrame, sv_fp: str) -> str:
        """
        Split the Pred-MutHTP database.

        Parameters
        ----------
        pred_muthtp_df : pd.DataFrame
            A list of dictionaries containing the Pred-MutHTP database.
        sv_fp : str
            The path to the directory where the split database will be saved.

        Returns
        -------
        str
            A message indicating the download is finished.

        """
        pred_muthtp_df = pred_muthtp_df[
            [
                "uniprot_id",
                "protein_mutation_site",
                "mut_prob",
            ]
        ]
        # uniprot_ids = pd.unique(muthtp_df['uniprot_id'])
        # pred_muthtp_uniprot_ids = pd.unique(pred_muthtp_df['uniprot_id'])
        pred_muthtp_df_gp = pred_muthtp_df.groupby(["uniprot_id"])
        pred_muthtp_df_gp_keys = pred_muthtp_df_gp.groups.keys()
        print(f"======>{len(pred_muthtp_df_gp_keys)} uniprot proteins")
        for i, prot_id in enumerate(pred_muthtp_df_gp_keys):
            print(f"=========>Splitting No.{i} protein from Pred-MutHTP")
            cc = pred_muthtp_df_gp.get_group(prot_id)
            self.gwriter.generic(
                df=cc,
                sv_fpn=sv_fp + prot_id + ".predmuthtp",
                header=True,
            )
        return 'Finished'
