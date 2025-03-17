# Evaluation involving two-site prediction

TMKit provides functions for evaluating the performance of contact prediction methods, with a unique focus on residues within transmembrane topologies, which are predominantly α-helices. Unlike other computational tools, TMKit specializes in assessing contact prediction accuracy specifically within these structurally distinct regions.

:::{dropdown} Reminder of data
:animate: fade-in
:icon: database
:open: 

Please make sure that [the build-in example dataset{octicon}`link-external;1em;sd-text-info`](../get_started/example_dataset.md) has been downloaded before you walk through the tutorial.
:::



## {octicon}`file-code;1em;sd-text-info` **Example usage**

We can use the following code to obtain the residue contacts of protein `1xqf` chain `A`. 

In the current version, TMKit supports evaluation using **precision**, **recall**, F1-**score**, **accuracy**, and **Matthews correlation coefficient (MCC)**.

```{code} python
import tmkit as tmk

res = tmk.rrc.evaluate(
    prot_name='1xqf',
    seq_chain='A',
    fasta_fp='data/fasta/',
    pdb_fp='data/pdb/',
    xml_fp='data/xml/',
    dist_fp='data/rrc/',
    tool_fp='data/rrc/tool/',
    cutoff=5.5,
    tool='membrain2',
    seq_sep_inferior=1,
    seq_sep_superior=None,
    sort=2,
)
print(res)
```



## {octicon}`key;1em;sd-text-info` **Attributes**

| **Attribute**    | **Description**                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| `pdb_fp`           | path where a target PDB file is placed                                                                                                       |
| `fasta_fp`         | path where a target Fasta file is placed                                                                                                     |
| `xml_fp`           | path where a target XML file is placed                                                                                                       |
| `dist_fp`          | path where a file containing real distances between residues is placed (please check the file at ./data/rrc in the example dataset)          |
| `tool_fp`          | path where a protein residue contact map file is placed                                                                                      |
| `tool`             | name of a contact prediction tool. It can be one of PSICOV, FreeContact, CCMPred, Gremlin, GDCA, PlmDCA, MemConP, Membrain2, and DeepHelicon |
| `seq_sep_inferior` | The lower bounds of how far any two residues are in pairs                                                                                    |
| `seq_sep_superior` | The upper bounds of how far any two residues are in pairs                                                                                    |
| `prot_name`        | name of a protein in the prefix of a PDB file name (e.g., 1xqf in 1xqfA.pdb)                                                                 |
| `seq_chain`        | chain of a protein in the prefix of a PDB file name (e.g., A in 1xqfA.pdb). Parameter file_chain will be converted within the function       |
| `cutoff`           | distance cutoff to see whether two residues are in spatial contact (e.g., 5.5 angstrom)                                                      |

:::{seealso}
Please see [here{octicon}`link-external;1em;sd-text-info`](../get_started/feature.md#nomenclature) for better understanding the file-naming system.
:::



## {octicon}`file-added;1em;sd-text-info` **Output**

Finally, you will see the following output.

```{code} python
======>Evaluating protein 1xqfA
=========>precision: 0.7818181818181819
=========>recall: 0.20772946859903382
=========>mcc: 0.39739008414082766
=========>f1score: 0.3282442748091603
=========>accuracy: 0.9819004524886877
```
