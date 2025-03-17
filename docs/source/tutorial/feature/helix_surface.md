# Helix surface

After generating LIPS results for protein `1xqf` chain `A`, we can make the most of them to annotate the protein at both surface and per-residue levels. In this tutorial, we show how we can use TMKit annotate each residue with helix surfaces of [LIPS results{octicon}`link-external;1em;sd-text-info`](./run_lips.md) that it belongs to.


:::{dropdown} Reminder of data
:animate: fade-in
:icon: database
:open: 

Please make sure that [the build-in example dataset{octicon}`link-external;1em;sd-text-info`](../get_started/example_dataset.md) has been downloaded before you walk through the tutorial.
:::



## {octicon}`file-code;1em;sd-text-info` **Example usage**
We can first read the file of a helix surface ID `id=1` using the following code. Please remember that we have put the results for protein `1xqf` chain `A` in folder `./data/lips/` as in [the last tutorial{octicon}`link-external;1em;sd-text-info`](./run_lips.md).


::::{tab-set}

:::{tab-item} {octicon}`code;1em;sd-text-info`Code
```{code} python
import tmkit as tmk

df = tmk.feature.read_helix_surf(
    fp='./data/lips/',
    prot_name='1xqf',
    file_chain='A',
    id=1,
)
print(df)
```
:::

:::{tab-item} {octicon}`file-added;1em;sd-text-info`Output
```{code} python
     aa_ids aa_names  lipos   ents  surf
0         2        V  0.026  1.158     1
1         5        K  0.804  6.798     1
2         6        A  0.573  4.896     1
3         9        A  0.697  4.852     1
4        12        M  0.973  3.694     1
..      ...      ...    ...    ...   ...
150     352        L  0.828  4.846     1
151     355        L  0.688  4.551     1
152     356        T  0.535  3.724     1
153     359        L  0.984  3.276     1
154     362        P  0.615  4.539     1

[155 rows x 5 columns]
```
:::

::::

The output is a dataframe containing 5 columns, as shown below.

| **Attribute** | **Description**                   |
|---------------|-----------------------------------|
| `aa_ids`      | amino acid ID                     |
| `aa_names`    | amino acid name                   |
| `lipos`       | the LIPOS score for an amino acid |
| `ents`        | entropy                           |
| `surf`        | the helix surface ID              |


If we want to annotate all amino acids with the helix surface IDs, we need to use all 7 surface data. In TMKit, we can do it this way.


::::{tab-set}

:::{tab-item} {octicon}`code;1em;sd-text-info`Code
```{code} python
import tmkit as tmk

aa_surf_rank, _, _, _ = tmk.feature.read(
    fp='./data/lips/',
    prot_name='1xqf',
    file_chain='A',
)
print(aa_surf_rank)
```
:::

:::{tab-item} {octicon}`file-added;1em;sd-text-info`Output
```{code} python
{1: 4, 4: 0, 5: 1, 8: 4, 11: 0, ..., 357: 2, 360: 5}
```
:::

::::



Actually, we can use TMKit to check the summary about all 7 surfaces, which shows the entropy, the LIPOS score, and the final LIPS score at the surface level.

::::{tab-set}

:::{tab-item} {octicon}`code;1em;sd-text-info`Code
```{code} python
import tmkit as tmk

df = tmk.feature.read_helix_all_surf(
    fp='./data/lips/',
    prot_name='1xqf',
    file_chain='A',
)
print(df)
```
:::

:::{tab-item} {octicon}`file-added;1em;sd-text-info`Output
```{code} python
   surfs  lipos   ents    lxe
0      5  1.834  4.846  8.889
1      0  1.770  4.912  8.694
2      3  1.729  4.852  8.389
3      1  1.815  4.885  8.865
4      2  1.791  4.749  8.507
5      6  1.777  4.746  8.435
6      4  1.767  4.948  8.741
```
:::

::::



## {octicon}`key;1em;sd-text-info` **Attributes**

| **Attribute** | **Description**                                                              |
|---------------|------------------------------------------------------------------------------|
| prot_name     | name of a protein in the prefix of a PDB file name (e.g., 1xqf in 1xqfA.pdb) |
| file_chain    | chain of a protein in the prefix of a PDB file name (e.g., A in 1xqfA.pdb)   |
| fp            | path where the LIPS results for a protein are placed                         |
| id            | surface id, 0-6                                                              |
 
:::{seealso}
Please see [here{octicon}`link-external;1em;sd-text-info`](../../get_started/feature.md#nomenclature) for better understanding the file-naming system.
:::



## {octicon}`file-added;1em;sd-text-info` **Output**
Please check the output in each vignette above.
