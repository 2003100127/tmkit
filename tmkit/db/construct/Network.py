__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import List, Tuple

import numpy as np
import pandas as pd


class Network:
    def single(
        self,
        interacting_df: pd.DataFrame,
        uniprot_id: str,
        by: List[str] = [],
        is_del_reflexive: bool = False,
        is_del_repeated: bool = False,
    ) -> np.ndarray:
        """
        Construct a single network for a given uniprot_id.

        Parameters
        ----------
        interacting_df : np.ndarray
            The input interaction dataframe.
        uniprot_id : str
            The uniprot_id for which to construct the network.
        by : List[str], optional
            The respective identifiers of interaction A and interaction B, by default [].
        is_del_reflexive : bool, optional
            Whether to delete interactions with itself, by default False.
        is_del_repeated : bool, optional
            Whether to delete interacting pairs occurring repeatedly, by default False.

        Returns
        -------
        np.ndarray
            The constructed network.
        """
        interacting_left = interacting_df.groupby(by=[by[0]])
        interacting_right = interacting_df.groupby(by=[by[1]])
        # print(interacting_left.groups.keys())
        if uniprot_id in interacting_left.groups.keys():
            interacting_left_grouped = np.array(interacting_left.get_group(uniprot_id))
            # print(interacting_left_grouped)
            print(
                "=========>Record(s) for {} found in the left column.".format(
                    uniprot_id
                )
            )
        else:
            print(
                "=========>No record(s) for {} found in the left column.".format(
                    uniprot_id
                )
            )
            interacting_left_grouped = np.empty(shape=[0, 2])
        if uniprot_id in interacting_right.groups.keys():
            interacting_right_grouped = np.array(
                interacting_right.get_group(uniprot_id)
            )[
                :, [1, 0]
            ]  # exchange the order of the two
            # print(interacting_right_grouped)
            print(
                "=========>Record(s) for {} found in the left column.".format(
                    uniprot_id
                )
            )
        else:
            print(
                "=========>No record(s) for {} found on the right column.".format(
                    uniprot_id
                )
            )
            interacting_right_grouped = np.empty(shape=[0, 2])
        if is_del_reflexive:
            A_row_marker = np.where(
                interacting_left_grouped[:, 0] == interacting_left_grouped[:, 1]
            )
            B_row_marker = np.where(
                interacting_right_grouped[:, 0] == interacting_right_grouped[:, 1]
            )
            interacting_left_grouped = np.delete(
                interacting_left_grouped, A_row_marker, axis=0
            )
            interacting_right_grouped = np.delete(
                interacting_right_grouped,
                B_row_marker,
                axis=0,
            )
        single_network = np.concatenate(
            (interacting_left_grouped, interacting_right_grouped), axis=0
        )
        if is_del_repeated:
            single_network_B = np.unique(single_network[:, 1])
            single_network = np.concatenate(
                (
                    np.array([uniprot_id] * single_network_B.shape[0])[:, np.newaxis],
                    single_network_B[:, np.newaxis],
                ),
                axis=1,
            )
        if len(single_network) > 0:
            return single_network
        else:
            return np.empty(shape=[0, 2])
