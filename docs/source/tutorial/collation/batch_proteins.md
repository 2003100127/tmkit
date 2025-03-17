# Batch collation

We use this tutorial to batch collate a list of proteins.

:::{dropdown} Reminder of data
:animate: fade-in
:icon: database
:open: 

Please make sure that [the build-in example dataset{octicon}`link-external;1em;sd-text-info`](../get_started/example_dataset.md) has been downloaded before you walk through the tutorial.
:::


## {octicon}`file-code;1em;sd-text-info` **Example usage**

We can first define a few Pandas dataframes to store the information about 4 example proteins: `6cxh` chain `C`, `3pux` chain `G`, `5guf` chain `A`, and `4kjs` chain `A`.

| **Attribute**   | **Description**                                                                                              |
|-----------------|--------------------------------------------------------------------------------------------------------------|
| `prot_df`       | stores the information about the four chains                                                                 |
| `prot_pdbtm_df` | stores the information about all chains of the protein PDBTM complexes that the four chains are derived from |
| `prot_rcsb_df`  | stores the information about all chains of the protein RCSB complexes that the four chains are derived from  |


```{code} python
import pandas as pd

prot_df = pd.DataFrame(
    [['6cxh', 'C'],
     ['3pux', 'G'],
     ['5guf', 'A'],
     ['4kjs', 'A'],]
)

prot_pdbtm_df = pd.DataFrame(
    [['3pux', 'E'],
    ['3pux', 'F'],
    ['3pux', 'G'],
    ['3pux', 'A'],
    ['3pux', 'B'],
    ['5guf', 'A'],
    ['5guf', 'B'],
    ['6cxh', 'A'],
    ['6cxh', 'B'],
    ['6cxh', 'C'],
    ['6cxh', 'D'],
    ['6cxh', 'E'],
    ['6cxh', 'F'],
    ['6cxh', 'G'],
    ['6cxh', 'H'],
    ['4kjs', 'A'],
    ['4kjs', 'C'],
    ['4kjs', 'D'],]
)

prot_rcsb_df = pd.DataFrame(
    [['4kjs', 'A'],
     ['4kjs', 'B'],
     ['6cxh', 'A'],
     ['6cxh', 'B'],
     ['6cxh', 'C'],
     ['5guf', 'A'],
     ['3pux', 'E'],
     ['3pux', 'F'],
     ['3pux', 'G'],
     ['3pux', 'A'],
     ['3pux', 'B'],],
)
```

We can use the following codes to batch collate them. If you have a large number of protein complexes, the `tmk.collate.batch` should be very effective for your needs.

```{code} python
import tmkit as tmk

df, transformation_detection = tmk.collate.batch(
    prot_df=prot_df,
    prot_pdbtm_df=prot_pdbtm_df,
    prot_rcsb_df=prot_rcsb_df,
    pdb_rcsb_fp=pdb_rcsb_fp,
    pdb_pdbtm_fp=pdb_pdbtm_fp,
)
print(df)
print(transformation_detection)
```



## {octicon}`key;1em;sd-text-info` **Attributes**

| **Attribute**   | **Description**                                                                                                                        |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------|
| `pdb_rcsb_fp`   | path where protein complexes from RCSB are placed                                                                                      |
| `pdb_pdbtm_fp`  | path where protein complexes from PDBTM are placed                                                                                     |
| `prot_df`       | tab-delimiter Pandas dataframe containing protein names and protein chains in two columns, respectively                                |
| `prot_pdbtm_df` | tab-delimiter Pandas dataframe containing protein names and all of the chains of the protein (from PDBTM) in two columns, respectively |
| `prot_rcsb_df`  | tab-delimiter Pandas dataframe containing protein names and all of the chains of the protein (from RCSB) in two columns, respectively  |
 

:::{seealso}
Please see [here{octicon}`link-external;1em;sd-text-info`](../get_started/feature.md#nomenclature) for better understanding the file-naming system.
:::



## {octicon}`file-added;1em;sd-text-info` **Output**

```{code} python
      0  1     pdbtm   rcsb   diff source
0  6cxh  C  ABCDEFGH    ABC  FDHEG   rcsb
1  3pux  G     EFGAB  EFGAB          rcsb
2  5guf  A        AB      A      B   rcsb
3  4kjs  A       ACD     AB     CD   rcsb
```


#### File format

 It returns two output objects.
protein collated df - It contains 6 columns:

| **Attribute** | **Description**                                                                                                                     |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------|
| 0             | protein name                                                                                                                        |
| 1             | chain name                                                                                                                          |
| pdbtm         | DB                                                                                                                                  |
| rcsb          | DB                                                                                                                                  |
| diff          | different chains (pdbtm and rcsb)                                                                                                   |
| source        | a chain(s) in PDBTM exists in the chains in RCSB, which means if this chain(s) in PDBTM is transformed using the BIOMAT 350 records |

If `strategy='diff'` is selected and values in column source are shown rcsb, which means all chains of a self.prot_df in PDBTM can be found in RCSB. `strategy_dict` stores the same or different chains between PDBTM and RCSB. `throwback` IS the path to the protein complex from PDBTM.
