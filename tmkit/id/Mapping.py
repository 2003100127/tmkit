__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import numpy as np
from tmkit.util.Reader import reader as tmkreader


class mapping:

    def tofas(
            self,
            pdbid_map,
            fasid_map,
            pdb_lower,
            pdb_upper,
    ):
        """

        Notes
        -----
            mapping fasta id from pdb id.

        Parameters
        ----------
        pdbid_map
        fasid_map
        pdb_lower
            lower 1d list of pdb ids
        pdb_upper
            upper 1d list of pdb ids

        Returns
        -------

        """
        pdb_fas_id_map = dict(zip([*pdbid_map.keys()], [*fasid_map.keys()]))
        pdb_ids = [*pdbid_map.keys()]
        pdb_seg_lower = np.array(pdb_lower)
        pdb_seg_upper = np.array(pdb_upper)
        # print('=========>Segment lower pdb id: {}'.format(pdb_seg_lower))
        # print('=========>Segment upper pdb id: {}'.format(pdb_seg_upper))
        fasta_seg_lower = []
        fasta_seg_upper = []
        num_segments = pdb_seg_lower.shape[0]
        for j in range(num_segments):
            if pdb_seg_lower[j] in pdb_ids:
                fasta_seg_lower.append(pdb_fas_id_map[pdb_seg_lower[j]])
                fasta_seg_upper.append(pdb_fas_id_map[pdb_seg_upper[j]])
            else:
                continue
        # print('=========>Segment lower fasta id: {}'.format(fasta_seg_lower))
        # print('=========>Segment upper fasta id: {}'.format(fasta_seg_upper))
        return fasta_seg_lower, fasta_seg_upper

    def entryConvert(
            self,
            id,
            ref_fpn,
            mode,
    ):
        df = tmkreader().generic(df_fpn=ref_fpn, df_sep=',', header=0)
        # print(df)
        if mode == 'pdb -> uniprot':
            tar = df.loc[df['PDB'].isin([id.split('.')[0]])].drop_duplicates(['PDB'])['SP_PRIMARY'].values
            if tar:
                return tar[0]
            else:
                return 'currently no accession id!'
        elif mode == 'uniprot -> pdb':
            tar = df.loc[df['SP_PRIMARY'].isin([id])].drop_duplicates(['SP_PRIMARY'])[['PDB', 'CHAIN']].values
            if len(tar) >= 1:
                return '.'.join(tar[0])
            else:
                return 'currently no accession id!'
