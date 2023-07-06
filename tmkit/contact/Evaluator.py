__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import Dict, List, Union

import numpy as np
import pandas as pd
from sklearn import metrics

from tmkit.contact.Reader import Reader as rrcreader


class evaluator:
    def __init__(
        self,
        prot_name: str,
        file_chain: str,
        dist_df: pd.DataFrame,
        pair_list: List,
        dist_limit: Union[float, None] = None,
        tool: Union[str, None] = None,
        tool_fp: Union[str, None] = None,
        sort_: Union[int, None] =None,
        seq_sep_inferior: Union[int, None] = None,
        seq_sep_superior: Union[int, None] = None,
    ) -> None:
        """
        Initializes the evaluator.

        Parameters
        ----------
        prot_name : str
            The name of the protein.
        file_chain : str
            The file chain.
        dist_df : pd.DataFrame
            The dataframe with distance information.
        pair_list : list
            The list of pairs.
        dist_limit : int or None, optional
            The distance limit, by default None.
        tool : str or None, optional
            The tool name, by default None.
        tool_fp : str or None, optional
            The tool file path, by default None.
        sort_ : bool or None, optional
            The sorting flag, by default None.
        seq_sep_inferior : int or None, optional
            The inferior sequence separation, by default None.
        seq_sep_superior : int or None, optional
            The superior sequence separation, by default None.
        """
        self.tool_fp = tool_fp
        self.prot_name = prot_name
        self.file_chain = file_chain
        self.dist_limit = dist_limit
        self.pair_list = pair_list
        self.tool = tool
        self.sort_ = sort_
        self.seq_sep_inferior = seq_sep_inferior
        self.seq_sep_superior = seq_sep_superior
        self.rrcreader = rrcreader(
            seq_sep_inferior=self.seq_sep_inferior,
            seq_sep_superior=self.seq_sep_superior,
        )
        self.dist_df = dist_df
        self.dist_df.columns = [
            "fasta_id_1",
            "aa_1",
            "pdb_id_1",
            "fasta_id_2",
            "aa_2",
            "pdb_id_2",
            "dist",
            "is_contact",
        ]
        self.row_real_dist = self.dist_df.shape[0]

        print(f"======>Evaluating protein {prot_name + file_chain}")

    def fetch(self):
        """
        Fetch results of a contact method prediction.

        Returns
        -------
        pd.DataFrame
            Contact prediction results.

        """
        switch = {
            "psicov": self.psicov,
            "freecontact": self.freecontact,
            "ccmpred": self.ccmpred,
            "gremlin": self.gremlin,
            "gdca": self.gdca,
            "plmc": self.plmc,
            "memconp": self.memconp,
            "membrain2": self.membrain2,
            "tma165": self.tma165,
        }
        return switch[self.tool]()

    def compare(self, target: pd.DataFrame, cut_off: int) -> Dict[str, float]:
        """
        Compares the target with given cutoff.

        Parameters
        ----------
        target : pd.DataFrame
            The target dataframe.
        cut_off : int
            The cutoff value.

        Returns
        -------
        dict
            The summary of the metrics.
        """
        # #/*** block fetch target results ***/
        res_sorted = target.sort_values(["score"], ascending=False)
        # self.pfwwriter.generic(res_sorted, sv_fpn='./cheers')
        res_cutoff = res_sorted.iloc[0:cut_off, :]
        new_index = np.arange(res_cutoff.shape[0])
        res_cutoff = res_cutoff.set_index(new_index, inplace=False, drop=True)
        # print(res_cutoff)
        row_cutoff = res_cutoff.shape[0]
        row_offset = target.shape[0] - row_cutoff
        # #/*** block y_true_cutoff ***/
        y_true_cutoff = []
        for i in range(row_cutoff):
            conid1 = self.dist_df["fasta_id_1"] == res_cutoff["fasta_id_1"][i]
            conid2 = self.dist_df["fasta_id_2"] == res_cutoff["fasta_id_2"][i]
            juery = (conid1) & (conid2)
            tmp = self.dist_df.loc[juery]
            y_true_cutoff.append(tmp["is_contact"].sum())
        # #/*** block y_true_all ***/
        y_true_all = list(res_sorted["is_contact"])
        # #/*** block y_pred_all ***/
        y_pred_all = list(
            np.concatenate(
                [np.zeros([row_cutoff]) + 1, np.zeros([row_offset])], axis=0
            ).astype(np.int64)
        )
        # #/*** block precision ***/
        precision = metrics.precision_score(y_true=y_true_all, y_pred=y_pred_all)
        print(f"=========>precision: {precision}")
        # #/*** block recall ***/
        recall = metrics.recall_score(y_true=y_true_all, y_pred=y_pred_all)
        print(f"=========>recall: {recall}")
        # #/*** block mcc ***/
        mcc = metrics.matthews_corrcoef(y_true=y_true_all, y_pred=y_pred_all)
        print(f"=========>mcc: {mcc}")
        # #/*** block f1score ***/
        f1score = metrics.f1_score(y_true=y_true_all, y_pred=y_pred_all)
        print(f"=========>f1score: {f1score}")
        # #/*** block accuracy ***/
        accuracy = metrics.accuracy_score(y_true=y_true_all, y_pred=y_pred_all)
        print(f"=========>accuracy: {accuracy}")
        metrics_summary = {
            "precision": precision,
            "recall": recall,
            "f1score": f1score,
            "mcc": mcc,
            "accuracy": accuracy,
        }
        return metrics_summary

    def psicov(self) -> pd.DataFrame:
        """
        Executes the PSICOV method.

        Returns
        -------
        pd.DataFrame
            The resulting dataframe after executing PSICOV.
        """
        pcv_dist, chain_dist_all = self.rrcreader.psicov(
            pcv_path=self.tool_fp,
            file_name=self.prot_name,
            file_chain=self.file_chain,
            pair_list=self.pair_list,
            dist_df=self.dist_df,
            sort_=self.sort_,
        )
        return pd.concat([pcv_dist, chain_dist_all], axis=1)

    def freecontact(self) -> pd.DataFrame:
        """
        Execute the FreeContact method and return the result.

        Returns
        -------
        pd.DataFrame
            The concatenated DataFrame of FreeContact and chain distance.
        """
        fc_dist, chain_dist_all = self.rrcreader.freecontact(
            fc_path=self.tool_fp,
            file_name=self.prot_name,
            file_chain=self.file_chain,
            pair_list=self.pair_list,
            dist_df=self.dist_df,
            sort_=self.sort_,
        )
        return pd.concat([fc_dist, chain_dist_all], axis=1)

    def ccmpred(self) -> pd.DataFrame:
        """
        Execute the CCMPred method and return the result.

        Returns
        -------
        pd.DataFrame
            The concatenated DataFrame of CCMPred and chain distance.
        """
        cp_dist, chain_dist_all = self.rrcreader.ccmpred(
            cp_path=self.tool_fp,
            file_name=self.prot_name,
            file_chain=self.file_chain,
            pair_list=self.pair_list,
            dist_df=self.dist_df,
            sort_=self.sort_,
        )
        return pd.concat([cp_dist, chain_dist_all], axis=1)

    def gremlin(self) -> pd.DataFrame:
        """
        Execute the Gremlin method and return the result.

        Returns
        -------
        pd.DataFrame
            The concatenated DataFrame of Gremlin and chain distance.
        """
        gl_dist, chain_dist_all = self.rrcreader.gremlin(
            gl_path=self.tool_fp,
            file_name=self.prot_name,
            file_chain=self.file_chain,
            pair_list=self.pair_list,
            dist_df=self.dist_df,
            sort_=self.sort_,
        )
        return pd.concat([gl_dist, chain_dist_all], axis=1)

    def gdca(self) -> pd.DataFrame:
        """
        Execute the GDCA method and return the result.

        Returns
        -------
        pd.DataFrame
            The concatenated DataFrame of GDCA and chain distance.
        """
        gdca_dist, chain_dist_all = self.rrcreader.gdca(
            gdca_path=self.tool_fp,
            file_name=self.prot_name,
            file_chain=self.file_chain,
            pair_list=self.pair_list,
            dist_df=self.dist_df,
            sort_=self.sort_,
        )
        return pd.concat([gdca_dist, chain_dist_all], axis=1)

    def plmc(self) -> pd.DataFrame:
        """
        Execute the PLMC method and return the result.

        Returns
        -------
        pd.DataFrame
            The concatenated DataFrame of PLMC and chain distance.
        """
        plmc_dist, chain_dist_all = self.rrcreader.plmc(
            plmc_path=self.tool_fp,
            file_name=self.prot_name,
            file_chain=self.file_chain,
            pair_list=self.pair_list,
            dist_df=self.dist_df,
            sort_=self.sort_,
        )
        return pd.concat([plmc_dist, chain_dist_all], axis=1)

    def memconp(self) -> pd.DataFrame:
        """
        Execute the MemConP method and return the result.

        Returns
        -------
        pd.DataFrame
            The concatenated DataFrame of MemConP and chain distance.
        """
        memconp_dist, chain_dist_all = self.rrcreader.memconp(
            mcp_path=self.tool_fp,
            file_name=self.prot_name,
            file_chain=self.file_chain,
            pair_list=self.pair_list,
            dist_df=self.dist_df,
            sort_=self.sort_,
        )
        return pd.concat([memconp_dist, chain_dist_all], axis=1)

    def membrain2(self) -> pd.DataFrame:
        """
        Executes the Membrain2 method and returns the results.

        Returns
        -------
        pd.DataFrame
            The concatenated DataFrame of Membrain2 distances and chain distances.
        """
        membrain2_dist, chain_dist_all = self.rrcreader.membrain2(
            mb_path=self.tool_fp,
            file_name=self.prot_name,
            file_chain=self.file_chain,
            pair_list=self.pair_list,
            dist_df=self.dist_df,
            sort_=self.sort_,
        )
        return pd.concat([membrain2_dist, chain_dist_all], axis=1)

    def tma165(self) -> pd.DataFrame:
        """
        Executes the Tma165 method and returns the results.

        Returns
        -------
        pd.DataFrame
            The concatenated DataFrame of Tma165 distances and chain distances.
        """
        tma165_dist, chain_dist_all = self.rrcreader.deephelicon(
            deephelicon_path=self.tool_fp,
            file_name=self.prot_name,
            file_chain=self.file_chain,
            pair_list=self.pair_list,
            dist_df=self.dist_df,
            sort_=self.sort_,
        )
        return pd.concat([tma165_dist, chain_dist_all], axis=1)
