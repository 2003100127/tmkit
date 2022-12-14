__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2022"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from tmkit.db.intact.Reader import reader as intactreader
from tmkit.db.biogrid.Reader import reader as biogridreader
from tmkit.db.Connectivity import connectivity as ppiconn


def read_biogrid_db(
        biogrid_fpn,
        sv_fpn,
        extract_ids=[
            'SWISS-PROT Accessions Interactor A',
            'SWISS-PROT Accessions Interactor B',
        ],
):
    """

    Parameters
    ----------
    biogrid_fpn
    sv_fpn
    extract_ids

    Returns
    -------

    """
    return biogridreader().tab3(
        biogrid_fpn=biogrid_fpn,
        sv_fpn=sv_fpn,
        extract_ids=extract_ids,
    )


def read_intact_db(
        intact_fpn,
        sv_fpn,
        extract_ids=[
            '#ID(s) interactor A',
            'ID(s) interactor B',
        ],
):
    """

    Parameters
    ----------
    intact_fpn
    sv_fpn
    extract_ids

    Returns
    -------

    """
    return intactreader().full(
        intact_fpn=intact_fpn,
        sv_fpn=sv_fpn,
        extract_ids=extract_ids,
    )


def get_network(
        prot_name,
        seq_chain,
        prot_idmap,
        interacting_partner_idmap,
        pdb_rcsb_fp,
        pdb_pdbtm_fp,
        sv_fpn,
        ppi_db_fpns,
):
    """

    Parameters
    ----------
    prot_name
    seq_chain
    prot_idmap
    interacting_partner_idmap
    pdb_rcsb_fp
    pdb_pdbtm_fp
    sv_fpn
    ppi_db_fpns

    Returns
    -------

    """
    return ppiconn(
        prot_name=prot_name,
        seq_chain=seq_chain,
        prot_idmap=prot_idmap,
        interacting_partner_idmap=interacting_partner_idmap,
        pdb_rcsb_fp=pdb_rcsb_fp,
        pdb_pdbtm_fp=pdb_pdbtm_fp,
        sv_fpn=sv_fpn,
    ).strategy(
        ppi_db_fpns=ppi_db_fpns,
        uniprot_id=prot_name + '.' + seq_chain,
        is_del_reflexive=False,
        is_del_repeated=False,
        overlap=True,
    )


def connectivity(
        prot_name,
        seq_chain,
        prot_idmap,
        interacting_partner_idmap,
        pdb_rcsb_fp,
        pdb_pdbtm_fp,
        sv_fpn,
        ppi_db_fpns,
):
    """

    Parameters
    ----------
    prot_name
    seq_chain
    prot_idmap
    interacting_partner_idmap
    pdb_rcsb_fp
    pdb_pdbtm_fp
    sv_fpn
    ppi_db_fpns

    Returns
    -------

    """
    return ppiconn(
        prot_name=prot_name,
        seq_chain=seq_chain,
        prot_idmap=prot_idmap,
        interacting_partner_idmap=interacting_partner_idmap,
        pdb_rcsb_fp=pdb_rcsb_fp,
        pdb_pdbtm_fp=pdb_pdbtm_fp,
        sv_fpn=sv_fpn,
    ).extract(
        ppi_db_fpns=ppi_db_fpns,
    )


if __name__ == "__main__":
    from tmkit.Path import to

    # print(read_biogrid_db(
    #     biogrid_fpn=to('data/example/ppi/BIOGRID-ALL-4.4.212.tab3.txt'),
    #     sv_fpn=to('data/example/ppi/BIOGRID-ALL-4.4.212.biogrid'),
    #     extract_ids=[
    #         'SWISS-PROT Accessions Interactor A',
    #         'SWISS-PROT Accessions Interactor B',
    #     ],
    # ))

    # print(read_intact_db(
    #     intact_fpn=to('data/example/ppi/intact.txt'),
    #     extract_ids=[
    #         '#ID(s) interactor A',
    #         'ID(s) interactor B',
    #     ],
    #     sv_fpn=to('data/example/ppi/interA_B.intact'),
    # ))

    # print(get_network(
    #     prot_name='3pux',
    #     seq_chain='G',
    #     prot_idmap={'3pux.G': 'P68183'},
    #     interacting_partner_idmap={
    #         '3pux.A': 'P68187',
    #         '3pux.B': 'P68187',
    #         '3pux.E': 'P0AEX9',
    #         '3pux.F': 'P02916',
    #     },
    #     pdb_rcsb_fp=to('data/example/pdb/indepdata/rcsb/'),
    #     pdb_pdbtm_fp=to('data/example/pdb/indepdata/pdbtm/'),
    #     sv_fpn=to('data/example/ppi/indepdata.ppidb'),
    #     ppi_db_fpns={
    #         'biogrid': to('data/example/ppi/BIOGRID-ALL-4.4.212.biogrid'),
    #         'intact': to('data/example/ppi/interA_B.intact'),
    #     },
    # ))

    print(connectivity(
        prot_name='3pux',
        seq_chain='G',
        prot_idmap={'3pux.G': 'P68183'},
        interacting_partner_idmap={
            '3pux.A': 'P68187',
            '3pux.B': 'P68187',
            '3pux.E': 'P0AEX9',
            '3pux.F': 'P02916',
        },
        pdb_rcsb_fp=to('data/example/pdb/indepdata/rcsb/'),
        pdb_pdbtm_fp=to('data/example/pdb/indepdata/pdbtm/'),
        sv_fpn=to('data/example/ppi/indepdata.ppidb'),
        ppi_db_fpns={
            'biogrid': to('data/example/ppi/BIOGRID-ALL-4.4.212.biogrid'),
            'intact': to('data/example/ppi/interA_B.intact'),
        },
    ))