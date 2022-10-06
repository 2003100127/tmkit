__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2022"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import sys
sys.path.append('../../')
import subprocess
import urllib.request
from tmkit.util.Writer import writer
from tmkit.util.Console import console


class xml(object):

    def __init__(
            self,
            prot_series,
            verbose=True,
    ):
        self.write = writer()
        self.prot_dedup = prot_series.unique()
        self.console = console()
        self.console.verbose = verbose

    def pdbtm(self, sv_fp, is_cmd=False):
        count = 0
        fails = []
        for i, prot_name in enumerate(self.prot_dedup):
            self.console.print('===>No.{} protein name: {}'.format(i, prot_name))
            try:
                url = 'http://pdbtm.enzim.hu/data/database/' + str(prot_name[1]) + str(prot_name[2]) + '/' + str(prot_name) + '.xml'
                if is_cmd:
                    subprocess.Popen(
                        'wget ' + url,
                        stderr=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        shell=True
                    ).communicate()
                else:
                    urllib.request.urlretrieve(
                        url=url,
                        filename=sv_fp + str(prot_name) + '.xml'
                    )
            except:
                count = count + 1
                fails.append(prot_name)
                self.console.print('===>number of xml that cannot be downloaded {}'.format(count))
                continue
        self.write.generic(fails, sv_fp + 'log_fail_ids.txt')
        return 0


if __name__ == "__main__":
    from tmkit.Path import to
    from tmkit.util.Reader import reader

    DEFINE = {
        'list_fpn': to('data/example/pdb/indepdata/prot_n30_.txt'),
        'sv_fp': to('data/'),
    }

    prot_df = reader().generic(DEFINE['list_fpn'])

    p = xml(prot_series=prot_df[0])

    print(p.pdbtm(
        sv_fp=DEFINE['sv_fp'],
        is_cmd=False
    ))