__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import subprocess
import numpy as np
import pandas as pd
from tmkit.util.Kit import chainid
from tmkit.util.Kit import tactic5, tactic6


class helixSurface:

    def __init__(
            self,
            msa_path=None,
            lips_fpn=None,
            prot_name=None,
            file_chain=None,
            sv_fp=None,
            df_prot=None,
    ):
        self.msa_path = msa_path
        self.lips_fpn = lips_fpn
        self.sv_fp = sv_fp
        self.df_prot = df_prot
        self.prot_name = prot_name
        self.file_chain = file_chain

    def generate(self):
        """"""
        msa_fpn = self.msa_path + self.prot_name + self.file_chain + '.aln'
        sv_fpn = self.sv_fp + self.prot_name + self.file_chain + '/'
        self.surf = subprocess.call([
            'perl',
            self.lips_fpn,
            msa_fpn,
            sv_fpn,
        ], shell=True)
        return 0

    def bgenerate(self):
        """"""
        for i, prot_name in enumerate(self.df_prot['prot']):
            prot_chain = self.df_prot['chain'][i]
            file_chain = chainid(prot_chain)
            print('=========>No.{} protein {}'.format(i, prot_name + file_chain))
            self.msa_fpn = self.msa_path + prot_name + file_chain + '.aln'
            sv_fpn = self.sv_fp + prot_name + file_chain + '/'
            self.surf = subprocess.call([
                'perl',
                self.lips_fpn,
                self.msa_fpn,
                sv_fpn,
            ], shell=True)
        return 0

    def surface(self, i):
        surf_fpn = self.sv_fp + self.prot_name + self.file_chain + '/' + str(i) + '.txt'
        with open(surf_fpn) as f:
            surf_x = [[str(digit) for digit in line.split()] for line in f]
            surf_x = pd.DataFrame(
                surf_x,
                columns=[
                    'aa_ids',
                    'aa_names',
                    'lipos',
                    'ents',
                ],
            )
            surf_x['aa_ids'] = surf_x['aa_ids'].apply(int)
            surf_x['lipos'] = surf_x['lipos'].apply(float)
            surf_x['ents'] = surf_x['ents'].apply(float)
            surf_x['surf'] = int(i)
        return surf_x

    def transformToRosseta(self, df_surf_lips):
        d = []
        for i in df_surf_lips.index:
            o = df_surf_lips['surfs'][i]
            b = self.surface(o)
            print('======>reading surface {}'.format(o))
            b['mean_lipo']= df_surf_lips.loc[o]['lxe']
            b = b[[
                'aa_ids',
                'mean_lipo',
                'lipos',
                'ents',
            ]]
            d.append(b)
        return pd.concat(d, axis=0).reset_index(drop=True)

    def lips(self):
        lips_fpn = self.sv_fp + self.prot_name + self.file_chain + '/LIPS.txt'
        with open(lips_fpn) as f:
            lips_ = [[digit for digit in line.split()] for line in f]
            lips_surf = pd.DataFrame(
                lips_,
                columns=[
                    'surfs',
                    'lipos',
                    'ents',
                    'lxe'
                ]
            )
            lips_surf['surfs'] = lips_surf['surfs'].apply(int)
            lips_surf['lipos'] = lips_surf['lipos'].apply(float)
            lips_surf['ents'] = lips_surf['ents'].apply(float)
            lips_surf['lxe'] = lips_surf['lxe'].apply(float)
        return lips_surf

    def read(self):
        surfs = pd.DataFrame()
        surf_lipos = pd.DataFrame()
        surf_ents = pd.DataFrame()
        for i in range(7):
            # print(self.surface(i)['lipos'].mean()*2)
            # print(self.surface(i)['ents'].mean())
            surfs = pd.concat([surfs, self.surface(i)[['aa_ids', 'surf']]], axis=0)
            surfs = surfs.reset_index(drop=True)
            surf_lipos = pd.concat([surf_lipos, self.surface(i)[['aa_ids', 'lipos']]], axis=0)
            surf_lipos = surf_lipos.reset_index(drop=True)
            surf_ents = pd.concat([surf_ents, self.surface(i)[['aa_ids', 'ents']]], axis=0)
            surf_ents = surf_ents.reset_index(drop=True)
        surfs_dict = tactic5(surfs.values.tolist())
        lipos_dict = tactic6(surf_lipos.values.tolist())
        entropy_dict = tactic6(surf_ents.values.tolist())
        lips_dict = tactic6(self.lips().values.tolist())
        aa_surf_rank = {}
        for k, v in surfs_dict.items():
            compare = []
            for s in v:
                compare.append(lips_dict[s][2])
            aa_surf_rank[k] = v[np.argmax(compare)]
            # print(compare)
            # print(np.argmax(compare))
            # print(v[np.argmax(compare)])
        return aa_surf_rank, lipos_dict, entropy_dict, lips_dict

    def boolean(self, aa_surf_rank, key):
        bool_ = np.zeros(7)
        bool_[aa_surf_rank[key]] = 1
        return bool_

    def boolean_(self, list_2d, window_aa_ids, aa_surf_rank):
        list_2d_ = list_2d
        for i, aa_win_ids in enumerate(window_aa_ids):
            for j in aa_win_ids:
                if j is None:
                    for k in range(7):
                        list_2d_[i].append(0)
                else:
                    r = aa_surf_rank[j]
                    bool_ = [0] * 7
                    bool_[r] = 1
                    for k in range(7):
                        list_2d_[i].append(bool_[k])
        return list_2d_

    def lipos_(self, list_2d, window_aa_ids, lipos_dict):
        list_2d_ = list_2d
        for i, aa_win_ids in enumerate(window_aa_ids):
            for j in aa_win_ids:
                if j is None:
                    list_2d_[i].append(0)
                else:
                    list_2d_[i].append(lipos_dict[j])
        return list_2d_

    def entropy_(self, list_2d, window_aa_ids, entropy_dict):
        list_2d_ = list_2d
        for i, aa_win_ids in enumerate(window_aa_ids):
            for j in aa_win_ids:
                if j is None:
                    list_2d_[i].append(0)
                else:
                    list_2d_[i].append(entropy_dict[j])
        return list_2d_

    def avlipos_(self, list_2d, window_aa_ids, aa_surf_rank, lips_dict):
        list_2d_ = list_2d
        for i, aa_win_ids in enumerate(window_aa_ids):
            for j in aa_win_ids:
                if j is None:
                    list_2d_[i].append(0)
                else:
                    r = aa_surf_rank[j]
                    list_2d_[i].append(lips_dict[r][0])
        return list_2d_

    def aventropy_(self, list_2d, window_aa_ids, aa_surf_rank, lips_dict):
        list_2d_ = list_2d
        for i, aa_win_ids in enumerate(window_aa_ids):
            for j in aa_win_ids:
                if j is None:
                    list_2d_[i].append(0)
                else:
                    r = aa_surf_rank[j]
                    list_2d_[i].append(lips_dict[r][1])
        return list_2d_

    def avlips_(self, list_2d, window_aa_ids, aa_surf_rank, lips_dict):
        list_2d_ = list_2d
        for i, aa_win_ids in enumerate(window_aa_ids):
            for j in aa_win_ids:
                if j is None:
                    list_2d_[i].append(0)
                else:
                    r = aa_surf_rank[j]
                    list_2d_[i].append(lips_dict[r][2])
        return list_2d_