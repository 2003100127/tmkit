# Individual collation

In this tutorial, we introduce `tmkit.collate`, a module designed to collate a protein chain downloaded from PDBTM by comparing it with chains of the same protein from RCSB.

:::{tip}
Collation is often necessary when working with PDBTM-derived protein chains, as PDBTM may transform or exclude certain chains present in the RCSB PDB structure file.
:::

This tutorial provides a step-by-step example of how to detect and analyze these differences at the per-protein level.

:::{dropdown} Reminder of data
:animate: fade-in
:icon: database
:open: 

Please make sure that [the build-in example dataset{octicon}`link-external;1em;sd-text-info`](../get_started/example_dataset.md) has been downloaded before you walk through the tutorial.
:::



## {octicon}`file-code;1em;sd-text-info` **Example usage**

First, we need to prepare RCSB and PDBTM structures of proteins. We have put a few protein structures in the following folders if you have downloaded our example dataset. Alternatively, you can obtain them through [this tutorial{octicon}`link-external;1em;sd-text-info`](../sequence/retrieve.md).


```{code} python
pdb_rcsb_fp = 'data/pdb/collate/rcsb/'
pdb_pdbtm_fp = 'data/pdb/collate/pdbtm/'
```

Then, we can check how many chains there are and what chains are contained in there by using the following code.

```{code} python
import tmkit as tmk

# PDBTM
chains = tmk.collate.chain(
    prot_name='6cxh',
    pdb_fp=pdb_pdbtm_fp,
)
print(chains)

# output
======>protein has chains ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
```

If we focus on a certain chain `C` of protein `6cxh`, we can get how many other chains differ to each other or are the same. The output dataframe allows you to see there are chains `GDEHF` from RCSB that are different from those from PDBTM. The `transformation_detection` is used to check if the chain of focus is transformed by another chain from a RCSB PDB structure. `untransformed` means it is not transformed by another chain. Please see the output below.

```{code} python
import tmkit as tmk

df, transformation_detection = tmk.collate.single(
    prot_name='6cxh',
    chain_focus='C',
    pdb_rcsb_fp=pdb_rcsb_fp,
    pdb_pdbtm_fp=pdb_pdbtm_fp,
)

# output
print(df)
prot_name chain pdbtm_chains rcsb_chains source   diff same
0      6cxh     C     ABCDEFGH         ABC   rcsb  GDEHF  ACB

print(transformation_detection)
{'6cxh.C': 'untransformed'}
```

If we test protein `3pux` chain `G`, we found that the PDB structure from PDBTM is the same as that from RCSB, shown below.

```{code} python
import tmkit as tmk

df, transformation_detection = tmk.collate.single(
    prot_name='3pux',
    chain_focus='G',
    pdb_rcsb_fp=pdb_rcsb_fp,
    pdb_pdbtm_fp=pdb_pdbtm_fp,
)

# output
print(df)
  prot_name chain pdbtm_chains rcsb_chains source diff   same
0      3pux     G        EFGAB       EFGAB   rcsb       AEFGB

print(transformation_detection)
{'3pux.G': 'untransformed'}
```



## {octicon}`key;1em;sd-text-info` **Attributes**

| **Attribute**  | **Description**                                                                  |
|----------------|----------------------------------------------------------------------------------|
| `prot_name`    | name of a protein in the prefix of a PDB file name (e.g., `1xqf` in `1xqfA.pdb`) |
| `chain_focus`  | chain of a protein in the prefix of a PDB file name (e.g., `A` in `1xqfA.pdb`)   |
| `pdb_rcsb_fp`  | path to a protein complex from RCSB                                              |
| `pdb_pdbtm_fp` | path to a protein complex from PDBTM                                             |
 
:::{seealso}
Please see [here{octicon}`link-external;1em;sd-text-info`](../get_started/feature.md#nomenclature) for better understanding the file-naming system.
:::



## {octicon}`file-added;1em;sd-text-info` **Output**

```{code} python
======>protein has chains ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
======>basic info:
  prot_name chain pdbtm_chains rcsb_chains source diff   same
0      3pux     G        EFGAB       EFGAB   rcsb       AEFGB
  prot_name chain pdbtm_chains rcsb_chains source diff   same
0      3pux     G        EFGAB       EFGAB   rcsb       AEFGB
{'3pux.G': 'untransformed'}
```
