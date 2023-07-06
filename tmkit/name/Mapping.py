__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"


from typing import Any, Dict, List, Union

import xml.etree.ElementTree as ET

import requests


class Mapping:
    """
    Class for mapping various types of protein sequence identifiers.
    """

    def __init__(self) -> None:
        """
        Initialization of the Mapping class with necessary endpoints.
        """
        self.BASE = "http://www.uniprot.org"
        self.KB_ENDPOINT = "/uniprot/"
        self.TOOL_ENDPOINT = "/uploadlists/"

    def uniprot_programmatically_py3(
        self,
        ids2map: Union[List[str], str],
        source_fmt: str = "ACC+ID",
        target_fmt: str = "ACC",
        output_fmt: str = "list",
    ) -> str:
        """
        Maps IDs from one format to another using the UniProt API.

        Parameters
        ----------
        ids2map : Union[List[str], str]
            The IDs to map.
        source_fmt : str, optional
            The format of the source IDs, by default "ACC+ID".
        target_fmt : str, optional
            The format of the target IDs, by default "ACC".
        output_fmt : str, optional
            The output format, by default "list".

        Returns
        -------
        str
            The result of the mapping request.

        References
        ----------
        .. [1] https://www.uniprot.org/help/api_idmapping
        .. [2] https://www.ebi.ac.uk/training/online/sites/ebi.ac.uk.training.online/files/UniProt_programmatically_py3.pdf
        """
        if hasattr(ids2map, "pop"):
            ids2map = " ".join(ids2map)
        payload = {
            "from": source_fmt,
            "to": target_fmt,
            "format": output_fmt,
            "query": ids2map,
        }
        response = requests.get(self.BASE + self.TOOL_ENDPOINT, params=payload)
        if response.ok:
            return response.text
        else:
            response.raise_for_status()

    def uniprot_id(self, response_xml: str) -> str:
        """
        Extracts UniProt ID from the given XML string.

        Parameters
        ----------
        response_xml : str
            XML string to parse.

        Returns
        -------
        str
            The UniProt ID extracted from the XML string.
        """
        root = ET.fromstring(response_xml, parser=ET.XMLParser(encoding="utf-8"))
        return next(
            el
            for el in root.getchildren()[0].getchildren()
            if el.attrib["dbSource"] == "UniProt"
        ).attrib["dbAccessionId"]

    def uniprot_name(self, uniport_id: str) -> str:
        """
        Retrieves the name of a UniProt entry given its ID.

        Parameters
        ----------
        uniport_id : str
            The UniProt ID to get the name of.

        Returns
        -------
        str
            The name of the UniProt entry.
        """
        uniprot_url = "http://www.uniprot.org/uniprot/{}.xml"
        uinprot_response = requests.get(uniprot_url.format(uniport_id)).text
        return (
            ET.fromstring(uinprot_response)
            .find(
                ".//{http://uniprot.org/uniprot}recommendedName/{http://uniprot.org/uniprot}fullName"
            )
            .text
        )

    def pdb2uniprot(self, pdb_ids: List[str] = ["1aij.L"]) -> Dict[str, str]:
        """
        Converts PDB IDs to UniProt IDs.

        Parameters
        ----------
        pdb_ids : List[str], optional
            The list of PDB IDs to convert, by default ["1aij.L"].

        Returns
        -------
        Dict[str, str]
            A dictionary mapping PDB IDs to UniProt IDs.
        """
        pdb_mapping_url = (
            "http://www.rcsb.org/pdb/rest/das/pdb_uniprot_mapping/alignment"
        )
        mapping_ids = {}
        for id in pdb_ids:
            try:
                pdb_mapping_xml = requests.get(
                    pdb_mapping_url, params={"query": id}
                ).text
                print(pdb_mapping_xml)
                mapping_ids[id] = self.uniprot_id(response_xml=pdb_mapping_xml)
            except:
                mapping_ids[id] = "no accession"
                # uniprot_name = self.uniprot_name(uniprot_id)
        return mapping_ids
