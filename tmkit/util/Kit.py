__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import Any, Dict, List, Tuple, Union

import gzip
import os
import re
import shutil
import urllib.request


def chainid(
    prot_chain: str,
) -> str:
    """
    Add 'l' to the end of the chain ID if it is lowercase.

    Parameters
    ----------
    prot_chain : str
        The chain ID of a protein.

    Returns
    -------
    str
        The chain ID with 'l' added if it is lowercase.
    """
    return str(prot_chain) + "l" if str(prot_chain).islower() else str(prot_chain)


def seqchainid(
    prot_chain: str,
) -> str:
    """
    Get the chain ID of a protein sequence.

    Parameters
    ----------
    prot_chain : str
        The chain ID of a protein sequence.

    Returns
    -------
    str
        The chain ID of the protein sequence.
    """
    return str(prot_chain[0])


def delete(
    fpn: str,
) -> None:
    """
    Delete a file.

    Parameters
    ----------
    fpn : str
        The file path and name.
    """
    os.remove(fpn)


def create(
    DIRECTORY: str,
    mode: str = "dir",
) -> None:
    """
    Create a directory.

    Parameters
    ----------
    DIRECTORY : str
        The directory path.
    mode : str, optional
        The mode of the creation. Default is 'dir'.
    """
    if mode == "dir":
        if not os.path.exists(DIRECTORY):
            os.makedirs(DIRECTORY)


def rename(
    old_fp: str,
    old_fn: str,
    new_fn: str,
    sv_fp: str,
    old_suffix: str,
    new_suffix: str,
):
    return os.rename(
        old_fp + old_fn + old_suffix,
        sv_fp + new_fn + new_suffix
    )


def batchRename(
    file_path: str,
    old_suffix: str,
    new_suffix: str,
    flag: int = 1,
) -> None:
    """
    Batch rename files.

    Parameters
    ----------
    file_path : str
        The path of the files.
    old_suffix : str
        The old suffix of the files.
    new_suffix : str
        The new suffix of the files.
    flag : int, optional
        The flag of the renaming. Default is 1.
    """
    if flag == 0:
        for file_name in os.listdir(file_path):
            if os.path.isfile(os.path.join(file_path, file_name)):
                file_name_re = re.sub(r"[p]db", "", file_name)
                file_name_re = re.sub(r"\.[e]nt", "", file_name_re)
                os.rename(
                    os.path.join(file_path, file_name),
                    os.path.join(file_path, file_name_re + ".pdb"),
                )
    elif flag == 1:
        for file in os.listdir(file_path):
            path = os.path.join(file_path, file)
            if os.path.splitext(path)[1] == old_suffix:
                file_name = os.path.splitext(file)[0]
                prot_name = re.sub(r"[A-Z].", "", os.path.splitext(file)[0])
                chain = re.sub(r"[a-z0-9]", "", os.path.splitext(file)[0])
                os.rename(
                    os.path.join(file_path, file_name + old_suffix),
                    os.path.join(file_path, prot_name + chain + new_suffix),
                )


def urlliby(
    url: str,
    fpn: str,
) -> None:
    """
    Download a file from a given URL and save it to the specified file path.

    Parameters
    ----------
    url : str
        The URL of the file to download.
    fpn : str
        The file path to save the downloaded file.

    Returns
    -------
    None
    """
    return urllib.request.urlretrieve(url=url, filename=fpn)


def ungz(
    file_path: str,
    file_name: str,
    sv_fp: str,
    new_suffix: str = ".pdb",
) -> None:
    """
    Extract a gzipped file and save it with a new suffix.

    Parameters
    ----------
    file_path : str
        The path where the gzipped file is located.
    file_name : str
        The name of the gzipped file (without the .gz extension).
    sv_fp : str
        The destination path where the extracted file will be saved.
    new_suffix : str, optional
        The new suffix for the extracted file, by default ".pdb"

    Returns
    -------
    None
    """
    try:
        with gzip.open(file_path + file_name + ".gz", "rb") as f_in:
            with open(sv_fp + file_name + new_suffix, "wb") as f_out:
                shutil.copyfileobj(f_in, f_out)
    except FileNotFoundError:
        print("No such file" + file_path + file_name)
    return


def tactic1(arr_2d: List[List[Any]]) -> Dict[Any, Dict[Any, Any]]:
    """
    Convert a 2D list into a nested dictionary using tactic 1.
    Is a 2D list has the following form [[15, 48, 78],...].
    The returned dictionary is {key1: {key2: value1}, ...},
    in which key 1 is 15, key 2 is 48, and value1
    is 78. Is a 2D list has the following form [[15, 48, 78, 82],...].
    The returned dictionary is {key1: {key2: value1}, ...},
    in which key 1 is 15, key 2 is 48, and value1
    is [78, 82]. See Examples below

    Parameters
    ----------
    arr_2d : List[List[Any]]
        The input 2D list.

    Examples
    --------
    1st example
    >>> arr_2d = [[15, 48, 78, 82], [30, 53, 99, 84], [2, 3, 11, 2]]
    >>> arr_2d
    # output
    >>> {15: {48: [78, 82]}, 30: {53: [99, 84]}, 2: {3: [11, 2]}}

    Returns
    -------
    Dict[Any, Dict[Any, Any]]
        The nested dictionary created from the 2D list.
    """
    result = {}
    len_arr = len(arr_2d[0])
    if len_arr == 3:
        for item in arr_2d:
            result.setdefault(item[0], {}).update({item[1]: item[2]})
    else:
        for item in arr_2d:
            result.setdefault(item[0], {}).update({item[1]: item[2:]})
    return result


def tactic5(arr_2d: List[List[Any]]) -> Dict[Any, List[Any]]:
    """
    Convert a 2D list into a dictionary. If the 1st element in
     list A in the 2nd dimension of a 2D list is the same as that in
     another list B in the 2nd dimension of the 2D list, then
     the unrepeated 2nd element in lists A and B will be put together in
      a Python dict. They share the same key (the 1st element).
      See below Examples. For key -> value, in this case, 'value'
      is a list.

    Parameters
    ----------
    arr_2d : List[List[Any]]
        The input 2D list.

    Examples
    --------
    1st example
    >>> arr_2d = [[15, 48], [15, 53], [2, 3]]
    >>> arr_2d
    # output
    >>> {15: [48, 53], 2: [3]}

    Returns
    -------
    Dict[Any, List[Any]]
        The dictionary created from the 2D list.
    """
    result = {}
    for item in arr_2d:
        result[item[0]] = []
    for item in arr_2d:
        if item[0] in result.keys():
            result[item[0]].append(item[1])
    return result


def tactic6(
    arr_2d: List[List[Union[int, float, str]]]
) -> Dict[Union[int, float, str], List[Union[float, str]]]:
    """
    Apply tactic 6 to a 2D list and return the result as a dictionary.
    If the second dimension of a 2D list is 2, then it returns a dictionary
    that consists of simply the key -> value by taking the 1st element
    (from the list at the second dimension, e.g., [15, 48]) as key
    and the 2nd element as the value. If the list at the second dimension
    has a length of more than 2, then the value of the returned dictionary
    will be this list but eliminating its 1st element, because
    the 1st element will be taken as the key. See Examples below.

    Parameters
    ----------
    arr_2d : List[List[Union[int, float, str]]]
        The input 2D array.

    Examples
    --------
    1st example
    >>> arr_2d = [[15, 48], [30, 53], [2, 3]]
    >>> arr_2d
    # output
    >>> {15: 53, 2: 3}

    2nd example
    >>> arr_2d = [[15, 48, 78], [30, 53, 99], [30, 3, 11]]
    >>> arr_2d
    # output
    >>> {15: [48, 78], 30: [3, 11]}

    Returns
    -------
    Dict[Union[int, float, str], List[Union[float, str]]]
        The result dictionary where the first element of each sublist in `arr_2d`
        is the key and the remaining elements are the values.
    """
    result = {}
    len_arr = len(arr_2d[0])
    if len_arr == 2:
        for item in arr_2d:
            result[item[0]] = item[1]
    else:
        for item in arr_2d:
            result[item[0]] = item[1:]
    return result


def tactic7(
    arr_2d: List[List[Union[int, float, str]]]
) -> Dict[
    Union[int, float, str], Dict[Union[int, float, str], List[Union[int, float, str]]]
]:
    """
    Apply tactic 7 to a 2D array and return the result as a nested dictionary.
    It is only applicable to the list (at the 2nd dimension) of a 2D list
    that has the length of 3, e.g.,[[15, 48, 78],...]. The returned dictionary
    is {key1: {key2: value1}, ...}, in which key 1 is 15, key 2 is 48, and value1
    is 78. See Examples below

    Parameters
    ----------
    arr_2d : List[List[Union[int, float, str]]]
        The input 2D array.

    Examples
    --------
    1st example
    >>> arr_2d = [[15, 48, 78], [30, 53, 99], [30, 3, 11]]
    >>> arr_2d
    # output
    >>> {15: {48: [78]}, 30: {53: [99], 3: [11]}}

    Returns
    -------
    Dict[Union[int, float, str], Dict[Union[int, float, str], List[Union[int, float, str]]]]
        The result nested dictionary where the first element of each sublist in `arr_2d`
        is the outer key, the second element is the inner key, and the third element
        is appended to the corresponding inner key's list.
    """
    result = {}
    for item in arr_2d:
        result[item[0]] = {}
    for item in arr_2d:
        result[item[0]][item[1]] = []
    for item in arr_2d:
        if item[1] in result[item[0]].keys():
            result[item[0]][item[1]].append(item[2])
    return result


def tactic8(
    arr_1d_1: List[Union[int, float, str]],
    arr_1d_2: List[Union[int, float, str]],
) -> Dict[Union[int, float, str], Union[int, float, str]]:
    """
    Create a dictionary by mapping elements from two 1D arrays.
    The input two 1D lists that must has the same length.
    The function will take each element from arr_1d_1 as the key,
    and each element from arr_1d_2 as the value. See Examples below.

    Parameters
    ----------
    arr_1d_1 : List[Union[int, float, str]]
        The first input 1D array.
    arr_1d_2 : List[Union[int, float, str]]
        The second input 1D array.

    Examples
    --------
    >>> l1 = [15, 48, 78, 82]
    >>> l2 = [30, 53, 99, 84]
    # output
    >>> {15: 30, 48: 53, 78: 99, 82: 84}

    Returns
    -------
    Dict[Union[int, float, str], Union[int, float, str]]
        The resulting dictionary where each element from `arr_1d_1` is a key
        and the corresponding element from `arr_1d_2` is the value.
    """
    map = {}
    for i, e in enumerate(arr_1d_1):
        map[e] = arr_1d_2[i]
    return map
