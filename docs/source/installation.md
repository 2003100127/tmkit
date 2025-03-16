# Installation


## System Requirement

UMIche is advised to be installed within a conda environment, which makes it easier to work on multiple platforms, such as :material-microsoft-windows: Windows (partial), :simple-apple: Mac, and :material-linux: Linux. Owing to the exclusivity of Pysam to the Linux and Mac environments, UMIche does not work with BAM-related analysis in the Windows system.

## PyPI

[umiche homepage on PyPI](https://pypi.org/project/umiche/)

```shell
# create a conda environment
conda create --name umiche python=3.11

# activate the conda environment
conda activate umiche

# the latest version
pip install umiche --upgrade
```

## Conda

[umiche homepage on Anaconda](https://anaconda.org/Jianfeng_Sun/umiche)

```shell
# create a conda environment
conda create --name umiche python=3.11

# activate the conda environment
conda activate umiche

# the latest version
conda install jianfeng_sun::umiche
```


## Docker

[umiche homepage on Docker](https://hub.docker.com/r/2003100127/umiche)

```shell
docker pull 2003100127/umiche
```


## Github

[umiche homepage on Github](https://github.com/2003100127/umiche)

```shell
# create a conda environment
conda create --name umiche python=3.11

# activate the conda environment
conda activate umiche

# create a folder
mkdir project

# go to the folder
cd project

# fetch UMIche repository with the latest version
git clone https://github.com/2003100127/umiche.git

# enter this repository
cd umiche

# do the following command
pip install .
# or
python setup.py install
```
