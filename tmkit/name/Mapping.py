__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import requests
import xml.etree.ElementTree as ET
import pypdb


class mapping:

    def __init__(self, ):
        self.BASE = 'http://www.uniprot.org'
        self.KB_ENDPOINT = '/uniprot/'
        self.TOOL_ENDPOINT = '/uploadlists/'

    def uniprot_programmatically_py3(self, ids2map, source_fmt='ACC+ID', target_fmt='ACC', output_fmt='list'):
        """
        ..  @description:
            -------------
            https://www.uniprot.org/help/api_idmapping

        ..  @see:
            -----
            https://www.ebi.ac.uk/training/online/sites/ebi.ac.uk.training.online/files/UniProt_programmatically_py3.pdf

        :param ids2map:
        :param source_fmt:
        :param target_fmt:
        :param output_fmt:
        :return:
        """
        if hasattr(ids2map, 'pop'):
            ids2map = ' '.join(ids2map)
        payload = {
            'from': source_fmt,
            'to': target_fmt,
            'format': output_fmt,
            'query': ids2map,
        }
        response = requests.get(self.BASE + self.TOOL_ENDPOINT, params=payload)
        if response.ok:
            return response.text
        else:
            response.raise_for_status()

    def uniprot_id(self, response_xml):
        root = ET.fromstring(response_xml, parser=ET.XMLParser(encoding='utf-8'))
        return next(
            el for el in root.getchildren()[0].getchildren()
            if el.attrib['dbSource'] == 'UniProt'
        ).attrib['dbAccessionId']

    def uniprot_name(self, uniport_id):
        uniprot_url = 'http://www.uniprot.org/uniprot/{}.xml'
        uinprot_response = requests.get(
            uniprot_url.format(uniport_id)
        ).text
        return ET.fromstring(uinprot_response).find(
            './/{http://uniprot.org/uniprot}recommendedName/{http://uniprot.org/uniprot}fullName'
            ).text

    def pdb2uniprot(self, pdb_ids=['1aij.L']):
        """

        :param pdb_ids:
        :return:
        """
        pdb_mapping_url = 'http://www.rcsb.org/pdb/rest/das/pdb_uniprot_mapping/alignment'
        mapping_ids = {}
        for id in pdb_ids:
            try:
                pdb_mapping_xml = requests.get(
                    pdb_mapping_url, params={'query': id}
                ).text
                # print(pdb_mapping_xml)
                mapping_ids[id] = self.uniprot_id(response_xml=pdb_mapping_xml)
            except:
                mapping_ids[id] = 'no accession'
            # uniprot_name = self.uniprot_name(uniprot_id)
        return mapping_ids

    def pypdb(self, pdb_ids=['1aij.L', '1aij.M']):
        mapping_ids = {}
        for id in pdb_ids:
            try:
                mapping_ids[id] = pypdb.get_all_info(id)['polymer']['macroMolecule']['accession']['@id']
            except:
                mapping_ids[id] = 'no accession'
            # else:
            #     print(mapping_ids[id])
        return mapping_ids