# Lipophilicity score

After generating LIPS results for protein `1xqf` chain `A`, we can utilize them to annotate the protein at both the surface level and per-residue level.

In this tutorial, we demonstrate how to use TMKit to annotate each residue with its corresponding lipophilicity scores derived from the LIPS results.


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

df = tmk.feature.get_surf_lips(
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
    aa_ids  lipos
0         2  0.026
1         5  0.804
2         6  0.573
3         9  0.697
4        12  0.973
..      ...    ...
150     352  0.828
151     355  0.688
152     356  0.535
153     359  0.984
154     362  0.615

[155 rows x 2 columns]
```
:::

::::

The output is a dataframe containing 2 columns, that is, aa_ids and lipos, as shown below.

| **Attribute** | **Description**     |
|---------------|---------------------|
| aa_ids        | amino acid ID       |
| lipos         | lipophilicity score |

If we want to annotate all amino acids with the lipophilicity scores, we need to use all 7 surface data. In TMKit, we can do it this way.


::::{tab-set}

:::{tab-item} {octicon}`code;1em;sd-text-info`Code
```{code} python
import tmkit as tmk

_, lipos_dict, _, _ = tmk.feature.read(
    fp='./data/lips/',
    prot_name='1xqf',
    file_chain='A',
)
print(lipos_dict)
```
:::

:::{tab-item} {octicon}`file-added;1em;sd-text-info`Output
```{code} python
{1.0: 0.018, 4.0: 0.74, 5.0: 0.804, ..., 357.0: 0.727, 360.0: 1.174}
```
:::

::::


Actually, we can use TMKit to check the summary about all 7 surfaces, which shows the overall lipophilicity score at the surface level.

::::{tab-set}

:::{tab-item} {octicon}`code;1em;sd-text-info`Code
```{code} python
import tmkit as tmk

df = tmk.feature.get_helix_all_surf_lips(
    prot_name='1xqf',
    file_chain='A',
    fp='./data/lips/',
)
print(df)
```
:::

:::{tab-item} {octicon}`file-added;1em;sd-text-info`Output
```{code} python
   surfs  lipos
0      5  1.834
1      0  1.770
2      3  1.729
3      1  1.815
4      2  1.791
5      6  1.777
6      4  1.767
```
:::

::::


Additionally, there are average lipophilicity scores at the surface level, which can be accessed as follows. The column `lxe` represents the average lipophilicity scores.

::::{tab-set}

:::{tab-item} {octicon}`code;1em;sd-text-info`Code
```{code} python
import tmkit as tmk

df = tmk.feature.get_helix_all_surf_avelips(
    fp='./data/lips/',
    prot_name='1xqf',
    file_chain='A',
)
print(df)
```
:::

:::{tab-item} {octicon}`file-added;1em;sd-text-info`Output
```{code} python
   surfs    lxe
0      5  8.889
1      0  8.694
2      3  8.389
3      1  8.865
4      2  8.507
5      6  8.435
6      4  8.741
```
:::

::::

We can continue to make most of the average lipophilicity scores to annotate helix surfaces.

::::{tab-set}

:::{tab-item} {octicon}`code;1em;sd-text-info`Code
```{code} python
import tmkit as tmk

_, _, _, lips_dict = tmk.feature.read(
    fp='./data/lips/',
    prot_name='1xqf',
    file_chain='A',
)
print(lips_dict)
```
:::

:::{tab-item} {octicon}`file-added;1em;sd-text-info`Output
```{code} python
{5.0: [1.834, 4.846, 8.889], 0.0: [1.77, 4.912, 8.694], 3.0: [1.729, 4.852, 8.389], 1.0: [1.815, 4.885, 8.865], 2.0: [1.791, 4.749, 8.507], 6.0: [1.777, 4.746, 8.435], 4.0: [1.767, 4.948, 8.741]}
```
:::

::::

We finally sort out an overall dataframe containing the LIPS results for all amino acids using the code below.

::::{tab-set}

:::{tab-item} {octicon}`code;1em;sd-text-info`Code
```{code} python
import tmkit as tmk

df_surf = tmk.feature.read_helix_all_surf(
    fp='./data/lips/',
    prot_name='1xqf',
    file_chain='A',
)

df = tmk.feature.torosseta(
    fp='./data/lips/',
    prot_name='1xqf',
    file_chain='A',
    df_surf_lips=df_surf,
)
print(df)
```
:::

:::{tab-item} {octicon}`file-added;1em;sd-text-info`Output
```{code} python
======>reading surface 5
======>reading surface 0
======>reading surface 3
======>reading surface 1
======>reading surface 2
======>reading surface 6
======>reading surface 4
      aa_ids  mean_lipo  lipos   ents
0          6      8.435  0.573  4.896
1          9      8.435  0.697  4.852
2         10      8.435  1.621  2.735
3         13      8.435  0.838  5.327
4         16      8.435  0.722  4.914
...      ...        ...    ...    ...
1080     358      8.507  0.522  2.980
1081     359      8.507  0.984  3.276
1082     362      8.507  0.615  4.539
1083       1      8.507  0.018  1.125
1084       2      8.507  0.026  1.158

[1085 rows x 4 columns]
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
