__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import json
import requests
import pandas as pd
from tmkit.util.Reader import reader as greader
from tmkit.util.Writer import writer
from tmkit.util.Kit import tactic7


class reader:

    def __init__(
            self,
    ):
        self.greader = greader()
        self.writer = writer()

    def api(self, identifier):
        """

        :param identifier: complex_name + chain_id + domain_id; e.g., 1h2sB00
        :return:
        """
        return {
            'domain': 'http://www.cathdb.info/version/v4_2_0/api/rest/domain_summary/' + identifier,
            'funfam': 'http://www.cathdb.info/version/v4_2_0/api/rest/superfamily/1.10.8.10/funfam/' + identifier,
            'superfamily': 'http://www.cathdb.info/version/v4_2_0/api/rest/superfamily/' + identifier,
        }

    def download(self, sv_fp, version='newest'):
        from tmkit.util.Kit import urlliby
        print('===>The CATH database of version ' + version + ' is being downloaded...')
        urlliby(
            url='ftp://orengoftp.biochem.ucl.ac.uk/cath/releases/daily-release/' + version + '/cath-b-' + version + '-all.gz',
            fpn=sv_fp + 'cath-b-' + version + '-all.gz',
        )
        print('===>The CATH database of version ' + version + ' is successfully downloaded!')
        print('===>The CATH database of version ' + version + ' is being decompressed...')
        from tmkit.util.Kit import ungz
        ungz(
            file_path=sv_fp,
            file_name='cath-b-' + version + '-all',
            sv_fp=sv_fp,
            new_suffix='.txt',
        )
        print('===>The CATH database of version ' + version + ' is successfully decompressed!')
        return 'Finished!'

    def fetch(self, domain_id, sort):
        """
        domain_id='4ni4H02', sort='domain'
        :param domain_id:
        :param sort:
        :return:
        """
        json = requests.get(self.api(domain_id)[sort]).json()
        if 'data' in json:
            # this is to avoid a domain in the file
            # exist but the domain via api does not exist.
            return json['data']
        else:
            return {}

    def domain(self, cath_fpn, groupby='version', group='v4_2_0'):
        print('======>reading CATH...')
        df_domain = self.greader.generic(df_fpn=cath_fpn, df_sep='\s+')
        df_domain = df_domain.rename(columns={
            0: 'domain',
            1: 'version',
            2: 'superfamily',
            3: 'bound',
        })
        print('======>CATH features are: '.format())
        for i, e in enumerate(df_domain.columns):
            print('=========>No.{}: {}'.format(i + 1, e))
        domain_info_grouped = df_domain.groupby(by=[groupby]).get_group(group)
        return domain_info_grouped

    def funfamsToJson(self, df_prot, df_domain, sv_fpn='./results.json', targets=['funfam_number']):
        complex_ids = df_domain['domain'].apply(lambda x: x[:4])
        chain_ids = df_domain['domain'].apply(lambda x: x[4])
        domain_ids = df_domain['domain'].apply(lambda x: x[5:])
        complex_info = pd.concat([complex_ids, chain_ids, domain_ids], axis=1).values.tolist()
        domain_dict = tactic7(complex_info)
        # print(domain_dict)
        cands = {}
        for i in df_prot.index:
            prot_name = df_prot.loc[i, 'prot']
            # seq_chain = self.df_prot.loc[i, 1]
            # print('----> No.{} protein {} chain {}'.format(i + 1, prot_name, seq_chain))
            print('======>No.{} protein complex: {}'.format(i + 1, prot_name))
            if prot_name in domain_dict.keys():
                cands[prot_name] = {}
                # if seq_chain in domain_dict[prot_name].keys():
                for seq_chain in domain_dict[prot_name].keys():
                    cands[prot_name][seq_chain] = {}
                    for domain_id in domain_dict[prot_name][seq_chain]:
                        print('=========>domain id is: {}'.format(prot_name + seq_chain + domain_id))
                        domain_data = self.fetch(
                            domain_id=prot_name + seq_chain + domain_id,
                            sort='domain'
                        )
                        cands[prot_name][seq_chain][domain_id] = {}
                        for target in targets:
                            if target in domain_data.keys():
                                cands[prot_name][seq_chain][domain_id][target] = domain_data[target]
        with open(sv_fpn, 'w') as fp:
            json.dump(cands, fp)
        print('======>The file is saved.')
        return cands