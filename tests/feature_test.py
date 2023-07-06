import os

import pandas as pd

import tmkit as tmk

from . import dir_data

fdir = os.path.join(dir_data, "lips-")


def test_read_helix_surf():
    df = tmk.feature.read_helix_surf(
        fp=fdir,
        prot_name="1xqf",
        file_chain="A",
        id=1,
    )
    assert df.shape == (155, 5)


def test_feature_read():
    aa_surf_rank, _, _, _ = tmk.feature.read(
        fp=fdir,
        prot_name="1xqf",
        file_chain="A",
    )
    assert aa_surf_rank[1] == 4


def test_read_helix_all_surf():
    df = tmk.feature.read_helix_all_surf(
        fp=fdir,
        prot_name="1xqf",
        file_chain="A",
    )
    assert df.shape == (7, 4)
