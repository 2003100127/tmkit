__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import subprocess
import urllib.request
from tmkit.util.Writer import writer


class xml:

    def __init__(
            self,
            prot_series,
    ):
        self.write = writer()
        self.prot_dedup = prot_series.unique()

    def pdbtm(self, sv_fp, is_cmd=False):
        count = 0
        fails = []
        for i, prot_name in enumerate(self.prot_dedup):
            print('===>No.{} protein name: {}'.format(i + 1, prot_name))
            try:
                url = 'http://pdbtm.enzim.hu/data/database/' + str(prot_name[1]) + str(prot_name[2]) + '/' + str(prot_name) + '.xml'
                if is_cmd:
                    subprocess.Popen(
                        'wget ' + url,
                        stderr=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        shell=True
                    ).communicate()
                    print("======>successfully downloaded!")
                else:
                    urllib.request.urlretrieve(
                        url=url,
                        filename=sv_fp + str(prot_name) + '.xml'
                    )
                    print("======>successfully downloaded!")
            except:
                count = count + 1
                fails.append(prot_name)
                print('===>number of xml that cannot be downloaded {}'.format(count))
                continue
        self.write.generic(fails, sv_fp + 'log_fail_ids.txt')
        return 0