__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from functools import wraps

from tmkit.id.Mapping import mapping as pdbid
from tmkit.topology.pdbtm.Component import component


class segment:
    def __init__(self, type="tmh"):
        self.type = type

    def __call__(self, deal):
        if self.type == "side1":
            segment = self.side1
        elif self.type == "side2":
            segment = self.side2
        elif self.type == "tmh":
            segment = self.tmh
        elif self.type == "nontmh":
            segment = self.nontmh
        elif self.type == "strand":
            segment = self.strand
        elif self.type == "coil":
            segment = self.coil
        elif self.type == "inside":
            segment = self.inside
        elif self.type == "loop":
            segment = self.loop
        elif self.type == "interfacial":
            segment = self.interfacial
        elif self.type == "unknown":
            segment = self.unknown
        elif self.type == "all":
            segment = self.all

        @wraps(deal)
        def switch(ph, *args, **kwargs):
            # print(args)
            # print(kwargs)
            # print(kwargs.keys())
            pdb_lower, pdb_upper = segment(
                xml_fp=kwargs["xml_fp"],
                prot_name=kwargs["prot_name"],
                seq_chain=kwargs["seq_chain"],
            )
            # print('PDBTM region:\n lower: {}\n upper: {}'.format(pdb_lower, pdb_upper))
            fas_lower, fas_upper = pdbid().tofas(
                pdbid_map=kwargs["pdbid_map"],
                fasid_map=kwargs["fasid_map"],
                pdb_lower=pdb_lower,
                pdb_upper=pdb_upper,
            )
            # print('FASTA region:\n lower: {}\n upper: {}'.format(fas_lower, fas_upper))
            return deal(ph, fas_lower, fas_upper, **kwargs)

        return switch

    @component(type="side1")
    def side1(self, start_id, last_id, xml_fp="", prot_name="", seq_chain=""):
        return start_id, last_id

    @component(type="side2")
    def side2(self, start_id, last_id, xml_fp="", prot_name="", seq_chain=""):
        return start_id, last_id

    @component(type="alpha-helix")
    def tmh(self, start_id, last_id, xml_fp="", prot_name="", seq_chain=""):
        return start_id, last_id

    @component(type="non-alpha-helix")
    def nontmh(self, start_id, last_id, xml_fp="", prot_name="", seq_chain=""):
        return start_id, last_id

    @component(type="beta-strand")
    def strand(self, start_id, last_id, xml_fp="", prot_name="", seq_chain=""):
        return start_id, last_id

    @component(type="coil")
    def coil(self, start_id, last_id, xml_fp="", prot_name="", seq_chain=""):
        return start_id, last_id

    @component(type="membrane-inside")
    def inside(self, start_id, last_id, xml_fp="", prot_name="", seq_chain=""):
        return start_id, last_id

    @component(type="membrane-loop")
    def loop(self, start_id, last_id, xml_fp="", prot_name="", seq_chain=""):
        return start_id, last_id

    @component(type="interfacial-helix")
    def interfacial(self, start_id, last_id, xml_fp="", prot_name="", seq_chain=""):
        return start_id, last_id

    @component(type="unknown")
    def unknown(self, start_id, last_id, xml_fp="", prot_name="", seq_chain=""):
        return start_id, last_id

    @component(type="all")
    def all(self, start_id, last_id, xml_fp="", prot_name="", seq_chain=""):
        return start_id, last_id
