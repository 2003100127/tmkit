__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2022"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import sys
sys.path.append('../')
from Bio.PDB import PDBList
from tmkit.util.Kit import ungz
from tmkit.util.Kit import urlliby
from tmkit.util.Kit import delete
from tmkit.util.Kit import batchRename
from tmkit.util.Console import console


class pdb(object):

    def __init__(
            self,
            prot_series,
            verbose=True,
    ):
        self.prot_dedup = prot_series.unique()
        self.console = console()
        self.console.verbose = verbose

    def rcsb(self, sv_fp, route='biopython'):
        """

        Notes
        -----
            Downloading a PDB file from RCSB PDB.

            file_format is specified with 'structure' to download a file
            with suffix of 'ent', which is totally the same with original
            format of file with suffix of 'structure', 'pdb'.

        See Also
        --------
            https://biopython.org/DIST/docs/api/Bio.PDB.PDBList%27-pysrc.html

        Parameters
        ----------
        sv_fp
            path to save files
        route
            'biopython' or 'external'

        Returns
        -------

        """
        pdb_list = PDBList()
        if route == 'biopython':
            for i, prot_name in enumerate(self.prot_dedup):
                self.console.print('===>No.{} protein name: {}'.format(i + 1, prot_name))
                pdb_list.retrieve_pdb_file(
                    pdb_code=str(prot_name),
                    file_format='pdb',
                    pdir=sv_fp,
                )
            batchRename(
                file_path=sv_fp,
                old_suffix='ent',
                new_suffix='pdb',
                flag=0,
            )
        else:
            for i, prot_name in enumerate(self.prot_dedup):
                self.console.print('===>No.{} protein name: {}'.format(i + 1, prot_name))
                url = 'https://files.rcsb.org/download/' + prot_name + '.pdb'
                urlliby(
                    url=url,
                    fpn=sv_fp + str(prot_name) + '.pdb',
                )
        return 0

    def pdbtm(self, sv_fp, kind='tr'):
        """

        Notes
        -----
            Downloading a PDB file from PDBTM.

        Parameters
        ----------
        sv_fp
            path to save files
        kind
            'tr' for 'transformed proteins'
            '' for 'rcsb'

        Returns
        -------

        """
        count = 0
        for i, prot_name in enumerate(self.prot_dedup):
            mark = str(prot_name[1] + prot_name[2])
            url = 'http://pdbtm.enzim.hu/data/database/' + mark + '/' + str(prot_name) + '.' + kind + 'pdb.gz'
            self.console.print('===>No.{} protein name: {}'.format(i + 1, prot_name))
            try:
                urlliby(
                    url=url,
                    fpn=sv_fp + str(prot_name) + '.gz'
                )
                ungz(
                    file_path=sv_fp,
                    file_name=prot_name,
                    sv_fp=sv_fp,
                    new_suffix='.pdb'
                )
                delete(sv_fp + str(prot_name) + '.gz')
            except:
                count = count + 1
                print(count)
                continue
        return 0


if __name__ == "__main__":
    from tmkit.util.Reader import reader
    from tmkit.Path import to

    DEFINE = {
        'list_fpn': to('data/example/pdb/indepdata/prot_n30_.txt'),
        'sv_fp': to('data/'),
    }

    prot_series = reader().generic(DEFINE['list_fpn'])
    print(prot_series[0].unique())

    p = pdb(prot_series=prot_series[0])

    print(p.rcsb(sv_fp=DEFINE['sv_fp'], route='biopython'))

    # print(p.pdbtm(sv_fp=DEFINE['sv_fp']))