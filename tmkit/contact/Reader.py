__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import Dict, List, Optional, Tuple, Union

import numpy as np
import pandas as pd

from tmkit.position.scenario.Separation import Separation as ppssep
from tmkit.util.Kit import tactic1
from tmkit.util.Reader import Reader as greader


class Reader:
    def __init__(
        self,
        seq_sep_inferior: Optional[int] = None,
        seq_sep_superior: Optional[int] = None,
    ):
        """
        The reader class.

        Parameters
        ----------
        seq_sep_inferior : int, optional
            Lower limit of sequence separation, by default None
        seq_sep_superior : int, optional
            Upper limit of sequence separation, by default None
        """
        self.__sort_ = -1
        self.seq_sep_inferior = seq_sep_inferior
        self.seq_sep_superior = seq_sep_superior
        self.greader = greader()

    @property
    def sort_(self) -> int:
        """
        Property getter for sort_.

        Returns
        -------
        int
            sort_ value.
        """
        return self.__sort_

    @sort_.setter
    def sort_(self, value: int):
        """
        Property setter for sort_.

        Parameters
        ----------
        value : int
            Value to be set.

        Raises
        ------
        ValueError
            If the value is not within the allowed range [0,7]
        """
        print("Please note that you are attempting externally.")
        if value > 7 or value < 0:
            raise ValueError(
                "`sort_` has yet to reach there.",
                "| 1: return results for entire-chain residue contacts.",
                "| 2: return results of residue contacts by given pairs of interest.",
                "| 3: return sorted results by `score`",
                "| 4: return sorted results by `contact_id_1` and `contact_id_2`",
                "| 5: return dict results of a predictor",
                "| 6: return results of a residue of a predictor",
                "| 7: return cumulative dict results of a predictor",
                "| else: return raw results of a predictor",
                "| beyond: you need to choose one of opts above.",
            )
        else:
            self.__sort_ = value

    def sort_1(
        self, recombine: pd.DataFrame, dist_df: pd.DataFrame
    ) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
        Perform first sort operation.

        Parameters
        ----------
        recombine : pd.DataFrame
            The dataframe to recombine.
        dist_df : pd.DataFrame
            The distance dataframe.

        Returns
        -------
        Tuple[pd.DataFrame, pd.DataFrame]
            Tuple of resulting dataframes after sorting.
        """
        dists_ = dist_df
        recombine_ = recombine
        len_recombine_ = recombine_.shape[0]
        dists_["fasta_id_1"] = dists_["fasta_id_1"].astype(int)
        dists_["fasta_id_2"] = dists_["fasta_id_2"].astype(int)
        dists__ = pd.DataFrame()
        dists__[0] = dists_["fasta_id_1"]
        dists__[1] = dists_["fasta_id_2"]
        dists__[2] = dists_.index.values
        dist_dict = self.todict(dists__)
        dist_ids = []
        for i in range(len_recombine_):
            id_1 = recombine_["contact_id_1"][i]
            id_2 = recombine_["contact_id_2"][i]
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

    def sort_2(
        self, recombine: pd.DataFrame, dist_df: pd.DataFrame, pair_df: pd.DataFrame
    ) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
        Perform second sort operation.

        Parameters
        ----------
        recombine : pd.DataFrame
            The dataframe to recombine.
        dist_df : pd.DataFrame
            The distance dataframe.
        pair_df : pd.DataFrame
            The pair dataframe.

        Returns
        -------
        Tuple[pd.DataFrame, pd.DataFrame]
            Tuple of resulting dataframes after sorting.
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
        predicts__[0] = predicts_["contact_id_1"]
        predicts__[1] = predicts_["contact_id_2"]
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
        recombine_pred.columns = ["contact_id_1", "contact_id_2", "score"]
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
        self,
        recombine: pd.DataFrame,
        is_sort: bool = False,
        is_uniform: bool = False,
        uniform_df: Optional[pd.DataFrame] = None,
        indicator: int = 0,
    ) -> pd.DataFrame:
        """
        Perform third sort operation.
        Nodes
        -----
        select data by specifying seq_sep_inferior and seq_sep_superior.
            The select data can be sorted by two ways:
            1.  'score'
            2.  'contact_id_1' and 'contact_id_2'

        Parameters
        ----------
        recombine : pd.DataFrame
            The dataframe to recombine.
        is_sort : bool, optional
            If the output should be sorted, by default False.
        is_uniform : bool, optional
            If the output should be uniform, by default False.
        uniform_df : pd.DataFrame, optional
            The dataframe to uniform, by default None.
        indicator : int, optional
            The indicator value, by default 0

        Returns
        -------
        pd.DataFrame
            The sorted dataframe.
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
            recombine_.columns = ["contact_id_1", "contact_id_2", "score"]
            # print(recombine_)
            # self.pfwwriter.generic(recombine_, sv_fpn='./cheer')
        # # /*** block 2 ***/
        recombine_ = ppssep(
            df=recombine_,
            first="contact_id_1",
            second="contact_id_2",
            target="score",
            seq_sep_inferior=self.seq_sep_inferior,
            seq_sep_superior=self.seq_sep_superior,
            is_sort=is_sort,
        ).extract()
        return recombine_

    def todict(self, recombine: pd.DataFrame) -> Dict:
        """
        Convert dataframe to dictionary.

        Parameters
        ----------
        recombine : pd.DataFrame
            The dataframe to convert.

        Returns
        -------
        Dict
            The converted dictionary.
        """
        arr_2d = recombine.values.tolist()
        # print(arr_2d)
        dicts = tactic1(arr_2d)
        return dicts

    def mi(
        self,
        mi_path: str,
        file_name: str,
        file_chain: str,
        dist_df: Optional[pd.DataFrame] = None,
        pair_list: Optional[List] = None,
        sort_: int = 0,
        is_sort: bool = False,
    ) -> Union[Tuple[pd.DataFrame, pd.DataFrame], pd.DataFrame]:
        """
        Perform the mi operation.

        Parameters
        ----------
        mi_path : str
            The path to the mi file.
        file_name : str
            The name of the file.
        file_chain : str
            The chain of the file.
        dist_df : pd.DataFrame, optional
            The distance dataframe, by default None.
        pair_list : List, optional
            The list of pairs, by default None.
        sort_ : int, optional
            The sort value, by default 0.
        is_sort : bool, optional
            If the output should be sorted, by default False.

        Returns
        -------
        Union[Tuple[pd.DataFrame, pd.DataFrame], pd.DataFrame]
            The result of the mi operation.
        """
        self.__sort_ = sort_
        results = self.greader.generic(
            mi_path + file_name + file_chain + ".evfold", df_sep=r"\s+", is_utf8=True
        )
        results.columns = [
            "contact_id_1",
            "aa_1",
            "contact_id_2",
            "aa_2",
            "score",
            "FC_score",
        ]
        recombine = results[["contact_id_1", "contact_id_2", "score"]]
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
        else:
            return recombine

    def psicov(
        self,
        pcv_path: str,
        file_name: str,
        file_chain: str,
        dist_df: Optional[pd.DataFrame] = None,
        pair_list: Optional[List[Tuple[int, int]]] = None,
        sort_: int = 0,
        is_sort: bool = False,
    ) -> Union[pd.DataFrame, Tuple[pd.DataFrame, pd.DataFrame]]:
        """
        Process and return the PSICOV results. The results can be sorted based on sequence separation,
        and eliminate low scores.
        psicov result not only sorted by seq_sep>4 but also
        eliminate tiny score.

        Parameters:
        -----------
        pcv_path: str
            Path to the PSICOV file.
        file_name: str
            Name of the PSICOV file.
        file_chain: str
            Chain identifier of the PSICOV file.
        dist_df: Optional[pd.DataFrame]
            DataFrame containing distance data. Default is None.
        pair_list: Optional[List[Tuple[int, int]]]
            List of pairs to be sorted. Default is None.
        sort_: int
            Sorting type. 0 for no sorting, 1 for sort_1, and 2 for sort_2. Default is 0.
        is_sort: bool
            Whether to sort or not. Default is False.

        Returns:
        --------
        Union[pd.DataFrame, Tuple[pd.DataFrame, pd.DataFrame]]:
            Returns the sorted PSICOV DataFrame. If sort_ is 1 or 2, returns a tuple of DataFrames containing the sorted PSICOV data and the corresponding distance data.
        """
        self.__sort_ = sort_
        results = self.greader.generic(
            pcv_path + file_name + file_chain + ".psicov", df_sep=r"\s+", is_utf8=True
        )
        results.columns = [
            "contact_id_1",
            "contact_id_2",
            "dist_inf",
            "dist_sup",
            "score",
        ]
        recombine = results[["contact_id_1", "contact_id_2", "score"]]
        if self.__sort_ == 1:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            recombine = self.sort_3(
                recombine, is_sort=is_sort, is_uniform=True, uniform_df=pair_df
            )
            dist_pcv, dist_true = self.sort_1(recombine, dist_df)
            return dist_pcv, dist_true
        elif self.__sort_ == 2:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            recombine = self.sort_3(
                recombine, is_sort=is_sort, is_uniform=True, uniform_df=pair_df
            )
            dist_pcv, dist_true = self.sort_2(recombine, dist_df, pair_df)
            # dist_pcv.to_csv('3rvy_helices.txt', sep='\t', header=None, index=False)
            # print(len(dist_pcv), len(dist_true))
            return dist_pcv, dist_true
        else:
            return recombine

    def freecontact(
        self,
        fc_path: str,
        file_name: str,
        file_chain: str,
        dist_df: Optional[pd.DataFrame] = None,
        pair_list: Optional[List[Tuple[int, int]]] = None,
        sort_: int = 0,
        is_sort: bool = False,
    ) -> Union[pd.DataFrame, Tuple[pd.DataFrame, pd.DataFrame]]:
        self.__sort_ = sort_
        results = self.greader.generic(
            fc_path + file_name + file_chain + ".evfold", df_sep=r"\s+", is_utf8=True
        )
        results.columns = [
            "contact_id_1",
            "aa_1",
            "contact_id_2",
            "aa_2",
            "MI_score",
            "score",
        ]
        recombine = results[["contact_id_1", "contact_id_2", "score"]]
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
        else:
            return recombine

    def ccmpred(
        self,
        cp_path: str,
        file_name: str,
        file_chain: str,
        dist_df: Optional[pd.DataFrame] = None,
        pair_list: Optional[List[Tuple[int, int]]] = None,
        sort_: int = 0,
        is_sort: bool = False,
    ) -> Union[pd.DataFrame, Tuple[pd.DataFrame, pd.DataFrame]]:
        self.__sort_ = sort_
        file_results = self.greader.generic(
            cp_path + file_name + file_chain + ".ccmpred", df_sep=r"\s+", is_utf8=True
        )
        results = []
        for i, row in file_results.iterrows():
            for j in range(file_results.shape[1]):
                if i < j:
                    # print(i+1, j+1, row[j])
                    results.append([i + 1, j + 1, row[j]])
        results = pd.DataFrame(results)
        results.columns = ["contact_id_1", "contact_id_2", "score"]
        recombine = results[["contact_id_1", "contact_id_2", "score"]]
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
        else:
            return recombine

    def gremlin(
        self,
        gl_path: str,
        file_name: str,
        file_chain: str,
        dist_df: pd.DataFrame = None,
        pair_list: List = None,
        sort_: int = 0,
        is_sort: bool = False,
    ) -> Union[pd.DataFrame, Tuple[pd.DataFrame, pd.DataFrame]]:
        """
        Process the Gremlin data and returns it in a sorted or unsorted form based on the provided parameters.

        Parameters
        ----------
        gl_path : str
            Path to the Gremlin data file.
        file_name : str
            Name of the data file.
        file_chain : str
            Chain to be processed in the data file.
        dist_df : pandas.DataFrame, optional
            DataFrame containing the distribution data.
        pair_list : list, optional
            List of pairs to be processed.
        sort_ : int, optional
            Determines the type of sorting to be applied. (default is 0, which means no sorting)
        is_sort : bool, optional
            Whether to sort the data or not.

        Returns
        -------
        pandas.DataFrame or Tuple[pandas.DataFrame, pandas.DataFrame]
            Processed data, returned according to the sort_ parameter's value.
        """
        self.__sort_ = sort_
        results = self.greader.generic(
            gl_path + file_name + file_chain + ".gremlin",
            df_sep=r"\s+",
            header=0,
            is_utf8=True,
        )
        results.columns = [
            "contact_id_1",
            "contact_id_2",
            "aa_1",
            "aa_2",
            "r_sco",
            "s_sco",
            "score",
        ]
        recombine = results[["contact_id_1", "contact_id_2", "score"]]
        # print(recombine)
        # print(recombine.dtypes)
        if self.__sort_ == 1:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            recombine = self.sort_3(
                recombine, is_sort=is_sort, is_uniform=True, uniform_df=pair_df
            )
            dist_gl, dist_true = self.sort_1(recombine, dist_df)
            return dist_gl, dist_true
        elif self.__sort_ == 2:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            recombine = self.sort_3(
                recombine, is_sort=is_sort, is_uniform=True, uniform_df=pair_df
            )
            dist_gl, dist_true = self.sort_2(recombine, dist_df, pair_df)
            # dist_gl.to_csv('3rvy_helices.txt', sep='\t', header=None, index=False)
            # print(len(dist_gl), len(dist_true))
            return dist_gl, dist_true
        else:
            return recombine

    def gdca(
        self,
        gdca_path: str,
        file_name: str,
        file_chain: str,
        dist_df: pd.DataFrame = None,
        pair_list: List = None,
        sort_: int = 0,
        is_sort: bool = False,
    ) -> Union[pd.DataFrame, dict, Tuple[pd.DataFrame, pd.DataFrame]]:
        """
        Process the GDCA data and returns it in a sorted or unsorted form based on the provided parameters.

        Parameters
        ----------
        gdca_path : str
            Path to the GDCA data file.
        file_name : str
            Name of the data file.
        file_chain : str
            Chain to be processed in the data file.
        dist_df : pd.DataFrame, optional
            DataFrame containing the distribution data.
        pair_list : List, optional
            List of pairs to be processed.
        sort_ : int, optional
            Determines the type of sorting to be applied (default is 0, which means no sorting).
        is_sort : bool, optional
            Whether to sort the data or not (default is False).

        Returns
        -------
        Union[pd.DataFrame, dict, Tuple[pd.DataFrame, pd.DataFrame]]
            Processed data, returned according to the sort_ parameter's value.
        """
        self.__sort_ = sort_
        results = self.greader.generic(
            gdca_path + file_name + file_chain + ".gdca", df_sep=r"\s+", is_utf8=True
        )
        results.columns = ["contact_id_1", "contact_id_2", "score"]
        recombine = results[["contact_id_1", "contact_id_2", "score"]]
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
        else:
            return recombine

    def plmc(
        self,
        plmc_path: str,
        file_name: str,
        file_chain: str,
        dist_df: pd.DataFrame = None,
        pair_list: List = None,
        sort_: int = 0,
        is_sort: bool = False,
    ) -> Union[pd.DataFrame, dict, Tuple[pd.DataFrame, pd.DataFrame]]:
        """
        Process the PLMC data and returns it in a sorted or unsorted form based on the provided parameters.

        Parameters
        ----------
        plmc_path : str
            Path to the PLMC data file.
        file_name : str
            Name of the data file.
        file_chain : str
            Chain to be processed in the data file.
        dist_df : pd.DataFrame, optional
            DataFrame containing the distribution data.
        pair_list : List, optional
            List of pairs to be processed.
        sort_ : int, optional
            Determines the type of sorting to be applied (default is 0, which means no sorting).
        is_sort : bool, optional
            Whether to sort the data or not (default is False).

        Returns
        -------
        Union[pd.DataFrame, dict, Tuple[pd.DataFrame, pd.DataFrame]]
            Processed data, returned according to the sort_ parameter's value.
        """
        self.__sort_ = sort_
        results = self.greader.generic(
            plmc_path + file_name + file_chain + ".plmc", df_sep=r"\s+", is_utf8=True
        )
        results.columns = [
            "contact_id_1",
            "aa_1",
            "contact_id_2",
            "aa_2",
            "placeholder",
            "score",
        ]
        recombine = results[["contact_id_1", "contact_id_2", "score"]]
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
        else:
            return recombine

    def memconp(
        self,
        mcp_path: str,
        file_name: str,
        file_chain: str,
        dist_df: pd.DataFrame = None,
        pair_list: List = None,
        sort_: int = 0,
        is_sort: bool = False,
    ) -> Union[pd.DataFrame, dict, Tuple[pd.DataFrame, pd.DataFrame]]:
        """
                Process the MemconP data and returns it in a sorted or unsorted form based on the provided parameters.

                Parameters
                ----------
                mcp_path : str
                    Path to the MemconI'm sorry, the response was cut off. I'll continue the `memconp` function and add the `membrain2` function.

        ```python
                mcp_path : str
                    Path to the MemconP data file.
                file_name : str
                    Name of the data file.
                file_chain : str
                    Chain to be processed in the data file.
                dist_df : pd.DataFrame, optional
                    DataFrame containing the distribution data.
                pair_list : List, optional
                    List of pairs to be processed.
                sort_ : int, optional
                    Determines the type of sorting to be applied (default is 0, which means no sorting).
                is_sort : bool, optional
                    Whether to sort the data or not (default is False).

                Returns
                -------
                Union[pd.DataFrame, dict, Tuple[pd.DataFrame, pd.DataFrame]]
                    Processed data, returned according to the sort_ parameter's value.
        """
        self.__sort_ = sort_
        file_path = mcp_path + file_name + file_chain + ".memconp"
        with open(file_path) as file:
            surface = [[str(digit) for digit in line.split()] for line in file]
            memconp = pd.DataFrame(surface)
            # print(memconp)
        row_mark = memconp.loc[(memconp[0] == "RESTHRESH")].index[0]
        results = memconp.drop(index=np.arange(row_mark + 1))
        new_index = np.arange(results.shape[0])
        results = results.set_index(new_index, inplace=False, drop=True)
        results.columns = [
            "Mark",
            "contact_id_1",
            "contact_id_2",
            "score",
            "isContact",
            "ph1",
            "ph2",
        ]
        results["contact_id_1"] = results["contact_id_1"].astype(int)
        results["contact_id_2"] = results["contact_id_2"].astype(int)
        results["score"] = results["score"].astype(np.float64)
        # print(results.dtypes)
        recombine = results[
            [
                "contact_id_1",
                "contact_id_2",
                "score",
            ]
        ]
        # print(recombine.dtypes)
        if self.__sort_ == 1:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            recombine = self.sort_3(
                recombine, is_sort=is_sort, is_uniform=True, uniform_df=pair_df
            )
            dist_mcp, dist_true = self.sort_1(recombine, dist_df)
            return dist_mcp, dist_true
        elif self.__sort_ == 2:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            recombine = self.sort_3(
                recombine, is_sort=is_sort, is_uniform=True, uniform_df=pair_df
            )
            dist_mcp, dist_true = self.sort_2(recombine, dist_df, pair_df)
            # dist_mcp.to_csv('3rvy_helices.txt', sep='\t', header=None, index=False)
            # print(len(dist_mcp), len(dist_true))
            return dist_mcp, dist_true
        else:
            return recombine

    def membrain2(
        self,
        mb_path: str,
        file_name: str,
        file_chain: str,
        dist_df: pd.DataFrame = None,
        pair_list: List = None,
        sort_: int = 0,
        is_sort: bool = False,
    ) -> Union[pd.DataFrame, dict, Tuple[pd.DataFrame, pd.DataFrame]]:
        """
        Process the Membrain2 data and returns it in a sorted or unsorted form based on the provided parameters.

        Parameters
        ----------
        mb_path : str
            Path to the Membrain2 data file.
        file_name : str
            Name of the data file.
        file_chain : str
            Chain to be processed in the data file.
        dist_df : pd.DataFrame, optional
            DataFrame containing the distribution data.
        pair_list : List, optional
            List of pairs to be processed.
        sort_ : int, optional
            Determines the type of sorting to be applied (default is 0, which means no sorting).
        is_sort : bool, optional
            Whether to sort the data or not (default is False).

        Returns
        -------
        Union[pd.DataFrame, dict, Tuple[pd.DataFrame, pd.DataFrame]]
            Processed data, returned according to the sort_ parameter's value.
        """
        self.__sort_ = sort_
        # new_file = re.sub(r'Query(.+?)\)', "", str(results), flags=re.S)
        file_path = mb_path + file_name + file_chain + ".membrain2"
        with open(file_path) as file:
            surface = [[str(digit) for digit in line.split()] for line in file]
            membrain2 = pd.DataFrame(surface)
        row_mark = membrain2.loc[(membrain2[2] == "contacts:")].index[0]
        results = membrain2.drop(index=np.arange(row_mark + 1))
        new_index = np.arange(results.shape[0])
        results = results.set_index(new_index, inplace=False, drop=True)
        results.columns = [
            "No",
            "TMH1",
            "contact_id_1",
            "aa_1",
            "TMH2",
            "contact_id_2",
            "aa_2",
            "score",
        ]
        results["contact_id_1"] = results["contact_id_1"].astype(int)
        results["contact_id_2"] = results["contact_id_2"].astype(int)
        results["score"] = results["score"].astype(np.float64)
        # print(results.dtypes)
        recombine = results[["contact_id_1", "contact_id_2", "score"]]
        if self.__sort_ == 1:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            recombine = self.sort_3(
                recombine, is_sort=is_sort, is_uniform=True, uniform_df=pair_df
            )
            dist_mb, dist_true = self.sort_1(recombine, dist_df)
            return dist_mb, dist_true
        elif self.__sort_ == 2:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            recombine = self.sort_3(
                recombine, is_sort=is_sort, is_uniform=True, uniform_df=pair_df
            )
            dist_mb, dist_true = self.sort_2(recombine, dist_df, pair_df)
            # dist_mb.to_csv('3rvy_helices.txt', sep='\t', header=None, index=False)
            # print(len(dist_mb), len(dist_true))
            return dist_mb, dist_true
        else:
            return recombine

    def deephelicon(
        self,
        deephelicon_path: str,
        file_name: str,
        file_chain: str,
        dist_df: pd.DataFrame = None,
        pair_list: List = None,
        sort_: int = 0,
        is_sort: bool = False,
    ) -> Union[pd.DataFrame, Tuple[pd.DataFrame, pd.DataFrame]]:
        """
        Process the DeepHelicon data and returns it in a sorted or unsorted form based on the provided parameters.

        Parameters
        ----------
        deephelicon_path : str
            Path to the DeepHelicon data file.
        file_name : str
            Name of the data file.
        file_chain : str
            Chain to be processed in the data file.
        dist_df : pandas.DataFrame, optional
            DataFrame containing the distribution data.
        pair_list : list, optional
            List of pairs to be processed.
        sort_ : int, optional
            Determines the type of sorting to be applied. (default is 0, which means no sorting)
        is_sort : bool, optional
            Whether to sort the data or not.

        Returns
        -------
        Union[pandas.DataFrame, Tuple[pandas.DataFrame, pandas.DataFrame]]
            Processed data, returned as DataFrame when sort_ is not 1 or 2,
            else returns a tuple of DataFrames.
        """
        self.__sort_ = sort_
        results = self.greader.generic(
            deephelicon_path + file_name + file_chain + ".tma165",
            df_sep="\t",
            is_utf8=True,
        )
        results.columns = ["contact_id_1", "aa_1", "contact_id_2", "aa_2", "score"]
        recombine = results[["contact_id_1", "contact_id_2", "score"]]
        if self.__sort_ == 1:
            pair_df = pd.DataFrame(pair_list)
            # print(pair_df)
            recombine = self.sort_3(
                recombine, is_sort=is_sort, is_uniform=True, uniform_df=pair_df
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
