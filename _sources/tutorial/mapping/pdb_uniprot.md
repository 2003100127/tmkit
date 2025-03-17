# Conversion between PDB and UniProt

TMKit provides a function to convert between a PDB ID to an UniProt accession code.




## {octicon}`file-code;1em;sd-text-info` **Example usage**

First, we can convert from a PDB ID to an UniProt accession code. The PDB ID that will be recognized by TMKit should be a protein name concatenated with a chain name by `_`, e.g., `1xqf.A`. In our example dataset, there is a file that can be found in `./data/map/pdb_chain_uniprot.csv`, which needs to be specified during the conversion.

```{code} python
import tmkit as tmk

res = tmk.mapping.pdb2uniprot(
    id='1qxf.A',
    ref_fpn='data/map/pdb_chain_uniprot.csv',
)
print(res)
```

It outputs `O28935`. Then, we can convert from an UniProt accession code to a PDB ID.

```{code} python
import tmkit as tmk

res = tmk.mapping.uniprot2pdb(
    id='O28935',
    ref_fpn='data/map/pdb_chain_uniprot.csv',
)
print(res)
```

It outputs `1qxf.A`.


If there is a list of protein IDs to be converted, we can do it like below.

```{code} python
import tmkit as tmk
import pandas as pd

prot_series = pd.Series(['6e3y', '6rfq', '6t0b'])
for prot in prot_series.index:
    res = tmk.mapping.pdb2uniprot(
        id=prot_series.iloc[prot],
        ref_fpn='data/map/pdb_chain_uniprot.csv',
    )
    print(res)
```

It outputs `P63092`, `Q9B6E8`, and `P07256`.




## {octicon}`key;1em;sd-text-info` **Attributes**

| **Attribute** | **Description**                                                           |
|---------------|---------------------------------------------------------------------------|
| `id`          | a PDB ID (e.g., 1qxf.A) or a UniProt accession code (e.g., O28935)        |
| `ref_fpn`     | reference file for conversion between PDB IDs and UniProt accession codes |

:::{seealso}
Please see [here{octicon}`link-external;1em;sd-text-info`](../get_started/feature.md#nomenclature) for better understanding the file-naming system.
:::



## {octicon}`file-added;1em;sd-text-info` **Output**

Please check the output in each vignette above.
