__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import numpy as np
import pandas as pd
from tmkit.util.Reader import reader
from tmkit.util.Writer import writer
from tmkit.chain.Collate import collate
from tmkit.util.Kit import seqchainid
from tmkit.db.construct.Network import network as ppinet
from tmkit.name.Mapping import mapping as idmap


class connectivity:

    def __init__(
            self,
            prot_name,
            seq_chain,
            prot_idmap,
            interacting_partner_idmap,
            pdb_pdbtm_fp=None,
            pdb_rcsb_fp=None,
            sv_fpn=None,
            symbol='.',
    ):
        self.reader = reader()
        self.writer = writer()
        self.idmap = idmap()

        self.pdb_pdbtm_fp = pdb_pdbtm_fp
        self.pdb_rcsb_fp = pdb_rcsb_fp
        self.symbol = symbol
        self.sv_fpn = sv_fpn

        self.collate = collate(
            prot_name=prot_name,
            chain_focus=seq_chain,
            pdb_rcsb_fp=self.pdb_rcsb_fp,
            pdb_pdbtm_fp=self.pdb_pdbtm_fp,
        )

        self.df_collate = self.collate.df
        # print('===>df collated chains:\n {}'.format(self.df_collate))

        self.prot_collate_dict = self.collate.throwback(symbol=symbol)
        # print('===>collated {}'.format(self.prot_collate_dict))

        self.prot_master_idmap = self.idmap.pdb2uniprot(
            self.prot_collate_dict.keys()
        )

        self.prot_master_idmap = prot_idmap
        self.interacting_partner_idmap = interacting_partner_idmap

        self.switch2by = {
            'biogrid': [
                'SWISS-PROT Accessions Interactor A',
                'SWISS-PROT Accessions Interactor B',
            ],
            'intact': [
                '#ID(s) interactor A',
                'ID(s) interactor B',
            ],
        }

    def extract(self, ppi_db_fpns):
        """

        Parameters
        ----------
        ppi_db_fpns

        Returns
        -------

        """
        print('===>UniProt protein id: {}'.format(self.prot_master_idmap))
        for i, key in enumerate(self.prot_master_idmap.keys()):
            prot_name = key[:4]
            seq_chain = seqchainid(key[5])
            print('===>protein {} chain {}'.format(i+1, prot_name, seq_chain))
            master_networks = self.strategy(
                ppi_db_fpns=ppi_db_fpns,
                uniprot_id=key,
                is_del_reflexive=False,
                is_del_repeated=False,
                overlap=True,
            )
            print('======>interacting partners from the ppi databases:\n{}'.format(master_networks))
            len_master_nets = len(master_networks)

            print('======>interacting partner idmap: {}'.format(self.interacting_partner_idmap))
            ip_all = [*self.interacting_partner_idmap.keys()]
            print('======>interacting partners from its complex: {}'.format(ip_all))
            ip_uniprot_ids = [*self.interacting_partner_idmap.values()]
            print('======>uniprot ids of interacting partners from its complex:{}'.format(ip_uniprot_ids))
            count_ip_in_network = 0
            if len(master_networks[:, 1]) > 0:
                for ip in ip_uniprot_ids:
                    for ele_mnet in master_networks[:, 1].tolist():
                        if len(ele_mnet.split('|')) != 1:
                            print(ele_mnet.split('|'))  # e.g. ['P68187']
                        if ip in ele_mnet.split('|'):
                            count_ip_in_network += 1
            print('======>{} records found from the ppi databases'.format(len_master_nets))
            print('======>{} interacting partners from its complex'.format(len(ip_all)))
            print('======>{} interacting partners from its complex and found in the ppi databases as well'.format(
                count_ip_in_network)
            )

            self.df_collate.loc[i, 'num_overlapped_db'] = len_master_nets
            self.df_collate.loc[i, 'num_ip'] = len(ip_all)
            self.df_collate.loc[i, 'ip_chains'] = ''.join([i.split(self.symbol)[1] for i in ip_all])
            self.df_collate.loc[i, 'num_ip_overlapped_db'] = count_ip_in_network
        self.writer.generic(
            df=self.df_collate,
            sv_fpn=self.sv_fpn,
            header=True,
        )
        return self.df_collate

    def strategy(self, ppi_db_fpns, uniprot_id, is_del_reflexive, is_del_repeated, overlap=False):
        """

        Parameters
        ----------
        ppi_db_fpns
        uniprot_id
        is_del_reflexive
        is_del_repeated
        overlap

        Returns
        -------

        """
        res = {}
        for db_name, db_fpn in ppi_db_fpns.items():
            print('======>scanning ppi db: {}'.format(db_name))
            db_df = self.reader.generic(db_fpn, header=0, comment=None)
            res[db_name] = ppinet().single(
                interacting_df=db_df,
                uniprot_id=self.prot_master_idmap[uniprot_id],
                # uniprot_id=uniprot_id,
                by=self.switch2by[db_name],
                is_del_reflexive=is_del_reflexive,
                is_del_repeated=is_del_repeated,
            )
        if overlap:
            res_ = np.unique(np.concatenate([*res.values()], axis=0)[:, 1])
        else:
            if len(res.keys()) == 1:
                res_ = [*res.values()][0][:, 1]
                print('============>no overlap + len == 1')
            else:
                print('============>no overlap + len > 2')
                df1 = pd.DataFrame(res['biogrid'])
                df2 = pd.DataFrame(res['intact'])
                biogrid_gaps = df1[1].loc[df1[1].isin(['-'])].values.tolist()
                biogrid_non_gaps = df1[1].loc[~df1[1].isin(['-'])].values.tolist()
                intact_no_overlap = df2[1].loc[df2[1].isin(biogrid_non_gaps)].values.tolist()
                res_ = np.array(biogrid_gaps + biogrid_non_gaps + intact_no_overlap)
        # print(res_)
        # print(res_.shape[0])
        return np.concatenate(
            (np.array([uniprot_id] * res_.shape[0])[:, np.newaxis], res_[:, np.newaxis]),
            axis=1,
        )