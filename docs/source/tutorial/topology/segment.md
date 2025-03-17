# Segment

Transmembrane (TM) segments play a crucial role in understanding various biological processes. In TMKit, the `tmh` attribute in the `tmkit.topo` module allows users to retrieve transmembrane segments from a **PDBTM XML** file for a given transmembrane protein. 

:::{tip}
Since PDBTM provides structure-based topologies, their quality is generally considered high. However, while PDBTM XML files document multiple types of topologies, they do not specify whether a segment is located in the cytoplasmic or extracellular environment.

In contrast, prediction-based tools like Phobius and TMHMM2 provide this cytoplasmic/extracellular orientation information. As a result, researchers have started inferring cytoplasmic and extracellular segments directly from PDBTM data, treating them as structure-derived annotations.

For further insights, please refer to the studies [MBPred{octicon}`link-external;1em;sd-text-info`](https://github.com/bojigu/MBPred)[^1] and [DeepTMInter{octicon}`link-external;1em;sd-text-info`](https://github.com/2003100127/deeptminter)[^2].
:::

In TMKit, we offer this function and its usage is shown below.

:::{dropdown} Reminder of data
:animate: fade-in
:icon: database
:open: 

Please make sure that [the build-in example dataset{octicon}`link-external;1em;sd-text-info`](../get_started/example_dataset.md) has been downloaded before you walk through the tutorial.
:::



## {octicon}`file-code;1em;sd-text-info` **Example usage**
We can achieve this using the `tmk.topo.cepdbtm` method, as illustrated above. First, we need to define several key parameters, including the file paths for a protein's PDB, XML, and FASTA files. We recommend users explore the corresponding paths in the downloaded example dataset to better understand the file contents.

For a detailed explanation of the parameters, please refer to the Parameter Illustration section below.

TMKit detects structure-derived cytoplasmic and extracellular segments based on predicted topologies. In this example, we use Phobius-predicted topology information, specifically from the file `./data/topo/1xqfA.jphobius`.

The inclusion of PDB, XML, and FASTA files is necessary because TMKit converts between FASTA IDs and PDB IDs based on the extracted topological data from the XML file. Ultimately, TMKit returns the exact residue positions in the PDB structure for the identified cytoplasmic or extracellular segments.

```{code} python
import tmkit as tmk

pdbtm_seg, pred_seg = tmk.topo.cepdbtm(
    pdb_fp='./data/pdb/',
    prot_name='1xqf',
    seq_chain='A',
    file_chain='A',
    topo_fp='./data/topo/1xqfA.jphobius',
    xml_fp='./data/xml/',
    fasta_fp='./data/fasta/',
)
print('---Cytoplasmic and extracellular segments that are structure-derived :\n', pdbtm_seg)
print('---Cytoplasmic and extracellular segments Predicted by the Phobius tool: \n', pred_seg)
```



## {octicon}`key;1em;sd-text-info` **Attributes**

| **Attribute** | **Description**                                                                                                                                                                                                        |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `pdb_fp`      | path where a target PDB file is placed                                                                                                                                                                                 |
| `fasta_fp`    | path where a target Fasta file is placed                                                                                                                                                                               |
| `xml_fp`      | path where a target XML file is placed                                                                                                                                                                                 |
| `topo_fp`     | path where a target topology file is placed. The topologies in this file are predicted an external prediction program. Currently, TMKit only supports the file format of the topologies predicted by TMHMM and Phobius |
| `prot_name`   | name of a protein in the prefix of a PDB file name (e.g., `1xqf` in `1xqfA.pdb`)                                                                                                                                           |
| `seq_chain`   | chain of a protein in the prefix of a PDB file name (e.g., `A` in `1xqfA.pdb`) (biological purpose)                                                                                                                        |
| `file_chain`  | chain of a protein in the prefix of a PDB file name (e.g., `A` in `1xqfA.pdb`) (technical purpose)                                                                                                                         |


:::{seealso}
Please see [here{octicon}`link-external;1em;sd-text-info`](../get_started/feature.md#nomenclature) for better understanding the file-naming system.
:::




## {octicon}`file-added;1em;sd-text-info` **Output**
Finally, you will see the following output showing the structure-derived cytoplasmic and extracellular segments of protein `1xqf` chain `A`.

Similar to the explanation, `xxx_lower` (for example, `tmh_lower`) is the set of starting positions of residues in the PDB structure while `xxx_upper` (for example, `tmh_upper`) is the set of ending positions of residues in the PDB structure. They match each other this way. For example, for topology alpha helix (`tmh`), the first continuous segment is from residue **13** to residue **30**, and the second one is from residue **44** to residue **62**, ..., and the last one is from residue **100** to residue **116**.

More importantly, the inferred structure-derived cytoplasmic segments can be found using the output `pdbtm_seg` through `cyto_lower` and `cyto_upper` and the inferred structure-derived extracellular segments can be found through `extra_lower` and `extra_upper`. The explanations of the list of coordinates are the same as those for alpha helix (`tmh`) above. Similarly, the predicted cytoplasmic and extracellular segments can be found using the output `pred_seg`.

```{code} python
---Cytoplasmic and extracellular segments that are structure-derived :
 {'tmh_lower': [13, 44, 100, 125, 159, 187, 216, 246, 267, 290, 329], 'tmh_upper': [30, 62, 116, 145, 176, 204, 233, 261, 284, 308, 353], 'cyto_lower': [31, 117, 177, 180, 234, 285, 287, 354], 'cyto_upper': [43, 124, 179, 186, 245, 286, 289, 362], 'extra_lower': [1, 63, 146, 205, 262, 309], 'extra_upper': [12, 99, 158, 215, 266, 328]}

---Cytoplasmic and extracellular segments Predicted by the Phobius tool:
 {'cyto_lower': [31, 119, 180, 232, 285, 351], 'cyto_upper': [41, 124, 185, 242, 290, 362], 'tmh_lower': [6, 42, 96, 125, 159, 186, 211, 243, 266, 291, 328], 'tmh_upper': [30, 62, 118, 147, 179, 205, 231, 260, 284, 316, 350], 'extra_lower': [1, 63, 148, 206, 261, 317], 'extra_upper': [5, 95, 158, 210, 265, 327], 'signal_lower': [], 'signal_upper': [], 'cregion_lower': [], 'cregion_upper': [], 'hregion_lower': [], 'hregion_upper': [], 'nregion_lower': [], 'nregion_upper': []}
```




[^1]: Zeng B, Hönigschmid P, Frishman D. Residue co-evolution helps predict interaction sites in α-helical membrane proteins. J Struct Biol. 2019 May 1;206(2):156-169. doi: 10.1016/j.jsb.2019.02.009. Epub 2019 Mar 2. PMID: 30836197.

[^2]: Sun J, Frishman D. Improved sequence-based prediction of interaction sites in α-helical transmembrane proteins by deep learning. Comput Struct Biotechnol J. 2021 Mar 9;19:1512-1530. doi: 10.1016/j.csbj.2021.03.005. PMID: 33815689; PMCID: PMC7985279.
