# About


We are a computational team at the University of Oxford to develop mathematical modelss and artificial intelligent tools to better interpret biology.

UMIche is a UMI-centric platform designed to support the development and verification of UMI  collapsing methods, using both external and internal simulated or experimental data across multiple sequencing contexts, such as bulk and single-cell levels. It is highly modular, featuring Python interfaces to facilitate seamlessly integrate into other computational programs and analysis pipelines. UMIche comprises main four modules: **UMI collapsing method implementation**, **UMI collapsing pipeline implementation**, **UMI count matrix implementation**, and **visualisation of UMI metrics** (**Fig. 1**). The core of UMIche offers multifaceted functionalities for UMI deduplication at the single locus, bulk, single-cell levels.

<figure markdown="span">
  ![Image title](./img/umiche.jpg){ width="780" }
    <figcaption><strong>Fig</strong> 1. UMIche platform. </figcaption>
</figure>


```{warning}

**UMIche** is designed to run at the platform level by harmonising data formats from different sequencing protocols, calculating deduplication counts, exploring features of different methods, visualising analysis results, and etc. We particularly implemented the majority vote and set cover optimisation programs for homotrimer UMI collapsing. To better support the UMI-centric analysis, we further provide a deep learning-based framework for on-demand simulation of UMI count matrices at the single-cell level.
