# PDBTM

TMKit is very powerful for obtaining different kinds of topologies from an XML file retrieved from [the PDBTM database{octicon}`link-external;1em;sd-text-info`](https://pdbtm.unitmp.org/)[^1]. Together with TMDET algorithm[^2], they constitute a nice community for managing the data source of transmembrane (TM) protein topologies. PDBTM defines 9 topologies:

:::{dropdown} Open dropdown
:open:

* Side1
* Side2
* Beta-strand
* Alpha-helix
* Coil
* Membrane-inside
* Membrane-loop
* Interfacial helix
* Unknown
:::

When working with an XML file that documents transmembrane topologies, it is essential to efficiently access each type of topology. In this tutorial, we demonstrate how to achieve this using an example XML file.

:::{hint}
Technically, we implement the tmkit.topo module by using [aspect-oriented programming (AOP){octicon}`link-external;1em;sd-text-info`](https://en.wikipedia.org/wiki/Aspect-oriented_programming), which makes it easier to use the topological information in other functions.
:::

:::{dropdown} Reminder of data
:animate: fade-in
:icon: database
:open: 

Please make sure that [the build-in example dataset{octicon}`link-external;1em;sd-text-info`](../get_started/example_dataset.md) has been downloaded before you walk through the tutorial.
:::



## {octicon}`file-code;1em;sd-text-info` **Example usage**
First, we can define all types of topologies of transmembrane proteins used in PDBTM in the following way.

```{code} python
topos = {
    'Side1': 'side1',
    'Side2': 'side2',
    'Beta': 'strand',
    'Alpha': 'tmh',
    'Coil': 'coil',
    'Membrane-inside': 'inside',
    'Membrane-loop': 'loop',
    'Interfacial ': 'interfacial',
    'Unknown': 'Unknown',
}
```

Then, we can scan a protein's **XML** file to see if it contains all types of the topologies. By default, we still use `1xqf.xml`. If we open this file, in chain `A`, there are only **Side1**, **Side2**, **Alpha helix**, and **Unknown** types. Using the following codes, we can get the results expected.

```{code} python
for topo, i in topos.items():
    print('Topology: {}'.format(topo))
    try:
        lower_ids, upper_ids = tmk.topo.from_pdbtm(
            xml_fp='data/xml/',
            prot_name='1xqf',
            seq_chain='A',
            topo=i,
        )
        if lower_ids:
            print('---lower bounds', lower_ids)
            print('---upper bounds', upper_ids)
    except:
        continue
    else:
        print('It does not has this topology.\n')
```



## {octicon}`key;1em;sd-text-info` **Attributes**

| **Attribute** | **Description**                                                                                                                                                                                                                              |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `xml_fp`        | path where a target XML file is placed                                                                                                                                                                                                       |
| `xml_name`      | name of the XML file                                                                                                                                                                                                                         |
| `seq_chain`     | chain of a protein                                                                                                                                                                                                                           |
| `topo`          | a topology code. It can be one of side1, side2, strand, tmh, coil, inside, loop, interfacial, and Unknown, which correspond to Side1, Side2, Beta strand, Alpha helix, Coil, Membrane-inside, Membrane-loop, Interfacial, Unknown topologies |
 
:::{seealso}
Please see [here{octicon}`link-external;1em;sd-text-info`](../get_started/feature.md#nomenclature) for better understanding the file-naming system.
:::



## {octicon}`file-added;1em;sd-text-info` **Output**

Finally, you will see the following output showing which one type of topology that protein `1xqf` chain `A` has.

In the output, ***lower bounds*** are the set of starting positions of residues in the PDB structure while ***upper bounds*** are the set of ending positions of residues in the PDB structure. They match each other this way. For example, for topology `Side2`, the first continuous segment is from residue **3** to residue **14**, and the second one is from residue **65** to residue **101**, ..., and the last one is from residue **333** to residue **352**.

```{code} python
Topology: Side1
---lower bounds [33, 119, 179, 195, 249, 300, 311, 378]
---upper bounds [45, 126, 181, 201, 260, 301, 313, 386]
It does not has this topology.

Topology: Side2
---lower bounds [3, 65, 148, 220, 277, 333]
---upper bounds [14, 101, 160, 230, 281, 352]
It does not has this topology.

Topology: Beta strand
It does not has this topology.

Topology: Alpha helix
---lower bounds [15, 46, 102, 127, 161, 202, 231, 261, 282, 314, 353]
---upper bounds [32, 64, 118, 147, 178, 219, 248, 276, 299, 332, 377]
It does not has this topology.

Topology: Coil
It does not has this topology.

Topology: Membrane-inside
It does not has this topology.

Topology: Membrane-loop
It does not has this topology.

Topology: Interfacial
It does not has this topology.

Topology: Unknown
---lower bounds [1, 3, 15, 33, 46, 65, 102, 119, 127, 148, 161, 179, 182, 195, 202, 220, 231, 249, 261, 277, 282, 300, 302, 311, 314, 333, 353, 378, 387]
---upper bounds [2, 14, 32, 45, 64, 101, 118, 126, 147, 160, 178, 181, 194, 201, 219, 230, 248, 260, 276, 281, 299, 301, 310, 313, 332, 352, 377, 386, 418]
It does not has this topology.
```

[^1]: Kozma D, Simon I, Tusnády GE. PDBTM: Protein Data Bank of transmembrane proteins after 8 years. Nucleic Acids Res. 2013 Jan;41(Database issue):D524-9. doi: 10.1093/nar/gks1169. Epub 2012 Nov 30. PMID: 23203988; PMCID: PMC3531219.
[^2]: Tusnády GE, Dosztányi Z, Simon I. TMDET: web server for detecting transmembrane regions of proteins by using their 3D coordinates. Bioinformatics. 2005 Apr 1;21(7):1276-7. doi: 10.1093/bioinformatics/bti121. Epub 2004 Nov 11. PMID: 15539454.
