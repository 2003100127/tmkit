__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"


from Bio import SeqIO


class EmptyFastaError(Exception):
    """Error raised if FASTA file does not contain sequence"""


def get(fasta_fpn: str) -> str:
    """
    Get the sequence from a FASTA file.

    Parameters
    ----------
    fasta_fpn : str
        The filepath of the FASTA file.

    Returns
    -------
    str
        A sequence from the FASTA file.

    Raises
    ------
    EmptyFastaError
        If the FASTA file does not contain any sequence.
    """
    sequence = "".join([str(seq.seq) for seq in SeqIO.parse(fasta_fpn, "fasta")])
    if not sequence:
        raise EmptyFastaError("The sequence is empty.")
    return sequence
