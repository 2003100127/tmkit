__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import Tuple, Dict

import pandas as pd

from tmkit.topology.pdbtm.ToFastaId import toFastaId
from tmkit.topology.Phobius import Phobius


class determine:
    def ce(
        self,
        pred_fp,
        prot_name,
        seq_chain,
        pdbid_map,
        fasid_map,
        xml_fp,
    ) -> Tuple[Dict, Dict]:
        """

        Parameters
        ----------
        pred_fp
            A topo file, i.e., Phobius or TMHMM
        prot_name : str
            name of a protein in the prefix of a PDB file name (e.g., 1xqf in 1xqfA.pdb).
        seq_chain : str
            chain of a protein in the prefix of a PDB file name (e.g., A in 1xqfA.pdb) (biological purpose).
        pdbid_map
            Dictionary mapping PDB residue IDs to amino acid symbols.
        fasid_map
            A dictionary of FASTA IDs and their corresponding sequences.
        xml_fp
            path where a target XML file is placed.
        Returns
        -------

        """
        fasta_lower_nontmh, fasta_upper_nontmh = toFastaId().nontmh(
            pdbid_map=pdbid_map,
            fasid_map=fasid_map,
            xml_fp=xml_fp,
            prot_name=prot_name,
            seq_chain=seq_chain,
        )
        # print(fasta_lower_nontmh)
        # print(fasta_upper_nontmh)
        fasta_lower_tmh, fasta_upper_tmh = toFastaId().tmh(
            pdbid_map=pdbid_map,
            fasid_map=fasid_map,
            xml_fp=xml_fp,
            prot_name=prot_name,
            seq_chain=seq_chain,
        )
        # print(fasta_lower_tmh)
        # print(fasta_upper_tmh)
        w = Phobius()
        df = w.format(phobius_fpn=pred_fp + prot_name + seq_chain + '.jphobius')
        pred_seg = w.extract(df=df)
        # print(pred_seg)
        pdbtm_seg = {}
        pdbtm_seg["tmh_lower"] = fasta_lower_tmh
        pdbtm_seg["tmh_upper"] = fasta_upper_tmh
        pdbtm_seg["cyto_lower"] = []
        pdbtm_seg["cyto_upper"] = []
        pdbtm_seg["extra_lower"] = []
        pdbtm_seg["extra_upper"] = []
        # print(pdbtm_seg)
        # print(len(fasta_upper_nontmh))
        # print(len(fasta_lower_nontmh))
        for i, e in enumerate(fasta_lower_nontmh):
            # print('No. ', i)
            i1 = pd.Interval(e, fasta_upper_nontmh[i], closed="both")
            ic_accumulator = 0
            for j, m in enumerate(pred_seg["cyto_lower"]):
                ic = pd.Interval(m, pred_seg["cyto_upper"][j], closed="both")
                if i1.overlaps(ic):
                    # print('---> r', i1)
                    # print('---> c', ic)
                    left_max = max(ic.left, i1.left)
                    right_min = min(ic.right, i1.right)
                    ic_accumulator = ic_accumulator + (right_min - left_max)
                    # print(ic_accumulator)
            ie_accumulator = 0
            for k, n in enumerate(pred_seg["extra_lower"]):
                ie = pd.Interval(n, pred_seg["extra_upper"][k], closed="both")
                if i1.overlaps(ie):
                    # print('---> r', i1)
                    # print('---> e', ie)
                    left_max = max(ie.left, i1.left)
                    right_min = min(ie.right, i1.right)
                    ie_accumulator = ie_accumulator + (right_min - left_max)
                    # print(ie_accumulator)
                    # print(right_min-left_max)
            if ic_accumulator >= ie_accumulator:
                pdbtm_seg["cyto_lower"].append(i1.left)
                pdbtm_seg["cyto_upper"].append(i1.right)
            else:
                pdbtm_seg["extra_lower"].append(i1.left)
                pdbtm_seg["extra_upper"].append(i1.right)
        return pdbtm_seg, pred_seg
