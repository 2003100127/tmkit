from typing import List, Tuple

import os

import tmkit as tmk
from tmkit.topo import from_pdbtm, from_phobius, from_tmhmm

from . import dir_data, fin_fasta, fin_pdb


def test_read_from_fasta():
    sequence = tmk.seq.read_from_fasta(fasta_fpn=fin_fasta)
    assert len(sequence) == 362
    assert sequence[0] == "A"
    assert sequence[-1] == "P"


def test_fasid():
    seq_fasta_ids = tmk.seq.fasid(fasta_fpn=fin_fasta)
    assert len(seq_fasta_ids) == 362
    assert seq_fasta_ids[1] == "A"
    assert seq_fasta_ids[362] == "P"
