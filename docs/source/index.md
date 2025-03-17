![](https://img.shields.io/pypi/v/tmkit?logo=PyPI)
![Test](https://github.com/2003100127/tmkit/actions/workflows/test.yml/badge.svg)
![](https://img.shields.io/badge/last_released-Jul14._2023-green.svg)
![](https://img.shields.io/badge/tmkit-executable-519dd9.svg)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/2003100127/tmkit/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Anaconda](https://github.com/2003100127/tmkit/actions/workflows/conda.yml/badge.svg)](https://github.com/2003100127/tmkit/actions/workflows/conda.yml)
[![run with docker](https://img.shields.io/badge/run%20with-Docker-0db7ed?logo=docker)](https://www.docker.com/2003100127/tmkit)
[![Downloads](https://pepy.tech/badge/tmkitx)](https://pepy.tech/project/tmkitx)

# TMKit: transmembrane protein analysis

TMKit is an open-source Python programming interface, which is modular, scalable, and specifically designed for processing transmembrane protein data. It enables users to perform database wrangling, engineer features at the mutational, domain, and topological levels, and visualize protein-protein interaction interfaces through its unique programming interface. In addition, TMKit includes seqNetRR, a high-performance computing library that allows for customised construction and rewiring of residue connections. This library is particularly well-suited for assigning coevolutionary features at a fast speed.

```{image} img/tmkit_logo.png
:width: 230px
:align: center
```

<div align="center">

![Python](https://img.shields.io/badge/-Python-000?&logo=Python)
![Docker](https://img.shields.io/badge/-Docker-000?&logo=Docker)
![Anaconda](https://img.shields.io/badge/-Anaconda-000?&logo=Anaconda)
![PyPI](https://img.shields.io/badge/-PyPI-000?&logo=PyPI)

</div>


:::{admonition} 🌟Feature
* ✅ handing multiple kinds of transmembrane protein data
* ✅ fast speed
* ✅ structural visualisation
:::



## 🔧 **Functionalities**
TMKit provides **9** function classes to handle a number of transmembrane protein sequence and structural analysis problems, including visualization, sequence, quality control, topology, mapping, annotation, connectivity, edge extraction, and feature.

:::::{grid} 1 2 3 3
:gutter: 2

::::{grid-item-card} Sequence
:img-top: img/module/seq.png
:img-alt: 
^^^
A fundamental component designed to handle sequence reading in diverse formats, sequence retrieval from various sources, and MSA generation.
+++
learn more>>
::::

::::{grid-item-card} Topology
:img-top: img/module/topology.png
:img-alt: 
^^^
TM and non-TM topologies (side 1, side 2, strand, coil, inside, loop, and interfacial), structure-derived (TOPDB) or predicted topologies (TMHMM and Phobius).
+++
learn more>>
::::

::::{grid-item-card} Annotation
:img-top: img/module/annotation.png
:img-alt: 
^^^
Amino acid residues in biological functions annotated through the MutHTP, Pred-MutHTP and CATH databases.
+++
learn more>>
::::

::::{grid-item-card} Edge extraction
:img-top: img/module/edge.png
:img-alt: 
^^^
A high-performance computing library for extracting connections between residues by building graphs and assigning features quickly.
+++
learn more>>
::::

::::{grid-item-card} Visualization
:img-top: img/module/visualization.png
:img-alt: 
^^^
Identification of protein-protein interaction (PPI) interfaces critical to understand the biological processes.
+++
learn more>>
::::

::::{grid-item-card} Quality control
:img-top: img/module/quality_control.png
:img-alt: 
^^^
Evaluation criteria, including the experimentation methods used, resolution, subclass, and sequence length, to qualify proteins.
+++
learn more>>
::::

::::{grid-item-card} Mapping
:img-top: img/module/mapping.png
:img-alt: 
^^^
Identifier mapping between structural and sequence data (e.g., FASTA IDs and PDB IDs) to guarantee the correct interpretation of biological findings.
+++
learn more>>
::::

::::{grid-item-card} Connectivity
:img-top: img/module/connectivity.png
:img-alt: 
^^^
Studying connections of a protein to others in a PPI network is of crucial importance to understand its biological role.
+++
learn more>>
::::

::::{grid-item-card} Feature
:img-top: img/module/feature.png
:img-alt: 
^^^
A set of transmembrane protein-specific and general-purpose features is provided by TMKit in support of machine learning modelling.
+++
learn more>>
::::

:::::



## 🎯 **Easy to use**
After installation, you can import TMKit by putting the following code in a Python script or a Jupyter notebook. 
```python
import tmkit as tmk
```



## 📌 **Modules**
You can access the **14** modules covering **9** function classes.

:::{seealso}
install
:::

| No. | Module name   | Function class	 |                         Description                         |
|-----|---------------|-----------------|:-----------------------------------------------------------:|
| 1   | `tmk.fetch`   | Quality control |                     fetch example data                      |
| 2   | `tmk.qc`      | Quality control |  generate and extract metrics of sequences and structures   |
| 3   | `tmk.seq`     | Sequence        |               parse sequences and structures                |
| 4   | `tmk.msa`     | Sequence        | produce commands for generating multiple sequence alignment |
| 5   | `tmk.feature` | Feature         |                	protein biological features                 |
| 6   | `tmk.collate` | Mapping         |      seek difference between RCSB and PDBTM structures      |
| 7   | `tmk.topo`    | Topology        |              transmembrane protein topologies               |
| 8   | `tmk.rrc`     | Feature         |    	performance evaluation of residue contact prediction    |
| 9   | `tmk.ppi`     | Connectivity    |                    	protein connectivity                    |
| 10  | `tmk.mut`     | Annotation      |      	transmembrane protein's mutation data processing      |
| 11  | `tmk.vs`      | Visualization   |                	visualize protein structures                |
| 12  | `tmk.cath`    | Annotation      |             access protein domains and families             |
| 13  | `tmk.mapping` | Mapping         |           	conversion between protein identifiers           |
| 14  | `tmk.edge`    | Edge extraction |          rewiring of connections between residues           |



## 👨‍💻 **Developer**
[Jianfeng Sun{octicon}`link-external;1em;sd-text-info`](https://scholar.google.com/citations?hl=en&user=TfLBR9kAAAAJ&view_op=list_works&sortby=pubdate),  Nuffield Department of Orthopaedics, Rheumatology and Musculoskeletal Sciences (NDORMS), Headington, Oxford OX3 7LD, University of Oxford.



## 📘 **Citation**
:::{admonition} Citation
 Citation Jianfeng Sun, Arulsamy Kulandaisamy, Jinlong Ru, M Michael Gromiha, Adam P Cribbs, TMKit: a Python interface for computational analysis of transmembrane proteins, Briefings in Bioinformatics, Volume 24, Issue 5, September 2023, bbad288, https://doi.org/10.1093/bib/bbad288
:::



```{toctree}
:hidden: true
:maxdepth: 1

installation
tutorial/index
feature
faq
about
contact
whatsnew
issue
versions
```
