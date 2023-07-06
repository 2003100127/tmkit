__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import Optional

import pandas as pd

from tmkit.seqnetrr.combo.Param import Param


class Separation(Param):
    """
    Class for extracting data from a pandas DataFrame based on the difference between two columns.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to extract data from.
    first : str, optional
        The name of the first column to calculate the difference from. Default is None.
    second : str, optional
        The name of the second column to calculate the difference from. Default is None.
    is_sort : bool, optional
        Whether to sort the extracted data by a target column. Default is False.
    target : str, optional
        The name of the target column to sort by. Default is None.
    seq_sep_inferior : float, optional
        The inferior limit of the difference between the two columns. Default is None.
    seq_sep_superior : float, optional
        The superior limit of the difference between the two columns. Default is None.

    Returns
    -------
    pd.DataFrame
        The extracted data from the input DataFrame.

    Notes
    -----
    The function extracts data from the input DataFrame based on the difference between two columns. The extracted data
    can be filtered based on the inferior and superior limits of the difference, and can be sorted by a target column.
    """

    def __init__(
        self,
        df: pd.DataFrame,
        first: Optional[str] = None,
        second: Optional[str] = None,
        is_sort: Optional[bool] = False,
        target: Optional[str] = None,
        seq_sep_inferior: Optional[float] = None,
        seq_sep_superior: Optional[float] = None,
    ) -> None:
        super().__init__(seq_sep_inferior, seq_sep_superior)
        self.df = df
        self.seq_sep_inferior = seq_sep_inferior
        self.seq_sep_superior = seq_sep_superior
        self.first = first
        self.second = second
        self.is_sort = is_sort
        self.target = target

    def extract(self) -> pd.DataFrame:
        """
        Extract data from the input DataFrame based on the difference between two columns.

        Returns
        -------
        pd.DataFrame
            The extracted data from the input DataFrame.

        Notes
        -----
        The function extracts data from the input DataFrame based on the difference between two columns. The extracted
        data can be filtered based on the inferior and superior limits of the difference, and can be sorted by a target
        column.

        The function performs the following steps:
        1. If `seq_sep_inferior` is not None and `seq_sep_superior` is None, return results greater than
           `seq_sep_inferior`.
        2. If `seq_sep_inferior` is None and `seq_sep_superior` is not None, return results smaller than
           `seq_sep_superior`.
        3. If `seq_sep_inferior` and `seq_sep_superior` are not None, return results greater than `seq_sep_inferior`
           but smaller than `seq_sep_superior`.
        4. If `seq_sep_inferior` and `seq_sep_superior` are None, return all results of the predictor.

        """
        df_ = self.df
        ### /* block 1 */ ###
        if self.seq_sep_inferior is not None and self.seq_sep_superior is None:
            query = df_[self.second] - df_[self.first] > self.seq_sep_inferior
        ### /* block 2 */ ###
        elif self.seq_sep_inferior is None and self.seq_sep_superior is not None:
            query = df_[self.second] - df_[self.first] < self.seq_sep_superior
        ### /* block 3 */ ###
        elif self.seq_sep_inferior is not None and self.seq_sep_superior is not None:
            ss_inf = df_[self.second] - df_[self.first] > self.seq_sep_inferior
            ss_sup = df_[self.second] - df_[self.first] < self.seq_sep_superior
            query = ss_inf & ss_sup
        ### /* block 4 */ ###
        else:
            query = 0 < df_[self.second] - df_[self.first]
        df_ = df_.loc[query].sort_values(by=[self.first, self.second], ascending=True)
        if self.is_sort:
            df_ = df_.loc[query].sort_values([self.target], ascending=False)
        else:
            df_ = df_.loc[query]
        df_ = df_.reset_index(inplace=False, drop=True)
        return df_
