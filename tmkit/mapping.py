__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2022"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from tmkit.id.Mapping import mapping as idmap


def pdb2uniprot(
        id,
        ref_fpn='',
):
    return idmap().entryConvert(id=id, ref_fpn=ref_fpn, mode='pdb -> uniprot')


def uniprot2pdb(
        id,
        ref_fpn='',
):
    return idmap().entryConvert(id=id, ref_fpn=ref_fpn, mode='uniprot -> pdb')


if __name__ == "__main__":
    from tmkit.Path import to
    print(pdb2uniprot(
        id='102l',
        ref_fpn=to('data/example/sifts/pdb_chain_uniprot.csv')
    ))

    print(uniprot2pdb(
        id='P00720',
        ref_fpn=to('data/example/sifts/pdb_chain_uniprot.csv'),
    ))