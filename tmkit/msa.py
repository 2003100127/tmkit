__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from tmkit.retrieve.MSA import msa as remsa


def run_hhblits(
        hhblits_fp,
        send2cloud,
        cloud_cmd,
        fasta_fpn,
        sv_fpn,
        db_path,
        cpu,
        iteration,
        maxfilter,
        realign_max,
        all,
        B,
        Z,
        e,
):
    """

    Parameters
    ----------
    hhblits_fp
    send2cloud
    cloud_cmd
    fasta_fpn
    sv_fpn
    db_path
    cpu
    iteration
    maxfilter
    realign_max
    all
    B
    Z
    e

    Returns
    -------

    """
    return remsa(
        tool='hhblits',
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
        hhfilter_fp,
        send2cloud,
        cloud_cmd,
        id,
        a3m_fpn,
        new_a3m_fpn,
):
    """

    Parameters
    ----------
    hhfilter_fp
    send2cloud
    cloud_cmd
    id
    a3m_fpn
    new_a3m_fpn

    Returns
    -------

    """
    return remsa(
        tool='hhfilter',
        tool_fp=hhfilter_fp,
        send2cloud=send2cloud,
        cloud_cmd=cloud_cmd,
        id=id,
        input=a3m_fpn,
        output=new_a3m_fpn,
    ).execute()


def run_jackhmmer(
        jackhmmer_fp,
        fasta_fpn,
        sv_fpn,
        db_path,
        cpu,
        iteration,
        jhm_E,
        incE,
        noali,
        send2cloud,
        cloud_cmd,
):
    """

    Parameters
    ----------
    jackhmmer_fp
    send2cloud
    cloud_cmd
    fasta_fpn
    sv_fpn
    db_path
    cpu
    iteration
    jhm_E
    incE
    noali

    Returns
    -------

    """
    return remsa(
        tool='jackhmmer',
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
        reformat_fp,
        send2cloud,
        cloud_cmd,
        max_length_per_name_line,
        aa_per_line,
        input_format,
        output_format,
        input_fpn,
        output_fpn,
):
    """

    Parameters
    ----------
    reformat_fp
    send2cloud
    cloud_cmd
    max_length_per_name_line
    aa_per_line
    input_format
    output_format
    input_fpn
    output_fpn

    Returns
    -------

    """
    return remsa(
        tool='reformat.pl',
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