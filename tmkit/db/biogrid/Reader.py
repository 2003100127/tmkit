__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from tmkit.util.Reader import reader as greader
from tmkit.util.Writer import writer


class reader:

    def __init__(
            self,
    ):
        self.greader = greader()
        self.writer = writer()

    def fetch(self, sv_fp, version='4.4.212'):
        from tmkit.util.Kit import urlliby
        print('===>The BioGRID database of version ' + version + ' is being downloaded...')
        urlliby(
            url='https://downloads.thebiogrid.org/Download/BioGRID/Release-Archive/BIOGRID-' + version + '/BIOGRID-ALL-' + version + '.tab3.zip',
            fpn=sv_fp + 'BIOGRID-ALL-' + version + '.tab3.zip',
        )
        print('===>The database of version ' + version + ' is successfully downloaded!')
        print('===>The database of version ' + version + ' is being decompressed...')
        import zipfile
        with zipfile.ZipFile(sv_fp + 'BIOGRID-ALL-' + version + '.tab3.zip', 'r') as zip_ref:
            zip_ref.extractall(sv_fp)
        print('===>The database of version ' + version + ' is successfully decompressed!')
        return 'Finished!'

    def tab3(self, biogrid_fpn, sv_fpn, extract_ids=['SWISS-PROT Accessions Interactor A', 'SWISS-PROT Accessions Interactor B']):
        print('======>reading BioGRID...')
        all = self.greader.generic(biogrid_fpn, header=0, comment=None)
        print('======>BioGRID features are: '.format())
        for i, e in enumerate(all.columns):
            print('=========>No.{}: {}'.format(i+1, e))
        self.writer.generic(
            df=all[extract_ids],
            sv_fpn=sv_fpn,
            header=True
        )
        print('======>The file is saved.')
        return all[extract_ids]