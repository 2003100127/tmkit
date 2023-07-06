__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import xml.etree.ElementTree as ET
from typing import List, Tuple
import numpy as np


class xml:
    """
    A class used to represent an XML parser.

    Attributes
    ----------
    prot_df : numpy.ndarray
        A numpy array containing protein data.
    """

    def __init__(self, prot_df: np.ndarray) -> None:
        """
        Constructs all the necessary attributes for the xml object.

        Parameters
        ----------
        prot_df : numpy.ndarray
            A numpy array containing protein data.
        """
        self.prot_df = prot_df

    def get(self, xml_fp: str, xml_name: str, seq_chain: str) -> str:
        """
        Parses an XML file and returns the sequence of a specific chain.

        Parameters
        ----------
        xml_fp : str
            The file path of the XML file.
        xml_name : str
            The name of the XML file.
        seq_chain : str
            The chain ID of the sequence to be returned.

        Returns
        -------
        str
            The sequence of the specified chain.
        """
        xml_fpn = xml_fp + xml_name + ".xml"
        tree = ET.parse(xml_fpn)
        parser_pdb = tree.getroot()
        for chains in parser_pdb:
            if chains.tag == "{http://pdbtm.enzim.hu}CHAIN":
                for seqs in chains.iter("{http://pdbtm.enzim.hu}SEQ"):
                    if chains.get("CHAINID") == seq_chain:
                        fasta_seq = "".join(seqs.text.split())
                        return fasta_seq

    def execute(self, xml_path: str, sv_fp: str) -> int:
        """
        Executes the XML parser and saves the sequences to a file.

        Parameters
        ----------
        xml_path : str
            The file path of the XML file.
        sv_fp : str
            The file path to save the sequences.

        Returns
        -------
        int
            0 if successful.
        """
        self.prot_df[2] = -1
        for i in range(self.prot_df.shape[0]):
            prot_name = self.prot_df[0][i]
            prot_chain = self.prot_df[1][i]
            if str(self.prot_df[1][i]).islower():
                file_chain = self.prot_df[1][i] + "l"
            else:
                file_chain = self.prot_df[1][i]
            seq = xml().get(
                xml_fp=xml_path,
                xml_name=self.prot_df.iloc[i][0],
                seq_chain=self.prot_df.iloc[i][1],
            )
            seq = re.sub(r"-", "", seq)
            seq = re.sub(r"\?", "", seq)
            f = open(sv_fp + prot_name + file_chain + ".fasta", "w")
            f.write(">" + prot_name + prot_chain + "\n")
            f.write(str(seq) + "\n")
            f.close()
        return 0
