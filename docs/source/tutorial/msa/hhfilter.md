# HHfilter

Filtering multiple sequence alignments (MSAs) is important as it can technically reduce the workload of computation by removing redundant protein sequences. This can be done by the HHfilter method, a tool in HHblits. TMKit provides the interface to HHfilter.

In this tutorial, we will go through how we can generate the HHfilter commands for filtering MSAs, ensuring that no proteins sharing a certain sequence identity are preserved.



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

We need to specify all parameters used for generating the HHblits commands. They mainly include `hhfilter_fp`, `a3m_path`, and `new_a3m_path`.

Please make sure that you have installed HHblits software. If not, please refer to [this tutorial{octicon}`link-external;1em;sd-text-info`](https://github.com/soedinglab/hh-suite) for how to install HHblits. In our case, an executable of the HHblits program is in `./hhblits/scripts/`.

Please specify the path `new_a3m_path` that you want to save the filtered MSAs in [the a3m format{octicon}`link-external;1em;sd-text-info`](https://github.com/soedinglab/hh-suite/wiki#the-same-alignment-in-a3m).

```{code} python
hhfilter_fp = './hhblits/bin/'
a3m_path = 'data/a3m/'
new_a3m_path = 'data/a3m/filter/'
```

Let's then filter the MSAs in the **a3m** format by using the following codes. Here, we used a maximum **pairwise sequence identity** of **90%** to filter a generated MSA file in **a3m** format, which ensures that no proteins sharing **90%** **sequence identity** are preserved.

```{code} python
import tmkit as tmk

for id in df.index:
    prot_name = df.loc[id, 'prot']
    seq_chain = df.loc[id, 'chain']
    tmk.msa.run_hhfilter(
        hhfilter_fp=hhfilter_fp,
        id=90,
        a3m_fpn=a3m_path + prot_name + seq_chain + '.a3m',
        new_a3m_fpn=new_a3m_path + prot_name + seq_chain + '.a3m',

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
| `hhfilter_fp`              | path where an executable of HHfilter is placed (normally it is in hhblits/bin)   |
| `a3m_path`                 | path where a protein a3m file is placed                                          |
| `new_a3m_path`             | path to where you want to save a filtered MSA in the a3m format                  |
| `id`                       | maximum pairwise sequence identity (def=90)                                      |

:::{seealso}
We encourage users to check the meaning of all parameters via [this route{octicon}`link-external;1em;sd-text-info`](https://github.com/soedinglab/hh-suite/wiki#summary-of-command-line-parameters). Please see [here{octicon}`link-external;1em;sd-text-info`](../../get_started/feature.md#nomenclature) for better understanding the file-naming system.
:::



## {octicon}`file-added;1em;sd-text-info` **Output**
Finally, you will see the following output showing the generated commands. It will tell HHfilter how to filter generated a3m files.

```{code} python
===>The current order: ./hhblits/bin/hhfilter -i data/a3m/6e3yE.a3m -o data/a3m/filter/6e3yE.a3m -id 90
===>The current order: ./hhblits/bin/hhfilter -i data/a3m/6rfqS.a3m -o data/a3m/filter/6rfqS.a3m -id 90
===>The current order: ./hhblits/bin/hhfilter -i data/a3m/6t0bm.a3m -o data/a3m/filter/6t0bm.a3m -id 90
```
