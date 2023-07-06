__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from tmkit.util.Reader import reader as greader
from tmkit.util.Writer import writer as gwriter


class reader:
    def __init__(
        self,
    ):
        self.greader = greader()
        self.gwriter = gwriter()

    def fetch(
        self,
        sv_fp,
    ):
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

    def readall(self, pred_muthtp_fpn):
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

    def readsingle(self, pred_split_muthtp_fpn):
        print("======>reading split Pred-MutHTP...")
        all = self.greader.generic(pred_split_muthtp_fpn, header=0)
        return all

    def split(self, pred_muthtp_df, sv_fp):
        """

        Parameters
        ----------
        pred_muthtp_df
        sv_fp

        Returns
        -------

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
        return 0
