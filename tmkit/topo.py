__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from tmkit.topology.pdbtm.Segment import segment
from tmkit.topology.Phobius import phobius
from tmkit.topology.TMHMM import tmhmm
from tmkit.topology.pdbtm.Determine import determine
from tmkit.id.Fasta import fasta as idfasta
from tmkit.id.PDB import pdb as idpdb


def from_pdbtm(
        xml_fp,
        prot_name,
        seq_chain,
        topo='tmh',
) -> tuple:
    """

    Parameters
    ----------
    xml_fp
    prot_name
    seq_chain
    topo

    Returns
    -------

    """
    if topo == 'side1':
        w = segment().side1
    elif topo == 'side2':
        w = segment().side2
    elif topo == 'tmh':
        w = segment().tmh
    elif topo == 'nontmh':
        w = segment().nontmh
    elif topo == 'strand':
        w = segment().strand
    elif topo == 'coil':
        w = segment().coil
    elif topo == 'inside':
        w = segment().inside
    elif topo == 'loop':
        w = segment().loop
    elif topo == 'interfacial':
        w = segment().interfacial
    elif topo == 'unknown':
        w = segment().unknown
    else:
        w = segment().all
    return w(
        xml_fp=xml_fp,
        prot_name=prot_name,
        seq_chain=seq_chain,
    )


def from_phobius(
        topo=None,
        phobius_fpn=None,
        from_fasta=False,
        fasta_fpn=None,
        sv_fp=None,
        tag=None,
):
    """

    Parameters
    ----------
    topo
    phobius_fpn
    from_fasta
    fasta_fpn
    sv_fp
    tag

    Returns
    -------

    """
    w = phobius()
    if from_fasta:
        w.run(fasta_fpn=fasta_fpn, sv_fpn=sv_fp + tag)
    df = w.format(phobius_fpn=sv_fp + tag + '.jphobius' if from_fasta else phobius_fpn)
    ptopos = w.extract(df)
    return ptopos[topo + '_lower'], ptopos[topo + '_upper']


def from_tmhmm(
        topo=None,
        tag=None,
        tmhmm_fpn=None,
        from_fasta=False,
        file_kind='linux',
        fasta_fpn=None,
        tmhmm_model_fpn=None,
        sv_fpn=None,

        # for the linux executable
        decodeanhmm=None,
        options=None,
        modelfile=None,
):
    """

    Parameters
    ----------
    topo
    tag
    tmhmm_fpn
    from_fasta
    file_kind
    fasta_fpn
    tmhmm_model_fpn
    sv_fpn
    decodeanhmm
    options
    modelfile

    Returns
    -------

    """
    w = tmhmm()
    if from_fasta:
        assert sv_fpn != None
        if file_kind == 'inline':
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
        if file_kind == 'inline':
            arr = w.formatFromInline(tmhmm_fpn=tmhmm_fpn)
        else:
            arr = w.formatFromLinux(tmhmm_fpn=tmhmm_fpn)
    # print(arr)
    ptopos = w.extract(arr)
    return ptopos[topo + '_lower'], ptopos[topo + '_upper']


def cepdbtm(
        prot_name,
        seq_chain,
        file_chain,
        pdb_fp,
        fasta_fp,
        topo_fp,
        xml_fp,
):
    """

    Parameters
    ----------
    prot_name
    seq_chain
    file_chain
    pdb_fp
    fasta_fp
    topo_fp
    xml_fp

    Returns
    -------

    """
    pdbids = idpdb(
        pdb_fp=pdb_fp,
        prot_name=prot_name,
        seq_chain=seq_chain,
        file_chain=file_chain,
    ).chain()

    fasids = idfasta().get(
        fasta_fpn=fasta_fp + prot_name + file_chain + '.fasta',
    )

    return determine().ce(
        pdbid_map=pdbids,
        fasid_map=fasids,
        pred_fp=topo_fp,
        prot_name=prot_name,
        seq_chain=seq_chain,
        xml_fp=xml_fp,
    )