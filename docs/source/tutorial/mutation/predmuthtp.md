# Pred-MutHTP

[The Pred-MutHTP database{octicon}`link-external;1em;sd-text-info`](https://www.iitm.ac.in/bioinfo/PredMutHTP/index.php)[^1] contains predicted disease‐causing and neutral mutations in human transmembrane proteins. In the absence of experimentally-verified records, these are extremely useful for providing information about the status of mutations that occur in amino acid sites of human transmembrane proteins.

TMKit offers an interface (`tmkit.mut`) to access the database.

:::{dropdown} Reminder of data
:animate: fade-in
:icon: database
:open: 

Please make sure that [the build-in example dataset{octicon}`link-external;1em;sd-text-info`](../get_started/example_dataset.md) has been downloaded before you walk through the tutorial.
:::



## {octicon}`download;1em;sd-text-info` **Download and read**

First, let's download the database of Pred-MutHTP. In the example dataset, there is a folder called `mutation`. The path is `./data/mutation/`, which is the place where we suggest users to manage the data used and generated.

The database is called `pred_varhtp_mut.zip`. You should decompress it after downloading.

```{code} python
import tmkit as tmk

tmk.mut.download_predmuthtp_db(
    sv_fp='./data/mutation/'
)
```

After decompressing it, you will have `pred_varhtp_mut.csv`. We can now access this database using the following code.

```{code} python
import tmkit as tmk

df = tmk.mut.read_predmuthtp_db(
    pred_muthtp_fpn='./data/mutation/pred_varhtp_mut.csv'
)
print(df)
```

Finally, you will see the following output, which shows 5 features in Pred-MutHTP, including:

* `uniprot_id` 
* `protein_mutation_site` 
* `topology` 
* `mutation_type` 
* `mut_prob`

You can extract each of the feature in Python, e.g., `df['topology']`.


#### {octicon}`key;1em;sd-text-info` **Attributes**

| **Attribute** | **Description**                                                  |
|---------------|------------------------------------------------------------------|
| `pred_muthtp_fpn`  | path where the Pred-MutHTP database is placed            |
| `sv_fp`       | path to where you want to save the Pred-MutHTP database to be downloaded |

:::{seealso}
Please see [here{octicon}`link-external;1em;sd-text-info`](../get_started/feature.md#nomenclature) for better understanding the file-naming system.
:::

#### {octicon}`file-added;1em;sd-text-info` **Output**

```{code} python
======>reading Pred-MutHTP...
======>Pred-MutHTP features are:
=========>No.1: uniprot_id
=========>No.2: protein_mutation_site
=========>No.3: topology
=========>No.4: mutation_type
=========>No.5: mut_prob
         uniprot_id protein_mutation_site  ...    mutation_type mut_prob
0            A0PJX4                   M1A  ...          Neutral    0.731
1            A0PJX4                   M1C  ...          Neutral    0.731
2            A0PJX4                   M1D  ...  Disease-causing    0.745
3            A0PJX4                   M1E  ...  Disease-causing    0.745
4            A0PJX4                   M1F  ...  Disease-causing    0.745
...             ...                   ...  ...              ...      ...
54962537     Q9Y277                 A283S  ...          Neutral    0.820
54962538     Q9Y277                 A283T  ...          Neutral    0.525
54962539     Q9Y277                 A283V  ...  Disease-causing    0.542
54962540     Q9Y277                 A283W  ...  Disease-causing    0.690
54962541     Q9Y277                 A283Y  ...  Disease-causing    0.658

[54962542 rows x 5 columns]
```



## {octicon}`unfold;1em;sd-text-info` **Split into individual files**

This will split the Pred-MutHTP database into individual files according to the UniProt accession codes of human transmembrane proteins.

```{code} python
import tmkit as tmk

df = tmk.mut.read_predmuthtp_db(
    pred_muthtp_fpn='./data/mutation/pred_varhtp_mut.csv'
)

tmk.mut.split_predmuthtp(
    pred_muthtp_df=df,
    sv_fp='data/mutation/'
)
```

#### {octicon}`key;1em;sd-text-info` **Attributes**

| **Attribute**     | **Description**                                                          |
|-------------------|--------------------------------------------------------------------------|
| `pred_muthtp_df`  | Pandas dataframe of the Pred-MutHTP database                             |
| `pred_muthtp_fpn` | path where the Pred-MutHTP database is placed                            |
| `sv_fp`           | path to where you want to save the Pred-MutHTP database to be downloaded |

:::{seealso}
Please see [here{octicon}`link-external;1em;sd-text-info`](../get_started/feature.md#nomenclature) for better understanding the file-naming system.
:::

#### {octicon}`file-added;1em;sd-text-info` **Output**

In the console, it prints the output as shown below.

```{code} python
======>5185 uniprot proteins
=========>Splitting No.0 protein from Pred-MutHTP
=========>Splitting No.1 protein from Pred-MutHTP
=========>Splitting No.2 protein from Pred-MutHTP
=========>Splitting No.3 protein from Pred-MutHTP
......
```



## {octicon}`file-symlink-file;1em;sd-text-info` **Access an individual file**

Now, we can see what is contained in an individual file. Let's check this protein `A0PK00` (UniProt accession code) using the following code.

```{code} python
import tmkit as tmk

df = tmk.mut.read_split_predmuthtp(
    pred_split_muthtp_fpn='data/mutation/A0PK00.predmuthtp'
)
```

#### {octicon}`key;1em;sd-text-info` **Attributes**

| **Attribute**     | **Description**                                                          |
|-------------------|--------------------------------------------------------------------------|
| `pred_split_muthtp_fpn`  | path where an individual file from the Pred-MutHTP database is placed |

:::{seealso}
Please see [here{octicon}`link-external;1em;sd-text-info`](../get_started/feature.md#nomenclature) for better understanding the file-naming system.
:::

#### {octicon}`file-added;1em;sd-text-info` **Output**

In the console, it prints the output as shown below.

```{code} python
======>reading split Pred-MutHTP...
     uniprot_id protein_mutation_site  mut_prob
0        W5XKT8                  Y34A     0.698
1        W5XKT8                  Y34C     0.567
2        W5XKT8                  Y34D     0.551
3        W5XKT8                  Y34E     0.642
4        W5XKT8                  Y34F     0.785
...         ...                   ...       ...
6151     W5XKT8                 N324S     0.598
6152     W5XKT8                 N324T     0.711
6153     W5XKT8                 N324V     0.859
6154     W5XKT8                 N324W     0.874
6155     W5XKT8                 N324Y     0.809

[6156 rows x 3 columns]
```


[^1]: Kulandaisamy, A., Jan Zaucha., Sakthivel, R., Frishman, D. and Gromiha, M.M. (2020). Pred-MutHTP: Prediction of disease-causing and neutral mutations in human transmembrane proteins Hum Mutat., 41(3): 581-590.
