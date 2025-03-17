# Residue contact


[Protein residue contacts{octicon}`link-external;1em;sd-text-info`](https://en.wikipedia.org/wiki/Protein_contact_map) are crucial for protein structural prediction and drug target interaction prediction. TMKit allows users to parse protein residue contacts predicted by PSICOV[^1], FreeContact[^2], CCMPred[^3], Gremlin[^4], GDCA[^5], PlmDCA[^6], MemConP[^7], Membrain2[^8], and DeepHelicon[^9].

PSICOV, FreeContact, CCMPred, Gremlin, GDCA, and PlmDCA are canonical covariance methods, while MemConP, Membrain2, and DeepHelicon are machine learning methods specialized for transmembrane proteins.

:::{dropdown} Reminder of data
:animate: fade-in
:icon: database
:open: 

Please make sure that [the build-in example dataset{octicon}`link-external;1em;sd-text-info`](../get_started/example_dataset.md) has been downloaded before you walk through the tutorial.
:::



## {octicon}`file-code;1em;sd-text-info` **Example usage**

We can use the following code to obtain the residue contacts of protein `1xqf` chain `A`. Similar to other cases in our tutorial, there are commonly used parameters. Please the next section for details.

```{code} python
import tmkit as tmk

df1, df2 = tmk.rrc.read(
    prot_name='1xqf',
    seq_chain='A',
    fasta_fp='data/fasta/',
    pdb_fp='data/pdb/',
    xml_fp='data/xml/',
    dist_fp='data/rrc/',
    tool_fp='data/rrc/tool/',
    seq_sep_inferior=1,
    seq_sep_superior=None,
    tool='membrain2',
)
```



## {octicon}`key;1em;sd-text-info` **Attributes**

| **Attribute**    | **Description**                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| `pdb_fp`           | path where a target PDB file is placed                                                                                                       |
| `fasta_fp`         | path where a target Fasta file is placed                                                                                                     |
| `xml_fp`           | path where a target XML file is placed                                                                                                       |
| `dist_fp`          | path where a file containing real distances between residues is placed (please check the file at ./data/rrc in the example dataset)          |
| `tool_fp`          | path where a protein residue contact map file is placed                                                                                      |
| `tool`             | name of a contact prediction tool. It can be one of PSICOV, FreeContact, CCMPred, Gremlin, GDCA, PlmDCA, MemConP, Membrain2, and DeepHelicon |
| `seq_sep_inferior` | The lower bounds of how far any two residues are in pairs                                                                                    |
| `seq_sep_superior` | The upper bounds of how far any two residues are in pairs                                                                                    |
| `prot_name`        | name of a protein in the prefix of a PDB file name (e.g., 1xqf in 1xqfA.pdb)                                                                 |
| `seq_chain`        | chain of a protein in the prefix of a PDB file name (e.g., A in 1xqfA.pdb). Parameter file_chain will be converted within the function       |

:::{seealso}
Please see [here{octicon}`link-external;1em;sd-text-info`](../get_started/feature.md#nomenclature) for better understanding the file-naming system.
:::



## {octicon}`file-added;1em;sd-text-info` **Output**

There are two Pandas dataframes. The first one df1 is the dataframe containing the predicted contacts by tool Membrain2.

```{code} python
print(df1)
contact_id_1  contact_id_2     score
0                13            44  0.032846
1                13            45  0.011669
2                13            46  0.019312
3                13            47  0.089862
4                13            48  0.026575
...             ...           ...       ...
19443           308           349  0.044726
19444           308           350  0.080527
19445           308           351  0.039438
19446           308           352  0.034000
19447           308           353  0.074005
[19448 rows x 3 columns]
```

The second one df2 is the dataframe containing the real distances between two residues, such that.

| **Attribute** | **Description**                       |
|---------------|---------------------------------------|
| fasta_id_1    | Fasta id of the first residue         |
| aa_1          | Amino acid type of the first residue  |
| pdb_id_1      | PDB id of the first residue           |
| fasta_id_2    | Fasta id of the second residue        |
| aa_2          | Amino acid type of the second residue |
| pdb_id_2      | PDB id of the second residue          |
| dist          | distance                              |
| is_contact    | if they are in contact                |

```{code} python
print(df2)
fasta_id_1 aa_1 pdb_id_1 fasta_id_2 aa_2 pdb_id_2       dist is_contact
0             13    I       15         44    T       46  23.495386          0
1             13    I       15         45    Q       47  22.651615          0
2             13    I       15         46    V       48   18.67347          0
3             13    I       15         47    T       49  19.484049          0
4             13    I       15         48    V       50   21.53894          0
...          ...  ...      ...        ...  ...      ...        ...        ...
19443        308    F      332        349    G      373  35.690994          0
19444        308    F      332        350    Y      374  32.043457          0
19445        308    F      332        351    K      375  38.532841          0
19446        308    F      332        352    L      376  40.355228          0
19447        308    F      332        353    A      377  40.803558          0
[19448 rows x 8 columns]
```

You can combine the two dataframes directly because they have been aligned this way below, which makes your research easier.

```{code} python
import pandas as pd
df = pd.concat([df1, df2], axis=1)
print(df)
```

It outputs:

```{code} python
       contact_id_1  contact_id_2     score  ... pdb_id_2       dist is_contact
0                13            44  0.032846  ...       46  23.495386          0
1                13            45  0.011669  ...       47  22.651615          0
2                13            46  0.019312  ...       48   18.67347          0
3                13            47  0.089862  ...       49  19.484049          0
4                13            48  0.026575  ...       50   21.53894          0
...             ...           ...       ...  ...      ...        ...        ...
19443           308           349  0.044726  ...      373  35.690994          0
19444           308           350  0.080527  ...      374  32.043457          0
19445           308           351  0.039438  ...      375  38.532841          0
19446           308           352  0.034000  ...      376  40.355228          0
19447           308           353  0.074005  ...      377  40.803558          0

[19448 rows x 11 columns]
```



[^1]: David T. Jones, Daniel W. A. Buchan, Domenico Cozzetto, Massimiliano Pontil, PSICOV: precise structural contact prediction using sparse inverse covariance estimation on large multiple sequence alignments, Bioinformatics, Volume 28, Issue 2, January 2012, Pages 184–190, https://doi.org/10.1093/bioinformatics/btr638
[^2]: Kaján, L., Hopf, T.A., Kalaš, M. et al. FreeContact: fast and free software for protein contact prediction from residue co-evolution. BMC Bioinformatics 15, 85 (2014). https://doi.org/10.1186/1471-2105-15-85
[^3]: Stefan Seemayer, Markus Gruber, Johannes Söding, CCMpred—fast and precise prediction of protein residue–residue contacts from correlated mutations, Bioinformatics, Volume 30, Issue 21, November 2014, Pages 3128–3130, https://doi.org/10.1093/bioinformatics/btu500
[^4]: Sergey OvchinnikovLisa KinchHahnbeom ParkYuxing LiaoJimin PeiDavid E KimHetunandan KamisettyNick V GrishinDavid Baker (2015) Large-scale determination of previously unsolved protein structures using evolutionary information eLife 4:e09248.
[^5]: Baldassi C, Zamparo M, Feinauer C, Procaccini A, Zecchina R, et al. (2014) Fast and Accurate Multivariate Gaussian Modeling of Protein Families: Predicting Residue Contacts and Protein-Interaction Partners. PLOS ONE 9(3): e92721. https://doi.org/10.1371/journal.pone.0092721
[^6]: Ekeberg M, Lövkvist C, Lan Y, Weigt M, Aurell E. Improved contact prediction in proteins: using pseudolikelihoods to infer Potts models. Phys Rev E Stat Nonlin Soft Matter Phys. 2013 Jan;87(1):012707. doi: 10.1103/PhysRevE.87.012707. Epub 2013 Jan 11. PMID: 23410359.
[^7]: Hönigschmid P, Frishman D. Accurate prediction of helix interactions and residue contacts in membrane proteins. J Struct Biol. 2016 Apr;194(1):112-23. doi: 10.1016/j.jsb.2016.02.005. Epub 2016 Feb 3. PMID: 26851352.
[^8]: Jing Yang, Hong-Bin Shen, MemBrain-contact 2.0: a new two-stage machine learning model for the prediction enhancement of transmembrane protein residue contacts in the full chain, Bioinformatics, Volume 34, Issue 2, January 2018, Pages 230–238, https://doi.org/10.1093/bioinformatics/btx593
[^9]: Sun J, Frishman D. DeepHelicon: Accurate prediction of inter-helical residue contacts in transmembrane proteins by residual neural networks. J Struct Biol. 2020 Oct 1;212(1):107574. doi: 10.1016/j.jsb.2020.107574. Epub 2020 Jul 11. PMID: 32663598.
