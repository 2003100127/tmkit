# Reformat

It is necessary to convert between MSAs in different formats. In HHblits, the Reformat method can support this function.

In this tutorial, we will show how we can convert between MSAs from the [Stockholm{octicon}`link-external;1em;sd-text-info`](https://github.com/soedinglab/hh-suite/wiki#summary-of-command-line-parameters) format to the  [A3M{octicon}`link-external;1em;sd-text-info`](https://github.com/soedinglab/hh-suite/wiki#summary-of-command-line-parameters) format.




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

We need to specify all parameters used for generating the HHblits commands. They mainly include `reformat_fp`, `input_fp`, and `sv_fp`.

Please make sure that you have installed HHblits software. If not, please refer to [this tutorial{octicon}`link-external;1em;sd-text-info`](https://github.com/soedinglab/hh-suite) for how to install HHblits. In our case, an executable of the HHblits program is in `./hhblits/scripts/`.

Please specify the path `sv_fp` that you want to save the reformatted MSAs in [the a3m format{octicon}`link-external;1em;sd-text-info`](https://github.com/soedinglab/hh-suite/wiki#the-same-alignment-in-a3m).

```{code} python
reformat_fp = './hhblits/scripts/'
input_fp ='./data/a3m/'
sv_fp ='./data/a3m/reformat/'
```


Let's then generate the MSAs for these proteins defined above by using the following codes. Of course, there are many more parameters other than the four above and you can change the values of [Attributes{octicon}`link-external;1em;sd-text-info`](#Attributes) below.

```{code} python
import tmkit as tmk

for id in df.index:
    prot_name = df.loc[id, 'prot']
    seq_chain = df.loc[id, 'chain']
    tmk.msa.run_format(
        reformat_fp=reformat_fp,
        max_length_per_name_line=1500,
        aa_per_line=1500,
        input_format='sto',
        output_format='a3m',
        input_fpn=input_fp + prot_name + seq_chain + '.sto',
        output_fpn=sv_fp + prot_name + seq_chain + '.a3m',

        # if you won't do it on clusters, please give False to the parameter send2cloud
        send2cloud=False,
        cloud_cmd="",

        # send2cloud=True,
        # cloud_cmd="qsub -q all.q -N 'jsun'",
    )
```



## {octicon}`key;1em;sd-text-info` **Attributes**

| Attribute                  | Description                                                                      |
|----------------------------|----------------------------------------------------------------------------------|
| `reformat_fp`              | path where an executable of Reformat is placed                                   |
| `input_fp`                 | path where a protein sequence database is placed                                 |
| `sv_fp`                    | path to where you want to save the MSAs in the a3m format                        |
| `input_format`             | input format, e.g., `.sto` for the Stockholm format                              |
| `output_format`            | output format, e.g., `.a3m` for the a3m format                                   |
| `max_length_per_name_line` | maximum number of characers in nameline (default=1000)                           |
| `aa_per_line`              | number of residues per line (for Clustal, FASTA, A2M, A3M formats) (default=100) |

:::{seealso}
We encourage users to check the meaning of all parameters via [this route{octicon}`link-external;1em;sd-text-info`](https://github.com/soedinglab/hh-suite/wiki#summary-of-command-line-parameters). Please see [here{octicon}`link-external;1em;sd-text-info`](../../get_started/feature.md#nomenclature) for better understanding the file-naming system.
:::



## {octicon}`file-added;1em;sd-text-info` **Output**
Finally, you will see the following output showing the generated commands. It will tell Reformat how to search MSAs.

```{code} python
===>The current order: ./hhblits/scripts/reformat.pl -d 1500 -l 1500 sto a3m ./data/a3m/6e3yE.sto ./data/a3m/reformat/6e3yE.a3m
===>The current order: ./hhblits/scripts/reformat.pl -d 1500 -l 1500 sto a3m ./data/a3m/6rfqS.sto ./data/a3m/reformat/6rfqS.a3m
===>The current order: ./hhblits/scripts/reformat.pl -d 1500 -l 1500 sto a3m ./data/a3m/6t0bm.sto ./data/a3m/reformat/6t0bm.a3m
```



