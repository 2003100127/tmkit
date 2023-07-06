import os

import numpy as np

from tmkit.topo import from_pdbtm, from_phobius, from_tmhmm

from . import dir_data


def test_from_phobius():
    phobius_fpn = os.path.join(dir_data, "1xqfA.jphobius")
    topo = "tmh"
    from_fasta = False
    lower, upper = from_phobius(
        topo=topo, phobius_fpn=phobius_fpn, from_fasta=from_fasta
    )
    assert isinstance(lower, list)
    assert isinstance(upper, list)
    assert len(lower) == len(upper)
    assert lower == [6, 42, 96, 125, 159, 186, 211, 243, 266, 291, 328]
    assert upper == [30, 62, 118, 147, 179, 205, 231, 260, 284, 316, 350]
