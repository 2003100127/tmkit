import re
import os
import gzip
import shutil
import urllib.request


def chainid(prot_chain):
    return str(prot_chain) + 'l' if str(prot_chain).islower() else str(prot_chain)


def seqchainid(prot_chain):
    return str(prot_chain[0])


def delete(fpn):
    return os.remove(fpn)


def create(DIRECTORY, mode='dir'):
    if mode == 'dir':
        if not os.path.exists(DIRECTORY):
            os.makedirs(DIRECTORY)
    return 0


def batchRename(file_path, old_suffix, new_suffix, flag=1):
    if flag == 0:
        for file_name in os.listdir(file_path):
            if os.path.isfile(os.path.join(file_path, file_name)):
                file_name_re = re.sub(r'[p]db', "", file_name)
                file_name_re = re.sub(r'\.[e]nt', "", file_name_re)
                # print(file_name_re)
                os.rename(
                    os.path.join(file_path, file_name),
                    os.path.join(file_path, file_name_re+'.pdb')
                )
    elif flag == 1:
        for file in os.listdir(file_path):
            path = os.path.join(file_path, file)
            if os.path.splitext(path)[1] == old_suffix:
                file_name = os.path.splitext(file)[0]
                prot_name = re.sub(r'[A-Z].', "", os.path.splitext(file)[0])
                chain = re.sub(r'[a-z0-9]', "", os.path.splitext(file)[0])
                os.rename(
                    os.path.join(file_path, file_name + old_suffix),
                    os.path.join(file_path, prot_name + chain + new_suffix)
                )
    return


def urlliby(url, fpn):
    return urllib.request.urlretrieve(
        url=url,
        filename=fpn
    )


def ungz(file_path, file_name, sv_fp, new_suffix='.pdb'):
    try:
        with gzip.open(file_path + file_name + '.gz', 'rb') as f_in:
            with open(sv_fp + file_name + new_suffix, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
    except FileNotFoundError:
        print('No such file' + file_path + file_name)
    return


def tactic1(arr_2d):
    result = {}
    len_arr = len(arr_2d[0])
    if len_arr == 3:
        for item in arr_2d:
            result.setdefault(item[0], {}).update({item[1]: item[2]})
    else:
        for item in arr_2d:
            result.setdefault(item[0], {}).update({item[1]: item[2:]})
    return result


def tactic5(arr_2d):
    result = {}
    for item in arr_2d:
        result[item[0]] = []
    for item in arr_2d:
        if item[0] in result.keys():
            result[item[0]].append(item[1])
            # print(result[item[0]])
    return result


def tactic6(arr_2d):
    result = {}
    len_arr = len(arr_2d[0])
    if len_arr == 2:
        for item in arr_2d:
            result[item[0]] = item[1]
    else:
        for item in arr_2d:
            result[item[0]] = item[1:]
    return result


def tactic7(arr_2d):
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


def tactic8(arr_1d_1, arr_1d_2):
    map = {}
    for i, e in enumerate(arr_1d_1):
        map[e] = arr_1d_2[i]
    return map