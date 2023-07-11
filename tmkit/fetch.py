__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import os

from tmkit.util.Kit import urlliby


def tmkit_data(
    sv_fpn: str,
    url: str = "https://sandbox.zenodo.org/record/1219139/files/data.zip?download=1",
) -> None:
    """
    Download TMKit example dataset.

    Parameters
    ----------
    url : str
        URL to download the TMKit example dataset
    sv_fpn : str
        path to save the TMKit example dataset
    """
    print("===>Dowloading TMKit example dataset...")

    # create directory if not exist
    sv_dir = os.path.dirname(sv_fpn)
    if not os.path.exists(sv_dir):
        os.makedirs(sv_dir)

    urlliby(url=url, fpn=sv_fpn)
    print("===>Dowloaded!")


def unzip(in_fpn: str, out_fp: str) -> None:
    """
    Decompressing TMKit example dataset

    Parameters
    ----------
    in_fpn : str
        path to save the TMKit example dataset
    out_fp : str
        path where the TMKit example dataset is decompressed
    """
    import zipfile

    print("===>Decompressing TMKit example dataset...")
    with zipfile.ZipFile(in_fpn, "r") as zip_ref:
        zip_ref.extractall(out_fp)
    print("===>Decompressed!")
