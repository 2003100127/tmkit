__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import numpy as np
import pandas as pd

from tmkit.db.Reader import Reader as ppireader
from tmkit.structure.PDB import PDB as spdb
from tmkit.structure.ppi.Label import Label as dlable
from tmkit.util.Kit import chainid, create, seqchainid, tactic8
from tmkit.util.Writer import Writer


class labelling:
    def __init__(
        self,
        tool: str,
        prot_name: str,
        prot_chain: str,
        pdb_fp: str,
        isite_fp: str,
        sv_fp: str,
    ) -> None:
        """
        Labelling a protein.

        Parameters
        ----------
        tool : str
            The tool to use for fetching data.
        prot_name : str
            name of a protein in the prefix of a PDB file name (e.g., 1xqf in 1xqfA.pdb).
        prot_chain : str
            chain of a protein in the prefix of a PDB file name (e.g., A in 1xqfA.pdb).
        pdb_fp : str
            The filepath of the PDB file.
        isite_fp : str
            Path where a file showing interaction sites and the interaction likelihoods is placed.
        sv_fp : str
            The filepath of the saved file.
        """
        self.writer = Writer()
        self.ppireader = ppireader()
        self.tool = tool
        self.prot_name = prot_name
        self.prot_chain = prot_chain
        self.pdb_fp = pdb_fp
        self.isite_fp = isite_fp
        self.sv_fp = sv_fp

        self.seq_chain = seqchainid(prot_chain)
        self.file_chain = chainid(prot_chain)
        self.pdb_file = spdb(
            pdb_fp=pdb_fp,
            prot_name=prot_name,
            file_chain=self.file_chain,
            seq_chain=self.seq_chain,
        ).read()["ATOM"]
        print(self.pdb_file.columns)

        self.pdb_ids = pd.unique(self.pdb_file["residue_number"]).tolist()

        self.isite_pred = self.fetch()(
            isite_fp,
            prot_name,
            self.file_chain,
            sort_=0,
        ).rename(
            columns={
                "interact_id": "fasta_id",
                "score": "probability",
            }
        )

        create(
            DIRECTORY=self.sv_fp,
            mode="dir",
        )

    def fetch(
        self,
    ) -> ppireader:
        """
        Fetch the data using the specified tool.

        Returns
        -------
        ppireader
            The fetched data.
        """
        switch = {
            "mbpred": self.ppireader.mbpred,
            "delphi": self.ppireader.delphi,
            "deeptminter": self.ppireader.tma300,
            "graphppis": self.ppireader.graphppis,
        }
        return switch[self.tool]

    def format(
        self,
    ) -> None:
        """
        Format the data.
        """
        pdb_on_use = self.pdb_file[
            [
                "chain_id",
                "residue_name",
                "residue_number",
                "atom_name",
            ]
        ]
        # print(pdb_on_use)
        pdb_ids = pd.unique(pdb_on_use["residue_number"])
        # print(pdb_ids)
        self.isite_pred = self.fetch()(
            self.isite_fp,
            self.prot_name,
            self.file_chain,
            sort_=0,
        ).rename(
            columns={
                "interact_id": "fasta_id",
                "score": "probability",
            }
        )
        fas_ids = self.isite_pred["fasta_id"].astype(np.int).values
        probs = self.isite_pred["probability"].values
        pdb_fas_map = tactic8(pdb_ids, fas_ids)
        fas_prob_map = tactic8(fas_ids, probs)
        # print(pdb_fas_map)
        # print(fas_prob_map)
        pdb_on_use["probability"] = -1
        # print(pdb_on_use)
        for i in pdb_on_use.index:
            pdb_id = pdb_on_use.loc[i, "residue_number"]
            # print(pdb_id)
            fas_id = pdb_fas_map[pdb_id]
            pdb_on_use.loc[i, "probability"] = fas_prob_map[fas_id]
        # print(pdb_on_use)
        self.writer.generic(df=pdb_on_use, df_sep=" ", sv_fpn=self.sv_fp)
        return

    def probs(
        self,
    ) -> pd.DataFrame:
        """
        Get the interaction probabilities.

        Returns
        -------
        pd.DataFrame
            DataFrame of the interaction probabilities.
        """
        df = pd.concat(
            [pd.DataFrame(self.pdb_ids), self.isite_pred["probability"]], axis=1
        )
        self.writer.generic(df=df, df_sep="\t", sv_fpn=self.sv_fp + "probs_bf.txt")
        return df

    def predictedLabels(
        self,
        dist_fp: str,
    ) -> pd.DataFrame:
        """
        Get the predicted labels.

        Parameters
        ----------
        dist_fp : str
            path where a file containing real distances between residues is placed (please check the file at ./data/rrc in the example dataset).

        Returns
        -------
        pd.DataFrame
            The predicted interaction labels.
        """
        self.isite_pred["is_interaction"] = -1
        ni_ids = self.isite_pred.loc[self.isite_pred["probability"] < 0.5].index
        i_ids = self.isite_pred.loc[self.isite_pred["probability"] >= 0.5].index
        self.isite_pred["is_interaction"].loc[ni_ids] = 0
        self.isite_pred["is_interaction"].loc[i_ids] = 1
        from sklearn import metrics

        dist_df = dlable(
            dist_path=dist_fp,
            prot_name=self.prot_name,
            file_chain=self.file_chain,
            cutoff=6,
        ).attach()
        print(dist_df)
        print(self.isite_pred)
        print(
            metrics.accuracy_score(
                dist_df["is_contact"].values,
                np.rint(self.isite_pred["probability"].values),
            )
        )
        print(
            metrics.average_precision_score(
                dist_df["is_contact"].values,
                np.rint(self.isite_pred["probability"].values),
            )
        )
        df = pd.concat(
            [
                pd.DataFrame(self.pdb_ids),
                self.isite_pred["is_interaction"],
            ],
            axis=1,
        )
        self.writer.generic(
            df=df, df_sep="\t", sv_fpn=self.sv_fp + "predicted_label_bf.txt"
        )
        return df

    def actualLabels(
        self,
        dist_fp: str,
    ) -> pd.DataFrame:
        """
        Get the actual interaction labels.

        Parameters
        ----------
        dist_fp : str
            path where a file containing real distances between residues is placed (please check the file at ./data/rrc in the example dataset).

        Returns
        -------
        pd.DataFrame
            The actual labels.
        """
        dist_df = dlable(
            dist_path=dist_fp,
            prot_name=self.prot_name,
            file_chain=self.file_chain,
            cutoff=6,
        ).attach()
        create(DIRECTORY=self.sv_fp, mode="dir")
        df = pd.concat([pd.DataFrame(self.pdb_ids), dist_df["is_contact"]], axis=1)
        self.writer.generic(
            df=df, df_sep="\t", sv_fpn=self.sv_fp + "actual_label_bf.txt"
        )
        return df
