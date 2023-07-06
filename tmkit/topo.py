__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import List, Tuple, Dict

from tmkit.id.Fasta import Fasta as idfasta
from tmkit.id.PDB import PDB as idpdb
from tmkit.topology.pdbtm.Determine import determine
from tmkit.topology.pdbtm.Segment import Segment
from tmkit.topology.Phobius import Phobius
from tmkit.topology.TMHMM import TMHMM


def from_pdbtm(
    xml_fp: str,
    prot_name: str,
    seq_chain: str,
    topo: str = "tmh",
) -> Tuple[List, List]:
    """
    Extracts topology information from PDBTM XML file.

    Parameters
    ----------
    xml_fp : str
        The file path of the PDBTM XML file.
    prot_name : str
        name of a protein in the prefix of a PDB file name (e.g., 1xqf in 1xqfA.pdb).
    seq_chain : str
        chain of a protein in the prefix of a PDB file name (e.g., A in 1xqfA.pdb) (biological purpose).
    topo : str, optional
        A topology code. It can be one of side1, side2, strand,
        tmh, coil, inside, loop, interfacial, and Unknown,
        which correspond to Side1, Side2, Beta strand, Alpha
        helix, Coil, Membrane-inside, Membrane-loop,
        Interfacial, Unknown topologies.

    Returns
    -------
    Tuple[List, List]
        A tuple of two Lists representing the lower and upper bounds of the topology.
    """
    if topo == "side1":
        w = Segment().side1
    elif topo == "side2":
        w = Segment().side2
    elif topo == "tmh":
        w = Segment().tmh
    elif topo == "nontmh":
        w = Segment().nontmh
    elif topo == "strand":
        w = Segment().strand
    elif topo == "coil":
        w = Segment().coil
    elif topo == "inside":
        w = Segment().inside
    elif topo == "loop":
        w = Segment().loop
    elif topo == "interfacial":
        w = Segment().interfacial
    elif topo == "unknown":
        w = Segment().unknown
    else:
        w = Segment().all
    return w(
        xml_fp=xml_fp,
        prot_name=prot_name,
        seq_chain=seq_chain,
    )


def from_phobius(
    topo: str = None,
    phobius_fpn: str = None,
    from_fasta: bool = False,
    fasta_fpn: str = None,
    sv_fp: str = None,
    tag: str = None,
) -> Tuple[List, List]:
    """
    Extracts topology information from Phobius output.

    Parameters
    ----------
    topo : str, optional
        The type of topology to extract, by default None.
    phobius_fpn : str, optional
        The file path of the Phobius output file, by default None.
    from_fasta : bool, optional
        Whether to extract from a fasta file, by default False.
    fasta_fpn : str, optional
        The file path of the fasta file, by default None.
    sv_fp : str, optional
        The file path of the output file, by default None.
    tag : str, optional
        The tag to use for the output file, by default None.

    Returns
    -------
    Tuple[List, List]
        A tuple of two numpy arrays representing the lower and upper bounds of the topology.
    """
    w = Phobius()
    if from_fasta:
        w.run(fasta_fpn=fasta_fpn, sv_fpn=sv_fp + tag)
    df = w.format(phobius_fpn=sv_fp + tag + ".jphobius" if from_fasta else phobius_fpn)
    ptopos = w.extract(df)
    return ptopos[topo + "_lower"], ptopos[topo + "_upper"]


def from_tmhmm(
    topo: str = None,
    tag: str = None,
    tmhmm_fpn: str = None,
    from_fasta: bool = True,
    file_kind: str = "inline",
    fasta_fpn: str = None,
    tmhmm_model_fpn: str = None,
    sv_fpn: str = None,
    decodeanhmm: str = None,
    options: List[str] = None,
    modelfile: str = None,
) -> Tuple[List, List]:
    """
    Extracts topology information from TMHMM output.

    Parameters
    ----------
    topo : str, optional
        The type of topology to extract, by default None.
    tag : str, optional
        The tag to use for the output file, by default None.
    tmhmm_fpn : str, optional
        The file path of the TMHMM output file, by default None.
    from_fasta : bool, optional
        from a fasta file, by default True.
    file_kind : str, optional
        The type of file to extract from, by default "inline".
    fasta_fpn : str, optional
        The file path of the fasta file, by default None.
    tmhmm_model_fpn : str, optional
        The file path of the TMHMM model file, by default None.
    sv_fpn : str, optional
        The file path of the output file, by default None.
    decodeanhmm : str, optional
        The file path of the decodeanhmm executable, by default None.
    options : List[str], optional
        A list of options to pass to the TMHMM executable, by default None.
    modelfile : str, optional
        The file path of the TMHMM model file, by default None.

    Returns
    -------
    Tuple[List, List]
        A tuple of two numpy arrays representing the lower and upper bounds of the topology.
    """
    w = TMHMM()
    if from_fasta:
        assert sv_fpn != None
        if file_kind == "inline":
            annot = w.run(
                fasta_fpn=fasta_fpn,
                tag=tag,
                tmhmm_model_fpn=tmhmm_model_fpn,
                sv_fpn=sv_fpn,
            )
            print(annot)
            arr = w.formatFromInline(tmhmm_fpn=sv_fpn)
        else:
            w.runLinux(
                fasta_fpn=fasta_fpn,
                decodeanhmm=decodeanhmm,
                options=options,
                modelfile=modelfile,
                sv_fpn=sv_fpn,
            )
            arr = w.formatFromLinux(tmhmm_fpn=sv_fpn)
    else:
        if file_kind == "inline":
            arr = w.formatFromInline(tmhmm_fpn=tmhmm_fpn)
        else:
            arr = w.formatFromLinux(tmhmm_fpn=tmhmm_fpn)
    ptopos = w.extract(arr)
    return ptopos[topo + "_lower"], ptopos[topo + "_upper"]


def cepdbtm(
    prot_name: str,
    seq_chain: str,
    file_chain: str,
    pdb_fp: str,
    fasta_fp: str,
    topo_fp: str,
    xml_fp: str,
) -> Tuple[Dict, Dict]:
    """
    Determines structure-derived intra- and extra-cellular topology of a protein.

    Parameters
    ----------
    prot_name : str
        name of a protein in the prefix of a PDB file name (e.g., 1xqf in 1xqfA.pdb).
    seq_chain : str
        chain of a protein in the prefix of a PDB file name (e.g., A in 1xqfA.pdb) (biological purpose).
    file_chain : str
        chain of a protein in the prefix of a PDB file name (e.g., A in 1xqfA.pdb) (technical purpose).
    pdb_fp : str
        The file path of the PDB file.
    fasta_fp : str
        The file path of the FASTA file.
    topo_fp : str
        The file path of the topology file.
    xml_fp : str
        The file path of the PDBTM XML file.

    Returns
    -------
    Tuple
        Two dictionaries (structure and prediction) the topology of the protein.
    """
    pdbids = idpdb(
        pdb_fp=pdb_fp,
        prot_name=prot_name,
        seq_chain=seq_chain,
        file_chain=file_chain,
    ).chain()

    fasids = idfasta().get(
        fasta_fpn=fasta_fp + prot_name + file_chain + ".fasta",
    )

    return determine().ce(
        pdbid_map=pdbids,
        fasid_map=fasids,
        pred_fp=topo_fp,
        prot_name=prot_name,
        seq_chain=seq_chain,
        xml_fp=xml_fp,
    )
