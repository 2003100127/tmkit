__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"


import os


def root_dict() -> str:
    """
    Get the absolute file path of the root directory.

    Returns
    -------
    str
        The absolute file path of the root directory.
    """
    ROOT_DICT = os.path.dirname(os.path.abspath(__file__))
    return ROOT_DICT


def to(path: str) -> str:
    """
    Join the root directory path with the given path.

    Parameters
    ----------
    path : str
        The path to join with the root directory path.

    Returns
    -------
    str
        The joined path.
    """
    return os.path.join(root_dict(), path)
