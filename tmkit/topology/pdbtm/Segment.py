__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from functools import wraps

from tmkit.id.Mapping import Mapping as pdbid
from tmkit.topology.pdbtm.Component import Component


class Segment:
    def __init__(self, type: str="tmh"):
        """

        Parameters
        ----------
        type: str
            A topology code. It can be one of side1, side2, strand,
            tmh, coil, inside, loop, interfacial, and Unknown,
            which correspond to Side1, Side2, Beta strand, Alpha
            helix, Coil, Membrane-inside, Membrane-loop,
            Interfacial, Unknown topologies.
        """
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

    @Component(type="side1")
    def side1(self, start_id, last_id, xml_fp="", prot_name="", seq_chain=""):
        """Return output of side1 topology, lower bounds (start_id) are the set of
        starting positions of residues in the PDB structure
        while upper bounds (last_id) are the set of ending positions
        of residues in the PDB structure. They match
        each other this way. For example, for topology
        Side2, the first continuous segment is from
        residue 3 to residue 14, and the second one is
        from residue 65 to residue 101, ..., and the last
        one is from residue 333 to residue 352."""
        return start_id, last_id

    @Component(type="side2")
    def side2(self, start_id, last_id, xml_fp="", prot_name="", seq_chain=""):
        """Return output of side2 topology, lower bounds (start_id) are the set of
        starting positions of residues in the PDB structure
        while upper bounds (last_id) are the set of ending positions
        of residues in the PDB structure. They match
        each other this way. For example, for topology
        Side2, the first continuous segment is from
        residue 3 to residue 14, and the second one is
        from residue 65 to residue 101, ..., and the last
        one is from residue 333 to residue 352."""
        return start_id, last_id

    @Component(type="alpha-helix")
    def tmh(self, start_id, last_id, xml_fp="", prot_name="", seq_chain=""):
        """Return output of helical topology, lower bounds (start_id) are the set of
        starting positions of residues in the PDB structure
        while upper bounds (last_id) are the set of ending positions
        of residues in the PDB structure. They match
        each other this way. For example, for topology
        Side2, the first continuous segment is from
        residue 3 to residue 14, and the second one is
        from residue 65 to residue 101, ..., and the last
        one is from residue 333 to residue 352."""
        return start_id, last_id

    @Component(type="non-alpha-helix")
    def nontmh(self, start_id, last_id, xml_fp="", prot_name="", seq_chain=""):
        """Return output of non-helical topology, lower bounds (start_id) are the set of
        starting positions of residues in the PDB structure
        while upper bounds (last_id) are the set of ending positions
        of residues in the PDB structure. They match
        each other this way. For example, for topology
        Side2, the first continuous segment is from
        residue 3 to residue 14, and the second one is
        from residue 65 to residue 101, ..., and the last
        one is from residue 333 to residue 352."""
        return start_id, last_id

    @Component(type="beta-strand")
    def strand(self, start_id, last_id, xml_fp="", prot_name="", seq_chain=""):
        """Return output of b-strand topology, lower bounds (start_id) are the set of
        starting positions of residues in the PDB structure
        while upper bounds (last_id) are the set of ending positions
        of residues in the PDB structure. They match
        each other this way. For example, for topology
        Side2, the first continuous segment is from
        residue 3 to residue 14, and the second one is
        from residue 65 to residue 101, ..., and the last
        one is from residue 333 to residue 352."""
        return start_id, last_id

    @Component(type="coil")
    def coil(self, start_id, last_id, xml_fp="", prot_name="", seq_chain=""):
        """Return output of coil topology, lower bounds (start_id) are the set of
        starting positions of residues in the PDB structure
        while upper bounds (last_id) are the set of ending positions
        of residues in the PDB structure. They match
        each other this way. For example, for topology
        Side2, the first continuous segment is from
        residue 3 to residue 14, and the second one is
        from residue 65 to residue 101, ..., and the last
        one is from residue 333 to residue 352."""
        return start_id, last_id

    @Component(type="membrane-inside")
    def inside(self, start_id, last_id, xml_fp="", prot_name="", seq_chain=""):
        """Return output of inside topology, lower bounds (start_id) are the set of
        starting positions of residues in the PDB structure
        while upper bounds (last_id) are the set of ending positions
        of residues in the PDB structure. They match
        each other this way. For example, for topology
        Side2, the first continuous segment is from
        residue 3 to residue 14, and the second one is
        from residue 65 to residue 101, ..., and the last
        one is from residue 333 to residue 352."""
        return start_id, last_id

    @Component(type="membrane-loop")
    def loop(self, start_id, last_id, xml_fp="", prot_name="", seq_chain=""):
        """Return output of loop topology, lower bounds (start_id) are the set of
        starting positions of residues in the PDB structure
        while upper bounds (last_id) are the set of ending positions
        of residues in the PDB structure. They match
        each other this way. For example, for topology
        Side2, the first continuous segment is from
        residue 3 to residue 14, and the second one is
        from residue 65 to residue 101, ..., and the last
        one is from residue 333 to residue 352."""
        return start_id, last_id

    @Component(type="interfacial-helix")
    def interfacial(self, start_id, last_id, xml_fp="", prot_name="", seq_chain=""):
        """Return output of interfacial topology, lower bounds (start_id) are the set of
        starting positions of residues in the PDB structure
        while upper bounds (last_id) are the set of ending positions
        of residues in the PDB structure. They match
        each other this way. For example, for topology
        Side2, the first continuous segment is from
        residue 3 to residue 14, and the second one is
        from residue 65 to residue 101, ..., and the last
        one is from residue 333 to residue 352."""
        return start_id, last_id

    @Component(type="unknown")
    def unknown(self, start_id, last_id, xml_fp="", prot_name="", seq_chain=""):
        """Return output of unknown topology, lower bounds (start_id) are the set of
        starting positions of residues in the PDB structure
        while upper bounds (last_id) are the set of ending positions
        of residues in the PDB structure. They match
        each other this way. For example, for topology
        Side2, the first continuous segment is from
        residue 3 to residue 14, and the second one is
        from residue 65 to residue 101, ..., and the last
        one is from residue 333 to residue 352."""
        return start_id, last_id

    @Component(type="all")
    def all(self, start_id, last_id, xml_fp="", prot_name="", seq_chain=""):
        """Return output of all topology, lower bounds (start_id) are the set of
        starting positions of residues in the PDB structure
        while upper bounds (last_id) are the set of ending positions
        of residues in the PDB structure. They match
        each other this way. For example, for topology
        Side2, the first continuous segment is from
        residue 3 to residue 14, and the second one is
        from residue 65 to residue 101, ..., and the last
        one is from residue 333 to residue 352."""
        return start_id, last_id
