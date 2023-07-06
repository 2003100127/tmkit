__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
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