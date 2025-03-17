# Entropy

After generating LIPS results for protein `1xqf` chain `A`, we can utilise them to annotate the protein at both the surface level and per-residue level.

In this tutorial, we demonstrate how to use TMKit to annotate each residue with entropy scores of the LIPS results that it belongs to.

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

df = tmk.feature.get_surf_entropy(
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
     aa_ids   ents
0         2  1.158
1         5  6.798
2         6  4.896
3         9  4.852
4        12  3.694
..      ...    ...
150     352  4.846
151     355  4.551
152     356  3.724
153     359  3.276
154     362  4.539

[155 rows x 2 columns]
```
:::

::::

The output is a dataframe containing 2 columns, that is, aa_ids and ents, as shown below.

| **Attribute** | **Description** |
|---------------|-----------------|
| aa_ids        | amino acid ID   |
| ents          | entropy score   |

If we want to annotate all amino acids with the entropy scores, we need to use all 7 surface data. In TMKit, we can do it this way.

::::{tab-set}

:::{tab-item} {octicon}`code;1em;sd-text-info`Code
```{code} python
import tmkit as tmk

_, _, entropy_dict, _ = tmk.feature.read(
    fp='./data/lips/',
    prot_name='1xqf',
    file_chain='A',
)
print(entropy_dict)
```
:::

:::{tab-item} {octicon}`file-added;1em;sd-text-info`Output
```{code} python
{1.0: 1.125, 4.0: 5.71, 5.0: 6.798, ..., 357.0: 5.976, 360.0: 1.749}
```
:::

::::

Actually, we can use TMKit to check the summary about all 7 surfaces, which shows the overall entropy score at the surface level.

::::{tab-set}

:::{tab-item} {octicon}`code;1em;sd-text-info`Code
```{code} python
import tmkit as tmk

df = tmk.feature.get_helix_all_surf_entropy(
    fp='./data/lips/',
    prot_name='1xqf',
    file_chain='A',
)
print(df)
```
:::

:::{tab-item} {octicon}`file-added;1em;sd-text-info`Output
```{code} python
   surfs   ents
0      5  4.846
1      0  4.912
2      3  4.852
3      1  4.885
4      2  4.749
5      6  4.746
6      4  4.948
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
