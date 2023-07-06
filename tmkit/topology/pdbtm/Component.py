__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import xml.etree.ElementTree as ET
from functools import wraps


class Component:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __call__(self, deal):
        type = self.kwargs["type"]

        @wraps(deal)
        def scan(self, *args, **kwargs):
            # print(kwargs)
            xml_fpn = kwargs["xml_fp"] + kwargs["prot_name"] + ".xml"
            tree = ET.parse(xml_fpn)
            parser_pdb = tree.getroot()
            start_id = []
            last_id = []
            # print(parser_pdb)
            # for chains in parser_pdb.findall('CHAIN'):
            #     chain_name = chains.get('CHAINID')
            #     print(chain_name)
            # for regions in parser_pdb.iter('CHAIN'):
            #     print(regions.get('CHAINID'))
            # for regions in parser_pdb.iter('REGION'):
            #     print(regions.get('type'))
            # chain_mark = []
            for chains in parser_pdb:
                if chains.tag == "{http://pdbtm.enzim.hu}CHAIN":
                    for regions in chains.iter("{http://pdbtm.enzim.hu}REGION"):
                        if type == "side1":
                            if (
                                chains.get("CHAINID") == kwargs["seq_chain"]
                                and regions.get("type") == 1
                            ):
                                start_id.append(int(regions.get("pdb_beg")))
                                last_id.append(int(regions.get("pdb_end")))
                        elif type == "side2":
                            if (
                                chains.get("CHAINID") == kwargs["seq_chain"]
                                and regions.get("type") == 2
                            ):
                                start_id.append(int(regions.get("pdb_beg")))
                                last_id.append(int(regions.get("pdb_end")))
                        elif type == "alpha-helix":
                            if (
                                chains.get("CHAINID") == kwargs["seq_chain"]
                                and regions.get("type") == "H"
                            ):
                                start_id.append(int(regions.get("pdb_beg")))
                                last_id.append(int(regions.get("pdb_end")))
                        elif type == "non-alpha-helix":
                            if (
                                chains.get("CHAINID") == kwargs["seq_chain"]
                                and regions.get("type") != "H"
                            ):
                                start_id.append(int(regions.get("pdb_beg")))
                                last_id.append(int(regions.get("pdb_end")))
                        elif type == "beta-strand":
                            if (
                                chains.get("CHAINID") == kwargs["seq_chain"]
                                and regions.get("type") == "B"
                            ):
                                start_id.append(int(regions.get("pdb_beg")))
                                last_id.append(int(regions.get("pdb_end")))
                        elif type == "coil":
                            if (
                                chains.get("CHAINID") == kwargs["seq_chain"]
                                and regions.get("type") == "C"
                            ):
                                start_id.append(int(regions.get("pdb_beg")))
                                last_id.append(int(regions.get("pdb_end")))
                        elif type == "membrane-inside":
                            if (
                                chains.get("CHAINID") == kwargs["seq_chain"]
                                and regions.get("type") == "I"
                            ):
                                start_id.append(int(regions.get("pdb_beg")))
                                last_id.append(int(regions.get("pdb_end")))
                        elif type == "membrane-loop":
                            if (
                                chains.get("CHAINID") == kwargs["seq_chain"]
                                and regions.get("type") == "L"
                            ):
                                start_id.append(int(regions.get("pdb_beg")))
                                last_id.append(int(regions.get("pdb_end")))
                        elif type == "interfacial-helix":
                            if (
                                chains.get("CHAINID") == kwargs["seq_chain"]
                                and regions.get("type") == "F"
                            ):
                                start_id.append(int(regions.get("pdb_beg")))
                                last_id.append(int(regions.get("pdb_end")))
                        elif type == "unknown":
                            if (
                                chains.get("CHAINID") == kwargs["seq_chain"]
                                and regions.get("type") == "U"
                            ):
                                start_id.append(int(regions.get("pdb_beg")))
                                last_id.append(int(regions.get("pdb_end")))
                        else:
                            if chains.get("CHAINID") == kwargs["seq_chain"]:
                                start_id.append(int(regions.get("pdb_beg")))
                                last_id.append(int(regions.get("pdb_end")))
            # print(start_id, last_id)
            return deal(self, start_id, last_id)

        return scan
