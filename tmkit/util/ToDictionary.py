from collections import defaultdict


class toDictionary(object):
    
    def __init__(self, ):
        pass
    
    def tactic1(self, arr_2d):
        result = {}
        len_arr = len(arr_2d[0])
        if len_arr == 3:
            for item in arr_2d:
                result.setdefault(item[0], {}).update({item[1]: item[2]})
        else:
            for item in arr_2d:
                result.setdefault(item[0], {}).update({item[1]: item[2:]})
        return result

    def tactic2(self, arr_2d):
        result = defaultdict(dict)
        len_arr = len(arr_2d[0])
        if len_arr == 3:
            for item in arr_2d:
                result[item[0]][item[1]] = item[2]
        else:
            for item in arr_2d:
                result[item[0]][item[1]] = item[2:]
        return result

    def tactic3(self, arr_2d):
        result = {}
        len_arr = len(arr_2d[0])
        if len_arr == 3:
            for item in arr_2d:
                result[item[0], item[1]] = item[2]
        else:
            for item in arr_2d:
                result[item[0], item[1]] = item[2:]
        return result

    def tactic4(self, ):
        """
        ..  @example:
            ---------
            >>> L = [['home', 'school', '5'], ['home', 'office', '10'], ['home', 'store', '7'], ['school', 'store', '8'], ['office', 'school', '4']]
            >>> d = defaultdict(list)
            >>> for i in L:
            ...     d[i[0]].append(i[1:])
            >>> {k: dict(v) for k, v in d.items()}
            {'home': {'school': '5', 'store': '7', 'office': '10'}, 'school': {'store': '8'}, 'office': {'school': '4'}}
        :return:
        """
        pass

    def tactic5(self, arr_2d):
        """
        ..  @description:
            -------------
            2d arr to 1d dict, each key in the 1d dict being an list

        :param arr_2d:
        :return:
        """
        result = {}
        for item in arr_2d:
            result[item[0]] = []
        for item in arr_2d:
            if item[0] in result.keys():
                result[item[0]].append(item[1])
                # print(result[item[0]])
        return result

    def tactic6(self, arr_2d):
        """
        ..  @description:
            -------------
            arr = [[1, 2.35], [2, 1.5], [3, 14.35]]
            2d arr to 1d dict, each key in the 1d dict being a value.

        :param arr_2d:
        :return:
        """
        result = {}
        len_arr = len(arr_2d[0])
        if len_arr == 2:
            for item in arr_2d:
                result[item[0]] = item[1]
        else:
            for item in arr_2d:
                result[item[0]] = item[1:]
        return result

    def tactic7(self, arr_2d):
        """
        arr_2d for three columns
        a typical example is used for looking up domains in CATH.
        [complex_id, chain_id, domain_id]
        one complex_id can have many chain ids.
        one chain_id can have many domain ids.
        e.g. {
            '9ldb': {'A': ['01', '02'], 'B': ['01', '02']},
            '9jdw': {'A': ['00']},
        }
        :param arr_2d:
        :return:
        """
        result = {}
        for item in arr_2d:
            result[item[0]] = {}
        for item in arr_2d:
            # if item[0] in result.keys():
                result[item[0]][item[1]] = []
        for item in arr_2d:
            if item[1] in result[item[0]].keys():
                result[item[0]][item[1]].append(item[2])
        return result

    def tactic8(self, arr_1d_1, arr_1d_2):
        map = {}
        for i, e in enumerate(arr_1d_1):
            map[e] = arr_1d_2[i]
        return map


if __name__ == "__main__":
    # import pandas as pd
    p = toDictionary()
    # arr_2d = [[15, 48], [30, 53], [2, 3]]
    # arr_2d = [[15, 48], [15, 53], [2, 3]]
    arr_2d = [[15, 48, 78], [30, 53, 99], [30, 3, 11]]
    # arr_2d = [[15, 48, 78, 82], [30, 53, 99, 84], [2, 3, 11, 2]]
    # arr_2d = [
    #     ['4ni4H', '01'],
    #     ['4ni4H', '01'],
    #     ['4ni4H', '02'],
    #     ['4ni4d', '02'],
    # ]
    # arr_2d = [
    #     ['Q9P0L9_R796H', ['1']],
    #     ['Q9P126_S28F', ['1', '2']],
    #     ['Q9P283_V840D', ['1']],
    # ]
    # arr_2d = [['4ni4H', '01'], ['4ni4H', '02']]
    # ol = p.tactic1(arr_2d=arr_2d)
    # pd.DataFrame(ol)
    # print(ol)

    # for i in ol.keys():
    #     print(i)
    #     print(list(ol[i])[0])

    # print(p.tactic1(arr_2d))

    # print(p.tactic2(arr_2d))

    # print(p.tactic3(arr_2d))

    # print(p.tactic4(arr_2d))

    print(p.tactic5(arr_2d))

    # print(p.tactic6(arr_2d))

    # print(p.tactic7(arr_2d))

    # print(p.tactic8(arr_2d))