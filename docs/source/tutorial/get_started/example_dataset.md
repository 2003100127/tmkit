# Dataset

To get started with TMKit, an example dataset is required to be downloaded beforehand. We release this dataset on Zenodo. After downloading this dataset and placing it properly, you should be walked through all cases presented in this tutorial.


## {octicon}`download;1em;sd-text-info` **Download datasets**
If you would like to save the dataset in the current folder, please specify `sv_fpn` as `./data.zip`. As the dataset URL is fixed, you can always use the code to get it.

```{code} python
import tmkit as tmk

# if you use tmkit version 0.0.3
tmk.fetch.tmkit_data(
    sv_fpn='./data.zip'
)

# if you still use tmkit version 0.0.2
tmk.fetch.tmkit_data(
    url='https://zenodo.org/records/10530158/files/TMKit%20data.zip?download=1',
    sv_fpn='./data.zip'
)
```

Then, unzip it as follows to the current folder `./`.

```{code} python
tmk.fetch.unzip(
    in_fpn='./data.zip',
    out_fp='./'
)
```


## {octicon}`file-directory-symlink;1em;sd-text-info` **Folder content**
It has the following folders, ie., `cath`, `contact`, `external_lib`, `fasta`, `isite`, `lips`, `map`, `msa`, `mutation`, `pdb`, `ppi`, `qc`, `rrc`, `topo`, `vs`, `xml`, which mainly contains **Fasta**, **PDB**, **XML** files, etc.
