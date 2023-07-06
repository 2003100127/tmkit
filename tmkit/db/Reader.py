__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import numpy as np
import pandas as pd
from tmkit.util.Reader import reader as greader


class reader:

    def __init__(self, ):
        self.__sort_ = -1
        self.greader = greader()

    @property
    def sort_(self):
        return self.__sort_

    @sort_.setter
    def sort_(self, value):
        if value > 7 or value < 0:
            raise ValueError(
                '`sort_` has yet to reach there.',
            )
        else:
            self.__sort_ = value

    def mbpred(self, mbp_path, file_name, file_chain, sort_=0):
        self.__sort_ = sort_
        results = self.greader.generic(
            mbp_path + file_name + file_chain + '.mbpred',
            df_sep=',',
            header=0,
            is_utf8=True
        )
        results.columns = [
            'index',
            'aa',
            'interact_id',
            'score'
        ]
        # print(results)
        results['aa'] = results['aa'].astype(str)
        recombine = results[[
            'interact_id',
            'score'
        ]]
        return recombine

    def delphi(self, delphi_path, file_name, file_chain, sort_=0):
        self.__sort_ = sort_
        delphi_fpn = delphi_path + file_name + file_chain + '.txt'
        with open(delphi_fpn) as file:
            cues = []
            for line in file:
                if line.split()[0] == '#':
                    continue
                else:
                    cues.append(line.split())
            results = pd.DataFrame(cues)
        results.columns = [
            'interact_id',
            'aa',
            'score'
        ]
        results['aa'] = results['aa'].astype(str)
        results['interact_id'] = results['interact_id'].astype(np.int)
        results['score'] = results['score'].astype(np.float)
        recombine = results[[
            'interact_id',
            'score'
        ]]
        return recombine

    def graphppis(self, graphppis_path, file_name, file_chain, sort_=0):
        self.__sort_ = sort_
        results = self.greader.generic(
            graphppis_path + file_name + file_chain + '.txt',
            df_sep='\t',
            header=0,
            is_utf8=True,
            comment='#',
        )
        results.columns = [
            'aa',
            'score',
            'label',
        ]
        results['interact_id'] = np.arange(len(results)) + 1
        results = results[['interact_id', 'score']]
        # print(results)
        recombine = results[[
            'interact_id',
            'score',
        ]]
        # print(recombine)
        return recombine

    def tma300(self, tma300_path, file_name, file_chain, sort_=0):
        self.__sort_ = sort_
        results = self.greader.generic(
            tma300_path + file_name + file_chain + '.tma300',
            df_sep='\t',
            header=None,
            is_utf8=True,
        )
        results.columns = [
            'interact_id',
            'aa',
            'score',
        ]
        results['aa'] = results['aa'].astype(str)
        recombine = results[[
            'interact_id',
            'score',
        ]]
        return recombine