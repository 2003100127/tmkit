__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2022"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import re
import sys
sys.path.append('../../../')
import pandas as pd
from tmkit.util.Reader import reader as greader
from tmkit.util.Writer import writer
from tmkit.util.Console import console


class reader(object):

    def __init__(
            self,
            verbose=True,
    ):
        self.greader = greader()
        self.writer = writer()

        self.console = console()
        self.console.verbose = verbose

    def decorate(self, x):
        c = re.sub(r'^uniprotkb:', '', x)
        return re.sub(r'.\-', '', c)

    def full(
            self,
            intact_fpn,
            extract_ids=[
                '#ID(s) interactor A',
                'ID(s) interactor B',
            ],
            sv_fpn=None,
    ):
        self.console.print('======>reading IntAct...')

        all = self.greader.generic(intact_fpn, header=0)

        self.console.print('======>IntAct features are: '.format())
        for i, e in enumerate(all.columns):
            self.console.print('=========>No.{}: {}'.format(i + 1, e))

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
        self.console.print('======>The file is saved.')
        return df


if __name__ == "__main__":
    from tmkit.Path import to

    p = reader()
    print(p.full(
        intact_fpn=to('data/example/ppi/intact.txt'),
        extract_ids=[
            '#ID(s) interactor A',
            'ID(s) interactor B',
        ],
        sv_fpn=to('data/example/ppi/interA_B.intact'),
    ))