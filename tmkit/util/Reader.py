__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import pandas as pd
from functools import wraps


class reader:

    def __call__(self, deal):
        generic = self.generic
        excel = self.excel
        @wraps(deal)
        def read(ph, *args, **kwargs):
            deal(ph, **kwargs)
            keys = [*kwargs.keys()]
            if kwargs['type'] == 'generic':
                return generic(
                    df_fpn=kwargs['df_fpn'],
                    df_sep='\t' if 'df_sep' not in keys else kwargs['df_sep'],
                    skiprows=False if 'skiprows' not in keys else kwargs['skiprows'],
                    header=None if 'header' not in keys else kwargs['header'],
                    is_utf8=False if 'is_utf8' not in keys else kwargs['is_utf8'],
                )
            elif kwargs['type'] == 'excel':
                return excel(
                    df_fpn=kwargs['df_fpn'],
                    sheet_name='Sheet1' if 'sheet_name' not in keys else kwargs['sheet_name'],
                    header=None if 'header' not in keys else kwargs['header'],
                    is_utf8=False if 'is_utf8' not in keys else kwargs['is_utf8'],
                )
        return read

    def generic(self, df_fpn, df_sep='\t', skiprows=None, header=None, is_utf8=False, comment='#'):
        """

        :param df_fpn:
        :param df_sep:
        :param header:
        :param is_utf8:
        :param dtype:
        :return:
        """
        if is_utf8:
            return pd.read_csv(
                df_fpn,
                sep=df_sep,
                header=header,
                encoding='utf-8',
                skiprows=skiprows,
                comment=comment,
            )
        else:
            return pd.read_csv(
                df_fpn,
                sep=df_sep,
                header=header,
                skiprows=None,
                comment=comment,
            )

    def excel(self, df_fpn, sheet_name='Sheet1', header=None, is_utf8=False):
        """

        :param df_fpn:
        :param sheet_name:
        :param header:
        :param is_utf8:
        :return:
        """
        if is_utf8:
            return pd.read_excel(
                df_fpn,
                sheet_name=sheet_name,
                header=header,
                encoding='utf-8',
                engine='openpyxl',
            )
        else:
            return pd.read_excel(
                df_fpn,
                sheet_name=sheet_name,
                header=header,
                engine='openpyxl',
            )