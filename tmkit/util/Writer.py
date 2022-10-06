__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2022"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import sys
sys.path.append('../../../')
import pandas as pd


class writer(object):

    def __init__(self, ):
        pass

    def generic(self, df, sv_fpn, df_sep='\t', header=None, index=False, id_from=0):
        df_ = pd.DataFrame(df)
        df_.index = df_.index + id_from
        return df_.to_csv(
            sv_fpn,
            sep=df_sep,
            header=header,
            index=index
        )

    def excel(self, df, sv_fpn=None, sheet_name='Sheet1', header=None, index=False, id_from=0):
        df_ = pd.DataFrame(df)
        df_.index = df_.index + id_from
        return df_.to_excel(
            sv_fpn,
            sheet_name=sheet_name,
            header=header,
            index=index
        )

    def save(self, list_2d, sv_fp):
        for i, e in enumerate(list_2d):
            prot_name = str(e[0])
            seq = str(e[1])
            print('No.{} saving {} in FASTA format.'.format(i+1, prot_name))
            f = open(sv_fp, 'w')
            f.write('>' + prot_name + '\n')
            f.write(seq + '\n')
            f.close()
        return 0