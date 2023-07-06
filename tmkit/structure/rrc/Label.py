__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import numpy as np
import pandas as pd

from tmkit.position.scenario.Separation import separation
from tmkit.util.Reader import reader


class label:
    def __init__(
        self,
        dist_path,
        prot_name,
        file_chain,
        cutoff=5.5,
        seq_sep_inferior=None,
        seq_sep_superior=None,
    ):
        self.prot_name = prot_name
        self.file_chain = file_chain
        self.dist_fpn = dist_path + self.prot_name + self.file_chain + ".dist"
        self.cutoff = cutoff
        self.seq_sep_inferior = seq_sep_inferior
        self.seq_sep_superior = seq_sep_superior

    def attach(self):
        dist_df = reader().generic(self.dist_fpn)
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
        dist_df = separation(
            df=dist_df,
            first="fasta_id_1",
            second="fasta_id_2",
            target=None,
            seq_sep_inferior=self.seq_sep_inferior,
            seq_sep_superior=self.seq_sep_superior,
            is_sort=False,
        ).extract()
        return dist_df.reset_index(inplace=False, drop=True)
