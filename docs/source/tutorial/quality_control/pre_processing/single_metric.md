# Single metric

TMkit can evaluate qualities of proteins using a QC metric. We currently compile 7 metrics shown as follows.

| **Attribute** | **Description**        |
|---------------|------------------------|
| desc          | biological description |
| met           | determination method   |
| bio_name      | biological name        |
| head          | headline notation      |
| mthm          | number of helices      |
| rez           | resolution             |
| seq           | sequence information   |

:::{dropdown} Reminder of data
:animate: fade-in
:icon: database
:open: 

Please make sure that [the build-in example dataset{octicon}`link-external;1em;sd-text-info`](../get_started/example_dataset.md) has been downloaded before you walk through the tutorial.
:::



## {octicon}`file-code;1em;sd-text-info` **Example usage**

First, let's define 5 transmembrane proteins to be used, protein `1xqf` chain `A`, protein `1eq8` chain `A`, protein `6e3y` chain `E`, protein `3pux` chain `G` and protein `3udc` chain `A`, and put them in a Pandas dataframe as follows.

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

We can download their PDB structures from PDBTM and save them in `./data/pdb/pdbtm/`.

::::{tab-set}

:::{tab-item} {octicon}`code;1em;sd-text-info`Code
```{code} python
import tmkit as tmk

tmk.seq.retrieve_pdb_from_pdbtm(
    prot_series=df_prot['prot'],
    sv_fp='./data/pdb/pdbtm/',
)
```
:::

:::{tab-item} {octicon}`file-added;1em;sd-text-info`Output
```{code} python
===>No.1 protein name: 1xqf
======>successfully downloaded!
===>No.2 protein name: 1eq8
======>successfully downloaded!
===>No.3 protein name: 6e3y
======>successfully downloaded!
===>No.4 protein name: 3pux
======>successfully downloaded!
===>No.5 protein name: 3udc
======>successfully downloaded!
===>No.6 protein name: 3rko
======>successfully downloaded!
```
:::

::::

We can then download their XML files from PDBTM and save them in `./data/xml/`.

::::{tab-set}

:::{tab-item} {octicon}`code;1em;sd-text-info`Code
```{code} python
import tmkit as tmk

tmk.seq.retrieve_xml_from_pdbtm(
    prot_series=df_prot['prot'],
    sv_fp='./data/xml/',
)
```
:::

:::{tab-item} {octicon}`file-added;1em;sd-text-info`Output
```{code} python
===>No.1 protein name: 1xqf
======>successfully downloaded!
===>No.2 protein name: 1eq8
======>successfully downloaded!
===>No.3 protein name: 6e3y
======>successfully downloaded!
===>No.4 protein name: 3pux
======>successfully downloaded!
===>No.5 protein name: 3udc
======>successfully downloaded!
===>No.6 protein name: 3rko
======>successfully downloaded!
```
:::

::::

Finally, we can just use the following one command generate the results using one of the above-mentioned 7 metrics. Each time you can just alter what's put in parameter metric.

```{code} python
import tmkit as tmk

df = tmk.qc.obtain_single(
    df_prot=df_prot,
    pdb_cplx_fp='./data/pdb/pdbtm/',
    fasta_fp='./data/fasta/',
    xml_fp='./data/xml/',
    sv_fp='./data/qc/',
    metric='desc', # 'desc' 'met', 'bio_name', 'head', 'mthm', 'seq'
)
print(df)
```



## {octicon}`key;1em;sd-text-info` **Attributes**

| **Attribute** | **Description**                                                      |
|---------------|----------------------------------------------------------------------|
| `df_prot`     | Pandas dataframe storing protein names and chain names               |
| `pdb_cplx_fp` | path where a protein complex file from PDBTM is placed               |
| `fasta_fp`    | path where a protein Fasta file is placed                            |
| `xml_fp`      | path where a protein XML file from PDBTM is placed                   |
| `sv_fp`       | path to save files                                                   |
| `metric`      | a QC metric: `rez`, `met`, `bio_name`, `head`, `desc`, `mthm`, `seq` |

:::{seealso}
Please see [here{octicon}`link-external;1em;sd-text-info`](../get_started/feature.md#nomenclature) for better understanding the file-naming system.
:::



## {octicon}`file-added;1em;sd-text-info` **Output**

::::{tab-set}

:::{tab-item} Resolution
```{code} python
=========>protein 1xqf chain A with rez 1.8
=========>protein 1eq8 chain A with rez nan
=========>protein 6e3y chain E with rez 3.3
=========>protein 3pux chain G with rez 2.3
=========>protein 3udc chain A with rez 3.35
=========>protein 3rko chain A with rez 3.0
   prot chain   rez
0  1xqf     A  1.80
1  1eq8     A   NaN
2  6e3y     E  3.30
3  3pux     G  2.30
4  3udc     A  3.35
5  3rko     A  3.00
```
:::

:::{tab-item} Determination method
```{code} python
=========>protein 1xqf chain A with met x-ray diffraction
=========>protein 1eq8 chain A with met unknown
=========>protein 6e3y chain E with met x-ray diffraction
=========>protein 3pux chain G with met x-ray diffraction
=========>protein 3udc chain A with met x-ray diffraction
=========>protein 3rko chain A with met x-ray diffraction
   prot chain                met
0  1xqf     A  x-ray diffraction
1  1eq8     A            unknown
2  6e3y     E  x-ray diffraction
3  3pux     G  x-ray diffraction
4  3udc     A  x-ray diffraction
5  3rko     A  x-ray diffraction
```
:::

:::{tab-item} Protein name
```{code} python
=========>protein 1xqf chain A with bio_name the mechanism of ammonia transport based on the crystal structure of amtb of e. coli.
=========>protein 1eq8 chain A with bio_name three-dimensional structure of the pentameric helical bundle of the acetylcholine receptor m2 transmembrane segment
=========>protein 6e3y chain E with bio_name cryo-em structure of the active, gs-protein complexed, human cgrp receptor
=========>protein 3pux chain G with bio_name crystal structure of an outward-facing mbp-maltose transporter complex bound to adp-bef3
=========>protein 3udc chain A with bio_name crystal structure of a membrane protein
=========>protein 3rko chain A with bio_name crystal structure of the membrane domain of respiratory complex i from e. coli at 3.0 angstrom resolution
   prot chain                                           bio_name
0  1xqf     A  the mechanism of ammonia transport based on th...
1  1eq8     A  three-dimensional structure of the pentameric ...
2  6e3y     E  cryo-em structure of the active, gs-protein co...
3  3pux     G  crystal structure of an outward-facing mbp-mal...
4  3udc     A            crystal structure of a membrane protein
5  3rko     A  crystal structure of the membrane domain of re...
```
:::

:::{tab-item} Header line information
```{code} python
=========>protein 1xqf chain A with head transport protein
=========>protein 1eq8 chain A with head signaling protein
=========>protein 6e3y chain E with head signaling protein
=========>protein 3pux chain G with head hydrolase/transport protein
=========>protein 3udc chain A with head membrane protein
=========>protein 3rko chain A with head oxidoreductase
   prot chain                         head
0  1xqf     A            transport protein
1  1eq8     A            signaling protein
2  6e3y     E            signaling protein
3  3pux     G  hydrolase/transport protein
4  3udc     A             membrane protein
5  3rko     A               oxidoreductase
```
:::

:::{tab-item} Description of proteins
```{code} python
=========>protein 1xqf chain A with desc TRANSPORT PROTEIN
=========>protein 1eq8 chain A with desc SIGNALING PROTEIN
=========>protein 6e3y chain E with desc SIGNALING PROTEIN
=========>protein 3pux chain G with desc HYDROLASE/TRANSPORT PROTEIN
=========>protein 3udc chain A with desc MEMBRANE PROTEIN
=========>protein 3rko chain A with desc OXIDOREDUCTASE
   prot chain                         desc
0  1xqf     A            TRANSPORT PROTEIN
1  1eq8     A            SIGNALING PROTEIN
2  6e3y     E            SIGNALING PROTEIN
3  3pux     G  HYDROLASE/TRANSPORT PROTEIN
4  3udc     A             MEMBRANE PROTEIN
5  3rko     A               OXIDOREDUCTASE
```
:::

:::{tab-item} Number of helices
```{code} python
=========>protein 1xqf chain A with mthm 11.0
=========>protein 1eq8 chain A with mthm 1.0
=========>protein 6e3y chain E with mthm 1.0
=========>protein 3pux chain G with mthm 6.0
=========>protein 3udc chain A with mthm 3.0
=========>protein 3rko chain A with mthm 3.0
   prot chain  mthm
0  1xqf     A  11.0
1  1eq8     A   1.0
2  6e3y     E   1.0
3  3pux     G   6.0
4  3udc     A   3.0
5  3rko     A   3.0
```
:::

:::{tab-item} Sequence information
```{code} python
=========>File failed: 1xqf A
=========>File failed: 1eq8 A
=========>File failed: 6e3y E
=========>File failed: 3pux G
=========>File failed: 3udc A
=========>File failed: 3rko A
   prot chain                                             seq_aa  seq_len
0  1xqf     A  AVADKADNAFMMICTALVLFMTIPGIALFYGGLIRGKNVLSMLTQV...    362.0
1  1eq8     A                            EKMSTAISVLLAQAVFLLLTSQR     23.0
2  6e3y     E  EANYGALLRELCLTQFQVDMEAVGETLWCDWGRTIRSYRELADCTW...    115.0
3  3pux     G  AMVQPQKARLFITHLLLLLFIAAIMFPLLMVVAISLRQGNFATGSL...    293.0
4  3udc     A  YDIKAVKFLLDVLKILIIAFIGIKFADFLIYRFYKLYSKSKIQLPQ...    267.0
5  3rko     A  AFAIFLIVAIGLCCLMLVGGWFLGGRARARLRLSAKFYLVAMFFVI...     95.0
```
:::

::::


You can use the information to do QC. For example, proteins that are determined by X-ray methods are reserved. You should do this as follows. Then, protein `1eq8` chain `A` will be eliminated.

```{code} python
df[df['met'] == 'x-ray diffraction']
```
