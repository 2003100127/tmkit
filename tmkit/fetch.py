__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from tmkit.util.Kit import urlliby


def tmkit_data(url, sv_fpn):
    urlliby(
        url=url,
        fpn=sv_fpn
    )

def unzip(in_fpn, out_fp):
    import zipfile
    with zipfile.ZipFile(in_fpn, 'r') as zip_ref:
        zip_ref.extractall(out_fp)