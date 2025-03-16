# Pipeline

In this tutorial, we show how to generate cumuCCs for amino acid residues at the per-protein level.

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



## {octicon}`list-ordered;1em;sd-text-info` **Extract residues**
 We can next extract all residues separated by a certain separation as shown below. The lower and upper bounds of how far a residue is next to another residue can be regulated by `seq_sep_inferior` and `seq_sep_superior`. When they are `0` and `None`, respectively, all unrepeated residues will be generated.

::::{tab-set}

:::{tab-item} {octicon}`code;1em;sd-text-info`Code
```{code} python
from tmkit.seqnetrr.combo.Length import length as plength

pos_list = plength(
    seq_sep_inferior=0,
    seq_sep_superior=None,
).tosgl(
    length=len(sequence),
)
print(pos_list[:10])
```
:::

:::{tab-item} {octicon}`file-added;1em;sd-text-info` **Output**
```{code} python
[[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], ...]
```
:::

::::



## {octicon}`list-unordered;1em;sd-text-info` **Generate a position list**
By utilizing `pos_list`, we can enrich residue information with additional details. The following code appends amino acid symbols to their respective positions.

For example, in the output, each array consists of four elements as shown below. For instance, an entry like [1, 'A', 1, 0] represents:

| Position | Case | Description                           |
|----------|------|---------------------------------------|
| 1        | `1`  | FASTA sequence position               |
| 2        | `A`  | Amino acid symbol                     |
| 3        | `1`  | Placeholder for PDB position          |
| 4        | `0`  | Placeholder for an additional feature |

This structure allows for flexible annotation and further feature integration.

::::{tab-set}

:::{tab-item} {octicon}`code;1em;sd-text-info`Code
```{code} python
from tmkit.seqnetrr.combo.Position import Position as pfasta

position = pfasta(
    sequence=sequence,
).single(
    pos_list=pos_list,
)
print(position[:10])
```
:::

:::{tab-item} {octicon}`file-added;1em;sd-text-info` **Output**
```{code} python
[[1, 'A', 1, 0],
[2, 'V', 2, 0],
[3, 'A', 3, 0],
[4, 'D', 4, 0],
[5, 'K', 5, 0],
[6, 'A', 6, 0],
[7, 'D', 7, 0],
[8, 'N', 8, 0],
[9, 'A', 9, 0],
[10, 'F', 10, 0],
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
from tmkit.seqnetrr.window.Single import Single

window_m_ids = Single(
    sequence=sequence,
    position=position,
    window_size=3,
).mid()
print(window_m_ids[:10])
```
:::

:::{tab-item} {octicon}`file-added;1em;sd-text-info` **Output**
```{code} python
[[None, None, None, 1, 2, 3, 4],
[None, None, 1, 2, 3, 4, 5],
[None, 1, 2, 3, 4, 5, 6],
[1, 2, 3, 4, 5, 6, 7],
[2, 3, 4, 5, 6, 7, 8],
[3, 4, 5, 6, 7, 8, 9],
[4, 5, 6, 7, 8, 9, 10],
[5, 6, 7, 8, 9, 10, 11],
[6, 7, 8, 9, 10, 11, 12],
[7, 8, 9, 10, 11, 12, 13],
 ...
 ]
```
:::

::::



## {octicon}`iterations;1em;sd-text-info` **Generate cumuCCs**
The code below can Generate cumuCCs for residues of interest.

::::{tab-set}

:::{tab-item} {octicon}`code;1em;sd-text-info`Code
```{code} python
from tmkit.seqnetrr.graph.Cumulative import Cumulative

res = Cumulative(
    sequence=sequence,
    window_size=5,
    window_m_ids=window_m_ids,
    input_kind='freecontact',
).assign(
    list_2d=position,
    L=int(len(sequence)/5),
    fpn='data/rrc/tool/1xqfA.evfold',
)
print(res)
```
:::

:::{tab-item} {octicon}`file-added;1em;sd-text-info` **Output**
```{code} python
[[1, 'A', 1, 0, 0, 0, 0, 0, 0, 0.0, 0.0, 981.2731380245631, 966.1044130133483, 876.1295995508353, 921.1073699092246],
[2, 'V', 2, 0, 0, 0, 0, 0, 0.0, 0.0, 981.2731380245631, 966.1044130133483, 876.1295995508353, 921.1073699092246, 866.7270683087568],
[3, 'A', 3, 0, 0, 0, 0, 0.0, 0.0, 981.2731380245631, 966.1044130133483, 876.1295995508353, 921.1073699092246, 866.7270683087568, 969.3246187616661],
[4, 'D', 4, 0, 0, 0, 0.0, 0.0, 981.2731380245631, 966.1044130133483, 876.1295995508353, 921.1073699092246, 866.7270683087568, 969.3246187616661, 819.806884450987],
[5, 'K', 5, 0, 0, 0.0, 0.0, 981.2731380245631, 966.1044130133483, 876.1295995508353, 921.1073699092246, 866.7270683087568, 969.3246187616661, 819.806884450987, 754.0407418336364],
[6, 'A', 6, 0, 0.0, 0.0, 981.2731380245631, 966.1044130133483, 876.1295995508353, 921.1073699092246, 866.7270683087568, 969.3246187616661, 819.806884450987, 754.0407418336364, 868.7066033260365],
[7, 'D', 7, 0, 0.0, 981.2731380245631, 966.1044130133483, 876.1295995508353, 921.1073699092246, 866.7270683087568, 969.3246187616661, 819.806884450987, 754.0407418336364, 868.7066033260365, 725.6260121243803],
[8, 'N', 8, 0, 981.2731380245631, 966.1044130133483, 876.1295995508353, 921.1073699092246, 866.7270683087568, 969.3246187616661, 819.806884450987, 754.0407418336364, 868.7066033260365, 725.6260121243803, 697.4153464206792],
[9, 'A', 9, 0, 966.1044130133483, 876.1295995508353, 921.1073699092246, 866.7270683087568, 969.3246187616661, 819.806884450987, 754.0407418336364, 868.7066033260365, 725.6260121243803, 697.4153464206792, 828.2056524269541],
[10, 'F', 10, 0, 876.1295995508353, 921.1073699092246, 866.7270683087568, 969.3246187616661, 819.806884450987, 754.0407418336364, 868.7066033260365, 725.6260121243803, 697.4153464206792, 828.2056524269541, 705.506309006248]],
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
| `L`            | top-ranked L co-evolutionary strengths that a residue of interest is involved in                                                                                                                                                                                                                  |

:::{seealso}
Please see [here{octicon}`link-external;1em;sd-text-info`](../../get_started/feature.md#nomenclature) for better understanding the file-naming system.
:::



## {octicon}`file-badge;1em;sd-text-info` **Mock test**
If you don't have a file of coevolutionary strengths for a protein, you still want to check what will happen with the function. You can use our built-in function for simulating a covariance matrix by assigning `simulate` to `input_kind` and `len(sequence)` to `simu_seq_len` and turning off parameter `fpn`. It will be like this.

::::{tab-set}

:::{tab-item} {octicon}`code;1em;sd-text-info`Code
```{code} python
from tmkit.seqnetrr.graph.Cumulative import Cumulative

res = Cumulative(
    sequence=sequence,
    window_size=5,
    window_m_ids=window_m_ids,
    input_kind='simulate',
).assign(
    list_2d=position,
    L=int(len(sequence)/5),
    simu_seq_len=len(sequence),
)
print(res[:10])
```
:::

:::{tab-item} {octicon}`file-added;1em;sd-text-info` **Output**
```{code} python
[[1, 'A', 1, 0, 0, 0, 0, 0, 0, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028],
[2, 'V', 2, 0, 0, 0, 0, 0, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028],
[3, 'A', 3, 0, 0, 0, 0, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028],
[4, 'D', 4, 0, 0, 0, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028],
[5, 'K', 5, 0, 0, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028],
[6, 'A', 6, 0, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028],
[7, 'D', 7, 0, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028],
[8, 'N', 8, 0, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028],
[9, 'A', 9, 0, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028],
[10, 'F', 10, 0, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028, 0.3988919667590028],
...
 ]
```
:::

::::
