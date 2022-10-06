__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2022"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import sys
sys.path.append('../../../')
from tmkit.util.Reader import reader as greader
from tmkit.util.Writer import writer
from tmkit.util.Console import console


class reader():

    def __init__(
            self,
            verbose=True,
    ):
        self.greader = greader()
        self.writer = writer()

        self.console = console()
        self.console.verbose = verbose

    def tab(self, ):
        pass

    def tab2(self, ):
        pass

    def tab3(self, biogrid_fpn, sv_fpn, extract_ids=['SWISS-PROT Accessions Interactor A', 'SWISS-PROT Accessions Interactor B']):
        self.console.print('======>reading BioGRID...')
        all = self.greader.generic(biogrid_fpn, header=0)
        self.console.print('======>BioGRID features are: '.format())
        for i, e in enumerate(all.columns):
            self.console.print('=========>No.{}: {}'.format(i+1, e))
        self.writer.generic(
            df=all[extract_ids],
            sv_fpn=sv_fpn,
            header=True
        )
        self.console.print('======>The file is saved.')
        return all[extract_ids]

    def mitab(self, ):
        pass


if __name__ == "__main__":
    from tmkit.Path import to

    p = reader()

    print(p.tab3(
        biogrid_fpn=to('data/example/ppi/BIOGRID-ALL-4.4.212.tab3.txt'),
        sv_fpn=to('data/example/ppi/BIOGRID-ALL-4.4.212.biogrid'),
        extract_ids=[
            'SWISS-PROT Accessions Interactor A',
            'SWISS-PROT Accessions Interactor B',
        ],
    ))