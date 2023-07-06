__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from tmkit.topology.pdbtm.Segment import segment


class tmh:

    def __init__(self, xml_fp, prot_name, seq_chain):
        self.xml_fp = xml_fp
        self.prot_name = prot_name
        self.seq_chain = seq_chain

    def get(self):
        """
        ..  @description:
            -------------
            # tree = ET.parse(self.xml_fpn)
            # parser_pdb = tree.getroot()
            # start_id = []
            # last_id = []
            # for chains in parser_pdb:
            #     # print(chains.tag)
            #     if chains.tag == '{http://pdbtm.enzim.hu}CHAIN':
            #         # print(chains.tag)
            #         for regions in chains.iter('{http://pdbtm.enzim.hu}REGION'):
            #             # print(chains.get('CHAINID'), len(regions.get('type')))
            #             if chains.get('CHAINID') == self.seq_chain and regions.get('type') == 'H':
            #                 start_id.append(int(regions.get('pdb_beg')))
            #                 last_id.append(int(regions.get('pdb_end')))
        :return:
        """
        start_id, last_id = segment().tmh(
            xml_fp=self.xml_fp,
            prot_name=self.prot_name,
            seq_chain=self.seq_chain,
        )
        return start_id, last_id