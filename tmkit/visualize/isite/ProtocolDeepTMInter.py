__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from tmkit.visualize.component.Select import select as libsel
from tmkit.visualize.component.Color import color as libcolor
from tmkit.visualize.isite.Labelling import labelling
from tmkit.chain.PDB import pdb as cpdb


class protocolDeepTMInter:

    def __init__(
            self,
            prot_name,
            prot_chain,
            pdb_chain_fp,
            pdb_complex_fp,
            tool,
            isite_fp,
            dist_fp,
            sv_bfactor_fp,

            pymol_bg_chain_ids,

            draw_type='label_actual',

            bg_chain_name='all',
            bg_chain_color='sulfur',
            focus_chain_name='focus',
            focus_representation='surface',
            color_list='white br7',
            bg_color="black",
    ):
        """

        Parameters
        ----------
        prot_name
            a pdb entry name
        prot_chain
            protein chain
        pdb_chain_fp
            the pdb file of the protein chain
        pdb_complex_fp
            the pdb file of the protein complex
        tool
            prediction tool name
            mbpred，delphi，deeptminter
        isite_fp
        dist_fp
        sv_bfactor_fp
            actual_label_bf.txt
            predicted_label_bf.txt
            probs_bf.txt
        pymol_bg_chain_ids
        draw_type
            label_actual
            label_predicted
            probability
        bg_chain_name
        bg_chain_color
            chromium, sulfur, xenon, technetium, germanium
        focus_chain_name
        focus_representation
        color_list
            'white br7', 'white tv_blue'
        bg_color

        """
        from pymol import finish_launching
        from pymol import cmd
        finish_launching()

        self.type = {
            'label_actual': 'actual_label_bf',
            'label_predicted': 'predicted_label_bf',
            'probability': 'probs_bf',
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

        cmd.bg_color(
            color=bg_color
        )

        chains = cpdb(
            pdb_fp=pdb_complex_fp,
            prot_name=prot_name,
        ).chains()
        print(chains)

        cmd.load(
            filename=pdb_complex_fp + prot_name + '.pdb'
        )

        libsel().chain(chain_name=bg_chain_name, chains=pymol_bg_chain_ids)

        libcolor(color=bg_chain_color, sel_name=bg_chain_name)

        libsel().chain(chain_name=focus_chain_name, chains=prot_chain + ' and not resn Zn')
        # cmd.alter(selection=focus_chain_name, expression='b=0')

        from tmkit.visualize.component.palette.data2bfactor import data2b_res
        data2b_res(
            mol=focus_chain_name,
            data_file=sv_bfactor_fp + '/' + self.type + '.txt',
        )

        from tmkit.visualize.component.palette.spectrumany import spectrumany
        spectrumany(
            expression='b',
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
            name='surface_quality',
            value=1,
            selection='',
        )

        cmd.set(
            name='transparency',
            value=0.1,
            selection='',
        )