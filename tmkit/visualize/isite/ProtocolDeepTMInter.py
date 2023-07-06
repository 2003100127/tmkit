__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from typing import List

from tmkit.chain.PDB import PDB as cpdb
from tmkit.visualize.component.Color import Color as libcolor
from tmkit.visualize.component.Select import Select as libsel
from tmkit.visualize.isite.Labelling import labelling


class ProtocolDeepTMInter:
    def __init__(
        self,
        prot_name: str,
        prot_chain: str,
        pdb_chain_fp: str,
        pdb_complex_fp: str,
        tool: str,
        isite_fp: str,
        dist_fp: str,
        sv_bfactor_fp: str,
        pymol_bg_chain_ids: str,
        draw_type: str = "label_actual",
        bg_chain_name: str = "all",
        bg_chain_color: str = "sulfur",
        focus_chain_name: str = "focus",
        focus_representation: str = "surface",
        color_list: str = "white br7",
        bg_color: str = "black",
    ) -> None:
        """
        Initialize the ProtocolDeepTMInter class.

        Parameters
        ----------
        prot_name : str
            name of a protein in the prefix of a PDB file name (e.g., 1xqf in 1xqfA.pdb).
        prot_chain : str
            chain of a protein in the prefix of a PDB file name (e.g., A in 1xqfA.pdb).
        pdb_chain_fp : str
            path where a target PDB file is place.
        dist_fp : str
            path where a file containing real distances between residues is placed (please check the file at ./data/rrc in the example dataset).
        pdb_complex_fp : str
            path where a PDB file showing a protein complex is placed.
        tool : str
            tool name. Currently, the reading of DeepTMInter, DELPHI, and MBPred files is supported.
        isite_fp : str
            path where a file showing interaction sites and the interaction likelihoods is placed.
        dist_fp : str
            File path to the distance.
        sv_bfactor_fp : str
            File path to the actual_label_bf.txt, predicted_label_bf.txt, and probs_bf.txt.
        pymol_bg_chain_ids : List[str]
            List of chain ids.
        draw_type : str, optional
            Type of drawing. Can be one of "label_actual", "label_predicted", or "probability", by default "label_actual".
        bg_chain_name : str, optional
            Name of the background chain, by default "all".
        bg_chain_color : str, optional
            ckground chain. Can be one of "chromium", "sulfur", "xenon", "technetium", or "germanium", by default "sulfur".
        focus_chain_name : str, optional
            the focus chain, by default "focus".
        focus_representation : str, optional
            Representation of the focus chain. Can be one of "surface", "cartoon", "lines", "sticks", or "spheres", by default "surface".
        color_list : str, optional
            List of colors. Can be one of "white br7" or "white tv_blue", by default "white br7".
        bg_color : str, optional
            Background color. Can be any valid PyMOL color, by default "black".
        """
        from pymol import cmd, finish_launching

        finish_launching()

        self.type = {
            "label_actual": "actual_label_bf",
            "label_predicted": "predicted_label_bf",
            "probability": "probs_bf",
        }[draw_type]

        label_op = labelling(
            prot_name=prot_name,
            prot_chain=prot_chain,
            pdb_fp=pdb_chain_fp,
            sv_fp=sv_bfactor_fp,
            isite_fp=isite_fp,
            tool=tool,
        )

        label_op.probs()
        label_op.predictedLabels(dist_fp)
        label_op.actualLabels(dist_fp)

        cmd.bg_color(color=bg_color)

        chains = cpdb(
            pdb_fp=pdb_complex_fp,
            prot_name=prot_name,
        ).chains()
        print(chains)

        cmd.load(filename=pdb_complex_fp + prot_name + ".pdb")

        libsel().chain(chain_name=bg_chain_name, chains=pymol_bg_chain_ids)

        libcolor(color=bg_chain_color, sel_name=bg_chain_name)

        libsel().chain(
            chain_name=focus_chain_name, chains=prot_chain + " and not resn Zn"
        )

        from tmkit.visualize.component.palette.data2bfactor import data2b_res

        data2b_res(
            mol=focus_chain_name,
            data_file=sv_bfactor_fp + "/" + self.type + ".txt",
        )

        from tmkit.visualize.component.palette.spectrumany import spectrumany

        spectrumany(
            expression="b",
            color_list=color_list,
            selection=focus_chain_name,
            minimum=0.01,
            maximum=1,
            quiet=1,
        )

        cmd.show(
            representation=focus_representation,
            selection=focus_chain_name,
        )

        cmd.set(
            name="surface_quality",
            value=1,
            selection="",
        )

        cmd.set(
            name="transparency",
            value=0.1,
            selection="",
        )
