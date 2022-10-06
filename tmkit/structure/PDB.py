__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2022"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from biopandas.pdb import PandasPdb
from tmkit.base import PDB


class pdb(PDB.structure):

    def __init__(
            self,
            pdb_fp,
            prot_name,
            seq_chain,
            file_chain,
    ):
        super(pdb, self).__init__(pdb_fp, prot_name, seq_chain, file_chain)

    def read(self, ):
        return PandasPdb().read_pdb(self.pdb_fpn).df