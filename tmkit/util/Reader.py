__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import Any, Dict, List, Optional, Union

from functools import wraps

import pandas as pd


class Reader:
    def __call__(self, deal: Any) -> Any:
        """
        A decorator that reads data from a file and passes it to the decorated function.

        Parameters
        ----------
        deal : function
            The function to be decorated.

        Returns
        -------
        function
            The decorated function.

        """
        generic = self.generic
        excel = self.excel

        @wraps(deal)
        def read(ph: str, *args: Any, **kwargs: Any) -> Any:
            """
            Reads data from a file and passes it to the decorated function.

            Parameters
            ----------
            ph : str
                The file path.
            *args : Any
                Positional arguments to be passed to the decorated function.
            **kwargs : Any
                Keyword arguments to be passed to the decorated function.

            Returns
            -------
            Any
                The return value of the decorated function.

            """
            deal(ph, **kwargs)
            keys = [*kwargs.keys()]
            if kwargs["type"] == "generic":
                return generic(
                    df_fpn=kwargs["df_fpn"],
                    df_sep="\t" if "df_sep" not in keys else kwargs["df_sep"],
                    skiprows=False if "skiprows" not in keys else kwargs["skiprows"],
                    header=None if "header" not in keys else kwargs["header"],
                    is_utf8=False if "is_utf8" not in keys else kwargs["is_utf8"],
                )
            elif kwargs["type"] == "excel":
                return excel(
                    df_fpn=kwargs["df_fpn"],
                    sheet_name="Sheet1"
                    if "sheet_name" not in keys
                    else kwargs["sheet_name"],
                    header=None if "header" not in keys else kwargs["header"],
                    is_utf8=False if "is_utf8" not in keys else kwargs["is_utf8"],
                )

        return read

    def generic(
        self,
        df_fpn: str,
        df_sep: str = "\t",
        skiprows: Optional[Union[int, List[int]]] = None,
        header: Optional[Union[int, List[int], None]] = None,
        is_utf8: bool = False,
        comment: str = "#",
    ) -> pd.DataFrame:
        """
        Reads a generic data file.

        Parameters
        ----------
        df_fpn : str
            The file path.
        df_sep : str, optional
            The delimiter to use, by default "\t".
        skiprows : Union[int, List[int]], optional
            Line numbers to skip (0-indexed), by default None.
        header : Union[int, List[int], None], optional
            Row(s) to use as the column names, by default None.
        is_utf8 : bool, optional
            Whether the file is encoded in UTF-8, by default False.
        comment : str, optional
            Indicates remainder of line should not be parsed, by default "#".

        Returns
        -------
        pd.DataFrame
            The data in the file.

        """
        if is_utf8:
            return pd.read_csv(
                df_fpn,
                sep=df_sep,
                header=header,
                encoding="utf-8",
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

    def excel(
        self,
        df_fpn: str,
        sheet_name: str = "Sheet1",
        header: Optional[Union[int, List[int], None]] = None,
        is_utf8: bool = False,
    ) -> pd.DataFrame:
        """
        Reads an Excel file.

        Parameters
        ----------
        df_fpn : str
            The file path.
        sheet_name : str, optional
            The name of the sheet to read, by default "Sheet1".
        header : Union[int, List[int], None], optional
            Row(s) to use as the column names, by default None.
        is_utf8 : bool, optional
            Whether the file is encoded in UTF-8, by default False.

        Returns
        -------
        pd.DataFrame
            The data in the file.

        """
        if is_utf8:
            return pd.read_excel(
                df_fpn,
                sheet_name=sheet_name,
                header=header,
                encoding="utf-8",
                engine="openpyxl",
            )
        else:
            return pd.read_excel(
                df_fpn,
                sheet_name=sheet_name,
                header=header,
                engine="openpyxl",
            )
