# FAQ

We put Q&A here on a regular basis according to users' questions.

:::{card} What does TMKit aim to do?
:link: ./tutorial/edge/unipartite/pipeline.html

Usually, computational analysis and modelling of transmembrane protein sequences and structures involve a wide range of procedures and requires different kinds of tools. For this reason, we developed TMKit, to simply address any of such procedures with a unified interface and significantly reduce the workload.
:::


:::{card} How is a window defined?
:link: ./tutorial/edge/unipartite/pipeline.html

A window of any size is applied to get the identifiers of serially ordered neighbouring residues of a residue/residue pairs of interest.
:::


:::{card} What questions is seqNetRR supposed to address?
:link: ./tutorial/edge/bipartite/concept.html

TMKit integrates **seqNetRR**, which is a high-performance computing library for constructing a variety of sets of residue connections and assigning features. It runs in linear time with respect to the number of residue pairs used. seqNetRR is mainly designed to learn the surrounding information of residues/residue pairs of interest for machine learning modelling.
:::


:::{card} What is the relation between TMKit and seqNetRR?
:link: ./tutorial/edge/bipartite/concept.html

seqNetRR works as a module in TMKit.
:::


:::{card} What are bipartite and unipartite graphs?
:link: ./tutorial/edge/bipartite/bigraph.html

seqNetRR constitutes bigraphs and unigraphs to build different kinds of connections between residues. Please refer to [bigraph](./tutorial/edge/bipartite/bigraph.md) and [unigraph](./tutorial/edge/unipartite/unigraph.md).
:::
