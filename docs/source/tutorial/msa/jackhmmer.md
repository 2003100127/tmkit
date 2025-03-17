# JackHmmer

Multiple sequence alignments (MSAs) can support the evolutionary analysis of a protein and have been widely used in protein research. MSAs were usually generated for a sequence by running a few iterations of JackHmmer searches[^1] against a protein database, such as [UniRef{octicon}`link-external;1em;sd-text-info`](https://www.uniprot.org/help/uniref).

In this tutorial, we will go through how we can generate the JackHmmer commands for further MSA generation.



## {octicon}`file-code;1em;sd-text-info` **Example usage**
First, let's prepare identifiers of some transmembrane proteins and make them recognisable in Python, like this.

```{code} python
prots = [
    ['6e3y', 'E'],
    ['6rfq', 'S'],
    ['6t0b', 'm'],
]
import pandas as pd
df = pd.DataFrame(prots, columns=['prot', 'chain'])
```

We need to specify all parameters used for generating the JackHmmer commands. They mainly include `jackhmmer_fp`, `fasta_fp`, `db_path`, and `sv_fp`.

Please make sure that you have installed JackHmmer software. If not, please refer to [this tutorial{octicon}`link-external;1em;sd-text-info`](http://hmmer.org/documentation.html) for how to install JackHmmer. In our case, an executable of the JackHmmer program is in `./hmmer3.1b2/bin/`.

Then, you need to prepare a protein sequence database that can be used for JackHmmer searches. For example, you may use [the UniClust database{octicon}`link-external;1em;sd-text-info`](https://uniclust.mmseqs.com/). After then, you can specify `db_path` as `./uniclust_2020.06/UniRef30_2020_06`.

Please specify the path `sv_fp` that you want to save the MSAs in [the a3m format{octicon}`link-external;1em;sd-text-info`](https://github.com/soedinglab/hh-suite/wiki#the-same-alignment-in-a3m).

```{code} python
fasta_fp = './data/fasta/'
jackhmmer_fp = '/home/hmmer3.1b2/bin/'
db_path ='./uniclust_2020.06/UniRef30_2020_06'
sv_fp ='./data/a3m/'
```

Let's then generate the MSAs for these proteins defined above by using the following codes. Of course, there are many more parameters other than the four above.

```{code} python
import tmkit as tmk

for id in df.index:
    prot_name = df.loc[id, 'prot']
    seq_chain = df.loc[id, 'chain']
    tmk.msa.run_jackhmmer(
        jackhmmer_fp=jackhmmer_fp,
        fasta_fpn=fasta_fp + prot_name + seq_chain + '.fasta',
        sv_fpn=sv_fp + prot_name + seq_chain + '.sto',
        db_path=db_path,

        # additional parameters
        cpu=4,
        iteration=3,
        jhm_E=10,
        incE=1e-3,
        noali='',

        # if you won't do it on clusters, please give False to the parameter send2cloud
        send2cloud=False,
        cloud_cmd="",

        # send2cloud=True,
        # cloud_cmd="qsub -q all.q -N 'jsun'",
    )
```



## {octicon}`key;1em;sd-text-info` **Attributes**

| Attribute     | Description                                                                     |
|---------------|---------------------------------------------------------------------------------|
| `fasta_fp`    | path where a protein Fasta file is placed                                       |
| `hhblits_fp`  | path where an executable of HHblits is placed (normally it is in `hhblits/bin`) |
| `db_path`     | path where a protein sequence database is placed                                |
| `sv_fp`       | path to where you want to save the MSAs in the a3m format                       |
| `cpu`         | number of CPUs                                                                  |
| `iteration`   | number of iterations by a hidden Markov model                                   |
| `maxfilter`   | max number of hits allowed to pass 2nd prefilter (default=20000)                |
| `realign_max` | realign maximum hits displayed hits with the max accuracy algorithm             |
| `all`         | do not filter the resulting MSA                                                 |
| `B`           | maximum number of alignments in alignment list (default=500)                    |
| `Z`           | maximum number of lines in summary hit list (default=500)                       |
| `e`           | maximum E-value in summary and alignment list (default=1E+06)                   |

:::{seealso}
We encourage users to check the meaning of all parameters via [this route{octicon}`link-external;1em;sd-text-info`](http://eddylab.org/software/hmmer/Userguide.pdf). Please see [here{octicon}`link-external;1em;sd-text-info`](../../get_started/feature.md#nomenclature) for better understanding the file-naming system.
:::



## {octicon}`file-added;1em;sd-text-info` **Output**
Finally, you will see the following output showing the generated commands. It will tell JackHmmer how to search MSAs.

```{code} python
===>The current order: /home/hmmer3.1b2/bin/jackhmmer --cpu 4 -N 3 -E 10 --incE 0.001 --noali -A ./data/a3m/6e3yE.sto ./data/fasta/6e3yE.fasta ./uniclust_2020.06/UniRef30_2020_06
===>The current order: /home/hmmer3.1b2/bin/jackhmmer --cpu 4 -N 3 -E 10 --incE 0.001 --noali -A ./data/a3m/6rfqS.sto ./data/fasta/6rfqS.fasta ./uniclust_2020.06/UniRef30_2020_06
===>The current order: /home/hmmer3.1b2/bin/jackhmmer --cpu 4 -N 3 -E 10 --incE 0.001 --noali -A ./data/a3m/6t0bm.sto ./data/fasta/6t0bm.fasta ./uniclust_2020.06/UniRef30_2020_06
```















[^1]: Johnson, L.S., Eddy, S.R. & Portugaly, E. Hidden Markov model speed heuristic and iterative HMM search procedure. BMC Bioinformatics 11, 431 (2010). https://doi.org/10.1186/1471-2105-11-431

