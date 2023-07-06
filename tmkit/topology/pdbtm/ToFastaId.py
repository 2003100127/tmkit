__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from tmkit.topology.pdbtm.Segment import Segment as fetchfasids


class toFastaId:
    def __init__(self, type="tmh"):
        self.type = type

    @fetchfasids(type="side1")
    def side1(
        self,
        start_id,
        last_id,
        fasid_map,
        pdbid_map,
        xml_fp="",
        prot_name="",
        seq_chain="",
    ):
        return start_id, last_id

    @fetchfasids(type="side2")
    def side2(
        self,
        start_id,
        last_id,
        fasid_map,
        pdbid_map,
        xml_fp="",
        prot_name="",
        seq_chain="",
    ):
        return start_id, last_id

    @fetchfasids(type="tmh")
    def tmh(
        self,
        start_id,
        last_id,
        fasid_map,
        pdbid_map,
        xml_fp="",
        prot_name="",
        seq_chain="",
    ):
        return start_id, last_id

    @fetchfasids(type="nontmh")
    def nontmh(
        self,
        start_id,
        last_id,
        fasid_map,
        pdbid_map,
        xml_fp="",
        prot_name="",
        seq_chain="",
    ):
        return start_id, last_id

    @fetchfasids(type="strand")
    def strand(
        self,
        start_id,
        last_id,
        fasid_map,
        pdbid_map,
        xml_fp="",
        prot_name="",
        seq_chain="",
    ):
        return start_id, last_id

    @fetchfasids(type="coil")
    def coil(
        self,
        start_id,
        last_id,
        fasid_map,
        pdbid_map,
        xml_fp="",
        prot_name="",
        seq_chain="",
    ):
        return start_id, last_id

    @fetchfasids(type="inside")
    def inside(
        self,
        start_id,
        last_id,
        fasid_map,
        pdbid_map,
        xml_fp="",
        prot_name="",
        seq_chain="",
    ):
        return start_id, last_id

    @fetchfasids(type="loop")
    def loop(
        self,
        start_id,
        last_id,
        fasid_map,
        pdbid_map,
        xml_fp="",
        prot_name="",
        seq_chain="",
    ):
        return start_id, last_id

    @fetchfasids(type="interfacial")
    def interfacial(
        self,
        start_id,
        last_id,
        fasid_map,
        pdbid_map,
        xml_fp="",
        prot_name="",
        seq_chain="",
    ):
        return start_id, last_id

    @fetchfasids(type="unknown")
    def unknown(
        self,
        start_id,
        last_id,
        fasid_map,
        pdbid_map,
        xml_fp="",
        prot_name="",
        seq_chain="",
    ):
        return start_id, last_id

    @fetchfasids(type="all")
    def all(
        self,
        start_id,
        last_id,
        fasid_map,
        pdbid_map,
        xml_fp="",
        prot_name="",
        seq_chain="",
    ):
        return start_id, last_id
