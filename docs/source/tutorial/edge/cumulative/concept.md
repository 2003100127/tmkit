# Concept

 We introduce the computational implementation of {bdg-link-primary-line}`co-evolutionary strengths/constraints<https://en.wikipedia.org/wiki/Coevolution>` quantification for individual residues. You may find it interesting for engineering this feature per residue. If you have a correlation matrix for any kind of biological interaction system, you may apply this idea to it.
 


## {octicon}`book;1em;sd-text-info` **Definition of cumuCCs**
Cumulated correlation coefficients (cumuCCs) are used to quantify co-evolutionary strength for individual residues, which is first brought to our eyes by Marks' team[^1]. It is different from globRRCs and LocRRCs for pairwise residues in biological networks.


:::{hint}
{bdg-danger-line}`how to calculate it?`
For a single residue, the cumuCCs of its ***k*** prioritized connections with other residue can reflect its biological importance in a network. In evolutionary biology, the sum of the highest evolutionary coupling scores of a residue can help evaluate the extent to which the residue bears evolutionary constraints. This has been used as an important feature to gauge whether a residue is an interaction site in transmembrane proteins[^2]<sup>&</sup>[^3].
:::



## {octicon}`pivot-column;1em;sd-text-info` **Illustration**
It is not problematic to generate cumuCCs at a fast speed for input proteins of any length. It is calculated as

```{math}
:label: mymath
cumuCC=1/c×CC_R
```

 where *CC_R* stands for the sum of correlation coefficients of ***k*** prioritized connections of a residue with other residues according to ranked correlation coefficients in descending order and *c* is the sum of the correlation matrix over all residues.


```{image} ../../../img/cumulated.jpg
:class: bg-primary
:width: 256px
:align: center
```
<div align="center">
Caption: cumuCCs shows the prioritized connections with the highest correlation scores between a central residue and others.
</div>



[^1]: Hopf TA, Colwell LJ, Sheridan R, Rost B, Sander C, Marks DS. Three-dimensional structures of membrane proteins from genomic sequencing. Cell. 2012 Jun 22;149(7):1607-21. doi: 10.1016/j.cell.2012.04.012. Epub 2012 May 10. PMID: 22579045; PMCID: PMC3641781.
[^2]: Zeng B, Hönigschmid P, Frishman D. Residue co-evolution helps predict interaction sites in α-helical membrane proteins. J Struct Biol. 2019 May 1;206(2):156-169. doi: 10.1016/j.jsb.2019.02.009. Epub 2019 Mar 2. PMID: 30836197.
[^3]: Sun J, Frishman D. Improved sequence-based prediction of interaction sites in α-helical transmembrane proteins by deep learning. Comput Struct Biotechnol J. 2021 Mar 9;19:1512-1530. doi: 10.1016/j.csbj.2021.03.005. PMID: 33815689; PMCID: PMC7985279.
