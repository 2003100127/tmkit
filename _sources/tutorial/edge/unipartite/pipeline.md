# Pipeline

In this tutorial, we show how to generate the unipartite graph of residue pairs (LocRRCs) at the per-protein level.

:::{tip}
Please make sure that [the build-in example dataset{octicon}`link-external;1em;sd-text-info`](../../get_started/example_dataset.md) has been downloaded before you walk through the tutorial.
:::

## {octicon}`file-code;1em;sd-text-info` **Read a sequence**
We begin by reading the sequence of protein `1xqf` chain `A` as shown below.

Please note that **seqNetRR** is capable of reading sequences from deoxyribonucleic acids (**DNA**), ribonucleic acids (**RNA**), and amino acids (**proteins**). Additionally, it can theoretically process sequences from any biological entity, making it a versatile tool for sequence analysis across multiple molecular types.

::::{tab-set}

:::{tab-item} {octicon}`code;1em;sd-text-info`Code
```{code} python
from tmkit.sequence import Fasta as sfasta

# read a sequence
sequence = sfasta.get(
    fasta_fpn='./data/fasta/1xqfA.fasta',
)
print(sequence)
```
:::

:::{tab-item} {octicon}`file-added;1em;sd-text-info` **Output**
```{code} python
AVADKADNAFMMICTALVLFMTIPGIALFYGGLIRGKNVLSMLTQVTVTFALVCILWVVYGYS
LAFGEGNNFFGNINWLMLKNIELTAVMGSIYQYIHVAFQGSFACITVGLIVGALAERIRFSAV
LIFVVVWLTLSYIPIAHMVWGGGLLASHGALDFAGGTVVHINAAIAGLVGAYLPHNLPMVFTG
TAILYIGWFGFNAGSAGTANEIAALAFVNTVVATAAAILGWIFGEWALRGKPSLLGACSGAIA
GLVGVTPACGYIGVGGALIIGVVAGLAGLWGVTMPCDVFGVHGVCGIVGCIMTGIFAASSLGG
VGFAEGVTMGHQLLVQLESIAITIVWSGVVAFIGYKLADLTVGLRVP
```
:::

::::



## {octicon}`list-ordered;1em;sd-text-info` **Extract residue pairs**
Next, we can generate all residue pairs that are separated by a specified distance range. The lower and upper bounds for residue separation are controlled by the parameters `seq_sep_inferior` and `seq_sep_superior`, respectively.

:::{tip}
If `seq_sep_inferior = 0` and `seq_sep_superior = None`, all possible non-redundant residue pairs will be generated, covering the entire sequence.
:::

Adjusting these parameters allows for fine-tuning residue pair selection based on sequence separation constraints.
The following example demonstrates how residue pairs are generated based on these settings.

::::{tab-set}

:::{tab-item} {octicon}`code;1em;sd-text-info`Code
```{code} python
from tmkit.seqnetrr.combo.Length import length as pl

# generate residue pairs according to sequence separation
pos_list = pl(
    seq_sep_superior=None,
    seq_sep_inferior=0
).to_pair(
    length=len(sequence)
)
print(pos_list[:10])
```
:::

:::{tab-item} {octicon}`file-added;1em;sd-text-info` **Output**
```{code} python
[[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], ...]
```
:::

::::



## {octicon}`list-unordered;1em;sd-text-info` **Generate a position list**
By utilizing `pos_list`, we can enrich residue information with additional details. The following code appends amino acid symbols to their respective positions.

For example, in the output, each array consists of four elements as shown below. For instance, an entry like [1, 'A', 1, 2, 'L', 2, 0] represents:

| Position | Case | Description                              |
|----------|------|------------------------------------------|
| 1        | `1`  | FASTA position (Residue 1)               |
| 2        | `A`  | Amino acid symbol (Residue 1)            |
| 3        | `1`  | Placeholder for PDB position (Residue 1) |
| 4        | `2`  | FASTA position (Residue 2)               |
| 5        | `L`  | Amino acid symbol (Residue 2)            |
| 6        | `2`  | Placeholder for PDB position (Residue 2) |
| 7        | `0`  | Placeholder for an additional feature    |

This structure allows for flexible annotation and further feature integration.

::::{tab-set}

:::{tab-item} {octicon}`code;1em;sd-text-info`Code
```{code} python
from tmkit.seqnetrr.combo.Position import Position as pfasta

position = pfasta(
    sequence=sequence,
).pair(
    pos_list=pos_list,
)
print(position[:10])
```
:::

:::{tab-item} {octicon}`file-added;1em;sd-text-info` **Output**
```{code} python
[[1, 'A', 1, 2, 'L', 2, 0],
 [1, 'A', 1, 3, 'L', 3, 0],
 [1, 'A', 1, 4, 'S', 4, 0],
 [1, 'A', 1, 5, 'F', 5, 0],
 [1, 'A', 1, 6, 'E', 6, 0],
 [1, 'A', 1, 7, 'R', 7, 0],
 [1, 'A', 1, 8, 'K', 8, 0],
 [1, 'A', 1, 9, 'Y', 9, 0],
 [1, 'A', 1, 10, 'R', 10, 0],
 [1, 'A', 1, 11, 'V', 11, 0],
 ...
]
```
:::

::::



## {octicon}`unfold;1em;sd-text-info` **Window setting**
A window with size **5** is placed to extract neighbouring residues of each of central residues.

::::{tab-set}

:::{tab-item} {octicon}`code;1em;sd-text-info`Code
```{code} python
from tmkit.seqnetrr.window.Pair import Pair

window_m_ids = Pair(
    sequence=sequence,
    position=position,
    window_size=5,
).mid()
print(window_m_ids[:10])
```
:::

:::{tab-item} {octicon}`file-added;1em;sd-text-info` **Output**
```{code} python
[[[None, None, 1, 2, 3], [None, 1, 2, 3, 4]],
 [[None, None, 1, 2, 3], [1, 2, 3, 4, 5]],
 [[None, None, 1, 2, 3], [2, 3, 4, 5, 6]],
 [[None, None, 1, 2, 3], [3, 4, 5, 6, 7]],
 [[None, None, 1, 2, 3], [4, 5, 6, 7, 8]],
 [[None, None, 1, 2, 3], [5, 6, 7, 8, 9]],
 [[None, None, 1, 2, 3], [6, 7, 8, 9, 10]],
 [[None, None, 1, 2, 3], [7, 8, 9, 10, 11]],
 [[None, None, 1, 2, 3], [8, 9, 10, 11, 12]],
 [[None, None, 1, 2, 3], [9, 10, 11, 12, 13]],
 ...
 ]
```
:::

::::

:::{tip}
The output lists the window-placed residues for each residue pair. The residues on the left or right are the window-placed residues of a central residue.
:::


## {octicon}`iterations;1em;sd-text-info` **Generate LocRRCs and assign features**
The code below can construct LocRRCs and assigns features to residue pairs of interest.

::::{tab-set}

:::{tab-item} {octicon}`code;1em;sd-text-info`Code
```{code} python
from tmkit.seqnetrr.graph.Unipartite import Unipartite as unigraph

res = unigraph(
    sequence=sequence,
    window_size=5,
    window_m_ids=window_m_ids,
    input_kind='freecontact',
).assign(
    list_2d=position,
    fpn='data/rrc/tool/1xqfA.evfold',
    mode='hash',
)
print(res)
```
:::

:::{tab-item} {octicon}`file-added;1em;sd-text-info` **Output**
```{code} python
[[1, 'A', 1, 2, 'V', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.20528, 1.62297, 0.867657, 5.95861, 2.41727, 4.77151, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.20528, 1.62297, 0.867657, 0.613155, 5.95861, 2.41727, 1.92145, 4.77151, 2.17778, 3.71394],
 [1, 'A', 1, 3, 'A', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.20528, 1.62297, 0.867657, 5.95861, 2.41727, 4.77151, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.20528, 1.62297, 0.867657, 0.613155, 1.22804, 5.95861, 2.41727, 1.92145, 1.15329, 4.77151, 2.17778, 1.78778, 3.71394, 2.28648, 3.84836],
 [1, 'A', 1, 4, 'D', 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.20528, 1.62297, 0.867657, 5.95861, 2.41727, 4.77151, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.20528, 1.62297, 0.867657, 0.613155, 1.22804, 0.457961, 5.95861, 2.41727, 1.92145, 1.15329, 0.981263, 4.77151, 2.17778, 1.78778, 0.812219, 3.71394, 2.28648, 3.22982, 3.84836, 2.79506, 3.31474],
 [1, 'A', 1, 5, 'K', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.20528, 1.62297, 0.867657, 5.95861, 2.41727, 4.77151, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.20528, 1.62297, 0.867657, 0.613155, 1.22804, 0.457961, 0.43229, 5.95861, 2.41727, 1.92145, 1.15329, 0.981263, 0.427951, 4.77151, 2.17778, 1.78778, 0.812219, 0.658312, 3.71394, 2.28648, 3.22982, 1.75035, 3.84836, 2.79506, 2.92361, 3.31474, 3.36977, 4.7285],
 [1, 'A', 1, 6, 'A', 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.20528, 1.62297, 0.867657, 5.95861, 2.41727, 4.77151, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.20528, 1.62297, 0.867657, 0.613155, 1.22804, 0.457961, 0.43229, 0.152289, 5.95861, 2.41727, 1.92145, 1.15329, 0.981263, 0.427951, 0.465656, 4.77151, 2.17778, 1.78778, 0.812219, 0.658312, 0.765282, 3.71394, 2.28648, 3.22982, 1.75035, 0.58954, 3.84836, 2.79506, 2.92361, 1.64622, 3.31474, 3.36977, 1.83432, 4.7285, 2.50384, 3.05042],
 ...
 ]
```
:::

::::


{bdg-warning-line}`Arributes`{octicon}`arrow-down-right;1em;sd-text-warning`

| **Arribute**   | **Description**                                                                                                                                                                                                                                                                                   |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `input_kind`   | feature format that is regulated by a co-evolution method, such ccmpred, freeContact, gdca, or plmc                                                                                                                                                                                               |
| `fpn`          | path where a covariance matrix (co-evolutionary features) is placed. The covariance matrix should be generated by either CCMPred, FreeContact, GDCA, or plm-DCA. Or, a file that contains three columns (the 1st two for residue pair IDs and the 3rd one for co-evolutionary strengths) is fine. |
| `mode`         | method to generate cumuCCs. It can be 'hash', 'hash_rf', 'hash_ori', 'pandas', or 'numpy'.                                                                                                                                                                                                        |
| `window_size`  | window size                                                                                                                                                                                                                                                                                       |
| `window_m_ids` | list of residues after applying a window                                                                                                                                                                                                                                                          |
| `sequence`     | molecular sequence                                                                                                                                                                                                                                                                                |

:::{seealso}
Please see [here{octicon}`link-external;1em;sd-text-info`](../../get_started/feature.md#nomenclature) for better understanding the file-naming system.
:::



## {octicon}`file-badge;1em;sd-text-info` **Mock test**
If you don't have a file of coevolutionary strengths for a protein, you still want to check what will happen with the function. You can use our built-in function for simulating a covariance matrix by assigning `simulate` to `input_kind` and `len(sequence)` to `simu_seq_len` and turning off parameter `fpn`. It will be like this.

::::{tab-set}

:::{tab-item} {octicon}`code;1em;sd-text-info`Code
```{code} python
from tmkit.seqnetrr.graph.Unipartite import Unipartite as unigraph

res = unigraph(
    sequence=sequence,
    window_size=5,
    window_m_ids=window_m_ids,
    input_kind='simulate',
).assign(
    list_2d=position,
    simu_seq_len=len(sequence),
    mode='hash',
)
print(res)
```
:::

:::{tab-item} {octicon}`file-added;1em;sd-text-info` **Output**
```{code} python
[[1, 'A', 1, 2, 'V', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 'A', 1, 3, 'A', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 'A', 1, 4, 'D', 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 'A', 1, 5, 'K', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 'A', 1, 6, 'A', 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 ...
 ]
```
:::

::::
