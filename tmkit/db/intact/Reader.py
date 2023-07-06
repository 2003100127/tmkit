__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import re
import pandas as pd
from tmkit.util.Reader import reader as greader
from tmkit.util.Writer import writer


class reader:

    def __init__(
            self,
    ):
        self.greader = greader()
        self.writer = writer()

    def decorate(self, x):
        c = re.sub(r'^uniprotkb:', '', x)
        return re.sub(r'.\-', '', c)

    def fetch(self, sv_fp, version='current'):
        """
        psimitab

        Parameters
        ----------
        sv_fp
        version

        Returns
        -------

        """
        from tmkit.util.Kit import urlliby
        print('===>The IntAct database of version ' + version + ' is being downloaded...')
        urlliby(
            url='https://ftp.ebi.ac.uk/pub/databases/intact/' + version + '/psimitab/intact.zip',
            fpn=sv_fp + 'intact.zip',
        )
        print('===>The database of version ' + version + ' is successfully downloaded!')
        print('===>The database of version ' + version + ' is being decompressed...')
        import zipfile
        with zipfile.ZipFile(sv_fp + 'intact.zip', 'r') as zip_ref:
            zip_ref.extractall(sv_fp)
        print('===>The database of version ' + version + ' is successfully decompressed!')
        return 'Finished!'

    def full(
            self,
            intact_fpn,
            extract_ids=[
                '#ID(s) interactor A',
                'ID(s) interactor B',
            ],
            sv_fpn=None,
    ):
        print('======>reading IntAct...')

        all = self.greader.generic(intact_fpn, header=0, comment=None)

        print('======>IntAct features are: '.format())
        for i, e in enumerate(all.columns):
            print('=========>No.{}: {}'.format(i + 1, e))

        df = pd.DataFrame()
        df['#ID(s) interactor A'] = all[extract_ids]['#ID(s) interactor A'].apply(
            lambda x: self.decorate(x)
        )
        df['ID(s) interactor B'] = all[extract_ids]['ID(s) interactor B'].apply(
            lambda x: self.decorate(x)
        )
        if sv_fpn:
            self.writer.generic(
                df=df,
                sv_fpn=sv_fpn,
                header=True
            )
        print('======>The file is saved.')
        return df