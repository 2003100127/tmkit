# Retrieve

Accessing both the sequence and structure of a transmembrane protein is crucial. Typically, sequences are provided in [the FASTA format{octicon}`link-external;1em;sd-text-info`](https://en.wikipedia.org/wiki/FASTA_format), while structural data is stored in [the Protein Data Bank (PDB){octicon}`link-external;1em;sd-text-info`](https://www.rcsb.org/) format.

In addition to these two standard formats, [PDBTM{octicon}`link-external;1em;sd-text-info`](https://pdbtm.unitmp.org/documents) introduced [the Extensible Markup Language (XML){octicon}`link-external;1em;sd-text-info`](https://en.wikipedia.org/wiki/XML) file, specifically designed to document transmembrane protein topologies in a structured and accessible manner.

In TMKit, the module that allows users to download protein files from different sources is `tmkit.seq`.




## {octicon}`file-code;1em;sd-text-info` **RCSB PDB file**
We can retrieve a RCSB PDB file. First, we need to specify all proteins of interest in a Pandas dataframe. In TMKit, the Pandas dataframe of proteins is recognised.

```{code} python
import pandas as pd

prot_series = pd.Series(['6e3y', '6rfq', '6t0b'])
```

You can save the files in `./data/pdb/`. Then, please put the following code.



::::{tab-set}

:::{tab-item} Label1
```{code} python
import tmkit as tmk

tmk.seq.retrieve_pdb_from_rcsb(
    prot_series=prot_series,
    sv_fp='./data/pdb/',
)
```
:::

:::{tab-item} {octicon}`key;1em;sd-text-info`Attributes

| **Attribute**          | **Description**                                 |
|---------------|-------------------------------------------------|
| `prot_series` | data series of proteins                         |
| `sv_fp`       | path to save the RCSB PDB file to be downloaded |

Please see [here{octicon}`link-external;1em;sd-text-info`](../get_started/feature.md#nomenclature) for better understanding the file-naming system.

:::

::::

#### {octicon}`file-added;1em;sd-text-info`Output

```{code} python
===>No.1 protein name: 6e3y
Downloading PDB structure '6e3y'...
======>successfully downloaded!
===>No.2 protein name: 6rfq
Downloading PDB structure '6rfq'...
======>successfully downloaded!
===>No.3 protein name: 6t0b
Downloading PDB structure '6t0b'...
======>successfully downloaded!
```




## {octicon}`file-code;1em;sd-text-info` **Retrieve a PDBTM PDB file**
Similarly, we can retrieve a PDBTM PDB file. Specifying all proteins of interest in a Pandas dataframe.

```{code} python
import pandas as pd

prot_series = pd.Series(['6e3y', '6rfq', '6t0b'])
```

You can save the files in `./data/pdb/`. Then, putting the following code.


::::{tab-set}

:::{tab-item} Label1
```{code} python
import tmkit as tmk

tmk.seq.retrieve_pdb_from_pdbtm(
    prot_series=prot_series,
    sv_fp='./data/pdb/pdbtm/',
)
```
:::

:::{tab-item} {octicon}`key;1em;sd-text-info`Attributes

| **Attribute**          | **Description**                                 |
|---------------|-------------------------------------------------|
| `prot_series` | data series of proteins                         |
| `sv_fp`       | path to save the RCSB PDB file to be downloaded |

Please see [here{octicon}`link-external;1em;sd-text-info`](../get_started/feature.md#nomenclature) for better understanding the file-naming system.

:::

::::

#### {octicon}`file-added;1em;sd-text-info`Output

```{code} python
===>No.1 protein name: 6e3y
======>successfully downloaded!
===>No.2 protein name: 6rfq
======>successfully downloaded!
===>No.3 protein name: 6t0b
======>successfully downloaded!
```



## {octicon}`file-code;1em;sd-text-info` **Retrieve a PDBTM XML file**
Similarly, we can retrieve a PDBTM PDB file. As introduced in the PDBTM official manual, there are many records in the PDBTM database, including

| **Attribute** | **Description**                  |
|---------------|----------------------------------|
| `pdb_id`      | PDB code                         |
| `ch_id`       | chain ID                         |
| `type`        | topologies                       |
| `title`       | TITLE section of PDB file        |
| `numtm`       | number of transmembrane segments |
| `seq`         | sequence                         |
| `n_ifh`       | number of interfacial helices    |
| `n_loop`      | number of loops                  |
| `source`      | SOURCE section of PDB file       |
| `class`       | HEADER section of PDB file       |
| `keyword`     | keyword                          |
| `creation`    | date of creation                 |
| `lmod_date`   | date of last modification        |
| `lmod_descr`  | description of last mod          |

These records help researchers understand and screen transmembrane proteins. All records are placed in the XML file of a PDB protein file. In these records, `<REGION>` represents the topology of a protein, as shown in the table below.

| **Attribute** | **Description**   |
|---------------|-------------------|
| `1`           | Side1             |
| `2`           | Side2             |
| `B`           | Beta-strand       |
| `H`           | alpha-helix       |
| `C`           | coil              |
| `I`           | membrane-inside   |
| `L`           | membrane-loop     |
| `F`           | interfacial helix |
| `U`           | unknown           |


Also, we can start specifying all proteins of interest in a Pandas dataframe.
```{code} python
import pandas as pd

prot_series = pd.Series(['6e3y', '6rfq', '6t0b'])
```

You can save the files in `./data/xml/`. Then, putting the following code.


::::{tab-set}

:::{tab-item} Label1
```{code} python
import tmkit as tmk

tmk.seq.retrieve_xml_from_pdbtm(
    prot_series=prot_series,
    sv_fp='./data/xml/',
)
```
:::

:::{tab-item} {octicon}`key;1em;sd-text-info`Attributes

| **Attribute**          | **Description**                                 |
|---------------|-------------------------------------------------|
| `prot_series` | data series of proteins                         |
| `sv_fp`       | path to save the RCSB PDB file to be downloaded |

Please see [here{octicon}`link-external;1em;sd-text-info`](../get_started/feature.md#nomenclature) for better understanding the file-naming system.

:::

::::


#### {octicon}`file-added;1em;sd-text-info`Output

```{code} python
===>No.1 protein name: 6e3y
======>successfully downloaded!
===>No.2 protein name: 6rfq
======>successfully downloaded!
===>No.3 protein name: 6t0b
======>successfully downloaded!
```



## {octicon}`file-code;1em;sd-text-info` **Retrieve a AlphaFold2 PDB file**
Since the emerging AlphaFold2[^1] technology has swept the whole protein field, with a profound impact on the development of both experiment- and computation-driven structural studies, we added a few its related functions to TMKit ( we are also continuing to release more of those.

Also, we can start specifying all proteins of interest in a Pandas dataframe. Differently, we need to put the UniProt accession codes of the proteins, because they usually do not have determined structures in the PDB.

```{code} python
import pandas as pd

prot_series = pd.Series(['P63092', 'Q9B6E8', 'P07256', 'P63027'])

```

 You can save the files in `./data/pdb/`. Then, putting the following code.


::::{tab-set}

:::{tab-item} Label1
```{code} python
import tmkit as tmk

tmk.seq.retrieve_pdb_alphafold(
    prot_series=prot_series,
    sv_fp='./data/pdb/',
)
```
:::

:::{tab-item} {octicon}`key;1em;sd-text-info`Attributes

| **Attribute**          | **Description**                                 |
|---------------|-------------------------------------------------|
| `prot_series` | data series of proteins                         |
| `sv_fp`       | path to save the RCSB PDB file to be downloaded |

Please see [here{octicon}`link-external;1em;sd-text-info`](../get_started/feature.md#nomenclature) for better understanding the file-naming system.

:::

::::


#### {octicon}`file-added;1em;sd-text-info`Output

```{code} python
===>No.0 protein name: P63092
======>successfully downloaded!
===>No.1 protein name: Q9B6E8
======>successfully downloaded!
===>No.2 protein name: P07256
======>successfully downloaded!
===>No.3 protein name: P63027
======>successfully downloaded!
```


[^1]: Jumper, J., Evans, R., Pritzel, A. et al. Highly accurate protein structure prediction with AlphaFold. Nature 596, 583–589 (2021). https://doi.org/10.1038/s41586-021-03819-2

