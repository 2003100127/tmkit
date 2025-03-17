# Phobius

In this tutorial, we showcase the usage of parsing the topologies predicted by Phobius[^1].

:::{attention}
TMKit includes a built-in Phobius program for predicting transmembrane protein topologies. However, in our latest version, we found that Python version upgrades have affected compatibility, making it unsupported for inline execution within Python.

To ensure compatibility with newer Python versions, we have discontinued the built-in Phobius-based topology prediction feature in TMKit. However, TMKit still fully supports parsing externally predicted transmembrane topologies.

You can generate Phobius-based topology predictions via [this link{octicon}`link-external;1em;sd-text-info`](https://phobius.sbc.su.se/).
:::

:::{dropdown} Reminder of data
:animate: fade-in
:icon: database
:open: 

Please make sure that [the build-in example dataset{octicon}`link-external;1em;sd-text-info`](../get_started/example_dataset.md) has been downloaded before you walk through the tutorial.
:::



## {octicon}`file-code;1em;sd-text-info` **Example usage**
In TMKit, you can obtain the topologies of a transmembrane protein through `tmk.topo.from_phobius` by simply specifying two attributes `topo` and `phobius_fpn`. See explanations in [Attributes{octicon}`link-external;1em;sd-text-info`](#Attributes) below. We placed an example Phobius prediction file in `./data/topo/1xqfA.jphobius`. Suppose you have this Phobius prediction file below.

```{code} python
ID   1XQF:A|PDBID|CHAIN|SEQUENCE
FT   DOMAIN        1      5       NON CYTOPLASMIC.
FT   TRANSMEM      6     30
FT   DOMAIN       31     41       CYTOPLASMIC.
FT   TRANSMEM     42     62
FT   DOMAIN       63     95       NON CYTOPLASMIC.
FT   TRANSMEM     96    118
FT   DOMAIN      119    124       CYTOPLASMIC.
FT   TRANSMEM    125    147
FT   DOMAIN      148    158       NON CYTOPLASMIC.
FT   TRANSMEM    159    179
FT   DOMAIN      180    185       CYTOPLASMIC.
FT   TRANSMEM    186    205
FT   DOMAIN      206    210       NON CYTOPLASMIC.
FT   TRANSMEM    211    231
FT   DOMAIN      232    242       CYTOPLASMIC.
FT   TRANSMEM    243    260
FT   DOMAIN      261    265       NON CYTOPLASMIC.
FT   TRANSMEM    266    284
FT   DOMAIN      285    290       CYTOPLASMIC.
FT   TRANSMEM    291    316
FT   DOMAIN      317    327       NON CYTOPLASMIC.
FT   TRANSMEM    328    350
FT   DOMAIN      351    362       CYTOPLASMIC.
//
```

You can put the following codes in either a Jupyter notevbook or a Python script. If you want to see the predicted transmembrane topologies there, you can simply assign `topo` `tmh`. If you want to see the predicted cytoplasmic or extra-cellular topologies there, you can simply assign `topo` `cyto`/`extra`.

```{code} python
import tmkit as tmk

lower_ids, upper_ids = tmk.topo.from_phobius(
    topo='tmh',
    phobius_fpn='./data/topo/1xqfA.jphobius',
)
print('---lower bounds', lower_ids)
print('---upper bounds', upper_ids)
```



## {octicon}`key;1em;sd-text-info` **Attributes**

| **Attribute** | **Description**                                              |
|---------------|--------------------------------------------------------------|
| `phobius_fpn`   | path to a target Phobius file                                  |
| `topo`        | name of a topology kind. It can be `cyto`, `extra`, or `tmh` |
 
:::{seealso}
Please see [here{octicon}`link-external;1em;sd-text-info`](../get_started/feature.md#nomenclature) for better understanding the file-naming system.
:::



## {octicon}`file-added;1em;sd-text-info` **Output**
Finally, you will see the following output showing the transmembrane segment that protein `1xqf` chain `A` has.

In the output, ***lower bounds*** are the set of starting positions of residues in the PDB structure while ***upper bounds*** are the set of ending positions of residues in the PDB structure. They match each other this way. For example, for topology `Side2`, the first continuous segment is from residue **6** to residue **30**, and the second one is from residue **42** to residue **62**, ..., and the last one is from residue **328** to residue **350**.

```{code} python
---lower bounds [6, 42, 96, 125, 159, 186, 211, 243, 266, 291, 328]
---upper bounds [30, 62, 118, 147, 179, 205, 231, 260, 284, 316, 350]
```



[^1]: Käll L, Krogh A, Sonnhammer EL. A combined transmembrane topology and signal peptide prediction method. J Mol Biol. 2004 May 14;338(5):1027-36. doi: 10.1016/j.jmb.2004.03.016. PMID: 15111065.
