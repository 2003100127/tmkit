# IntAct

[IntAct{octicon}`link-external;1em;sd-text-info`](https://www.ebi.ac.uk/intact/home)[^1]  is another one of the most widely-used databases that catalogues protein-protein interactions.

TMKit offers an interface, `tmkit.ppi`, to access the database. In this tutorial, we will show how we can use this database in Python, starting from downloading it.



## {octicon}`file-code;1em;sd-text-info` **Example usage**

First, let's download the IntAct database. In the example dataset, there is a folder called `ppi`. The path is `./data/ppi/`, which is the place where we suggest users to manage the data used and generated. We can choose either a specific version or the most recent version of the database. Using `current`, we can download the most recent version. Then we can save it in `./data/ppi/` through parameter `sv_fp`.

You should have a file called `intact.zip` after downloading. The `tmk.ppi.download_intact_db` function will automatically decompress it as `intact.txt`.

```{code} python
import tmkit as tmk

tmk.ppi.download_intact_db(
    version='current',
    sv_fp='./data/ppi/',
)
```

Then, using the following codes, you can access the database. The `data/ppi/intact.txt` is the IntAct database. The `tmk.ppi.read_intact_db` function will extract a subset of it containing only protein interactors A and B (`#ID(s) interactor A` and `ID(s) interactor B`).

Importantly, this function will save the subset as in `interA_B.intact` in `./data/ppi/interA_B.intact`.

```{code} python
import tmkit as tmk

df = tmk.ppi.read_intact_db(
    intact_fpn='./data/ppi/intact.txt',
    extract_ids=[
        '#ID(s) interactor A',
        'ID(s) interactor B',
    ],
    sv_fpn='data/ppi/interA_B.intact',
)
print(df)
```



## {octicon}`key;1em;sd-text-info` **Attributes**

| **Attribute** | **Description**                                                                                                                      |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------|
| `version`     | version of a BioGRID database, for example, `4.4.212`.                                                                               |
| `intact_fpn` | path where a IntAct database is placed                                                                                              |
| `sv_fp`       | path to where you want to save files                                                                                                 |
| `extract_ids` | a list that can include more than one feature, such as `#ID(s) interactor A` and `ID(s) interactor B`. |

:::{seealso}
Please see [here{octicon}`link-external;1em;sd-text-info`](../get_started/feature.md#nomenclature) for better understanding the file-naming system.
:::



## {octicon}`file-added;1em;sd-text-info` **Output**

Finally, you will see the following output, which shows **42** features in IntAct, for example `Taxid interactor A`. You can extract each of the feature in Python, e.g., `df['ID(s) interactor B']`.

```{code} python
======>reading IntAct...
======>IntAct features are:
=========>No.1: #ID(s) interactor A
=========>No.2: ID(s) interactor B
=========>No.3: Alt. ID(s) interactor A
=========>No.4: Alt. ID(s) interactor B
=========>No.5: Alias(es) interactor A
=========>No.6: Alias(es) interactor B
=========>No.7: Interaction detection method(s)
=========>No.8: Publication 1st author(s)
=========>No.9: Publication Identifier(s)
=========>No.10: Taxid interactor A
=========>No.11: Taxid interactor B
=========>No.12: Interaction type(s)
=========>No.13: Source database(s)
=========>No.14: Interaction identifier(s)
=========>No.15: Confidence value(s)
=========>No.16: Expansion method(s)
=========>No.17: Biological role(s) interactor A
=========>No.18: Biological role(s) interactor B
=========>No.19: Experimental role(s) interactor A
=========>No.20: Experimental role(s) interactor B
=========>No.21: Type(s) interactor A
=========>No.22: Type(s) interactor B
=========>No.23: Xref(s) interactor A
=========>No.24: Xref(s) interactor B
=========>No.25: Interaction Xref(s)
=========>No.26: Annotation(s) interactor A
=========>No.27: Annotation(s) interactor B
=========>No.28: Interaction annotation(s)
=========>No.29: Host organism(s)
=========>No.30: Interaction parameter(s)
=========>No.31: Creation date
=========>No.32: Update date
=========>No.33: Checksum(s) interactor A
=========>No.34: Checksum(s) interactor B
=========>No.35: Interaction Checksum(s)
=========>No.36: Negative
=========>No.37: Feature(s) interactor A
=========>No.38: Feature(s) interactor B
=========>No.39: Stoichiometry(s) interactor A
=========>No.40: Stoichiometry(s) interactor B
=========>No.41: Identification method participant A
=========>No.42: Identification method participant B
======>The file is saved.
        #ID(s) interactor A ID(s) interactor B
0                    P49418             O43426
1          intact:EB7121639             P49418
2          intact:EB7121654             P49418
3          intact:EB7121715             P49418
4                    P49418   intact:EB7121765
...                     ...                ...
1262938              Q80TR1             Q9WTS4
1262939              Q92556             P07355
1262940              Q92556             Q14185
1262941              Q92556             P07355
1262942              Q92556             P07355

[1262943 rows x 2 columns]
```



[^1]: Orchard S, Ammari M, Aranda B, Breuza L, Briganti L, Broackes-Carter F, Campbell NH, Chavali G, Chen C, del-Toro N, Duesbury M, Dumousseau M, Galeota E, Hinz U, Iannuccelli M, Jagannathan S, Jimenez R, Khadake J, Lagreid A, Licata L, Lovering RC, Meldal B, Melidoni AN, Milagros M, Peluso D, Perfetto L, Porras P, Raghunath A, Ricard-Blum S, Roechert B, Stutz A, Tognolli M, van Roey K, Cesareni G, Hermjakob H. The MIntAct project--IntAct as a common curation platform for 11 molecular interaction databases. Nucleic Acids Res. 2014 Jan;42(Database issue):D358-63. doi: 10.1093/nar/gkt1115. Epub 2013 Nov 13. PMID: 24234451; PMCID: PMC3965093.
