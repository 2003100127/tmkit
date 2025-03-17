# HHblits


[Multiple sequence alignments (MSAs){octicon}`link-external;1em;sd-text-info`](https://en.wikipedia.org/wiki/Multiple_sequence_alignment) can support the evolutionary analysis of a protein and have been widely used in protein research. MSAs were usually generated for a sequence by running a few iterations of HHblits searches against a protein database, such as [UniRef{octicon}`link-external;1em;sd-text-info`](https://www.uniprot.org/help/uniref) ({bdg-primary-line}`version`: [30_2020_06{octicon}`link-external;1em;sd-text-info`](https://uniclust.mmseqs.com/)). The HHblits method is a method that runs at a lightening-fast speed[^1].

In this tutorial, we will go through how we can generate the HHblits commands for further MSA generation.




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

We need to specify all parameters used for generating the HHblits commands. They mainly include `hhblits_fp`, `fasta_fp`, `db_path`, and `sv_fp`.

Please make sure that you have installed HHblits software. If not, please refer to [this tutorial{octicon}`link-external;1em;sd-text-info`](https://github.com/soedinglab/hh-suite) for how to install HHblits. In our case, an executable of the HHblits program is in `./hhblits/bin/`.

Then, you need to prepare a protein sequence database that can be used for HHblits searches. For example, you may use [the UniClust database{octicon}`link-external;1em;sd-text-info`](https://uniclust.mmseqs.com/). After then, you can specify `db_path` as `./uniclust_2020.06/UniRef30_2020_06`.

Please specify the path `sv_fp` that you want to save the MSAs in [the a3m format{octicon}`link-external;1em;sd-text-info`](https://github.com/soedinglab/hh-suite/wiki#the-same-alignment-in-a3m).

```{code} python
fasta_fp = './data/fasta/'
hhblits_fp = './hhblits/bin/'
db_path ='./uniclust_2020.06/UniRef30_2020_06'
sv_fp ='./data/a3m/'
```

Let's then generate the MSAs for these proteins defined above by using the following codes. Of course, there are many more parameters other than the four above. But you can use some recommended options of the additional parameters, like what is suggested by [the CCMPred tool{octicon}`link-external;1em;sd-text-info`](https://github.com/soedinglab/CCMpred/wiki/FAQ#what-is-the-recommended-workflow-of-generating-alignments-for-ccmpred).

```{code} python
import tmkit as tmk

for id in df.index:
    prot_name = df.loc[id, 'prot']
    seq_chain = df.loc[id, 'chain']
    tmk.msa.run_hhblits(
        hhblits_fp=hhblits_fp,
        fasta_fpn=fasta_fp + prot_name + seq_chain + '.fasta',
        sv_fpn=sv_fp + prot_name + seq_chain + '.a3m',
        db_path=db_path,

        # additional parameters
        cpu=2,
        iteration=3,
        maxfilter=100000,
        realign_max=100000,
        all='',
        B=100000,
        Z=100000,
        e=0.001,

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
| `jackhmmer_fp`  | path where an executable of JackHmmer is placed (normally it is in `hmmer3.1b2/bin`) |
| `db_path`     | path where a protein sequence database is placed                                |
| `sv_fp`       | path to where you want to save the MSAs in the a3m format                       |
| `cpu`         | number of CPUs                                                                  |
| `iteration`   | number of iterations by a hidden Markov model                                   |
| `jhm_E`   | In the per-target output, report target sequences with an E-value of <= . The default is 10.0, meaning that on average, about 10 false positives will be reported per query, so you can see the top of the noise and decide for yourself if it’s really noise |
| `incE` | Use an E-value as the per-target inclusion threshold. The default is 0.01, meaning that on average, about 1 false positive would be expected in every 100 searches with different query sequences |
| `noali`         | Omit the alignment section from the main output. This can greatly reduce the output volume |

:::{seealso}
We encourage users to check the meaning of all parameters via [this route{octicon}`link-external;1em;sd-text-info`](https://github.com/soedinglab/hh-suite/wiki#summary-of-command-line-parameters). Please see [here{octicon}`link-external;1em;sd-text-info`](../../get_started/feature.md#nomenclature) for better understanding the file-naming system.
:::



## {octicon}`file-added;1em;sd-text-info` **Output**
Finally, you will see the following output showing the generated commands. It will tell HHblits how to search MSAs.

```{code} python
===>The current order: ./hhblits/bin/hhblits -cpu 2 -i ./data/fasta/6e3yE.fasta -d ./uniclust_2020.06/UniRef30_2020_06 -oa3m ./data/a3m/6e3yE.a3m -n 3 -maxfilt 100000 -realign_max 100000 -B 100000 -Z 100000 -all -e 0.001
===>The current order: ./hhblits/bin/hhblits -cpu 2 -i ./data/fasta/6rfqS.fasta -d ./uniclust_2020.06/UniRef30_2020_06 -oa3m ./data/a3m/6rfqS.a3m -n 3 -maxfilt 100000 -realign_max 100000 -B 100000 -Z 100000 -all -e 0.001
===>The current order: ./hhblits/bin/hhblits -cpu 2 -i ./data/fasta/6t0bm.fasta -d ./uniclust_2020.06/UniRef30_2020_06 -oa3m ./data/a3m/6t0bm.a3m -n 3 -maxfilt 100000 -realign_max 100000 -B 100000 -Z 100000 -all -e 0.001
```



[^1]: Remmert, M., Biegert, A., Hauser, A. et al. HHblits: lightning-fast iterative protein sequence searching by HMM-HMM alignment. Nat Methods 9, 173–175 (2012). https://doi.org/10.1038/nmeth.1818
