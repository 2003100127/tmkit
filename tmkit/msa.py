__author__: str = "Jianfeng Sun"
__version__: str = "v1.0"
__copyright__: str = "Copyright 2023"
__license__: str = "GPL v3.0"
__email__: str = "jianfeng.sunmt@gmail.com"
__maintainer__: str = "Jianfeng Sun"

from typing import List, Union
from tmkit.retrieve.MSA import msa as remsa


def run_hhblits(
    hhblits_fp: str,
    send2cloud: bool,
    cloud_cmd: str,
    fasta_fpn: str,
    sv_fpn: str,
    db_path: str,
    cpu: int,
    iteration: int,
    maxfilter: int,
    realign_max: int,
    all: bool,
    B: Union[bool, str],
    Z: Union[bool, str],
    e: float,
) -> str:
    """_summary_

    Parameters
    ----------
    hhblits_fp : str
        _description_
    send2cloud : bool
        _description_
    cloud_cmd : str
        _description_
    fasta_fpn : str
        _description_
    sv_fpn : str
        _description_
    db_path : str
        _description_
    cpu : int
        _description_
    iteration : int
        _description_
    maxfilter : int
        _description_
    realign_max : int
        _description_
    all : bool
        _description_
    B : Union[bool, str]
        _description_
    Z : Union[bool, str]
        _description_
    e : float
        _description_

    Returns
    -------
    str
        _description_
    """
    return remsa(
        tool="hhblits",
        tool_fp=hhblits_fp,
        send2cloud=send2cloud,
        cloud_cmd=cloud_cmd,
        input=fasta_fpn,
        output2a3m=sv_fpn,
        database=db_path,
        cpu=cpu,
        iteration=iteration,
        maxfilter=maxfilter,
        realign_max=realign_max,
        all=all,
        B=B,
        Z=Z,
        e=e,
    ).execute()


def run_hhfilter(
    hhfilter_fp: str,
    send2cloud: bool,
    cloud_cmd: str,
    id: float,
    a3m_fpn: str,
    new_a3m_fpn: str,
) -> str:
    """_summary_

    Parameters
    ----------
    hhfilter_fp : str
        _description_
    send2cloud : bool
        _description_
    cloud_cmd : str
        _description_
    id : float
        _description_
    a3m_fpn : str
        _description_
    new_a3m_fpn : str
        _description_

    Returns
    -------
    str
        _description_
    """
    return remsa(
        tool="hhfilter",
        tool_fp=hhfilter_fp,
        send2cloud=send2cloud,
        cloud_cmd=cloud_cmd,
        id=id,
        input=a3m_fpn,
        output=new_a3m_fpn,
    ).execute()


def run_jackhmmer(
    jackhmmer_fp: str,
    fasta_fpn: str,
    sv_fpn: str,
    db_path: str,
    cpu: int,
    iteration: int,
    jhm_E: float,
    incE: float,
    noali: bool,
    send2cloud: bool,
    cloud_cmd: str,
) -> str:
    """_summary_

    Parameters
    ----------
    jackhmmer_fp : str
        _description_
    fasta_fpn : str
        _description_
    sv_fpn : str
        _description_
    db_path : str
        _description_
    cpu : int
        _description_
    iteration : int
        _description_
    jhm_E : float
        _description_
    incE : float
        _description_
    noali : bool
        _description_
    send2cloud : bool
        _description_
    cloud_cmd : str
        _description_

    Returns
    -------
    str
        _description_
    """
    return remsa(
        tool="jackhmmer",
        tool_fp=jackhmmer_fp,
        send2cloud=send2cloud,
        cloud_cmd=cloud_cmd,
        input=fasta_fpn,
        output2sto=sv_fpn,
        database=db_path,
        cpu=cpu,
        iteration=iteration,
        jhm_E=jhm_E,
        incE=incE,
        noali=noali,
    ).execute()


def run_format(
    reformat_fp: str,
    send2cloud: bool,
    cloud_cmd: str,
    max_length_per_name_line: int,
    aa_per_line: int,
    input_format: str,
    output_format: str,
    input_fpn: str,
    output_fpn: str,
) -> str:
    """_summary_

    Parameters
    ----------
    reformat_fp : str
        _description_
    send2cloud : bool
        _description_
    cloud_cmd : str
        _description_
    max_length_per_name_line : int
        _description_
    aa_per_line : int
        _description_
    input_format : str
        _description_
    output_format : str
        _description_
    input_fpn : str
        _description_
    output_fpn : str
        _description_

    Returns
    -------
    str
        _description_
    """
    return remsa(
        tool="reformat.pl",
        tool_fp=reformat_fp,
        send2cloud=send2cloud,
        cloud_cmd=cloud_cmd,
        max_length_per_name_line=max_length_per_name_line,
        aa_per_line=aa_per_line,
        input_format=input_format,
        output_format=output_format,
        input=input_fpn,
        output=output_fpn,
    ).execute()
