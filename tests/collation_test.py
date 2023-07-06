import os

import tmkit as tmk

from . import dir_data

# PDBTM


# def test_collate_chain():
#     pdb_pdbtm_fp = os.path.join(dir_data, "pdb/collate/pdbtm/")
#     chains = tmk.collate.chain(
#         prot_name="6cxh",
#         pdb_fp=pdb_pdbtm_fp,
#     )
#     assert len(chains) == 8
#     assert chains[0] == "A"
