__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import Optional
import pandas as pd
from tmkit.base.Position import position


class Separation(position):
    """
    Class for extracting results from a dataframe based on the difference between two columns.

    Parameters
    ----------
    df : pandas.DataFrame
        The dataframe to extract results from.
    first : str, optional
        The name of the first column to calculate the difference from.
    second : str, optional
        The name of the second column to calculate the difference from.
    is_sort : bool, optional
        Whether to sort the results by a target column.
    target : str, optional
        The name of the column to sort the results by.
    seq_sep_inferior : float, optional
        The minimum difference between the two columns to include in the results.
    seq_sep_superior : float, optional
        The maximum difference between the two columns to include in the results.

    Returns
    -------
    pandas.DataFrame
        The extracted results from the dataframe.
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
        Extracts results from the dataframe based on the difference between two columns.
        block 1
                |--- block 1.1  return results greater than seq_sep_inferior
                |--- block 1.2  return results smaller than seq_sep_superior
                |--- block 1.3  return results greater than seq_sep_inferior
                                but smaller than seq_sep_superior
                |--- block 1.4  return all results of the predictor

        Returns
        -------
        pandas.DataFrame
            The extracted results from the dataframe.
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
        df_ = df_.loc[query].sort_values(
            by=[self.first, self.second], ascending=True)
        if self.is_sort:
            df_ = df_.loc[query].sort_values([self.target], ascending=False)
        else:
            df_ = df_.loc[query]
        df_ = df_.reset_index(inplace=False, drop=True)
        return df_
