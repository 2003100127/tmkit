__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import Any, Dict, List, Tuple, Union

from functools import wraps

import pandas as pd


class Writer:
    """
    A class that provides methods for writing data to files.

    Attributes:
    -----------
    None

    Methods:
    --------
    __call__(self, deal) -> Callable:
        A decorator that wraps the `deal` function and returns a new function `write`.
        The `write` function writes data to a file based on the `type` argument in `kwargs`.

    generic(self, df: Union[pd.DataFrame, List[List[Any]]], sv_fpn: str, df_sep: str = "\t",
            header: Union[None, bool, List[str]] = None, index: bool = False, id_from: int = 0) -> None:
        Writes a DataFrame or a 2D list to a file in generic format.

    excel(self, df: Union[pd.DataFrame, List[List[Any]]], sv_fpn: str, sheet_name: str = "Sheet1",
          header: Union[None, bool, List[str]] = None, index: bool = False, id_from: int = 0) -> None:
        Writes a DataFrame or a 2D list to an Excel file.

    save(self, list_2d: List[Tuple[str, str]], sv_fp: str) -> int:
        Saves a list of 2-tuples to a file in FASTA format.

    """

    def __call__(self, deal: callable) -> callable:
        """
        A decorator that wraps the `deal` function and returns a new function `write`.
        The `write` function writes data to a file based on the `type` argument in `kwargs`.

        Parameters:
        -----------
        deal: callable
            The function to be decorated.

        Returns:
        --------
        write: callable
            The decorated function.
        """
        generic = self.generic
        excel = self.excel

        @wraps(deal)
        def write(ph: Any, *args: Any, **kwargs: Any) -> Any:
            """
            The decorated function that writes data to a file based on the `type` argument in `kwargs`.

            Parameters:
            -----------
            ph: Any
                The placeholder argument.
            *args: Any
                Positional arguments.
            **kwargs: Any
                Keyword arguments.

            Returns:
            --------
            res: Any
                The result of the `deal` function.
            """
            res = deal(ph, **kwargs)
            keys = [*kwargs.keys()]
            if kwargs["type"] == "generic":
                generic(
                    df=kwargs["df"],
                    sv_fpn=kwargs["sv_fpn"],
                    df_sep="\t" if "df_sep" not in keys else kwargs["df_sep"],
                    id_from=0 if "id_from" not in keys else kwargs["id_from"],
                    header=None if "header" not in keys else kwargs["header"],
                    index=False if "index" not in keys else kwargs["index"],
                )
            elif kwargs["type"] == "excel":
                excel(
                    df=kwargs["df"],
                    sv_fpn=kwargs["sv_fpn"],
                    sheet_name="Sheet1"
                    if "sheet_name" not in keys
                    else kwargs["sheet_name"],
                    id_from=0 if "id_from" not in keys else kwargs["id_from"],
                    header=None if "header" not in keys else kwargs["header"],
                    index=False if "index" not in keys else kwargs["index"],
                )
            return res

        return write

    def generic(
        self,
        df: Union[pd.DataFrame, List[List[Any]]],
        sv_fpn: str,
        df_sep: str = "\t",
        header: Union[None, bool, List[str]] = None,
        index: bool = False,
        id_from: int = 0,
    ) -> None:
        """
        Writes a DataFrame or a 2D list to a file in generic format.

        Parameters:
        -----------
        df: Union[pd.DataFrame, List[List[Any]]]
            The DataFrame or 2D list to be written to a file.
        sv_fpn: str
            The file path to save the file.
        df_sep: str, optional (default="\t")
            The separator used in the file.
        header: Union[None, bool, List[str]], optional (default=None)
            Whether to include the header in the file.
        index: bool, optional (default=False)
            Whether to include the index in the file.
        id_from: int, optional (default=0)
            The starting index.

        Returns:
        --------
        None
        """
        df_ = pd.DataFrame(df)
        df_.index = df_.index + id_from
        return df_.to_csv(sv_fpn, sep=df_sep, header=header, index=index)

    def excel(
        self,
        df: Union[pd.DataFrame, List[List[Any]]],
        sv_fpn: str,
        sheet_name: str = "Sheet1",
        header: Union[None, bool, List[str]] = None,
        index: bool = False,
        id_from: int = 0,
    ) -> None:
        """
        Writes a DataFrame or a 2D list to an Excel file.

        Parameters:
        -----------
        df: Union[pd.DataFrame, List[List[Any]]]
            The DataFrame or 2D list to be written to an Excel file.
        sv_fpn: str
            The file path to save the file.
        sheet_name: str, optional (default="Sheet1")
            The name of the sheet in the Excel file.
        header: Union[None, bool, List[str]], optional (default=None)
            Whether to include the header in the file.
        index: bool, optional (default=False)
            Whether to include the index in the file.
        id_from: int, optional (default=0)
            The starting index.

        Returns:
        --------
        None
        """
        df_ = pd.DataFrame(df)
        df_.index = df_.index + id_from
        return df_.to_excel(sv_fpn, sheet_name=sheet_name, header=header, index=index)

    def save(self, list_2d: List[Tuple[str, str]], sv_fp: str) -> int:
        """
        Saves a list of 2-tuples to a file in FASTA format.

        Parameters:
        -----------
        list_2d: List[Tuple[str, str]]
            The list of 2-tuples to be saved to a file in FASTA format.
        sv_fp: str
            The file path to save the file.

        Returns:
        --------
        int
            0 if the file is saved successfully.
        """
        for i, e in enumerate(list_2d):
            prot_name = str(e[0])
            seq = str(e[1])
            print(f"No.{i + 1} saving {prot_name} in FASTA format.")
            f = open(sv_fp, "w")
            f.write(">" + prot_name + "\n")
            f.write(seq + "\n")
            f.close()
        return 0
