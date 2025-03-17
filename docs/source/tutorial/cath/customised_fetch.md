# Fetch with customised metrics

 This tutorial will walk you through how to extract structure-related information from a Cath database using your customised metrics.

TMKit offers an interface, `tmkit.cath`, to access the database.



## {octicon}`file-code;1em;sd-text-info` **Example usage**

Suppose you have two proteins of interest. They are `3udc` chain `A` and `3rko` chain `A`. Let's define them in Python and render them in a Pandas dataframe as shown below.


```{code} python
import pandas as pd
prots = [['3udc', 'A'], ['3rko', 'A']]
df_prot = pd.DataFrame(prots, columns=['prot', 'chain'])
```

Then, we also need to read the downloaded Cath database (if you miss it, please see [here{octicon}`link-external;1em;sd-text-info`](./fetch_data.md)) in the following way.

```{code} python
import tmkit as tmk

df = tmk.cath.read(
    cath_fpn='./data/cath/cath-b-newest-all.txt',
    groupby='version',
    group='v4_2_0',
)
print(df)
```

If you are interested in `funfam_number`, `superfamily_id` and `pdb_segments` of the proteins, you can tell TMKit by using a list like below.

```{code} python
metrics = [
    'funfam_number',
    'superfamily_id',
    'pdb_segments',
]
```

Finally, we can extract all information about the two proteins using the `tmk.cath.fftojson` function. The results will be saved in `data/cath/processed.json`.

```{code} python
import tmkit as tmk

res = tmk.cath.fftojson(
    df_prot=df_prot,
    df_cath_domain=df,
    sv_fpn='data/cath/processed.json',
    targets=metrics,
)
print(res)
```



## {octicon}`key;1em;sd-text-info`**Attributes**

| **Attribute**    | **Description**                                                                                                               |
|------------------|-------------------------------------------------------------------------------------------------------------------------------|
| `version`        | version of the Cath database                                                                                                  |
| `sv_fpn`         | path to a file to save results                                                                                                |
| `cath_fpn`       | path to the downloaded Cath database                                                                                          |
| `groupby`        | metric used to group data, e.g., version. There are 4 metrics in total, i.e., `domain`, `version`, `superfamily`, and `bound` |
| `group`          | value of a metric. For example, if version is chosen, there are two, namely, `v4_2_0` and `putative`                          |
| `df_prot`        | Pandas dataframe of a series of proteins, consisting of protein names in the 1st column and chains in the 2nd column          |
| `df_cath_domain` | Pandas dataframe of the Cath database                                                                                         |
| `targets`        | protein structure-related metrics, e.g., `superfamily ID`                                                                     |



## {octicon}`file-added;1em;sd-text-info`**Output**

Finally, you will see the following output.

```{code} python
======>No.1 protein complex: 3udc
=========>domain id is: 3udcA01
=========>domain id is: 3udcA02
=========>domain id is: 3udcA03
=========>domain id is: 3udcB01
=========>domain id is: 3udcB02
=========>domain id is: 3udcB03
=========>domain id is: 3udcC01
=========>domain id is: 3udcC02
=========>domain id is: 3udcC03
=========>domain id is: 3udcD01
=========>domain id is: 3udcD02
=========>domain id is: 3udcD03
=========>domain id is: 3udcE01
=========>domain id is: 3udcE02
=========>domain id is: 3udcE03
=========>domain id is: 3udcF01
=========>domain id is: 3udcF02
=========>domain id is: 3udcF03
=========>domain id is: 3udcG01
=========>domain id is: 3udcG02
=========>domain id is: 3udcG03
======>No.2 protein complex: 3rko
=========>domain id is: 3rkoA00
=========>domain id is: 3rkoB02
=========>domain id is: 3rkoE00
=========>domain id is: 3rkoF01
=========>domain id is: 3rkoG00
=========>domain id is: 3rkoJ01
=========>domain id is: 3rkoK00
=========>domain id is: 3rkoL02
======>The file is saved.
{'3udc': {'A': {'01': {}, '02': {'funfam_number': 4564, 'superfamily_id': '2.30.30.60', 'pdb_segments': [{'pdb_code': '3udc', 'stop': '177', 'chain_code': 'A', 'start': '128'}]}, '03': {'funfam_number': None, 'superfamily_id': '3.30.70.100', 'pdb_segments': [{'pdb_code': '3udc', 'stop': '265', 'chain_code': 'A', 'start': '178'}]}}, 'B': {'01': {}, '02': {'funfam_number': 4564, 'superfamily_id': '2.30.30.60', 'pdb_segments': [{'pdb_code': '3udc', 'stop': '177', 'chain_code': 'B', 'start': '128'}]}, '03': {'funfam_number': None, 'superfamily_id': '3.30.70.100', 'pdb_segments': [{'pdb_code': '3udc', 'stop': '265', 'chain_code': 'B', 'start': '178'}]}}, 'C': {'01': {}, '02': {'funfam_number': 4564, 'superfamily_id': '2.30.30.60', 'pdb_segments': [{'pdb_code': '3udc', 'stop': '177', 'chain_code': 'C', 'start': '128'}]}, '03': {'funfam_number': None, 'superfamily_id': '3.30.70.100', 'pdb_segments': [{'pdb_code': '3udc', 'stop': '265', 'chain_code': 'C', 'start': '178'}]}}, 'D': {'01': {}, '02': {'funfam_number': 4564, 'superfamily_id': '2.30.30.60', 'pdb_segments': [{'pdb_code': '3udc', 'stop': '177', 'chain_code': 'D', 'start': '128'}]}, '03': {'funfam_number': None, 'superfamily_id': '3.30.70.100', 'pdb_segments': [{'pdb_code': '3udc', 'stop': '265', 'chain_code': 'D', 'start': '178'}]}}, 'E': {'01': {}, '02': {'funfam_number': 4564, 'superfamily_id': '2.30.30.60', 'pdb_segments': [{'pdb_code': '3udc', 'stop': '177', 'chain_code': 'E', 'start': '128'}]}, '03': {'funfam_number': None, 'superfamily_id': '3.30.70.100', 'pdb_segments': [{'pdb_code': '3udc', 'stop': '265', 'chain_code': 'E', 'start': '178'}]}}, 'F': {'01': {}, '02': {'funfam_number': 4564, 'superfamily_id': '2.30.30.60', 'pdb_segments': [{'pdb_code': '3udc', 'stop': '177', 'chain_code': 'F', 'start': '128'}]}, '03': {'funfam_number': None, 'superfamily_id': '3.30.70.100', 'pdb_segments': [{'pdb_code': '3udc', 'stop': '265', 'chain_code': 'F', 'start': '178'}]}}, 'G': {'01': {}, '02': {'funfam_number': 4564, 'superfamily_id': '2.30.30.60', 'pdb_segments': [{'pdb_code': '3udc', 'stop': '177', 'chain_code': 'G', 'start': '128'}]}, '03': {'funfam_number': None, 'superfamily_id': '3.30.70.100', 'pdb_segments': [{'pdb_code': '3udc', 'stop': '265', 'chain_code': 'G', 'start': '178'}]}}}, '3rko': {'A': {'00': {'funfam_number': None, 'superfamily_id': '1.20.58.1610', 'pdb_segments': [{'pdb_code': '3rko', 'stop': '126', 'chain_code': 'A', 'start': '15'}]}}, 'B': {'02': {}}, 'E': {'00': {'funfam_number': None, 'superfamily_id': '1.20.58.1610', 'pdb_segments': [{'pdb_code': '3rko', 'stop': '126', 'chain_code': 'E', 'start': '15'}]}}, 'F': {'01': {'funfam_number': None, 'superfamily_id': '1.20.120.1200', 'pdb_segments': [{'pdb_code': '3rko', 'stop': '160', 'chain_code': 'F', 'start': '1'}]}}, 'G': {'00': {}}, 'J': {'01': {'funfam_number': None, 'superfamily_id': '1.20.120.1200', 'pdb_segments': [{'pdb_code': '3rko', 'stop': '160', 'chain_code': 'J', 'start': '1'}]}}, 'K': {'00': {}}, 'L': {'02': {}}}}
```
