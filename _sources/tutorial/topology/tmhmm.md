# TMHMM

In this tutorial, we showcase the usage of parsing the topologies predicted by TMHMM2[^1].

:::{attention}
TMKit originally supported transmembrane topology prediction using the TMHMM program entirely within Python. However, in our latest version, we observed that updates in Python—particularly major revisions in NumPy’s numerical operations (e.g., deprecation of `np.int` and `np.float`)—have introduced compatibility issues with the Python-based TMHMM method.

To accommodate these Python version updates, we have discontinued the built-in TMHMM topology prediction feature in TMKit. However, TMKit still fully supports parsing transmembrane topologies predicted externally using the TMHMM method.

You can still generate TMHMM-based topology predictions via [this link{octicon}`link-external;1em;sd-text-info`](https://services.healthtech.dtu.dk/services/TMHMM-2.0/).
:::


:::{dropdown} Reminder of data
:animate: fade-in
:icon: database
:open: 

Please make sure that [the build-in example dataset{octicon}`link-external;1em;sd-text-info`](../get_started/example_dataset.md) has been downloaded before you walk through the tutorial.
:::



## {octicon}`file-code;1em;sd-text-info` **Example usage**
In TMKit, you can obtain the topologies of a transmembrane protein through `tmk.topo.from_tmhmm` by simply specifying two parameters topo and `tmhmm_fpn`. See explanations in [Attributes{octicon}`link-external;1em;sd-text-info`](#Attributes) below. We placed an example TMHMM prediction file in `./data/topo/1xqfA.tmhmm`. Suppose you have this TMHMM prediction file below.

```{code} python
%pred NB(0): o 1 9, M 10 32, i 33 38, M 39 61, o 62 95, M 96 118, i 119 124, M 125 147, o 148 181, M 182 204, i 205 210, M 211 233, o 234 261, M 262 284, i 285 290, M 291 313, o 314 327, M 328 350, i 351 362
?0 oooooooooMMMMMMMMMMMMMMMMMMMMMMMiiiiiiMMMMMMMMMMMMMMMMMMMMMMMooooooooooo

?0 oooooooooooooooooooooooMMMMMMMMMMMMMMMMMMMMMMMiiiiiiMMMMMMMMMMMMMMMMMMMM

?0 MMMooooooooooooooooooooooooooooooooooMMMMMMMMMMMMMMMMMMMMMMMiiiiiiMMMMMM

?0 MMMMMMMMMMMMMMMMMooooooooooooooooooooooooooooMMMMMMMMMMMMMMMMMMMMMMMiiii

?0 iiMMMMMMMMMMMMMMMMMMMMMMMooooooooooooooMMMMMMMMMMMMMMMMMMMMMMMiiiiiiiiii

?0 ii
```


You can put the following codes in either a Jupyter notevbook or a Python script. If you want to see the predicted transmembrane topologies there, you can simply assign `topo` `tmh`. If you want to see the predicted cytoplasmic or extra-cellular topologies there, you can simply assign `topo` `cyto`/`extra`.

```{code} python
import tmkit as tmk

lower_ids, upper_ids = tmk.topo.from_tmhmm(
    topo='tmh',
    tmhmm_fpn='./data/topo/1xqfA.tmhmm',
    from_fasta=False,
    file_kind='Linux',
)
print('---lower bounds', lower_ids)
print('---upper bounds', upper_ids)
```



## {octicon}`key;1em;sd-text-info` **Attributes**

| **Attribute** | **Description**                                              |
|---------------|--------------------------------------------------------------|
| `tmhmm_fpn`   | path to a target TMHMM file                                  |
| `topo`        | name of a topology kind. It can be `cyto`, `extra`, or `tmh` |
 
:::{seealso}
Please see [here{octicon}`link-external;1em;sd-text-info`](../get_started/feature.md#nomenclature) for better understanding the file-naming system.
:::



## {octicon}`file-added;1em;sd-text-info` **Output**
Finally, you will see the following output showing the transmembrane segment that protein `1xqf` chain `A` has.

In the output, ***lower bounds*** are the set of starting positions of residues in the PDB structure while ***upper bounds*** are the set of ending positions of residues in the PDB structure. They match each other this way. For example, for topology `Side2`, the first continuous segment is from residue **10** to residue **32**, and the second one is from residue **39** to residue **61**, ..., and the last one is from residue **328** to residue **350**.

```{code} python
---lower bounds [10, 39, 96, 125, 182, 211, 262, 291, 328]
---upper bounds [32, 61, 118, 147, 204, 233, 284, 313, 350]
```



[^1]: Krogh A, Larsson B, von Heijne G, Sonnhammer EL. Predicting transmembrane protein topology with a hidden Markov model: application to complete genomes. J Mol Biol. 2001 Jan 19;305(3):567-80. doi: 10.1006/jmbi.2000.4315. PMID: 11152613.
