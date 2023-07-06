__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import os
import subprocess
import numpy as np
import pandas as pd
from tmkit.interface import Topology


class phobius(Topology.topology):

    def run(
            self,
            fasta_fpn,
            sv_fpn,
            email='jianfeng.sunmt@gmail.com',
    ):
        print('===>Phobius is running python inline...')
        if sv_fpn is None:
            raise 'sv_fpn has to be specified'
        fpnf = os.path.dirname(__file__) + '/lib/Phobius.py'
        order = 'python ' + fpnf + ' --email ' + email + ' --sequence ' + fasta_fpn + ' --stype protein --outfile ' + sv_fpn
        # print('Command to run Phobius: {}'.format(order))
        subprocess.Popen(
            order,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            shell=True,
        ).communicate()
        # print(1)
        # os.system(order)
        os.rename(
            sv_fpn + '.out.txt',
            sv_fpn + '.jphobius',
        )
        return 'finished.'

    @classmethod
    def format(cls, phobius_fpn):
        f = open(phobius_fpn)
        content = [[str(e) for e in line.split()] for line in f]
        df = pd.DataFrame(content)
        # print(df)
        row_mark = df.loc[(df[0] == 'ID')].index[0]
        df = df.drop(index=np.arange(row_mark + 1))
        row_mark = df.loc[(df[0] == '//')].index[0]
        try:
            df = df.drop(index=[row_mark, row_mark + 1])
        except:
            df = df.drop(index=[row_mark])
        df = df.reset_index(drop=True)
        df['type'] = ''
        # print(df)
        if 4 not in df.columns:
            df[4] = None
        if 5 not in df.columns:
            df[5] = None
        # print(df)
        for i in range(df.shape[0]):
            if df.iloc[i][4] is None:
                df.at[i, 4] = ''
            if df.iloc[i][5] is None:
                df.at[i, 5] = ''
            df.at[i, 'type'] = df.iloc[i][4] + df.iloc[i][5]
        # print(df)
        df[2] = df[2].astype(int)
        df[3] = df[3].astype(int)
        return df

    def extract(self, df):
        # print(df.groupby('type').apply(lambda x: x == 'CYTOPLASMIC.'))
        inside = df[[2, 3]].loc[df['type'].isin(['CYTOPLASMIC.'])].values.tolist()
        tms = df[[2, 3]].loc[df[1].isin(['TRANSMEM'])].values.tolist()
        outside = df[[2, 3]].loc[df['type'].isin(['NONCYTOPLASMIC.'])].values.tolist()
        signal = df[[2, 3]].loc[df[1].isin(['SIGNAL'])].values.tolist()
        cregion = df[[2, 3]].loc[df['type'].isin(['C-REGION.'])].values.tolist()
        hregion = df[[2, 3]].loc[df['type'].isin(['H-REGION.'])].values.tolist()
        nregion = df[[2, 3]].loc[df['type'].isin(['N-REGION.'])].values.tolist()
        # print(inside)
        # print(tms)
        # print(outside)
        cytoplasmic = self.separate(inside)
        transmembrane = self.separate(tms)
        extracellular = self.separate(outside)
        signal = self.separate(signal)
        cregion = self.separate(cregion)
        hregion = self.separate(hregion)
        nregion = self.separate(nregion)
        phobius_dict = {
            'cyto_lower': cytoplasmic[0],
            'cyto_upper': cytoplasmic[1],
            'tmh_lower': transmembrane[0],
            'tmh_upper': transmembrane[1],
            'extra_lower': extracellular[0],
            'extra_upper': extracellular[1],
            'signal_lower': signal[0],
            'signal_upper': signal[1],
            'cregion_lower': cregion[0],
            'cregion_upper': cregion[1],
            'hregion_lower': hregion[0],
            'hregion_upper': hregion[1],
            'nregion_lower': nregion[0],
            'nregion_upper': nregion[1],
        }
        return phobius_dict

    def separate(self, arr):
        lower = []
        upper = []
        for i in arr:
            lower.append(i[0])
            upper.append(i[1])
        return lower, upper