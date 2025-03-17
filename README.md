<h1>
    <img src="https://github.com/2003100127/tmkit/blob/main/tmkit/util/tmkit_sign.png?raw=true" width="300" height="100">
    <br>
</h1>

![](https://img.shields.io/pypi/v/tmkit?logo=PyPI)
![Test](https://github.com/2003100127/tmkit/actions/workflows/test.yml/badge.svg)
![](https://img.shields.io/badge/last_released-Jul14._2023-green.svg)
![](https://img.shields.io/badge/tmkit-executable-519dd9.svg)
![Coverage Report](assets/images/coverage.svg)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/2003100127/tmkit/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Anaconda](https://github.com/2003100127/tmkit/actions/workflows/conda.yml/badge.svg)](https://github.com/2003100127/tmkit/actions/workflows/conda.yml)
[![run with docker](https://img.shields.io/badge/run%20with-Docker-0db7ed?logo=docker)](https://www.docker.com/2003100127/tmkit)
[![Downloads](https://pepy.tech/badge/tmkitx)](https://pepy.tech/project/tmkitx)

<!-- ![Build](https://github.com/2003100127/tmkit/actions/workflows/build.yml/badge.svg) -->

###### tags: `bioinformatics`, `protein-protein interfaces`

## Overview

TMKit is a scalable Python programming interface holding a bundle of function modules to allow a variety of transmembrane protein studies.

## Documentation

Website: https://tmkit-guide.herokuapp.com/doc/overview

Source: https://github.com/2003100127/tmkit-guide

We also provided a jupyter notebook (`examples.ipynb`) to demonstrate the usage of TMKit.

## Installation

### Using pip (recommended)

```sh
# create a conda environment
conda create --name tmkit python=3.11

# activate the conda environment
conda activate tmkit

# a stable version 0.0.2 and 0.0.3 (recommended)
pip install tmkit==0.0.3
```

### Using conda

If you want to install TMKit with some optional packages, including hh-suite, pymol, and hmmer, you can select the conda option. You should have [miniconda](https://docs.conda.io/en/latest/miniconda.html) installed first. Please run the following commands to create a new conda environment and install TMKit.

```sh
# create a conda environment
conda create --name tmkit python=3.11

# activate the conda environment
conda activate tmkit

conda install -c 2003100127 -c conda-forge -c bioconda tmkit
```

### Using docker

You can also use docker to run TMKit. You should have [docker](https://docs.docker.com/get-docker/) installed first. Then run the following commands to pull the docker image.

```sh
docker pull jinlongru/tmkit:latest
```


## Citation

Please cite our work if you use TMKit in your research.

## Contact

Please report any questions on [issue](https://github.com/2003100127/tmkit/issues) pages.
