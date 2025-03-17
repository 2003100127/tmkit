# Integrated metric

TMkit can bulk generate quality control (QC) metrics. The `tmk.qc.integrate` will integrate separate metrics generated through [this tutorial{octicon}`link-external;1em;sd-text-info`](../../quality_control/pre_processing/single_metric.md).

:::{dropdown} Reminder of data
:animate: fade-in
:icon: database
:open: 

Please make sure that [the build-in example dataset{octicon}`link-external;1em;sd-text-info`](../get_started/example_dataset.md) has been downloaded before you walk through the tutorial.
:::



## {octicon}`file-code;1em;sd-text-info` **Example usage**

First, we still use the 5 transmembrane proteins, that is, protein `1xqf` chain `A`, protein `1eq8` chain `A`, protein `6e3y` chain `E`, protein `3pux` chain `G` and protein `3udc` chain `A`, and put them in a Pandas dataframe as follows.

```{code} python
import pandas as pd

prots = [['1xqf', 'A'], ['1eq8', 'A'], ['6e3y', 'E'], ['3pux', 'G'], ['3udc', 'A'], ['3rko', 'A']]
df_prot = pd.DataFrame(prots, columns=['prot', 'chain'])
df_prot = df_prot.rename(columns={
    0: 'prot',
    1: 'chain',
})
print(df_prot)
```

Please refer to [this tutorial{octicon}`link-external;1em;sd-text-info`](../../quality_control/pre_processing/single_metric.md) for generating their PDB structures and XML files.

Then, we can generate QC metrics for them altogether using the following code.

```{code} python
import tmkit as tmk

df = tmk.qc.integrate(
    df_prot=df_prot,
    pdb_cplx_fp='data/pdb/pdbtm/',
    fasta_fp='data/fasta/',
    xml_fp='data/xml/',
    sv_fp='data/qc/',
    metrics=['rez', 'met', 'bio_name', 'head', 'desc', 'mthm', 'seq'],
)
print(df)
```


## {octicon}`key;1em;sd-text-info` **Attributes**

| **Attribute** | **Description**                                                          |
|---------------|--------------------------------------------------------------------------|
| `df_prot`     | Pandas dataframe storing protein names and chain names                   |
| `pdb_cplx_fp` | path where a protein complex file from PDBTM is placed                   |
| `fasta_fp`    | path where a protein Fasta file is placed                                |
| `xml_fp`      | path where a protein XML file from PDBTM is placed                       |
| `sv_fp`       | path to save files                                                       |
| `metrics`     | a QC metric: `rez`, `met`, `bio_name`, `head`, `desc`, `mthm`, and `seq` |

:::{seealso}
Please see [here{octicon}`link-external;1em;sd-text-info`](../get_started/feature.md#nomenclature) for better understanding the file-naming system.
:::



## {octicon}`file-added;1em;sd-text-info` **Output**

Finally, you can see the following output containing 7 metrics as illustrated above to allow for further QC analysis of the proteins.

```{code} python
======>metric: rez
=========>protein 1xqf chain A with rez 1.8
=========>protein 1eq8 chain A with rez nan
=========>protein 6e3y chain E with rez 3.3
=========>protein 3pux chain G with rez 2.3
=========>protein 3udc chain A with rez 3.35
=========>protein 3rko chain A with rez 3.0
======>metric: met
=========>protein 1xqf chain A with met x-ray diffraction
=========>protein 1eq8 chain A with met unknown
=========>protein 6e3y chain E with met x-ray diffraction
=========>protein 3pux chain G with met x-ray diffraction
=========>protein 3udc chain A with met x-ray diffraction
=========>protein 3rko chain A with met x-ray diffraction
======>metric: bio_name
=========>protein 1xqf chain A with bio_name the mechanism of ammonia transport based on the crystal structure of amtb of e. coli.
=========>protein 1eq8 chain A with bio_name three-dimensional structure of the pentameric helical bundle of the acetylcholine receptor m2 transmembrane segment
=========>protein 6e3y chain E with bio_name cryo-em structure of the active, gs-protein complexed, human cgrp receptor
=========>protein 3pux chain G with bio_name crystal structure of an outward-facing mbp-maltose transporter complex bound to adp-bef3
=========>protein 3udc chain A with bio_name crystal structure of a membrane protein
=========>protein 3rko chain A with bio_name crystal structure of the membrane domain of respiratory complex i from e. coli at 3.0 angstrom resolution
======>metric: head
=========>protein 1xqf chain A with head transport protein
=========>protein 1eq8 chain A with head signaling protein
=========>protein 6e3y chain E with head signaling protein
=========>protein 3pux chain G with head hydrolase/transport protein
=========>protein 3udc chain A with head membrane protein
=========>protein 3rko chain A with head oxidoreductase
======>metric: desc
=========>protein 1xqf chain A with desc TRANSPORT PROTEIN
=========>protein 1eq8 chain A with desc SIGNALING PROTEIN
=========>protein 6e3y chain E with desc SIGNALING PROTEIN
=========>protein 3pux chain G with desc HYDROLASE/TRANSPORT PROTEIN
=========>protein 3udc chain A with desc MEMBRANE PROTEIN
=========>protein 3rko chain A with desc OXIDOREDUCTASE
======>metric: mthm
=========>protein 1xqf chain A with mthm 11.0
=========>protein 1eq8 chain A with mthm 1.0
=========>protein 6e3y chain E with mthm 1.0
=========>protein 3pux chain G with mthm 6.0
=========>protein 3udc chain A with mthm 3.0
=========>protein 3rko chain A with mthm 3.0
======>0 extraction items failed using mthm.
======>metric: seq
   prot chain  ...                                             seq_aa  seq_len
0  1xqf     A  ...  AVADKADNAFMMICTALVLFMTIPGIALFYGGLIRGKNVLSMLTQV...    362.0
1  1eq8     A  ...                            EKMSTAISVLLAQAVFLLLTSQR     23.0
2  6e3y     E  ...  EANYGALLRELCLTQFQVDMEAVGETLWCDWGRTIRSYRELADCTW...    115.0
3  3pux     G  ...  AMVQPQKARLFITHLLLLLFIAAIMFPLLMVVAISLRQGNFATGSL...    293.0
4  3udc     A  ...  YDIKAVKFLLDVLKILIIAFIGIKFADFLIYRFYKLYSKSKIQLPQ...    267.0
5  3rko     A  ...  AFAIFLIVAIGLCCLMLVGGWFLGGRARARLRLSAKFYLVAMFFVI...     95.0

[6 rows x 11 columns]
```
