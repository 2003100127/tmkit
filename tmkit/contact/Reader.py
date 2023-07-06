__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import numpy as np
import pandas as pd
from tmkit.util.Kit import tactic1
from tmkit.util.Reader import reader as greader
from tmkit.position.scenario.Separation import separation as ppssep


class reader:

    def __init__(self, seq_sep_inferior=None, seq_sep_superior=None):
        self.__sort_ = -1
        self.seq_sep_inferior = seq_sep_inferior
        self.seq_sep_superior = seq_sep_superior
        self.greader = greader()

    @property
    def sort_(self):
        return self.__sort_

    @sort_.setter
    def sort_(self, value):
        print('Please note that you are attempting externally.')
        if value > 7 or value < 0:
            raise ValueError(
                '`sort_` has yet to reach there.',
                '| 1: return results for entire-chain residue contacts.',
                '| 2: return results of residue contacts by given pairs of interest.',
                '| 3: return sorted results by `score`',
                '| 4: return sorted results by `contact_id_1` and `contact_id_2`',
                '| 5: return dict results of a predictor',
                '| 6: return results of a residue of a predictor',
                '| 7: return cumulative dict results of a predictor',
                '| else: return raw results of a predictor',
                '| beyond: you need to choose one of opts above.',
            )
        else:
            self.__sort_ = value

    def sort_1(self, recombine, dist_df):
        dists_ = dist_df
        recombine_ = recombine
        len_recombine_ = recombine_.shape[0]
        dists_['fasta_id_1'] = dists_['fasta_id_1'].astype(int)
        dists_['fasta_id_2'] = dists_['fasta_id_2'].astype(int)
        dists__ = pd.DataFrame()
        dists__[0] = dists_['fasta_id_1']
        dists__[1] = dists_['fasta_id_2']
        dists__[2] = dists_.index.values
        dist_dict = self.todict(dists__)
        dist_ids = []
        for i in range(len_recombine_):
            id_1 = recombine_['contact_id_1'][i]
            id_2 = recombine_['contact_id_2'][i]
            # print(id_1, id_2)
            # ### /* block 3.2 */ ###
            dist_id = dist_dict[id_1][id_2]
            dist_ids.append(dist_id)
        recombine_dist = dists_.iloc[dist_ids]
        recombine_dist.columns = [
            'fasta_id_1',
            'aa_1',
            'pdb_id_1',
            'fasta_id_2',
            'aa_2',
            'pdb_id_2',
            'dist',
            'is_contact'
        ]
        recombine_dist = recombine_dist.reset_index(inplace=False, drop=True)
        return recombine_, recombine_dist

    def sort_2(self, recombine, dist_df, pair_df):
        # #/*** block 1 ***/
        predicts_ = recombine
        dists_ = dist_df
        pair_df_ = pair_df
        pair_df_[2] = 0
        # print(pair_df_)
        # #/*** block 2 ***/
        # #/*** block 2.1 ***/
        predicts__ = pd.DataFrame()
        predicts__[0] = predicts_['contact_id_1']
        predicts__[1] = predicts_['contact_id_2']
        predicts__[2] = predicts_.index.values
        predict_dict = self.todict(predicts__)
        # print(predict_dict)
        # #/*** block 2.2 ***/
        dists__ = pd.DataFrame()
        dists__[0] = dists_['fasta_id_1']
        dists__[1] = dists_['fasta_id_2']
        dists__[2] = dists_.index.values
        dist_dict = self.todict(dists__)
        # print(dist_dict)
        # #/*** block 3 ***/
        pred_ids = []
        dist_ids = []
        len_pairs = pair_df_.shape[0]
        for i in range(len_pairs):
            id_1 = pair_df_[0][i]
            id_2 = pair_df_[1][i]
            try:
                # #/*** block 3.1 ***/
                pred_id = predict_dict[id_1][id_2]
                pred_ids.append(pred_id)
                # #/*** block 3.2 ***/
                dist_id = dist_dict[id_1][id_2]
                dist_ids.append(dist_id)
            except KeyError:
                continue
        # #/*** block 4 ***/
        recombine_pred = predicts_.iloc[pred_ids]
        recombine_pred.columns = [
            'contact_id_1',
            'contact_id_2',
            'score'
        ]
        recombine_pred = recombine_pred.reset_index(inplace=False, drop=True)
        # #/*** block 5 ***/
        recombine_dist = dists_.iloc[dist_ids]
        recombine_dist.columns = [
            'fasta_id_1',
            'aa_1',
            'pdb_id_1',
            'fasta_id_2',
            'aa_2',
            'pdb_id_2',
            'dist',
            'is_contact',
        ]
        recombine_dist = recombine_dist.reset_index(inplace=False, drop=True)
        return recombine_pred, recombine_dist

    def sort_3(self, recombine, is_sort=False, is_uniform=False, uniform_df=None, indicator=0):
        """
        ..  @description:
            -------------
            select data by specifying seq_sep_inferior and seq_sep_superior.
            The select data can be sorted by two ways:
            1.  'score'
            2.  'contact_id_1' and 'contact_id_2'

        :param recombine: results of a predictor
        :param is_sort: False
        :return:
        """
        recombine_ = recombine
        # print(recombine_)
        # # /*** block 1 ***/
        if is_uniform:
            predict_dict = self.todict(recombine_)
            uniform_df[2] = indicator
            # print(uniform_df)
            uniform_list = uniform_df.values.tolist()
            uniform_shape = len(uniform_list)
            for i in range(uniform_shape):
                id_1 = uniform_list[i][0]
                id_2 = uniform_list[i][1]
                try:
                    uniform_list[i][2] = predict_dict[id_1][id_2]
                except KeyError:
                    continue
            recombine_ = pd.DataFrame(uniform_list)
            recombine_.columns = [
                'contact_id_1',
                'contact_id_2',
                'score'
            ]
            # print(recombine_)
            # self.pfwwriter.generic(recombine_, sv_fpn='./cheer')
        # # /*** block 2 ***/
        recombine_ = ppssep(
            df=recombine_,
            first='contact_id_1',
            second='contact_id_2',
            target='score',
            seq_sep_inferior=self.seq_sep_inferior,
            seq_sep_superior=self.seq_sep_superior,
            is_sort=is_sort
        ).extract()
        return recombine_

    def todict(self, recombine):
        arr_2d = recombine.values.tolist()
        # print(arr_2d)
        dicts = tactic1(arr_2d)
        return dicts

    def mi(self, mi_path, file_name, file_chain, dist_df=None, pair_list=None, sort_=0, is_sort=False):
        self.__sort_ = sort_
        results = self.greader.generic(
            mi_path + file_name + file_chain + '.evfold',
            df_sep='\s+',
            is_utf8=True
        )
        results.columns = [
            'contact_id_1',
            'aa_1',
            'contact_id_2',
            'aa_2',
            'score',
            'FC_score'
        ]
        recombine = results[[
            'contact_id_1',
            'contact_id_2',
            'score'
        ]]
        if self.__sort_ == 1:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            recombine = self.sort_3(
                recombine,
                is_sort=is_sort,
                is_uniform=True,
                uniform_df=pair_df
            )
            dist_mi, dist_true = self.sort_1(recombine, dist_df)
            return dist_mi, dist_true
        elif self.__sort_ == 2:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            recombine = self.sort_3(
                recombine,
                is_sort=is_sort,
                is_uniform=True,
                uniform_df=pair_df
            )
            dist_mi, dist_true = self.sort_2(recombine, dist_df, pair_df)
            # dist_mi.to_csv('3rvy_helices.txt', sep='\t', header=None, index=False)
            # print(len(dist_mi), len(dist_true))
            return dist_mi, dist_true
        else:
            return recombine

    def psicov(self, pcv_path, file_name, file_chain, dist_df=None, pair_list=None, sort_=0, is_sort=False):
        """
        ..  @description:
            -------------
            psicov result not only sorted by seq_sep>4 but also
            eliminate tiny score.

        :param pcv_path:
        :param file_name:
        :param file_chain:
        :param xml_path:
        :param dist_path:
        :param sort_:
        :param is_sort:
        :return:
        """
        self.__sort_ = sort_
        results = self.greader.generic(
            pcv_path + file_name + file_chain + '.psicov',
            df_sep='\s+',
            is_utf8=True
        )
        results.columns = [
            'contact_id_1',
            'contact_id_2',
            'dist_inf',
            'dist_sup',
            'score'
        ]
        recombine = results[[
            'contact_id_1',
            'contact_id_2',
            'score'
        ]]
        if self.__sort_ == 1:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            recombine = self.sort_3(
                recombine,
                is_sort=is_sort,
                is_uniform=True,
                uniform_df=pair_df
            )
            dist_pcv, dist_true = self.sort_1(recombine, dist_df)
            return dist_pcv, dist_true
        elif self.__sort_ == 2:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            recombine = self.sort_3(
                recombine,
                is_sort=is_sort,
                is_uniform=True,
                uniform_df=pair_df
            )
            dist_pcv, dist_true = self.sort_2(recombine, dist_df, pair_df)
            # dist_pcv.to_csv('3rvy_helices.txt', sep='\t', header=None, index=False)
            # print(len(dist_pcv), len(dist_true))
            return dist_pcv, dist_true
        else:
            return recombine

    def freecontact(self, fc_path, file_name, file_chain, dist_df=None, pair_list=None, sort_=0, is_sort=False):
        self.__sort_ = sort_
        results = self.greader.generic(
            fc_path + file_name + file_chain + '.evfold',
            df_sep='\s+',
            is_utf8=True
        )
        results.columns = [
            'contact_id_1',
            'aa_1',
            'contact_id_2',
            'aa_2',
            'MI_score',
            'score'
        ]
        recombine = results[[
            'contact_id_1',
            'contact_id_2',
            'score'
        ]]
        if self.__sort_ == 1:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            recombine = self.sort_3(
                recombine,
                is_sort=is_sort,
                is_uniform=True,
                uniform_df=pair_df
            )
            dist_fc, dist_true = self.sort_1(recombine, dist_df)
            return dist_fc, dist_true
        elif self.__sort_ == 2:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            recombine = self.sort_3(
                recombine,
                is_sort=is_sort,
                is_uniform=True,
                uniform_df=pair_df
            )
            dist_fc, dist_true = self.sort_2(recombine, dist_df, pair_df)
            # dist_fc.to_csv('3rvy_helices.txt', sep='\t', header=None, index=False)
            # print(len(dist_fc), len(dist_true))
            return dist_fc, dist_true
        else:
            return recombine

    def ccmpred(self, cp_path, file_name, file_chain, dist_df=None, pair_list=None, sort_=0, is_sort=False):
        self.__sort_ = sort_
        file_results = self.greader.generic(
            cp_path + file_name + file_chain + '.ccmpred',
            df_sep='\s+',
            is_utf8=True
        )
        results = []
        for i, row in file_results.iterrows():
            for j in range(file_results.shape[1]):
                if i < j:
                    # print(i+1, j+1, row[j])
                    results.append([i+1, j+1, row[j]])
        results = pd.DataFrame(results)
        results.columns = [
            'contact_id_1',
            'contact_id_2',
            'score'
        ]
        recombine = results[[
            'contact_id_1',
            'contact_id_2',
            'score'
        ]]
        if self.__sort_ == 1:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            recombine = self.sort_3(
                recombine,
                is_sort=is_sort,
                is_uniform=True,
                uniform_df=pair_df
            )
            dist_cp, dist_true = self.sort_1(recombine, dist_df)
            return dist_cp, dist_true
        elif self.__sort_ == 2:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            print(recombine.shape)
            recombine = self.sort_3(recombine, is_sort=is_sort)
            print(recombine.shape)
            dist_cp, dist_true = self.sort_2(recombine, dist_df, pair_df)
            # dist_cp.to_csv('3rvy_helices.txt', sep='\t', header=None, index=False)
            # print(len(dist_cp), len(dist_true))
            return dist_cp, dist_true
        else:
            return recombine

    def gremlin(self, gl_path, file_name, file_chain, dist_df=None, pair_list=None, sort_=0, is_sort=False):
        self.__sort_ = sort_
        results = self.greader.generic(
            gl_path + file_name + file_chain + '.gremlin',
            df_sep='\s+',
            header=0,
            is_utf8=True
        )
        results.columns = [
            'contact_id_1',
            'contact_id_2',
            'aa_1',
            'aa_2',
            'r_sco',
            's_sco',
            'score'
        ]
        recombine = results[[
            'contact_id_1',
            'contact_id_2',
            'score'
        ]]
        # print(recombine)
        # print(recombine.dtypes)
        if self.__sort_ == 1:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            recombine = self.sort_3(
                recombine,
                is_sort=is_sort,
                is_uniform=True,
                uniform_df=pair_df
            )
            dist_gl, dist_true = self.sort_1(recombine, dist_df)
            return dist_gl, dist_true
        elif self.__sort_ == 2:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            recombine = self.sort_3(
                recombine,
                is_sort=is_sort,
                is_uniform=True,
                uniform_df=pair_df
            )
            dist_gl, dist_true = self.sort_2(recombine, dist_df, pair_df)
            # dist_gl.to_csv('3rvy_helices.txt', sep='\t', header=None, index=False)
            # print(len(dist_gl), len(dist_true))
            return dist_gl, dist_true
        else:
            return recombine

    def gdca(self, gdca_path, file_name, file_chain, dist_df=None, pair_list=None, sort_=0, is_sort=False):
        self.__sort_ = sort_
        results = self.greader.generic(
            gdca_path + file_name + file_chain + '.gdca',
            df_sep='\s+',
            is_utf8=True
        )
        results.columns = [
            'contact_id_1',
            'contact_id_2',
            'score'
        ]
        recombine = results[[
            'contact_id_1',
            'contact_id_2',
            'score'
        ]]
        if self.__sort_ == 1:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            recombine = self.sort_3(
                recombine,
                is_sort=is_sort,
                is_uniform=True,
                uniform_df=pair_df
            )
            dist_gdca, dist_true = self.sort_1(recombine, dist_df)
            return dist_gdca, dist_true
        elif self.__sort_ == 2:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            recombine = self.sort_3(
                recombine,
                is_sort=is_sort,
                is_uniform=True,
                uniform_df=pair_df
            )
            dist_gdca, dist_true = self.sort_2(recombine, dist_df, pair_df)
            # dist_gdca.to_csv('3rvy_helices.txt', sep='\t', header=None, index=False)
            # print(len(dist_gdca), len(dist_true))
            return dist_gdca, dist_true
        else:
            return recombine

    def plmc(self, plmc_path, file_name, file_chain, dist_df=None, pair_list=None, sort_=0, is_sort=False):
        self.__sort_ = sort_
        results = self.greader.generic(
            plmc_path + file_name + file_chain + '.plmc',
            df_sep='\s+',
            is_utf8=True
        )
        results.columns = [
            'contact_id_1',
            'aa_1',
            'contact_id_2',
            'aa_2',
            'placeholder',
            'score'
        ]
        recombine = results[[
            'contact_id_1',
            'contact_id_2',
            'score'
        ]]
        if self.__sort_ == 1:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            recombine = self.sort_3(
                recombine,
                is_sort=is_sort,
                is_uniform=True,
                uniform_df=pair_df
            )
            dist_plmc, dist_true = self.sort_1(recombine, dist_df)
            return dist_plmc, dist_true
        elif self.__sort_ == 2:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            recombine = self.sort_3(
                recombine,
                is_sort=is_sort,
                is_uniform=True,
                uniform_df=pair_df
            )
            dist_plmc, dist_true = self.sort_2(recombine, dist_df, pair_df)
            # dist_plmc.to_csv('3rvy_helices.txt', sep='\t', header=None, index=False)
            # print(len(dist_plmc), len(dist_true))
            return dist_plmc, dist_true
        else:
            return recombine

    def memconp(self, mcp_path, file_name, file_chain, dist_df=None, pair_list=None, sort_=0, is_sort=False):
        self.__sort_ = sort_
        file_path = mcp_path + file_name + file_chain + '.memconp'
        with open(file_path) as file:
            surface = [[str(digit) for digit in line.split()] for line in file]
            memconp = pd.DataFrame(surface)
            # print(memconp)
        row_mark = memconp.loc[(memconp[0] == 'RESTHRESH')].index[0]
        results = memconp.drop(index=np.arange(row_mark + 1))
        new_index = np.arange(results.shape[0])
        results = results.set_index(new_index, inplace=False, drop=True)
        results.columns = [
            'Mark',
            'contact_id_1',
            'contact_id_2',
            'score',
            'isContact',
            'ph1',
            'ph2'
        ]
        results['contact_id_1'] = results['contact_id_1'].astype(int)
        results['contact_id_2'] = results['contact_id_2'].astype(int)
        results['score'] = results['score'].astype(np.float64)
        # print(results.dtypes)
        recombine = results[[
            'contact_id_1',
            'contact_id_2',
            'score',
        ]]
        # print(recombine.dtypes)
        if self.__sort_ == 1:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            recombine = self.sort_3(
                recombine,
                is_sort=is_sort,
                is_uniform=True,
                uniform_df=pair_df
            )
            dist_mcp, dist_true = self.sort_1(recombine, dist_df)
            return dist_mcp, dist_true
        elif self.__sort_ == 2:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            recombine = self.sort_3(
                recombine,
                is_sort=is_sort,
                is_uniform=True,
                uniform_df=pair_df
            )
            dist_mcp, dist_true = self.sort_2(recombine, dist_df, pair_df)
            # dist_mcp.to_csv('3rvy_helices.txt', sep='\t', header=None, index=False)
            # print(len(dist_mcp), len(dist_true))
            return dist_mcp, dist_true
        else:
            return recombine

    def membrain2(self, mb_path, file_name, file_chain, dist_df=None, pair_list=None, sort_=0, is_sort=False):
        self.__sort_ = sort_
        # new_file = re.sub(r'Query(.+?)\)', "", str(results), flags=re.S)
        file_path = mb_path + file_name + file_chain + '.membrain2'
        with open(file_path) as file:
            surface = [[str(digit) for digit in line.split()] for line in file]
            membrain2 = pd.DataFrame(surface)
        row_mark = membrain2.loc[(membrain2[2] == 'contacts:')].index[0]
        results = membrain2.drop(index=np.arange(row_mark + 1))
        new_index = np.arange(results.shape[0])
        results = results.set_index(new_index, inplace=False, drop=True)
        results.columns = [
            'No',
            'TMH1',
            'contact_id_1',
            'aa_1',
            'TMH2',
            'contact_id_2',
            'aa_2',
            'score'
        ]
        results['contact_id_1'] = results['contact_id_1'].astype(int)
        results['contact_id_2'] = results['contact_id_2'].astype(int)
        results['score'] = results['score'].astype(np.float64)
        # print(results.dtypes)
        recombine = results[[
            'contact_id_1',
            'contact_id_2',
            'score'
        ]]
        if self.__sort_ == 1:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            recombine = self.sort_3(
                recombine,
                is_sort=is_sort,
                is_uniform=True,
                uniform_df=pair_df
            )
            dist_mb, dist_true = self.sort_1(recombine, dist_df)
            return dist_mb, dist_true
        elif self.__sort_ == 2:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            recombine = self.sort_3(
                recombine,
                is_sort=is_sort,
                is_uniform=True,
                uniform_df=pair_df
            )
            dist_mb, dist_true = self.sort_2(recombine, dist_df, pair_df)
            # dist_mb.to_csv('3rvy_helices.txt', sep='\t', header=None, index=False)
            # print(len(dist_mb), len(dist_true))
            return dist_mb, dist_true
        else:
            return recombine

    def deephelicon(self, deephelicon_path, file_name, file_chain, dist_df=None, pair_list=None, sort_=0, is_sort=False):
        self.__sort_ = sort_
        results = self.greader.generic(
            deephelicon_path + file_name + file_chain + '.tma165',
            df_sep='\t',
            is_utf8=True
        )
        results.columns = [
            'contact_id_1',
            'aa_1',
            'contact_id_2',
            'aa_2',
            'score'
        ]
        recombine = results[[
            'contact_id_1',
            'contact_id_2',
            'score'
        ]]
        if self.__sort_ == 1:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            recombine = self.sort_3(
                recombine,
                is_sort=is_sort,
                is_uniform=True,
                uniform_df=pair_df
            )
            dist_tma165, dist_true = self.sort_1(recombine, dist_df)
            return dist_tma165, dist_true
        elif self.__sort_ == 2:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            recombine = self.sort_3(
                recombine,
                is_sort=is_sort,
                # is_uniform=True,
                # uniform_df=pair_df
            )
            dist_tma165, dist_true = self.sort_2(recombine, dist_df, pair_df)
            return dist_tma165, dist_true
        else:
            return recombine