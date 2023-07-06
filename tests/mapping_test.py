import os

import tmkit as tmk

from . import dir_data


def test_mapping_pdb2uniprot():
    res = tmk.mapping.pdb2uniprot(
        id="101m.A",
        ref_fpn=os.path.join(dir_data, "map/pdb_chain_uniprot.csv"),
    )
    assert res == "P02185"
