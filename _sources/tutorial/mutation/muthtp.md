# MutHTP

[The MutHTP database{octicon}`link-external;1em;sd-text-info`](https://www.iitm.ac.in/bioinfo/MutHTP/index.php)[^1] collects a cohort of missense, insertion, and deletion mutation sites from the 5 commonly used resources: `Humsavar`, `SwissVar`, `1000 Genomes`, `COSMIC` and `ClinVar` databases.

TMKit offers an interface, `tmkit.mut` to access the MutHTP database.

:::{dropdown} Reminder of data
:animate: fade-in
:icon: database
:open: 

Please make sure that [the build-in example dataset{octicon}`link-external;1em;sd-text-info`](../get_started/example_dataset.md) has been downloaded before you walk through the tutorial.
:::



## {octicon}`file-code;1em;sd-text-info` **Example usage**

First, let's download a database of MutHTP. In the example dataset, there is a folder called `mutation`. The path is `./data/mutation/`, which is the place where we suggest users to manage the data used and generated.

```{code} python
import tmkit as tmk

tmk.mut.download_muthtp_db(
    version='2020',
    sv_fp='./data/mutation/'
)
```

After decompressing it, you will have `MutHTP_2020.txt`. We can now access this database using the following code.

```{code} python
import tmkit as tmk

df = tmk.mut.read_muthtp_db(
    muthtp_fpn='./data/mutation/MutHTP_2020.txt'
)
print(df)
```




## {octicon}`key;1em;sd-text-info` **Attributes**

| **Attribute** | **Description**                                                   |
|---------------|-------------------------------------------------------------------|
| `version`     | version of a MutHTP database, for example, 2020                   |
| `muthtp_fpn`  | path where a MutHTP database is placed                            |
| `sv_fp`       | path to where you want to save a MutHTP database to be downloaded |

:::{seealso}
Please see [here{octicon}`link-external;1em;sd-text-info`](../get_started/feature.md#nomenclature) for better understanding the file-naming system.
:::



## {octicon}`file-added;1em;sd-text-info` **Output**

Finally, you will see the following output, which shows 22 features in MutHTP, including Uniprot IDs (`uniprot_id`), PDB IDs (`pdb_id`), topological information (`topology`), etc. You can extract each of the feature in Python, e.g., `df['topology']`.

```{code} python
======>reading MutHTP...
======>MutHTP features are:
=========>No.1: id
=========>No.2: gene_id
=========>No.3: uniprot_id
=========>No.4: mutation_type
=========>No.5: chromosome_number
=========>No.6: origin_cell
=========>No.7: nucleotide_mutation_site
=========>No.8: protein_mutation_site
=========>No.9: pdb_id
=========>No.10: protein_structure_mutation_site
=========>No.11: 3D_structure
=========>No.12: interface
=========>No.13: transmembrane_domain
=========>No.14: topology
=========>No.15: disease
=========>No.16: disease_class
=========>No.17: uniprot_id_isoform
=========>No.18: neighbouring_residue
=========>No.19: source_database
=========>No.20: conservation_score
=========>No.21: odds_ratio
=========>No.22: type_passing_membrane
            id  gene_id  ... odds_ratio type_passing_membrane
0            1    ESYT2  ...          -            Multi-pass
1            2  SLC5A10  ...          -            Multi-pass
2            3  SLC5A10  ...          -            Multi-pass
3            4  SLC5A10  ...          -            Multi-pass
4            5  SLC5A10  ...          -            Multi-pass
...        ...      ...  ...        ...                   ...
206384  206385   SLC4A4  ...        NaN                   NaN
206385  206386   SLC4A4  ...        NaN                   NaN
206386  206387   SLC4A4  ...        NaN                   NaN
206387  206388   SLC4A4  ...        NaN                   NaN
206388  206389   SLC4A4  ...        NaN                   NaN

[206389 rows x 22 columns]
```

[^1]: A. Kulandaisamy, S. Binny Priya, R. Sakthivel, Svetlana Tarnovskaya, Ilya Bizin, Peter Hönigschmid, Dmitrij Frishman and M. Michael Gromiha* (2018) MutHTP: Mutations in Human Transmembrane Proteins . Bioinformatics, 34(13):2325-2326.
