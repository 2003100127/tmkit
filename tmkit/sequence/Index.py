__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"


class index:

    def __init__(self, sequence):
        self.sequence = sequence
        self.len_seq = len(self.sequence)

    def get(self):
        ids = []
        for id in range(self.len_seq):
            ids.append(id + 1)
        return ids