# BioGRID

[BioGRID{octicon}`link-external;1em;sd-text-info`](https://thebiogrid.org/)[^1] is one of the most widely-used databases that catalogues protein-protein interactions. In {bdg-primary-line}`version` 4.4.223, the database is constructed by going through more than 80,000 publications, which has 2,629,002 protein and genetic interactions.

According to the BioGRID database, transmembrane proteins are involved in nearly **a quarter of all confirmed human interactions**, and an even higher percentage (**almost 40%**) was identified based on the most recent human interactome map[^2].

TMKit offers an interface, `tmkit.ppi`, to access the database. In this tutorial, we will show how we can use this database in Python, starting from downloading it.


## {octicon}`file-code;1em;sd-text-info` **Example usage**

First, let's download the BioGRID database. In the example dataset, there is a folder called `ppi`. The path is `./data/ppi/`, which is the place where we suggest users to manage the data used and generated. We can choose a specific version of the database, namely, `4.4.212` and save it in `./data/ppi/` through parameter `sv_fp`.

You should have a file called `BIOGRID-ALL-4.4.212.tab3.zip` after downloading. The `tmk.ppi.download_biogrid_db` function will automatically decompress it as `BIOGRID-ALL-4.4.212.tab3.txt`.

```{code} python
import tmkit as tmk

tmk.ppi.download_biogrid_db(
    version='4.4.212',
    sv_fp='./data/ppi/',
)
```

Then, using the following codes, you can access the database. The `data/ppi/BIOGRID-ALL-4.4.212.tab3.txt` is the BioGRID database. The `tmk.ppi.read_biogrid_db` function will extract a subset of it containing only protein interactors A and B (`SWISS-PROT Accessions Interactor A` and `SWISS-PROT Accessions Interactor B`).

Importantly, this function will save the subset as in `BIOGRID-ALL-4.4.212.biogrid` in `./data/ppi/BIOGRID-ALL-4.4.212.biogrid`.

```{code} python
import tmkit as tmk

df = tmk.ppi.read_biogrid_db(
    biogrid_fpn='data/ppi/BIOGRID-ALL-4.4.212.tab3.txt',
    sv_fpn='data/ppi/BIOGRID-ALL-4.4.212.biogrid',
    extract_ids=[
        'SWISS-PROT Accessions Interactor A',
        'SWISS-PROT Accessions Interactor B',
    ],
)
print(df)
```



## {octicon}`key;1em;sd-text-info` **Attributes**

| **Attribute** | **Description**                                                                                                                      |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------|
| `version`     | version of a BioGRID database, for example, `4.4.212`.                                                                               |
| `biogrid_fpn` | path where a BioGRID database is placed                                                                                              |
| `sv_fp`       | path to where you want to save files                                                                                                 |
| `extract_ids` | a list that can include more than one feature, such as `SWISS-PROT Accessions Interactor A` and `SWISS-PROT Accessions Interactor B` |

:::{seealso}
Please see [here{octicon}`link-external;1em;sd-text-info`](../get_started/feature.md#nomenclature) for better understanding the file-naming system.
:::



## {octicon}`file-added;1em;sd-text-info` **Output**

Finally, you will see the following output, which shows **37** features in BioGRID, for example `Entrez Gene Interactor A`. You can extract each of the feature in Python, e.g., `df['SWISS-PROT Accessions Interactor A']`.

```{code} python
======>reading BioGRID...
======>BioGRID features are:
=========>No.1: #BioGRID Interaction ID
=========>No.2: Entrez Gene Interactor A
=========>No.3: Entrez Gene Interactor B
=========>No.4: BioGRID ID Interactor A
=========>No.5: BioGRID ID Interactor B
=========>No.6: Systematic Name Interactor A
=========>No.7: Systematic Name Interactor B
=========>No.8: Official Symbol Interactor A
=========>No.9: Official Symbol Interactor B
=========>No.10: Synonyms Interactor A
=========>No.11: Synonyms Interactor B
=========>No.12: Experimental System
=========>No.13: Experimental System Type
=========>No.14: Author
=========>No.15: Publication Source
=========>No.16: Organism ID Interactor A
=========>No.17: Organism ID Interactor B
=========>No.18: Throughput
=========>No.19: Score
=========>No.20: Modification
=========>No.21: Qualifications
=========>No.22: Tags
=========>No.23: Source Database
=========>No.24: SWISS-PROT Accessions Interactor A
=========>No.25: TREMBL Accessions Interactor A
=========>No.26: REFSEQ Accessions Interactor A
=========>No.27: SWISS-PROT Accessions Interactor B
=========>No.28: TREMBL Accessions Interactor B
=========>No.29: REFSEQ Accessions Interactor B
=========>No.30: Ontology Term IDs
=========>No.31: Ontology Term Names
=========>No.32: Ontology Term Categories
=========>No.33: Ontology Term Qualifier IDs
=========>No.34: Ontology Term Qualifier Names
=========>No.35: Ontology Term Types
=========>No.36: Organism Name Interactor A
=========>No.37: Organism Name Interactor B
======>The file is saved.
        SWISS-PROT Accessions Interactor A SWISS-PROT Accessions Interactor B
0                                   P45985                             Q14315
1                                   Q86TC9                             P35609
2                                   Q04771                             P49354
3                                   P23769                             P29590
4                                   P15927                             P40763
...                                    ...                                ...
2407708                             P0DTC2                             P53622
2407709                             P0DTC2                             Q96WV5
2407710                             P38260                             P11484
2407711                             P38260                             P32589
2407712                             P59594                             P53621

[2407713 rows x 2 columns]
```



[^1]: Chris Stark, Bobby-Joe Breitkreutz, Teresa Reguly, Lorrie Boucher, Ashton Breitkreutz, Mike Tyers, BioGRID: a general repository for interaction datasets, Nucleic Acids Research, Volume 34, Issue suppl_1, 1 January 2006, Pages D535–D539, https://doi.org/10.1093/nar/gkj109
[^2]: Luck, K., Kim, DK., Lambourne, L. et al. A reference map of the human binary protein interactome. Nature 580, 402–408 (2020). https://doi.org/10.1038/s41586-020-2188-x
