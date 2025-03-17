# Foldseek-AlphaFold2

In this tutorial, we introduce how TMKit can use a structural alignment method, [Foldseek{octicon}`link-external;1em;sd-text-info`](https://search.foldseek.com/)[^1], for seeking functional similar protein structures to an input protein struture by searching a few databases.




## {octicon}`file-code;1em;sd-text-info` **Example usage**
First, a good scenario where Foldseek is applied is when we need to understand a predicted structure of a protein. For conveniences, we use 4 AlphaFold2-predicted structures of proteins `P63092`, `Q9B6E8`, `P07256`, and `P63027`. They are saved in `./data/`.

```{code} python
import tmkit as tmk
import pandas as pd

prot_series = pd.Series(['P63092', 'Q9B6E8', 'P07256', 'P63027'])
tmk.seq.retrieve_pdb_alphafold(
    prot_series=prot_series,
    sv_fp='./data/',
)
```

#### {octicon}`file-added;1em;sd-text-info` **Output**

```{code} python
===>No.1 protein name: P63092
======>successfully downloaded!
===>No.2 protein name: Q9B6E8
======>successfully downloaded!
===>No.3 protein name: P07256
======>successfully downloaded!
===>No.4 protein name: P63027
======>successfully downloaded!
```

Then, we can run `tmk.seq.retrieve_foldseek` to search a few databases by Foldseek. By default, the databases include `afdb50`, `afdb-swissprot`, `afdb-proteome`, `cath50`, `mgnify_esm30`, `pdb100`, and `gmgcl_id`. We can save the Foldseek results in `./data/` as well.

```{code} python
import tmkit as tmk

tmk.seq.retrieve_foldseek(
    pdb_fp='./data/',
    prot_name='P63027', # https://alphafold.ebi.ac.uk/entry/P63027
    sv_fp='./data/',
)
```

#### {octicon}`file-added;1em;sd-text-info` **Output**

```{code} python
===>Searching databases by foldseek...
===>Results have been saved!
```

Then, we can check the results using the following code. For example, we want to check the result for `P63027` and the file is saved as `./data/P63027_foldseek_result.gz`. Please find the output in section 3 Output below.

```{code} python
import tarfile
import pandas as pd

with tarfile.open('./data/P63027_foldseek_result.gz', "r") as tar:
    csv_path = tar.getnames()[0]
    for i in tar.getnames():
        print(tar.extractfile(i))
        df = pd.read_csv(tar.extractfile(i), header=None, sep="\t")
        print(df)
```



## {octicon}`file-added;1em;sd-text-info` **Output**

```{code} python
===>Database: alis_afdb-proteome.m8
         0   ...                               20
0   job.pdb  ...                Rattus norvegicus
1   job.pdb  ...                      Danio rerio
2   job.pdb  ...                     Mus musculus
3   job.pdb  ...              Trichuris trichiura
4   job.pdb  ...       Cladophialophora carrionii
5   job.pdb  ...            Madurella mycetomatis
6   job.pdb  ...  Sporothrix schenckii ATCC 58251
7   job.pdb  ...  Schizosaccharomyces pombe 972h-
8   job.pdb  ...    Fonsecaea pedrosoi CBS 271.37
9   job.pdb  ...           Caenorhabditis elegans
10  job.pdb  ...    Histoplasma capsulatum G186AR
11  job.pdb  ...                         Zea mays

[12 rows x 21 columns]
===>Database: alis_afdb-swissprot.m8
         0   ...                               20
0   job.pdb  ...                     Homo sapiens
1   job.pdb  ...                   Macaca mulatta
2   job.pdb  ...                       Bos taurus
3   job.pdb  ...                Rattus norvegicus
4   job.pdb  ...                     Mus musculus
5   job.pdb  ...                   Xenopus laevis
6   job.pdb  ...                     Mus musculus
7   job.pdb  ...                       Bos taurus
8   job.pdb  ...                     Homo sapiens
9   job.pdb  ...                Rattus norvegicus
10  job.pdb  ...                     Mus musculus
11  job.pdb  ...              Macaca fascicularis
12  job.pdb  ...                     Homo sapiens
13  job.pdb  ...           Caenorhabditis elegans
14  job.pdb  ...              Schistosoma mansoni
15  job.pdb  ...                       Bos taurus
16  job.pdb  ...                     Pongo abelii
17  job.pdb  ...   Saccharomyces cerevisiae S288C
18  job.pdb  ...  Schizosaccharomyces pombe 972h-
19  job.pdb  ...           Caenorhabditis elegans
20  job.pdb  ...                     Homo sapiens
21  job.pdb  ...                     Homo sapiens

[22 rows x 21 columns]
===>Database: alis_afdb50.m8
         0   ...                             20
0   job.pdb  ...                    Danio rerio
1   job.pdb  ...                    Danio rerio
2   job.pdb  ...                   Mus musculus
3   job.pdb  ...            Macaca fascicularis
4   job.pdb  ...  Periophthalmus magnuspinnatus
..      ...  ...                            ...
56  job.pdb  ...      Verrucomicrobia bacterium
57  job.pdb  ...           Caulobacter sp. FWC2
58  job.pdb  ...           Fusarium euwallaceae
59  job.pdb  ...                Jatropha curcas
60  job.pdb  ...            Tribolium castaneum

[61 rows x 21 columns]
===>Database: alis_cath50.m8
         0        1   ...       19                              20
0   job.pdb  3hd7A00  ...    10116               Rattus norvegicus
1   job.pdb  3hd7E00  ...    10116               Rattus norvegicus
2   job.pdb  1sfcE00  ...    10116               Rattus norvegicus
3   job.pdb  1sfcI00  ...    10116               Rattus norvegicus
4   job.pdb  1sfcA00  ...    10116               Rattus norvegicus
5   job.pdb  1kilA00  ...     9606                    Homo sapiens
6   job.pdb  2n1tA00  ...     9606                    Homo sapiens
7   job.pdb  5ccgG00  ...    10116               Rattus norvegicus
8   job.pdb  5ccgA00  ...    10116               Rattus norvegicus
9   job.pdb  5kj7A00  ...    10116               Rattus norvegicus
10  job.pdb  5cchA00  ...    10116               Rattus norvegicus
11  job.pdb  6ip1A00  ...     9913                      Bos taurus
12  job.pdb  1l4aA00  ...  1051067             Doryteuthis pealeii
13  job.pdb  2npsA00  ...    10116               Rattus norvegicus
14  job.pdb  4wy4A00  ...     9606                    Homo sapiens
15  job.pdb  3b5nA00  ...   559292  Saccharomyces cerevisiae S288C

[16 rows x 21 columns]
===>Database: alis_gmgcl_id.m8
        0   ...                                                 18
0  job.pdb  ...  YEVTNVSPDEITGDGPGFTDTEWDGDDVTASLPNPSEADDAAGVLD...
1  job.pdb  ...  LTTVSDEWCVSTCAAGCPPAASLWCRCEDVRAADAVPANQGAAAWG...
2  job.pdb  ...  IILSISNKQDTEKIQRESWNIWGTSQWYSTYTIMIKTDVDEYKIVE...

[3 rows x 19 columns]
===>Database: alis_mgnify_esm30.m8
        0   ...                                                 18
0  job.pdb  ...  MSIKYLLIGNPEDCEEIGHYPDRGASKTTAKEADKIFKKLSQSGIQ...
1  job.pdb  ...  MSIQYVLIGNPEDCEEIGHYPDRGASKSIAKEANQIFKKLSESGIK...
2  job.pdb  ...  MTSSSPYEYSAVARNTTILAQFANSNGNFDVLVTEILQKINIPENQ...
3  job.pdb  ...  MAVQYSSIYQGQDLLASKSNGSLPNNVKKLMDSIAIQAKPNDLACV...
4  job.pdb  ...  MASSSATTPACPSLRHVLIVRHDAAIREGTLLCEAWAAAVGTARTS...
5  job.pdb  ...  YLASDKTTGADVAIKEFFPRDYCGRAPDGSLAMSPGHNAGLVDTLK...
6  job.pdb  ...  LMFADGPLTQPPNLAALVRLAGTTAAVDRAIRLTEQQAGNLITTAA...
7  job.pdb  ...  MQEILPARGLARRRSLAASTGIGETTEMDQDSNQTSPGAVAAGPGS...
8  job.pdb  ...  APAASTAPAAPSGGPASACGPEAQGTTPEGRAERELLGALRARRAE...

[9 rows x 19 columns]
===>Database: alis_pdb100.m8
        0   ...                 20
0  job.pdb  ...  Rattus norvegicus
1  job.pdb  ...  Rattus norvegicus

[2 rows x 21 columns]
```

Results from each database contains 20 columns. Please see [this issue comment{octicon}`link-external;1em;sd-text-info`](https://github.com/steineggerlab/foldseek/issues/25#issuecomment-1193354723) for their explanations.

```{code} python
[
    'job_desc',
    'query','target','pident','alnlen','mismatch','gapopen','qstart','qend','tstart','tend','evalue','bits',
    'qlen','tlen','qaln','taln','tca','tseq',
    'taxid','taxname',
]
```

[^1]: van Kempen, M., Kim, S.S., Tumescheit, C. et al. Fast and accurate protein structure search with Foldseek. Nat Biotechnol 42, 243–246 (2024). https://doi.org/10.1038/s41587-023-01773-0





