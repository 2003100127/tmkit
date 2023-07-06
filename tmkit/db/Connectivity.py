__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import Dict, List

import numpy as np
import pandas as pd

from tmkit.chain.Collate import Collate
from tmkit.db.construct.Network import Network as ppinet
from tmkit.name.Mapping import Mapping as idmap
from tmkit.util.Kit import seqchainid
from tmkit.util.Reader import Reader as greader
from tmkit.util.Writer import Writer as gwriter


class Connectivity:
    def __init__(
        self,
        prot_name: str,
        seq_chain: str,
        prot_idmap: Dict,
        interacting_partner_idmap: Dict,
        pdb_pdbtm_fp: str=None,
        pdb_rcsb_fp: str=None,
        sv_fpn: str=None,
        symbol: str=".",
    ):
        """

        Parameters
        ----------
        prot_name : str
            name of a protein in the prefix of a PDB file name (e.g., 1xqf in 1xqfA.pdb).
        seq_chain : str
            chain of a protein in the prefix of a PDB file name (e.g., A in 1xqfA.pdb) (biological purpose).
        sv_fp : str
            path to where you want to save files.
        prot_idmap : Dict
            a Python dict with key -> value for PDB ID -> UniProt accession code (please see the command below for details).
        interacting_partner_idmap : Dict
            a Python dict with key -> value for PDB ID -> UniProt accession code (please see the command below for details).
        pdb_rcsb_fp : str
            path where a target PDB file is placed..
        pdb_pdbtm_fp : str
            path where a target PDB file is placed..
        ppi_db_fpns : str
            paths where interaction databases are placed (e.g., BIOGRID-ALL-4.4.212.biogrid and interA_B.intact).
        symbol : str
            '.'
        """
        self.reader = greader()
        self.writer = gwriter()
        self.idmap = idmap()

        self.pdb_pdbtm_fp = pdb_pdbtm_fp
        self.pdb_rcsb_fp = pdb_rcsb_fp
        self.symbol = symbol
        self.sv_fpn = sv_fpn

        self.collate = Collate(
            prot_name=prot_name,
            chain_focus=seq_chain,
            pdb_rcsb_fp=self.pdb_rcsb_fp,
            pdb_pdbtm_fp=self.pdb_pdbtm_fp,
        )

        self.df_collate = self.collate.df
        print(f"===>df collated chains:\n {self.df_collate}")

        self.prot_collate_dict = self.collate.throwback(symbol=symbol)
        print(f"===>collated {self.prot_collate_dict}")

        self.prot_master_idmap = self.idmap.pdb2uniprot(pdb_ids=self.prot_collate_dict.keys())

        self.prot_master_idmap = prot_idmap
        self.interacting_partner_idmap = interacting_partner_idmap

        self.switch2by = {
            "biogrid": [
                "SWISS-PROT Accessions Interactor A",
                "SWISS-PROT Accessions Interactor B",
            ],
            "intact": [
                "#ID(s) interactor A",
                "ID(s) interactor B",
            ],
        }

    def extract(self, ppi_db_fpns: Dict) -> pd.DataFrame:
        """
        Get PPI networks.

        Parameters
        ----------
        ppi_db_fpns : str
            Paths where interaction databases are placed (e.g., BIOGRID-ALL-4.4.212.biogrid and interA_B.intact).

        Returns
        -------
        pd.DataFrame
            PPI networks
        """
        print(f"===>UniProt protein id: {self.prot_master_idmap}")
        for i, key in enumerate(self.prot_master_idmap.keys()):
            prot_name = key[:4]
            seq_chain = seqchainid(key[5])
            print(f"===>protein {i + 1} chain {prot_name}")
            master_networks = self.strategy(
                ppi_db_fpns=ppi_db_fpns,
                uniprot_id=key,
                is_del_reflexive=False,
                is_del_repeated=False,
                overlap=True,
            )
            print(
                "======>interacting partners from the ppi databases:\n{}".format(
                    master_networks
                )
            )
            len_master_nets = len(master_networks)

            print(
                "======>interacting partner idmap: {}".format(
                    self.interacting_partner_idmap
                )
            )
            ip_all = [*self.interacting_partner_idmap.keys()]
            print(f"======>interacting partners from its complex: {ip_all}")
            ip_uniprot_ids = [*self.interacting_partner_idmap.values()]
            print(
                "======>uniprot ids of interacting partners from its complex:{}".format(
                    ip_uniprot_ids
                )
            )
            count_ip_in_network = 0
            if len(master_networks[:, 1]) > 0:
                for ip in ip_uniprot_ids:
                    for ele_mnet in master_networks[:, 1].tolist():
                        if len(ele_mnet.split("|")) != 1:
                            print(ele_mnet.split("|"))  # e.g. ['P68187']
                        if ip in ele_mnet.split("|"):
                            count_ip_in_network += 1
            print(f"======>{len_master_nets} records found from the ppi databases")
            print(f"======>{len(ip_all)} interacting partners from its complex")
            print(
                "======>{} interacting partners from its complex and found in the ppi databases as well".format(
                    count_ip_in_network
                )
            )

            self.df_collate.loc[i, "num_overlapped_db"] = len_master_nets
            self.df_collate.loc[i, "num_ip"] = len(ip_all)
            self.df_collate.loc[i, "ip_chains"] = "".join(
                [i.split(self.symbol)[1] for i in ip_all]
            )
            self.df_collate.loc[i, "num_ip_overlapped_db"] = count_ip_in_network
        self.writer.generic(
            df=self.df_collate,
            sv_fpn=self.sv_fpn,
            header=True,
        )
        return self.df_collate

    def strategy(
        self, ppi_db_fpns: Dict,
        uniprot_id: str,
        is_del_reflexive: bool,
        is_del_repeated: bool,
        overlap: bool=False
    ) -> np.ndarray:
        """
        Get PPI networks.

        Parameters
        ----------
        ppi_db_fpns : str
            Paths where interaction databases are placed (e.g., BIOGRID-ALL-4.4.212.biogrid and interA_B.intact).
        uniprot_id : str
            UniProt accession code.
        is_del_reflexive : bool
            if deleted reflexive ones. False by default.
        is_del_repeated : bool
            if deleted repeated ones. False by default.
        overlap: bool
            False by default.
        Returns
        -------
        np.ndarray
            PPI networks

        """
        res = {}
        for db_name, db_fpn in ppi_db_fpns.items():
            print(f"======>scanning ppi db: {db_name}")
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
                print("============>no overlap + len == 1")
            else:
                print("============>no overlap + len > 2")
                df1 = pd.DataFrame(res["biogrid"])
                df2 = pd.DataFrame(res["intact"])
                biogrid_gaps = df1[1].loc[df1[1].isin(["-"])].values.tolist()
                biogrid_non_gaps = df1[1].loc[~df1[1].isin(["-"])].values.tolist()
                intact_no_overlap = (
                    df2[1].loc[df2[1].isin(biogrid_non_gaps)].values.tolist()
                )
                res_ = np.array(biogrid_gaps + biogrid_non_gaps + intact_no_overlap)
        # print(res_)
        # print(res_.shape[0])
        return np.concatenate(
            (
                np.array([uniprot_id] * res_.shape[0])[:, np.newaxis],
                res_[:, np.newaxis],
            ),
            axis=1,
        )
