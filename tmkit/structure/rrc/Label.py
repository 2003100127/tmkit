__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import numpy as np
import pandas as pd

from tmkit.position.scenario.Separation import Separation
from tmkit.util.Reader import Reader


class Label:
    def __init__(
        self,
        dist_path,
        prot_name,
        file_chain,
        cutoff=5.5,
        seq_sep_inferior=None,
        seq_sep_superior=None,
    ):
        """
        Parameters
        ----------
        dist_path
            path where a file containing real distances between residues is placed
            (please check the file at ./data/rrc in the example dataset).
        prot_name
            Name of a protein in the prefix of a PDB file name (e.g., 1xqf in 1xqfA.pdb).
        file_chain
            Chain of a protein in the prefix of a PDB file name (e.g., A in 1xqfA.pdb).
             Parameter file_chain will be converted within the function.
        cutoff
            distance cutoff to see whether two residues are in spatial contact (e.g., 5.5 angstrom).
        seq_sep_inferior
            The lower bounds of how far any two residues are in pairs.
        seq_sep_superior
            The upper bounds of how far any two residues are in pairs.
        """
        self.prot_name = prot_name
        self.file_chain = file_chain
        self.dist_fpn = dist_path + self.prot_name + self.file_chain + ".dist"
        self.cutoff = cutoff
        self.seq_sep_inferior = seq_sep_inferior
        self.seq_sep_superior = seq_sep_superior

    def attach(self) -> pd.DataFrame:
        """
        Attach distance between residues.

        Returns
        -------
        pd.DataFrame
            A Pandas DataFrame.

        """
        dist_df = Reader().generic(self.dist_fpn)
        dist_np = np.array(dist_df)
        row = dist_np.shape[0]
        new_col = np.array([np.ones(row) * -1])
        dist_np = np.column_stack((dist_np, new_col.T))
        for i in range(row):
            if dist_np[i][6] < self.cutoff:
                dist_np[i][7] = 1
            else:
                dist_np[i][7] = 0
        dist_df = pd.DataFrame(dist_np)
        dist_df.columns = [
            "fasta_id_1",
            "aa_1",
            "pdb_id_1",
            "fasta_id_2",
            "aa_2",
            "pdb_id_2",
            "dist",
            "is_contact",
        ]
        dist_df = Separation(
            df=dist_df,
            first="fasta_id_1",
            second="fasta_id_2",
            target=None,
            seq_sep_inferior=self.seq_sep_inferior,
            seq_sep_superior=self.seq_sep_superior,
            is_sort=False,
        ).extract()
        return dist_df.reset_index(inplace=False, drop=True)
