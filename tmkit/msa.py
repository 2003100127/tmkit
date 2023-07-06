__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from tmkit.retrieve.MSA import MSA as remsa


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
    B: int,
    Z: int,
    e: float,
) -> str:
    """
    Generate a HHblits command.

    Parameters
    ----------
    fasta_fp : str
        path where a protein Fasta file is placed.
    hhblits_fp : str
        path where an executable of HHblits is placed (normally it is in hhblits/bin).
    db_path : str
        path where a protein sequence database is placed.
    sv_fp : str
        path to where you want to save the MSAs in a3m format.
    cpu : int
        number of CPUs.
    iteration : int
        number of iterations by a hidden Markov model.
    maxfilter : int
        max number of hits allowed to pass 2nd prefilter (default=20000).
    realign_max :
        realign maximum hits displayed hits with the max accuracy algorithm.
    all :
        do not filter the resulting MSA. '' by default.
    B : int
        maximum number of alignments in alignment list (default=500).
    Z : int
        maximum number of lines in summary hit list (default=500).
    e : float
        maximum E-value in summary and alignment list (default=1E+06).

        # if you won't do it on clusters, please give False to the parameter send2cloud
    send2cloud : bool
        If in cluster running. False or True
    cloud_cmd :str

    Returns
    -------
    str
        'Finished' if this operation is passed.
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
    id: int,
    a3m_fpn: str,
    new_a3m_fpn: str,
) -> str:
    """
    Generate a HHfilter command.

    Parameters
    ----------
    hhfilter_fp :
        path where an executable of HHfilter is placed (normally it is in hhblits/bin).
    a3m_path :
        path where a protein a3m file is placed.
    new_a3m_path :
        path to where you want to save a filtered MSA in a3m format.
    id :
        maximum pairwise sequence identity (def=90).

        # if you won't do it on clusters, please give False to the parameter send2cloud
    send2cloud : bool
        If in cluster running. False or True
    cloud_cmd :str

    Returns
    -------
    str
        'Finished' if this operation is passed.
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
    jhm_E: int,
    incE: float,
    noali: str,
    send2cloud: bool,
    cloud_cmd: str,
) -> str:
    """
    Generate a Jackhmmer command.

    Parameters
    ----------
    fasta_fp : str
        Path where a protein Fasta file is placed.
    jackhmmer_fp : str
        Path where an executable of JackHmmer is placed (normally it is in hmmer3.1b2/bin).
    db_path : str
        Path where a protein sequence database is placed.
    sv_fp : str
        Path to where you want to save the MSAs in a3m format.
    cpu : int
        Number of CPUs.
    iteration : int
        Number of iterations by a hidden Markov model.
    jhm_E : int
        In the per-target output, report target sequences with an E-value of <= . The default is 10.0, meaning that on average, about 10 false positives will be reported per query, so you can see the top of the noise and decide for yourself if it’s really noise.
    incE : float
        Use an E-value as the per-target inclusion threshold. The default is 0.01, meaning that on average, about 1 false positive would be expected in every 100 searches with different query sequences.
    noali :
        Omit the alignment section from the main output. This can greatly reduce the output volume.

        # if you won't do it on clusters, please give False to the parameter send2cloud
    send2cloud : bool
        If in cluster running. False or True
    cloud_cmd :str

    Returns
    -------
    str
        'Finished' if this operation is passed.
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
    """
    Generate a HHBlits reformat command.

    Parameters
    ----------

    reformat_fp : str
        path where an executable of Reformat is placed.
    input_fp : str
        path where a protein sequence database is placed.
    sv_fp : str
        path to where you want to save the MSAs in a3m format.
    input_format : str
        input format, e.g., .sto for Stockholm format.
    output_format : str
        output format, e.g., .a3m for a3m format.
    max_length_per_name_line : int
        maximum number of characers in nameline (default=1000)
    aa_per_line : int
        number of residues per line (for Clustal, FASTA, A2M, A3M formats) (default=100)

        # if you won't do it on clusters, please give False to the parameter send2cloud
    send2cloud : bool
        If in cluster running. False or True
    cloud_cmd :str
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
