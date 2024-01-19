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

```angular2html
 _____ __  __ _  ___ _
|_   _|  \/  | |/ (_) |_
  | | | |\/| | ' /| | __|
  | | | |  | | . \| | |_
  |_| |_|  |_|_|\_\_|\__|
```

TMKit is a scalable Python programming interface holding a bundle of function modules to allow a variety of transmembrane protein studies.

## Documentation

Website: https://tmkit-guide.herokuapp.com/doc/overview

Source: https://github.com/2003100127/tmkit-guide

We also provided a jupyter notebook (`examples.ipynb`) to demonstrate the usage of TMKit.

## Installation

### Using pip (recommended)

```sh
# create a conda environment
conda create --name tmkit python=3.10

# activate the conda environment
conda activate tmkit

# a stable version 0.0.5 (recommended)
pip install tmkit==0.0.5
```

### Using conda

If you want to install TMKit with some optional packages, including hh-suite, pymol, and hmmer, you can select the conda option. You should have [miniconda](https://docs.conda.io/en/latest/miniconda.html) installed first. Please run the following commands to create a new conda environment and install TMKit.

```sh
# create a conda environment
conda create --name tmkit python=3.10

# activate the conda environment
conda activate tmkit

conda install -c 2003100127 -c conda-forge -c bioconda tmkit
```

### Using docker

You can also use docker to run TMKit. You should have [docker](https://docs.docker.com/get-docker/) installed first. Then run the following commands to pull the docker image.

```sh
docker pull 2003100127/tmkit:latest
```

## For developers

If you want to contribute to TMKit, be sure to review the [contribution guidelines](CONTRIBUTING.md). Please fork the repository and create a new branch for development. We provided a [docker image](https://hub.docker.com/r/2003100127/tmkit-dev/tags) and a `Makefile` to help you get started quickly. After cloned the repo and connected to the docker container, you can run the following commands to get started.

```sh
# install poetry
make poetry-download

# create a virtual environment
make create-venv

# install dependencies
make install

# install pre-commit hooks
make pre-commit-install

# happy coding :)
# ...

# after coding, run the following commands to check your code before making a pull request
make test
```

The development environment is managed by [Poetry](https://python-poetry.org/). [`pre-commit`](https://github.com/pre-commit/pre-commit) is used to manage the git hooks, which include code formatting, linting, security check, etc, and is configured in the `.pre-commit-config.yaml` file. Using `pre-commit` is highly recommended to ensure the code quality.

### Makefile usage

[`Makefile`](https://github.com/2003100127/tmkit/blob/main/Makefile) contains a lot of functions for faster development.

<details>
<summary>1. Download and remove Poetry</summary>
<p>

To download and install Poetry run:

```bash
make poetry-download
```

To uninstall

```bash
make poetry-remove
```

</p>
</details>

<details>
<summary>2. Install all dependencies and pre-commit hooks</summary>
<p>

Install requirements:

```bash
make install
```

Pre-commit hooks coulb be installed after `git init` via

```bash
make pre-commit-install
```

</p>
</details>

<details>
<summary>3. Codestyle</summary>
<p>

Automatic formatting uses `pyupgrade`, `isort` and `black`.

```bash
make codestyle

# or use synonym
make formatting
```

Codestyle checks only, without rewriting files:

```bash
make check-codestyle
```

> Note: `check-codestyle` uses `isort`, `black` and `darglint` library

Update all dev libraries to the latest version using one comand

```bash
make update-dev-deps
```

</p>
</details>

<details>
<summary>4. Code security</summary>
<p>

```bash
make check-safety
```

This command launches `Poetry` integrity checks as well as identifies security issues with `Safety` and `Bandit`.

```bash
make check-safety
```

</p>
</details>

<details>
<summary>5. Type checks</summary>
<p>

Run `mypy` static type checker

```bash
make mypy
```

</p>
</details>

<details>
<summary>6. Tests with coverage badges</summary>
<p>

Run `pytest`

```bash
make test
```

</p>
</details>

<details>
<summary>7. All linters</summary>
<p>

Of course there is a command to ~~rule~~ run all linters in one:

```bash
make lint
```

the same as:

```bash
make test && make check-codestyle && make mypy && make check-safety
```

</p>
</details>

<details>
<summary>8. Docker</summary>
<p>

```bash
make docker-build
```

which is equivalent to:

```bash
make docker-build VERSION=latest
```

Remove docker image with

```bash
make docker-remove
```

More information [about docker](https://github.com/2003100127/tmkit/tree/master/docker).

</p>
</details>

<details>
<summary>9. Cleanup</summary>
<p>
Delete pycache files

```bash
make pycache-remove
```

Remove package build

```bash
make build-remove
```

Delete .DS_STORE files

```bash
make dsstore-remove
```

Remove .mypycache

```bash
make mypycache-remove
```

Or to remove all above run:

```bash
make cleanup
```

</p>
</details>

## Citation

Please cite our work if you use TMKit in your research.

## Contact

Please report any questions on [issue](https://github.com/2003100127/tmkit/issues) pages.
