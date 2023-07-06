__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from tmkit.channel.Workbench import workbench


def obtain_single(
        df_prot,
        pdb_cplx_fp,
        fasta_fp,
        xml_fp,
        sv_fp,
        metric='rez',
):
    """

    Parameters
    ----------
    df_prot
    pdb_cplx_fp
    fasta_fp
    xml_fp
    sv_fp
    metric
        rez, met, bio_name, head, desc, mthm, or seq

    Returns
    -------

    """
    return workbench(
        df_prot=df_prot,
        pdb_cplx_fp=pdb_cplx_fp,
        fasta_fp=fasta_fp,
        xml_fp=xml_fp,
        sv_fp=sv_fp,
    ).template(metric=metric)


def integrate(
        df_prot,
        pdb_cplx_fp,
        fasta_fp,
        xml_fp,
        sv_fp,
        metrics,
):
    """

    Parameters
    ----------
    df_prot
    pdb_cplx_fp
    fasta_fp
    xml_fp
    sv_fp
    metrics
        rez, met, bio_name, head, desc, mthm, and seq

    Returns
    -------

    """
    return workbench(
        df_prot=df_prot,
        pdb_cplx_fp=pdb_cplx_fp,
        fasta_fp=fasta_fp,
        xml_fp=xml_fp,
        sv_fp=sv_fp,
    ).integrate(metrics=metrics)