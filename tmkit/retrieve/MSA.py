__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import subprocess

from tmkit.interface.Tool import tool

from typing import List, Union, Optional


class msa(tool):
    """
    Methods
    -------
    toolInitializer, execute, HHblits, .

    Notes
    -----
    This class uses tools of multiple sequence alignment in Python interface.

    See Also
    --------
    It was introduced since v1.0.
    """

    def __init__(
    self,
    tool: str,
    tool_fp: str,
    input: str,
    database: Optional[str] = None,
    output2a3m: Optional[str] = None,
    send2cloud: bool = False,
    cloud_cmd: Optional[str] = None,
    iteration: Optional[str] = None,
    output: Optional[str] = None,
    input_format: Optional[str] = None,
    output_format: Optional[str] = None,
    cpu: Optional[str] = None,
    maxfilter: Optional[str] = None,
    diff: Optional[str] = None,
    id: Optional[str] = None,
    cov: Optional[str] = None,
    e: Optional[str] = None,
    B: Optional[str] = None,
    Z: Optional[str] = None,
    all: Optional[str] = None,
    realign_max: Optional[str] = None,
    output2a2m: Optional[str] = None,
    log: Optional[str] = None,
    output2sto: Optional[str] = None,
    jhm_E: Optional[str] = None,
    incE: Optional[str] = None,
    noali: Optional[str] = None,
    tblout: Optional[str] = None,
    remove_lower_aa: Optional[str] = None,
    count_seqs_name_line: Optional[str] = None,
    remove_secondary_structure: Optional[str] = None,
    retain_solvent_seq: Optional[str] = None,
    max_length_per_name_line: Optional[str] = None,
    aa_per_line: Optional[str] = None,
    w_upper: Optional[str] = None,
    w_lower: Optional[str] = None,
    gap_reformat: Optional[str] = None,
    match_reformat: Optional[str] = None,
    min_seq_id_query: Optional[str] = None,
    min_score_per_col_query: Optional[str] = None,
    neff: Optional[str] = None,
    ):
        self.tool = tool
        self.tool_fp = tool_fp
        self.send2cloud = send2cloud
        self.cloud_cmd = cloud_cmd
        self.input = input
        self.output = output
        self.input_format = input_format
        self.output_format = output_format
        self.database = database
        self.iteration = iteration
        self.output2a3m = output2a3m
        self.output2a2m = output2a2m
        self.output2sto = output2sto
        self.cpu = cpu
        self.maxfilter = maxfilter
        self.diff = diff
        self.id = id
        self.cov = cov
        self.e = e
        self.B = B
        self.Z = Z
        self.all = all
        self.realign_max = realign_max
        self.log = log
        self.incE = incE
        self.noali = noali
        self.tblout = tblout
        self.jhm_E = jhm_E
        self.tblout = tblout
        self.remove_lower_aa = remove_lower_aa
        self.count_seqs_name_line = count_seqs_name_line
        self.remove_secondary_structure = remove_secondary_structure
        self.retain_solvent_seq = retain_solvent_seq
        self.max_length_per_name_line = max_length_per_name_line
        self.aa_per_line = aa_per_line
        self.w_upper = w_upper
        self.w_lower = w_lower
        self.gap_reformat = gap_reformat
        self.match_reformat = match_reformat
        self.min_seq_id_query = min_seq_id_query
        self.min_score_per_col_query = min_score_per_col_query
        self.neff = neff

    def initializer(self):
        """
        Notes
        -----
        which tool is selected.

        Returns
        -------
            command of a querying tool.

        """
        switch = {
            "hhblits": self.hhblits,
            "jackhmmer": self.jackhmmer,
            "blast": self.blast,
            "hhfilter": self.hhfilter,
            "reformat.pl": self.reformat,
        }
        execute_order = switch[self.tool]()
        print(f"===>The current order: {execute_order}")
        return execute_order

    def execute(self):
        """

        Notes
        -----
           which tool is executed.

        Returns
        -------

        """
        s = subprocess.Popen(
            str(self.initializer()),
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            shell=True,
        )
        s.communicate()

    def hhblits(self):
        """

        Notes
        -----
           obtain hhblits' command

        Examples
        --------
            MemConP: iteration=3, maxfilter=999999999, id=99, diff='inf', B=999999999, Z=999999999,
            PSICOV: iteration=3, maxfilter=50, id=99
            x: iteration=3, diff='inf', cov=60

        See Also
        --------
           https://github.com/soedinglab/hh-suite [Source of hhblits]

        Returns
        -------
            command

        """
        order_list = {
            "input": "-i",
            "output": "-o",
            "database": "-d",
            "output2a3m": "-oa3m",
            "output2a2m": "-oa2m",
            "iteration": "-n",
            "cpu": "-cpu",
            "maxfilter": "-maxfilt",
            "realign_max": "-realign_max",
            "diff": "-diff",
            "id": "-id",
            "cov": "-cov",
            "B": "-B",
            "Z": "-Z",
            "all": "-all",
            "e": "-e",
            "log": ">",
        }
        orderc = [
            str("echo " '"' + str(self.tool_fp) + str(self.tool))
            if self.send2cloud
            else str(self.tool_fp) + str(self.tool),
            order_list["cpu"],
            str(self.cpu),
            order_list["input"],
            str(self.input),
            order_list["database"],
            str(self.database),
            order_list["output2a3m"],
            str(self.output2a3m),
            order_list["output2a2m"],
            str(self.output2a2m),
            order_list["output"],
            str(self.output),
            order_list["iteration"],
            str(self.iteration),
            order_list["maxfilter"],
            str(self.maxfilter),
            order_list["realign_max"],
            str(self.realign_max),
            order_list["diff"],
            str(self.diff),
            order_list["id"],
            str(self.id),
            order_list["cov"],
            str(self.cov),
            order_list["B"],
            str(self.B),
            order_list["Z"],
            str(self.Z),
            str(self.all).join(order_list["all"]),
            order_list["e"],
            str(self.e),
            order_list["log"],
            str(self.log),
        ]
        return self.recast(orderc, self.send2cloud, self.cloud_cmd)

    def blast(self):
        pass

    def jackhmmer(self):
        """

        Notes
        -----
           obtain jackhmmer's command

        Returns
        -------
            command
        """
        order_list = {
            "cpu": "--cpu",
            "iteration": "-N",
            "reporting_E": "-E",
            "inclusion_E": "--incE",
            "omit_alignment": "--noali",
            "Stockholm_alignment": "-A",
            "tabular_output": "--tblout",
            "input": "",
            "database": "",
        }
        orderc = [
            str("echo " '"' + str(self.tool_fp) + str(self.tool))
            if self.send2cloud
            else str(self.tool_fp) + str(self.tool),
            order_list["cpu"],
            str(self.cpu),
            order_list["iteration"],
            str(self.iteration),
            order_list["reporting_E"],
            str(self.jhm_E),
            order_list["inclusion_E"],
            str(self.incE),
            str(self.noali).join(order_list["omit_alignment"]),
            order_list["Stockholm_alignment"],
            str(self.output2sto),
            order_list["tabular_output"],
            str(self.tblout),
            order_list["input"].join(str(self.input)),
            order_list["database"].join(str(self.database)),
        ]
        return self.recast(orderc, self.send2cloud, self.cloud_cmd)

    def hhfilter(
        self,
    ):
        """

        Notes
        -----
           obtain hhfilter's command.

        Returns
        -------
            command
        """
        order_list = {
            "input": "-i",
            "output": "-o",
            "diff": "-diff",
            "id": "-id",
            "cov": "-cov",
            "min_seq_id_query": "-qid",
            "min_score_per_col_query": "-qsc",
            "neff": "-neff",
        }
        orderc = [
            str("echo " '"' + str(self.tool_fp) + str(self.tool))
            if self.send2cloud
            else str(self.tool_fp) + str(self.tool),
            order_list["input"],
            str(self.input),
            order_list["output"],
            str(self.output),
            order_list["diff"],
            str(self.diff),
            order_list["id"],
            str(self.id),
            order_list["cov"],
            str(self.cov),
            order_list["min_seq_id_query"],
            str(self.min_seq_id_query),
            order_list["min_score_per_col_query"],
            str(self.min_score_per_col_query),
            order_list["neff"],
            str(self.neff),
        ]
        return self.recast(orderc, self.send2cloud, self.cloud_cmd)

    def reformat(
        self,
    ):
        """

        Notes
        -----
           obtain reformat's command.

        Returns
        -------
            command
        """
        order_list = {
            "input_format": "",
            "output_format": "",
            "input": "",
            "output": "",
            "remove_lower_aa": "-r",
            "count_seqs_name_line": "-num",
            "remove_secondary_structure": "-noss",
            "retain_solvent_seq": "-sa",
            "max_length_per_name_line": "-d",
            "aa_per_line": "-l",
            "w_upper": "-uc",
            "w_lower": "-r",
            "match_reformat": "-M",
            "gap_reformat": "-g",
        }
        orderc = [
            str("echo " '"' + str(self.tool_fp) + str(self.tool))
            if self.send2cloud
            else str(self.tool_fp) + str(self.tool),
            order_list["remove_lower_aa"],
            str(self.remove_lower_aa),
            order_list["count_seqs_name_line"],
            str(self.count_seqs_name_line),
            order_list["remove_secondary_structure"],
            str(self.remove_secondary_structure),
            order_list["retain_solvent_seq"],
            str(self.retain_solvent_seq),
            order_list["max_length_per_name_line"],
            str(self.max_length_per_name_line),
            order_list["aa_per_line"],
            str(self.aa_per_line),
            order_list["w_upper"],
            str(self.w_upper),
            order_list["w_lower"],
            str(self.w_lower),
            order_list["gap_reformat"],
            str(self.gap_reformat),
            order_list["match_reformat"],
            str(self.match_reformat),
            order_list["input_format"].join(str(self.input_format)),
            order_list["output_format"].join(str(self.output_format)),
            order_list["input"].join(str(self.input)),
            order_list["output"].join(str(self.output)),
        ]
        return self.recast(orderc, self.send2cloud, self.cloud_cmd)

    @staticmethod


    def recast(orderc: List[Union[str, None]], send2cloud: bool, cloud_cmd: str) -> str:
        """
        Parameters
        ----------
        orderc: List[Union[str, None]]
            A list of strings and/or None values.
        send2cloud: bool
            A boolean indicating whether to send the output to the cloud.
        cloud_cmd: str
            A string containing the command to send the output to the cloud.

        Returns
        -------
        str
            A string containing the modified command.
        """
        order = []
        for i in range(len(orderc)):
            order.append(orderc[i])
            if orderc[i] == "None":
                order.remove(orderc[i - 1])
                order.remove(orderc[i])
        a = " "
        if send2cloud:
            suffix = str(' "' + " | " + cloud_cmd)
            b = a.join(order)
            return "".join([b, suffix])
        else:
            return a.join(order)
