__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import pandas as pd

from Bio.PDB import PDBList

from tmkit.util.Kit import batchRename, delete, ungz, urlliby


class PDB:
    def __init__(
        self,
        prot_series: pd.Series,
    ) -> None:
        """
        Parameters
        ----------
        prot_series : pd.Series
            A Pandas series of protein names.
        """
        self.prot_dedup = prot_series.unique()

    def rcsb(self, sv_fp: str, route: str = "biopython") -> str:
        """
        Downloading a PDB file from RCSB PDB.

        file_format is specified with 'structure' to download a file
        with suffix of 'ent', which is totally the same with original
        format of file with suffix of 'structure', 'pdb'.

        See Also
        --------
        https://biopython.org/DIST/docs/api/Bio.PDB.PDBList%27-pysrc.html

        Parameters
        ----------
        sv_fp : str
            Path to save files.
        route : str, optional
            'biopython' or 'external', by default 'biopython'

        Returns
        -------
        str
            'Finished' if a PDB file is downloaded
        """
        pdb_list = PDBList()
        if route == "biopython":
            for i, prot_name in enumerate(self.prot_dedup):
                print(f"===>No.{i + 1} protein name: {prot_name}")
                pdb_list.retrieve_pdb_file(
                    pdb_code=str(prot_name),
                    file_format="pdb",
                    pdir=sv_fp,
                )
            batchRename(
                file_path=sv_fp,
                old_suffix="ent",
                new_suffix="pdb",
                flag=0,
            )
        else:
            for i, prot_name in enumerate(self.prot_dedup):
                print(f"===>No.{i + 1} protein name: {prot_name}")
                url = "https://files.rcsb.org/download/" + prot_name + ".pdb"
                urlliby(
                    url=url,
                    fpn=sv_fp + str(prot_name) + ".pdb",
                )
        return 'Finished'

    def pdbtm(self, sv_fp: str, kind: str = "tr") -> str:
        """
        Download PDB files from PDBTM.

        Parameters
        ----------
        sv_fp : str
            Path to save files.
        kind : str, optional
            'tr' for 'transformed proteins', '' for 'rcsb', by default 'tr'

        Notes
        -----
        Downloading a PDB file from PDBTM.

        Returns
        -------
        str
            'Finished' if a PDB file is successfully retrieved.
        """
        count = 0
        for i, prot_name in enumerate(self.prot_dedup):
            mark = str(prot_name[1] + prot_name[2])
            url = (
                "http://pdbtm.enzim.hu/data/database/"
                + mark
                + "/"
                + str(prot_name)
                + "."
                + kind
                + "pdb.gz"
            )
            print(f"===>No.{i + 1} protein name: {prot_name}")
            try:
                urlliby(url=url, fpn=sv_fp + str(prot_name) + ".gz")
                ungz(
                    file_path=sv_fp, file_name=prot_name, sv_fp=sv_fp, new_suffix=".pdb"
                )
                delete(sv_fp + str(prot_name) + ".gz")
            except:
                count = count + 1
                # print(count)
                continue
        return 'Finished'

    def alphafold(self, sv_fp: str) -> str:
        """
        Download a PDB file of a protein from the AlphaFold database.

        Parameters
        ----------
        sv_fp : str
            The path to save the downloaded PDB file.

        Examples
        --------
        >>> alphafold("Q5VSL9", "Q5VSL9.pdb")

        Returns
        -------
        str
            'Finished' if a PDB file is successfully retrieved.
        """
        import requests

        for i, uniprot_acc in enumerate(self.prot_dedup):
            url = f"https://alphafold.ebi.ac.uk/files/AF-{uniprot_acc}-F1-model_v4.pdb"
            result = requests.get(url, allow_redirects=True)
            if result.status_code == 200:
                with open(sv_fp + uniprot_acc + ".pdb", "wb") as f:
                    f.write(result.content)
            else:
                print(f"Failed to download. HTTP status code: {result.status_code}")
        return 'Finished'
