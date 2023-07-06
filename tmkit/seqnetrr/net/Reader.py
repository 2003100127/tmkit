__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import numpy as np
import pandas as pd

from tmkit.seqnetrr.combo.Separation import Separation as ppssep
from tmkit.seqnetrr.ComputLib import ComputLib
from tmkit.util.Reader import Reader as pfrreader
from tmkit.util.Writer import Writer as pfwwriter


class Reader:
    def __init__(self, seq_sep_inferior=None, seq_sep_superior=None):
        self.__sort_ = -1
        self.seq_sep_inferior = seq_sep_inferior
        self.seq_sep_superior = seq_sep_superior
        self.pfrreader = pfrreader()
        self.pfwwriter = pfwwriter()
        self.computlib = ComputLib()

    @property
    def sort_(self):
        return self.__sort_

    @sort_.setter
    def sort_(self, value):
        print("Please note that you are attempting externally.")
        if value > 7 or value < 0:
            raise ValueError(
                "`sort_` has yet to reach there.",
                "| 1: return results for entire-chain residue contacts.",
                "| 2: return results of residue contacts by given pairs of interest.",
                "| 3: return sorted results by `score`",
                "| 4: return sorted results by `id_1` and `id_2`",
                "| 5: return dict results of a predictor",
                "| 6: return results of a residue of a predictor",
                "| 7: return cumulative dict results of a predictor",
                "| else: return raw results of a predictor",
                "| beyond: you need to choose one of opts above.",
            )
        else:
            self.__sort_ = value

    def sort_1(self, recombine, dist_df):
        """
        ..  @description
            ------------
            block 1
                |--- block 1.1  return results greater than seq_sep_inferior
                                but smaller than seq_sep_superior
                |--- block 1.2  return results greater than seq_sep_inferior
                |--- block 1.3  return results smaller than seq_sep_superior
                |--- block 1.4  return all results of the predictor

        :param recombine:
        :param dist_df: a df of distances of residue pairs
        :param is_sort: False or True
        :return:
        """
        dists_ = dist_df
        recombine_ = recombine
        len_recombine_ = recombine_.shape[0]
        dists_["fasta_id_1"] = dists_["fasta_id_1"].astype(np.int)
        dists_["fasta_id_2"] = dists_["fasta_id_2"].astype(np.int)
        dists__ = pd.DataFrame()
        dists__[0] = dists_["fasta_id_1"]
        dists__[1] = dists_["fasta_id_2"]
        dists__[2] = dists_.index.values
        dist_dict = self.todict(dists__)
        dist_ids = []
        for i in range(len_recombine_):
            id_1 = recombine_["id_1"][i]
            id_2 = recombine_["id_2"][i]
            # print(id_1, id_2)
            # ### /* block 3.2 */ ###
            dist_id = dist_dict[id_1][id_2]
            dist_ids.append(dist_id)
        recombine_dist = dists_.iloc[dist_ids]
        recombine_dist.columns = [
            "fasta_id_1",
            "aa_1",
            "pdb_id_1",
            "fasta_id_2",
            "aa_2",
            "pdb_id_2",
            "dist",
            "is_contact",
        ]
        recombine_dist = recombine_dist.reset_index(inplace=False, drop=True)
        return recombine_, recombine_dist

    def sort_2(self, recombine, dist_df, pair_df):
        """
        ..  @description
            ------------
            overview:
                                    ---> tool in fasta id (juery)
                                    |
                                    |
                                    |
            pdb id -> fasta id   ---|---> tmh in fasta id (final purpose)
                                    |
                                    |
                                    |
                                    ---> dist in fasta id (juery)
            block 1.    clear variables
            block 2.
                |---> block 2.1  predict dictionary
                |---> block 2.2  distance dictionary
            block 3.
                |---> block 3.1  find dist ids
                |---> block 3.2  find predict ids
            block 4.    query predict ids
            block 5.    query dist ids
            return:
            recombine of predictor in thm, recombine of distance in thm

        :param recombine: a df
        :param dist_df: a df
        :param pair_df: a df of pairs
        :return: two dfs
        """
        # #/*** block 1 ***/
        predicts_ = recombine
        dists_ = dist_df
        pair_df_ = pair_df
        pair_df_[2] = 0
        # print(pair_df_)
        # #/*** block 2 ***/
        # #/*** block 2.1 ***/
        predicts__ = pd.DataFrame()
        predicts__[0] = predicts_["id_1"]
        predicts__[1] = predicts_["id_2"]
        predicts__[2] = predicts_.index.values
        predict_dict = self.todict(predicts__)
        # print(predict_dict)
        # #/*** block 2.2 ***/
        dists__ = pd.DataFrame()
        dists__[0] = dists_["fasta_id_1"]
        dists__[1] = dists_["fasta_id_2"]
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
        recombine_pred.columns = ["id_1", "id_2", "score"]
        recombine_pred = recombine_pred.reset_index(inplace=False, drop=True)
        # #/*** block 5 ***/
        recombine_dist = dists_.iloc[dist_ids]
        recombine_dist.columns = [
            "fasta_id_1",
            "aa_1",
            "pdb_id_1",
            "fasta_id_2",
            "aa_2",
            "pdb_id_2",
            "dist",
            "is_contact",
        ]
        recombine_dist = recombine_dist.reset_index(inplace=False, drop=True)
        return recombine_pred, recombine_dist

    def sort_3(
        self, recombine, is_sort=False, is_uniform=False, uniform_df=None, indicator=0
    ):
        """
        ..  @description:
            -------------
            select data by specifying seq_sep_inferior and seq_sep_superior.
            The select data can be sorted by two ways:
            1.  'score'
            2.  'id_1' and 'id_2'

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
            recombine_.columns = ["id_1", "id_2", "score"]
            # print(recombine_)
            # self.pfwwriter.generic(recombine_, sv_fpn='./cheer')
        # # /*** block 2 ***/
        recombine_ = ppssep(
            df=recombine_,
            first="id_1",
            second="id_2",
            target="score",
            seq_sep_inferior=self.seq_sep_inferior,
            seq_sep_superior=self.seq_sep_superior,
            is_sort=is_sort,
        ).extract()
        return recombine_

    def sort_6(self, recombine, id, L):
        recombine_ = recombine
        constraint_1 = recombine_["id_1"] == id
        query = constraint_1
        recombine_ = recombine_.loc[query]
        recombine_ = recombine_.sort_values(by=["score"], ascending=False).iloc[0:L, :]
        return recombine_

    def cumulative(self, recombine, L, len_seq):
        """
        ..  @summary:
            ---------
            sort_6 calculates cummulative eca values.

        :param recombine:
        :param num:
        :param L:
        :return:
        """
        recombine_ = recombine
        cumu_dict = dict()
        for i in range(len_seq):
            recombine_cumu = self.sort_6(recombine_, id=i + 1, L=L)
            cumu_dict[i + 1] = self.addition(recombine_cumu)
        return cumu_dict

    def addition(self, recombine):
        recombine_ = recombine
        cumu = recombine_["score"].sum()
        return cumu

    def todict(self, recombine):
        arr_2d = recombine.values.tolist()
        # print(arr_2d)
        dicts = self.computlib.tactic1(arr_2d)
        return dicts

    def mi(
        self,
        fpn,
        dist_df=None,
        pair_list=None,
        sort_=0,
        is_sort=False,
        id=0,
        L=50,
        len_seq=50,
    ):
        self.__sort_ = sort_
        results = self.pfrreader.generic(fpn, df_sep=r"\s+", is_utf8=True)
        results.columns = ["id_1", "aa_1", "id_2", "aa_2", "score", "FC_score"]
        recombine = results[["id_1", "id_2", "score"]]
        if self.__sort_ == 1:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            recombine = self.sort_3(
                recombine, is_sort=is_sort, is_uniform=True, uniform_df=pair_df
            )
            dist_mi, dist_true = self.sort_1(recombine, dist_df)
            return dist_mi, dist_true
        elif self.__sort_ == 2:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            recombine = self.sort_3(
                recombine, is_sort=is_sort, is_uniform=True, uniform_df=pair_df
            )
            dist_mi, dist_true = self.sort_2(recombine, dist_df, pair_df)
            # dist_mi.to_csv('3rvy_helices.txt', sep='\t', header=None, index=False)
            # print(len(dist_mi), len(dist_true))
            return dist_mi, dist_true
        elif self.__sort_ == 3:
            recombine = self.sort_3(recombine, is_sort=is_sort)
            return recombine
        elif self.__sort_ == 4:
            recombine = self.sort_3(recombine, is_sort=False)
            return recombine
        elif self.__sort_ == 5:
            recombine_dict = self.todict(recombine)
            return recombine_dict
        elif self.__sort_ == 6:
            recombine = self.sort_6(recombine, id=id, L=L)
            return recombine
        elif self.__sort_ == 7:
            cumu_dict = self.cumulative(recombine, L=L, len_seq=len_seq)
            return cumu_dict
        elif self.__sort_ == 8:
            pass
        else:
            return recombine

    def freecontact(
        self,
        fpn,
        dist_df=None,
        pair_list=None,
        sort_=0,
        is_sort=False,
        id=0,
        L=50,
        len_seq=50,
    ):
        self.__sort_ = sort_
        results = self.pfrreader.generic(fpn, df_sep=r"\s+", is_utf8=True)
        results.columns = ["id_1", "aa_1", "id_2", "aa_2", "MI_score", "score"]
        recombine = results[["id_1", "id_2", "score"]]
        if self.__sort_ == 1:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            recombine = self.sort_3(
                recombine, is_sort=is_sort, is_uniform=True, uniform_df=pair_df
            )
            dist_fc, dist_true = self.sort_1(recombine, dist_df)
            return dist_fc, dist_true
        elif self.__sort_ == 2:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            recombine = self.sort_3(
                recombine, is_sort=is_sort, is_uniform=True, uniform_df=pair_df
            )
            dist_fc, dist_true = self.sort_2(recombine, dist_df, pair_df)
            # dist_fc.to_csv('3rvy_helices.txt', sep='\t', header=None, index=False)
            # print(len(dist_fc), len(dist_true))
            return dist_fc, dist_true
        elif self.__sort_ == 3:
            recombine = self.sort_3(recombine, is_sort=is_sort)
            return recombine
        elif self.__sort_ == 4:
            recombine = self.sort_3(recombine, is_sort=False)
            return recombine
        elif self.__sort_ == 5:
            recombine_dict = self.todict(recombine)
            return recombine_dict
        elif self.__sort_ == 6:
            recombine = self.sort_6(recombine, id=id, L=L)
            return recombine
        elif self.__sort_ == 7:
            cumu_dict = self.cumulative(recombine, L=L, len_seq=len_seq)
            return cumu_dict
        elif self.__sort_ == 8:
            pass
        else:
            return recombine

    def ccmpred(
        self,
        fpn,
        dist_df=None,
        pair_list=None,
        sort_=0,
        is_sort=False,
        id=0,
        L=50,
        len_seq=50,
    ):
        self.__sort_ = sort_
        file_results = self.pfrreader.generic(fpn, df_sep=r"\s+", is_utf8=True)
        results = []
        for i, row in file_results.iterrows():
            for j in range(file_results.shape[1]):
                if i < j:
                    # print(i+1, j+1, row[j])
                    results.append([i + 1, j + 1, row[j]])
        results = pd.DataFrame(results)
        results.columns = ["id_1", "id_2", "score"]
        recombine = results[["id_1", "id_2", "score"]]
        if self.__sort_ == 1:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            recombine = self.sort_3(
                recombine, is_sort=is_sort, is_uniform=True, uniform_df=pair_df
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
        elif self.__sort_ == 3:
            recombine = self.sort_3(recombine, is_sort=is_sort)
            return recombine
        elif self.__sort_ == 4:
            recombine = self.sort_3(recombine, is_sort=False)
            return recombine
        elif self.__sort_ == 5:
            recombine_dict = self.todict(recombine)
            return recombine_dict
        elif self.__sort_ == 6:
            recombine = self.sort_6(recombine, id=id, L=L)
            return recombine
        elif self.__sort_ == 7:
            cumu_dict = self.cumulative(recombine, L=L, len_seq=len_seq)
            return cumu_dict
        elif self.__sort_ == 8:
            pass
        else:
            return recombine

    def gdca(
        self,
        fpn,
        dist_df=None,
        pair_list=None,
        sort_=0,
        is_sort=False,
        id=0,
        L=50,
        len_seq=50,
    ):
        self.__sort_ = sort_
        results = self.pfrreader.generic(fpn, df_sep=r"\s+", is_utf8=True)
        results.columns = ["id_1", "id_2", "score"]
        recombine = results[["id_1", "id_2", "score"]]
        if self.__sort_ == 1:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            recombine = self.sort_3(
                recombine, is_sort=is_sort, is_uniform=True, uniform_df=pair_df
            )
            dist_gdca, dist_true = self.sort_1(recombine, dist_df)
            return dist_gdca, dist_true
        elif self.__sort_ == 2:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            recombine = self.sort_3(
                recombine, is_sort=is_sort, is_uniform=True, uniform_df=pair_df
            )
            dist_gdca, dist_true = self.sort_2(recombine, dist_df, pair_df)
            # dist_gdca.to_csv('3rvy_helices.txt', sep='\t', header=None, index=False)
            # print(len(dist_gdca), len(dist_true))
            return dist_gdca, dist_true
        elif self.__sort_ == 3:
            recombine = self.sort_3(recombine, is_sort=is_sort)
            return recombine
        elif self.__sort_ == 4:
            recombine = self.sort_3(recombine, is_sort=False)
            return recombine
        elif self.__sort_ == 5:
            recombine_dict = self.todict(recombine)
            return recombine_dict
        elif self.__sort_ == 6:
            recombine = self.sort_6(recombine, id=id, L=L)
            return recombine
        elif self.__sort_ == 7:
            cumu_dict = self.cumulative(recombine, L=L, len_seq=len_seq)
            return cumu_dict
        elif self.__sort_ == 8:
            pass
        else:
            return recombine

    def plmc(
        self,
        fpn,
        dist_df=None,
        pair_list=None,
        sort_=0,
        is_sort=False,
        id=0,
        L=50,
        len_seq=50,
    ):
        self.__sort_ = sort_
        results = self.pfrreader.generic(fpn, df_sep=r"\s+", is_utf8=True)
        results.columns = ["id_1", "aa_1", "id_2", "aa_2", "placeholder", "score"]
        recombine = results[["id_1", "id_2", "score"]]
        if self.__sort_ == 1:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            recombine = self.sort_3(
                recombine, is_sort=is_sort, is_uniform=True, uniform_df=pair_df
            )
            dist_plmc, dist_true = self.sort_1(recombine, dist_df)
            return dist_plmc, dist_true
        elif self.__sort_ == 2:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            recombine = self.sort_3(
                recombine, is_sort=is_sort, is_uniform=True, uniform_df=pair_df
            )
            dist_plmc, dist_true = self.sort_2(recombine, dist_df, pair_df)
            # dist_plmc.to_csv('3rvy_helices.txt', sep='\t', header=None, index=False)
            # print(len(dist_plmc), len(dist_true))
            return dist_plmc, dist_true
        elif self.__sort_ == 3:
            recombine = self.sort_3(recombine, is_sort=is_sort)
            return recombine
        elif self.__sort_ == 4:
            recombine = self.sort_3(recombine, is_sort=False)
            return recombine
        elif self.__sort_ == 5:
            recombine_dict = self.todict(recombine)
            return recombine_dict
        elif self.__sort_ == 6:
            recombine = self.sort_6(recombine, id=id, L=L)
            return recombine
        elif self.__sort_ == 7:
            cumu_dict = self.cumulative(recombine, L=L, len_seq=len_seq)
            return cumu_dict
        elif self.__sort_ == 8:
            pass
        else:
            return recombine

    def general(
        self,
        fpn,
        dist_df=None,
        pair_list=None,
        sort_=0,
        is_sort=False,
        id=0,
        L=50,
        len_seq=50,
    ):
        self.__sort_ = sort_
        results = self.pfrreader.generic(fpn, df_sep=r"\s+", is_utf8=True)
        results.columns = ["id_1", "id_2", "score"]
        recombine = results[["id_1", "id_2", "score"]]
        if self.__sort_ == 1:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            recombine = self.sort_3(
                recombine, is_sort=is_sort, is_uniform=True, uniform_df=pair_df
            )
            dist_gdca, dist_true = self.sort_1(recombine, dist_df)
            return dist_gdca, dist_true
        elif self.__sort_ == 2:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            recombine = self.sort_3(
                recombine, is_sort=is_sort, is_uniform=True, uniform_df=pair_df
            )
            dist_gdca, dist_true = self.sort_2(recombine, dist_df, pair_df)
            # dist_gdca.to_csv('3rvy_helices.txt', sep='\t', header=None, index=False)
            # print(len(dist_gdca), len(dist_true))
            return dist_gdca, dist_true
        elif self.__sort_ == 3:
            recombine = self.sort_3(recombine, is_sort=is_sort)
            return recombine
        elif self.__sort_ == 4:
            recombine = self.sort_3(recombine, is_sort=False)
            return recombine
        elif self.__sort_ == 5:
            recombine_dict = self.todict(recombine)
            return recombine_dict
        elif self.__sort_ == 6:
            recombine = self.sort_6(recombine, id=id, L=L)
            return recombine
        elif self.__sort_ == 7:
            cumu_dict = self.cumulative(recombine, L=L, len_seq=len_seq)
            return cumu_dict
        elif self.__sort_ == 8:
            pass
        else:
            return recombine

    def simulate(
        self,
        fpn,
        dist_df=None,
        pair_list=None,
        sort_=0,
        is_sort=False,
        id=0,
        L=50,
        len_seq=50,
    ):
        self.__sort_ = sort_
        simu_seq_len = fpn
        results = pd.DataFrame(self.computlib.numTo3cols(length=simu_seq_len))
        print(results)
        results.columns = [
            "id_1",
            "id_2",
            "score",
        ]
        recombine = results[
            [
                "id_1",
                "id_2",
                "score",
            ]
        ]
        if self.__sort_ == 1:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            recombine = self.sort_3(
                recombine,
                is_sort=is_sort,
                is_uniform=True,
                uniform_df=pair_df,
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
                uniform_df=pair_df,
            )
            dist_fc, dist_true = self.sort_2(recombine, dist_df, pair_df)
            # dist_fc.to_csv('3rvy_helices.txt', sep='\t', header=None, index=False)
            # print(len(dist_fc), len(dist_true))
            return dist_fc, dist_true
        elif self.__sort_ == 3:
            recombine = self.sort_3(recombine, is_sort=is_sort)
            return recombine
        elif self.__sort_ == 4:
            recombine = self.sort_3(recombine, is_sort=False)
            return recombine
        elif self.__sort_ == 5:
            recombine_dict = self.todict(recombine)
            return recombine_dict
        elif self.__sort_ == 6:
            recombine = self.sort_6(recombine, id=id, L=L)
            return recombine
        elif self.__sort_ == 7:
            cumu_dict = self.cumulative(recombine, L=L, len_seq=len_seq)
            return cumu_dict
        elif self.__sort_ == 8:
            pass
        else:
            return recombine
