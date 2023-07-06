__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import Dict, List, Tuple

import numpy as np

from tmkit.util.Reader import Reader as tmkreader


class Mapping:
    def tofas(
        self,
        pdbid_map: Dict[str, str],
        fasid_map: Dict[str, str],
        pdb_lower: List[str],
        pdb_upper: List[str],
    ) -> Tuple[List[str], List[str]]:
        """
        Map fasta id from pdb id.

        Parameters
        ----------
        pdbid_map : dict
            Dictionary mapping pdb ids to fasta ids.
        fasid_map : dict
            Dictionary mapping fasta ids to pdb ids.
        pdb_lower : list
            Lower 1d list of pdb ids.
        pdb_upper : list
            Upper 1d list of pdb ids.

        Returns
        -------
        Tuple of two lists
            Lower and upper fasta ids.
        """
        pdb_fas_id_map = dict(zip([*pdbid_map.keys()], [*fasid_map.keys()]))
        pdb_ids = [*pdbid_map.keys()]
        pdb_seg_lower = np.array(pdb_lower)
        pdb_seg_upper = np.array(pdb_upper)
        print(f"=========>Segment lower pdb id: {pdb_seg_lower}")
        print(f"=========>Segment upper pdb id: {pdb_seg_upper}")
        fasta_seg_lower = []
        fasta_seg_upper = []
        num_segments = pdb_seg_lower.shape[0]
        for j in range(num_segments):
            if pdb_seg_lower[j] in pdb_ids:
                fasta_seg_lower.append(pdb_fas_id_map[pdb_seg_lower[j]])
                fasta_seg_upper.append(pdb_fas_id_map[pdb_seg_upper[j]])
            else:
                continue
        print(f"=========>Segment lower fasta id: {fasta_seg_lower}")
        print(f"=========>Segment upper fasta id: {fasta_seg_upper}")
        return fasta_seg_lower, fasta_seg_upper

    def entry_convert(
        self,
        id: str,
        ref_fpn: str,
        mode: str,
    ) -> str:
        """
        Convert between pdb and uniprot ids.

        Parameters
        ----------
        id : str
            PDB or UniProt accession code.
        ref_fpn : str
            Reference file for conversion between PDB IDs and UniProt accession codes.
        mode : str
            Conversion mode, either "pdb -> uniprot" or "uniprot -> pdb".

        Returns
        -------
        str
            Converted id.
        """
        df = tmkreader().generic(df_fpn=ref_fpn, df_sep=",", header=0)
        # print(df)
        if mode == "pdb -> uniprot":
            tar = (
                df.loc[df["PDB"].isin([id.split(".")[0]])]
                .drop_duplicates(["PDB"])["SP_PRIMARY"]
                .values
            )
            if tar:
                return tar[0]
            else:
                return "currently no accession id!"
        elif mode == "uniprot -> pdb":
            tar = (
                df.loc[df["SP_PRIMARY"].isin([id])]
                .drop_duplicates(["SP_PRIMARY"])[["PDB", "CHAIN"]]
                .values
            )
            if len(tar) >= 1:
                return ".".join(tar[0])
            else:
                return "currently no accession id!"
