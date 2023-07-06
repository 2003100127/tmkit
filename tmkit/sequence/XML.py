__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import xml.etree.ElementTree as ET


class xml:

    def get(self, xml_fp, xml_name, seq_chain):
        xml_fpn = xml_fp + xml_name + '.xml'
        tree = ET.parse(xml_fpn)
        parser_pdb = tree.getroot()
        for chains in parser_pdb:
            if chains.tag == '{http://pdbtm.enzim.hu}CHAIN':
                for seqs in chains.iter('{http://pdbtm.enzim.hu}SEQ'):
                    if chains.get('CHAINID') == seq_chain:
                        # print(seqs.text)
                        fasta_seq = ''.join(seqs.text.split())
                        return fasta_seq

    def execute(self, xml_path, sv_fp):
        self.prot_df[2] = -1
        for i in range(self.prot_df.shape[0]):
            prot_name = self.prot_df[0][i]
            prot_chain = self.prot_df[1][i]
            if str(self.prot_df[1][i]).islower():
                file_chain = self.prot_df[1][i] + 'l'
            else:
                file_chain = self.prot_df[1][i]
            seq = xml().get(
                xml_path=xml_path,
                xml_name=self.prot_df.iloc[i][0],
                seq_chain=self.prot_df.iloc[i][1]
            )
            seq = re.sub(r'-', '', seq)
            seq = re.sub(r'\?', '', seq)
            f = open(sv_fp + prot_name + file_chain + '.fasta', 'w')
            f.write('>' + prot_name + prot_chain + '\n')
            f.write(str(seq) + '\n')
            f.close()
        return 0