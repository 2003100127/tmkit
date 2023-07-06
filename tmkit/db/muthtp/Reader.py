__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import Dict

import pandas as pd

from tmkit.util.Reader import Reader as greader


class Reader:
    def __init__(self) -> None:
        self.greader = greader()

        self.muthtp_dz_std_keys: Dict[str, str] = {
            "cancers": "1",
            "Cancers": "1",
            "cardiovascular diseases": "2",
            "congenital disorders of metabolism": "3",
            "digestive system diseases": "4",
            "endocrine and metabolic diseases": "5",
            "immune system diseases": "6",
            "musculoskeletal diseases": "7",
            "nervous system diseases": "8",
            "other congenital disorders": "9",
            "urinary system diseases": "10",
            "reproductive system diseases": "11",
            "respiratory diseases": "12",
            "skin diseases": "13",
            "unknown": "14",
            "Not provided": "14",
            "-": "14",
            "nan": "-1",
        }
        self.muthtp_keys_std_dzs: Dict[str, str] = {
            "1": "cancers",
            "2": "cardiovascular diseases",
            "3": "congenital disorders of metabolism",
            "4": "digestive system diseases",
            "5": "endocrine and metabolic diseases",
            "6": "immune system diseases",
            "7": "musculoskeletal diseases",
            "8": "nervous system diseases",
            "9": "other congenital disorders",
            "10": "urinary system diseases",
            "11": "reproductive system diseases",
            "12": "respiratory diseases",
            "13": "skin diseases",
            "14": "unknown",
        }

    def fetch(self, sv_fp: str, version: str = "2020") -> str:
        """
        Download the MutHTP database of a specific version from GitHub.

        Parameters
        ----------
        sv_fp : str
            The file path to save the downloaded MutHTP database.
        version : str, optional
            The version of the MutHTP database to download, by default "2020".

        Returns
        -------
        str
            A message indicating the download is finished.
        """
        from tmkit.util.Kit import urlliby

        print(
            "===>The MutHTP database of version " + version + " is being downloaded..."
        )
        urlliby(
            url="https://github.com/2003100127/tmkit/releases/download/muthtp/MutHTP_"
            + version
            + ".zip",
            fpn=sv_fp + "MutHTP_" + version + ".zip",
        )
        print(
            "===>The MutHTP database of version "
            + version
            + " is successfully downloaded!"
        )
        print(
            "===>The MutHTP database of version "
            + version
            + " is being decompressed..."
        )
        import zipfile

        with zipfile.ZipFile(sv_fp + "MutHTP_" + version + ".zip", "r") as zip_ref:
            zip_ref.extractall(sv_fp)
        print(
            "===>The MutHTP database of version "
            + version
            + " is successfully decompressed!"
        )
        return "Finished!"

    def full(self, muthtp_fpn: str) -> pd.DataFrame:
        """
        Read the MutHTP database from a file.

        Parameters
        ----------
        muthtp_fpn : str
            The path to the MutHTP database file.

        Returns
        -------
        pd.DataFrame
            A pandas DataFrame containing the MutHTP database.
        """
        print("======>reading MutHTP...")
        all = self.greader.generic(muthtp_fpn, header=0)
        all = all.rename(
            columns={
                "Entry": "id",
                "genename": "gene_id",
                "uniportid": "uniprot_id",
                "type_of_mutation": "mutation_type",
                "chromosome_number": "chromosome_number",
                "origin": "origin_cell",
                "n_w": "nucleotide_mutation_site",
                "p_w": "protein_mutation_site",
                "pdbid": "pdb_id",
                "str_mut": "protein_structure_mutation_site",
                "exp_3d_str": "3D_structure",
                "interface": "interface",
                "domain": "transmembrane_domain",
                "top": "topology",
                "Disease": "disease",
                "dis_class": "disease_class",
                "isoform": "uniprot_id_isoform",
                "neighbour": "neighbouring_residue",
                "source": "source_database",
                "cs": "conservation_score",
                "exac_freq": "odds_ratio",
                "type_pass": "type_passing_membrane",
            }
        )
        print(f"======>MutHTP features are: ")
        for i, e in enumerate(all.columns):
            print(f"=========>No.{i + 1}: {e}")
        return all
