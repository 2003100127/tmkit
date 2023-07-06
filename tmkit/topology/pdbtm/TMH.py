__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"

from typing import List, Tuple

from tmkit.topology.pdbtm.Segment import Segment


class TMH:
    def __init__(self, xml_fp: str, prot_name: str, seq_chain: str) -> None:
        """
        Initialize a TMH object.

        Parameters
        ----------
        xml_fp : str
            The filepath of the XML file.
        prot_name : str
            The name of the protein.
        seq_chain : str
            The sequence chain of the protein.

        Returns
        -------
        None
        """
        self.xml_fp = xml_fp
        self.prot_name = prot_name
        self.seq_chain = seq_chain

    def get(self) -> Tuple[List[int], List[int]]:
        """
        Get the start and end positions of the transmembrane helices.

        Returns
        -------
        Tuple[List[int], List[int]]
            A tuple containing two lists: the start positions and the end positions of the transmembrane helices.
        """
        start_id, last_id = Segment().tmh(
            xml_fp=self.xml_fp,
            prot_name=self.prot_name,
            seq_chain=self.seq_chain,
        )
        return start_id, last_id
