__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import time
from tmkit.util.Reader import reader


class label:

    def __init__(self, dist_path, prot_name, file_chain, cutoff=6):
        self.prot_name = prot_name
        self.file_chain = file_chain
        self.dist_fpn = dist_path + self.prot_name + self.file_chain + '.dist'
        self.cutoff = cutoff
        self.read = reader()

    def attach(self):
        start_time = time.time()
        dist_df = self.read.generic(self.dist_fpn)
        dists = dist_df.iloc[:, 3:]
        dist_mins = dists.min(axis=1)
        # print(dist_mins)
        inter_ids = dist_mins.loc[dist_mins < self.cutoff].index.tolist()
        noninter_ids = dist_mins.loc[dist_mins >= self.cutoff].index.tolist()
        dist_df['is_contact'] = -1
        dist_df.loc[inter_ids, 'is_contact'] = 1
        dist_df.loc[noninter_ids, 'is_contact'] = 0
        columns = ['fasta_id', 'aa', 'pdb_id']
        for i in range(dists.shape[1]):
            columns.append('dist_' + str(i+1))
        columns.append('is_contact')
        dist_df.columns = columns
        end_time = time.time()
        print('======>Time to read&label distances for {} {}: {}s.'.format(self.prot_name, self.file_chain, end_time - start_time))
        return dist_df