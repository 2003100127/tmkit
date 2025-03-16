# Unigraph

 Consider two unipartite graphs 

```{math}
:label: mymath
(V_P+V_P, E_{uni,P})
```

and

```{math}
:label: mymath
(V_Q+V_Q, E_{uni,Q})
```

where edges between two vertices from the same set are only available are used to demarcate local residue-residue connections (LocRRCs, see [here{octicon}`link-external;1em;sd-text-info`](./concept.md)). A LocRRC is formed by any two elements from set V<sub>P</sub> or set V<sub>Q</sub>. We introduce a few kinds of unigraphs.


## {octicon}`share-android;1em;sd-text-info` **Fully-connected**
 Here, we mainly want to show how to construct a unipartite graph in Python, which can be recognised by TMKit. The unipartite graph is constructed by considering residue pairs in a fully-connected manner, as shown in the plot below.

```{image} ../../../img/local.jpg
:class: bg-primary
:width: 300px
:align: center
```
<div align="center">
Caption: Connections in a fully-connected manner in a unipartite graph.
</div>


:::{tip}
If there are two residues 1 and 2, how does TMKit find them and their neighbouring residues?
:::

In fact, either is marked by the **coordinate** `0`. If a neighbouring residue appears on the left side of residue 1, the **coordinate** of the neighbouring residue is `-1` (which will be paired to residue 1 per se), and a neighbouring residue appear on the right side of residue 1 the **coordinate** of the neighbouring residue is `1` (which will be paired to residue 1 per se).

In TMKit, we use the function below to generate a unigraph of one residue of a residue pair of interest.

```{code} python
import itertools

def combo2x2(array):
    combo = []
    ob = itertools.combinations(array, 2)
    for i in ob:
        combo.append(list(i))
    return combo
```

 If we have a residue at sequence position `4`, we want to check out the connections between each of its 3 neighbouring residues on the right and left sides (as shown in the plot below), we can first assign a list of positions to array, like the code below.

```{code} python
array = [1, 2, 3, 4, 5, 6, 7]
```


 Then, we can pass the array to the `combo2x2` function, we will obtain all the coordinates of all residue pairs in this unigraph, like below.


```{code} python
unigraph = combo2x2(array=array)
print(unigraph)

# output
[[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7],
 [2, 3], [2, 4], [2, 5], [2, 6], [2, 7],
 [3, 4], [3, 5], [3, 6], [3, 7],
 [4, 5], [4, 6], [4, 7],
 [5, 6], [5, 7],
 [6, 7],
]
```


 If the central residue is at sequence position `1`, the left positions of it will be padded by `None`, like this `[None, None, None, 1, 2, 3, 4]`. Then, the unigraph of it looks like this below.

```{code} python
[[None, None], [None, None], [None, 1], [None, 2], [None, 3], [None, 4],
 [None, None], [None, 1], [None, 2], [None, 3], [None, 4],
 [None, 1], [None, 2], [None, 3], [None, 4],
 [1, 2], [1, 3], [1, 4],
 [2, 3], [2, 4],
 [3, 4]
]
```

:::{attention}
Other kinds of unigraphs will be added...
:::
