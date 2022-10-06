__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2022"
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
        send2cloud,
        cloud_cmd,
        fasta_fpn,
        sv_fpn,
        db_path,
        cpu,
        iteration,
        jhm_E,
        incE,
        noali,
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


if __name__ == "__main__":
    from tmkit.Path import to
    import pandas as pd
    from tmkit.util.Kit import chainid
    params = {
        'list_fpn': to('data/example/pdb/indepdata/prot_n30_.txt'),
        'hhblits_fp': '/home/software/BioInformatics/Fedora31/bin/',
        'hhfilter_fp': '/home/students/j.sun/store/hhblits/bin/',
        'reformat_fp': '/home/students/j.sun/store/hhblits/scripts/',
        'jackhmmer_fp': '/home/students/j.sun/store/software/hmmer3.1b2/bin/',
        'fasta_fp': to('data/protein/fasta/human/isoform/isoform/'),
        'a3m_path': to('data/protein/fasta/human/isoform/isoform/uniclust2020.06/'),
        'new_a3m_path': to('data/protein/fasta/human/isoform/isoform/uniclust2020.06/filter/'),
        'db_path': '/scratch/uniclust_2020.06/UniRef30_2020_06',
        'sv_fp': to('data/protein/fasta/human/isoform/isoform/uniclust2020.06/'),
        'cloud_cmd': "qsub -q all.q -N 'jsun'",
    }
    df_prot = pd.DataFrame([['3udc', 'A'], ['3rko', 'A']], columns=['prot', 'chain'])
    for i in range(df_prot.shape[0]):
        prot_name = df_prot['prot'][i]
        seq_chain = df_prot['chain'][i]
        print(run_hhblits(
            hhblits_fp=params['hhblits_fp'],
            send2cloud=False,
            cloud_cmd=params['cloud_cmd'],
            fasta_fpn=params['fasta_fp'] + prot_name + chainid(seq_chain) + '.fasta',
            sv_fpn=params['sv_fp'] + prot_name + chainid(seq_chain) + '.a3m',
            db_path=params['db_path'],
            cpu=2,
            iteration=3,
            maxfilter=100000,
            realign_max=100000,
            all='',
            B=100000,
            Z=100000,
            e=0.001,
        ))

        print(run_hhfilter(
            hhfilter_fp=params['hhfilter_fp'],
            send2cloud=False,
            cloud_cmd=params['cloud_cmd'],
            id=90,
            a3m_fpn=params['a3m_path'] + prot_name + chainid(seq_chain) + '.a3m',
            new_a3m_fpn=params['new_a3m_path'] + prot_name + chainid(seq_chain) + '.a3m',
        ))

        print(run_jackhmmer(
            jackhmmer_fp=params['jackhmmer_fp'],
            send2cloud=False,
            cloud_cmd=params['cloud_cmd'],
            fasta_fpn=params['fasta_fp'] + prot_name + chainid(seq_chain) + '.fasta',
            sv_fpn=params['sv_fp'] + prot_name + chainid(seq_chain) + '.sto',
            db_path=params['db_path'],
            cpu=4,
            iteration=3,
            jhm_E=10,
            incE=1e-3,
            noali='',
        ))

        print(run_format(
            reformat_fp=params['reformat_fp'],
            send2cloud=False,
            cloud_cmd=params['cloud_cmd'],
            max_length_per_name_line=1500,
            aa_per_line=1500,
            input_format='sto',
            output_format='a3m',
            input_fpn=params['sv_fp'] + prot_name + chainid(seq_chain) + '.sto',
            output_fpn=params['sv_fp'] + prot_name + chainid(seq_chain) + '.a3m',
        ))
