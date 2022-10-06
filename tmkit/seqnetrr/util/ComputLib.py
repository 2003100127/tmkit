__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2022"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import itertools
import numpy as np


class computLib(object):

    def __init__(self, ):
        pass

    @classmethod
    def interv2combi(cls, inf_arr, sup_arr):
        """

        Notes
        -----
                        1   2   3
            inf_arr = [15, 48, 78]
            sup_arr = [30, 53, 99]
            element in interval No.1 matches elements in No.2,
            No.3 one by one. and then, element in interval No.2
            matches elements in interval No.3 until finished.

        Parameters
        ----------
        inf_arr
            1d list
        sup_arr
            1d list

        Returns
        -------

        """
        tmp_2d = []
        num_interv = len(inf_arr)
        for i in range(num_interv):
            tmp_2d.append(list(np.arange(inf_arr[i], sup_arr[i] + 1)))
        combi = []
        for i in range(num_interv):
            for j in range(num_interv):
                if i < j:
                    for p in range(len(tmp_2d[i])):
                        for q in range(len(tmp_2d[j])):
                            combi.append([tmp_2d[i][p], tmp_2d[j][q]])
        # print(combi)
        return combi

    def interv2single(self, inf_arr, sup_arr):
        """

        Methods
        -------
                        1   2   3
            inf_arr = [15, 48, 78]
            sup_arr = [30, 53, 99]
            element in interval No.1 matches elements in No.2,
            No.3 one by one. and then, element in interval No.2
            matches elements in interval No.3 until finished.

        Parameters
        ----------
        inf_arr
            1d list
        sup_arr
            1d list

        Returns
        -------

        """
        single = []
        num_interv = len(inf_arr)
        for i in range(num_interv):
            segment = self.num2arr2d(inf_arr[i], sup_arr[i])
            for j in segment:
                single.append(j)
        return single

    def num2arr(self, length):
        """

        Notes
        -----
            generate a 2x2 array by given an number from 1.

        Parameters
        ----------
        length

        Returns
        -------

        """
        arr = []
        for i in range(length):
            for j in range(length):
                if i < j:
                    arr.append([i + 1, j + 1])
        return arr

    def numTo3cols(self, length):
        """

        Notes
        -----
            generate a 2x2 array by given an number from 1.

        Parameters
        ----------
        length

        Returns
        -------

        """
        arr = []
        for i in range(length):
            for j in range(length):
                if i < j:
                    arr.append([i+1, j+1, 1])
        return arr

    def tactic1(self, arr_2d):
        """

        Parameters
        ----------
        arr_2d

        Returns
        -------

        """
        result = {}
        len_arr = len(arr_2d[0])
        if len_arr == 3:
            for item in arr_2d:
                result.setdefault(item[0], {}).update({item[1]: item[2]})
        else:
            for item in arr_2d:
                result.setdefault(item[0], {}).update({item[1]: item[2:]})
        return result

    def num2triangular(self, length):
        """

        Notes
        -----
            generate a 2x2 array by given an number from 1.

        Parameters
        ----------
        length

        Returns
        -------

        """
        arr = []
        for i in range(length):
            for j in range(i, length):
                arr.append([i + 1, j + 1])
        return arr

    def num2arr2d(self, inf, sup):
        """

        Notes
        -----
            generate a 1d array by given an inf and sup.

        Parameters
        ----------
        inf
        sup

        Returns
        -------

        """
        arr = []
        for i in range(inf, sup + 1):
            arr.append([i])
        return arr

    def patch(self, length, step=1):
        """

        Parameters
        ----------
        length
        step

        Returns
        -------

        """
        arr = []
        for i in range(-length, length + 1, step):
            for j in range(-length, length + 1, step):
                arr.append([i, j])
        return arr

    def combo2x2(self, array):
        """

        Notes
        -----
            repeated 2x2 combination of elements of an array.

        Parameters
        ----------
        array

        Returns
        -------
            amount of combo2x2: L*L.

        """
        combo = []
        ob = itertools.product(array, repeat=2)
        for i in ob:
            combo.append(list(i))
        return combo

    def combo2x2_(self, array):
        """

        Notes
        -----
            nonrepeated 2x2 combination of elements of an array.

        Parameters
        ----------
        array

        Returns
        -------
            amount of combo2x2: L*(L-1)/2.

        """
        combo = []
        ob = itertools.combinations(array, 2)
        # #/*** block 1.1 ***/
        for i in ob:
            combo.append(list(i))
        return combo
