import os

import pandas as pd

import tmkit as tmk

from . import dir_data

# def test_rrc_read():
#     df1, df2 = tmk.rrc.read(
#         prot_name="1xqf",
#         seq_chain="A",
#         fasta_fp=os.path.join(dir_data, "fasta/"),
#         pdb_fp=os.path.join(dir_data, "pdb/"),
#         xml_fp=os.path.join(dir_data, "xml/"),
#         dist_fp=os.path.join(dir_data, "rrc/"),
#         tool_fp=os.path.join(dir_data, "rrc/tool/"),
#         seq_sep_inferior=1,
#         seq_sep_superior=None,
#         tool="membrain2",
#     )
#     assert df1.shape == (19448, 3)
