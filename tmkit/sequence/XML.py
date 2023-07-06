__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import xml.etree.ElementTree as ET


class XML:
    """
    A class used to represent an XML parser.

    Attributes
    ----------
    prot_df : numpy.ndarray
        A numpy array containing protein data.
    """

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
