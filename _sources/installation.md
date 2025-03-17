# Installation

To benefit a broad audience, we made TMKit available from multiple sources, which can be installed via **PyPI**, **Conda**, **GitHub**, and **Docker**. Among them, we highly recommend installing it using PyPI, considering the time and the number of steps that users will spend on making it available to use.

In principle, TMKit can be built on any version of Python. However, considering that NumPy and Pandas that are dependent libraries of TMKit have experienced a significant revision in their respective latest versions and there are some potential conflicts between Python versions and themselves, we suggest you to install TMKit on Python versions of above {bdg-primary-line}`v3.8`, especially, Python {bdg-primary-line}`v3.11`. We have tested TMKit running on Python {bdg-primary-line}`v3.10` and {bdg-primary-line}`v3.11`.



## PyPI

We highly recommend installing TMKit in a conda environment with a specific Python version built. This allows you to manage other packages via both PyPI and Conda after then. To achieve this purpose, it needs a couple of procedures below. We recommend using TMKit version {bdg-warning-line}`0.0.3`.

```{code} python
# create a conda environment
conda create --name tmkit python=3.11.4
# You can also simply omit ".4" to make it like "python=3.11", which will allow conda to choose the most recent version for you.
# We do not really suggest using version Python versions. If you do stick to a Python version, please make sure
# it is above 3.8.
# the tmkit name in "--name tmkit" can be altered to your preferred environment name.

# activate the conda environment
conda activate tmkit

# do the following command, stable versions: 0.0.2 and 0.0.3 (recommended)
pip install tmkit==0.0.3
```



## Github
The latest version of TMKit may differ to it in PyPI and it is based at GitHub. Similarly, we highly recommend installing TMKit in a conda environment with a specific Python version built. You are able to use the latest version after doing the following procedures.

```{code} python
# create a conda environment
conda create --name tmkit python=3.11.4

# activate the conda environment
conda activate tmkit

# create a folder
mkdir project

# go to the folder
cd project

# fetch TMKit repository with the latest version
git clone https://github.com/2003100127/tmkit.git

# enter this repository
cd tmkit

# do the following command
pip install .
# or
python setup.py install
```



## Conda
If you want to install TMKit with some optional packages, including [hh-suite{octicon}`link-external;1em;sd-text-info`](https://anaconda.org/bioconda/hhsuite), [pymol{octicon}`link-external;1em;sd-text-info`](https://anaconda.org/conda-forge/pymol-open-source), and [hmmer{octicon}`link-external;1em;sd-text-info`](https://anaconda.org/bioconda/hmmer), you can select the conda option. You should have [miniconda{octicon}`link-external;1em;sd-text-info`](https://www.anaconda.com/docs/getting-started/miniconda/install) installed first. Please run the following commands to create a new conda environment and install TMKit.

```{code} python
# create a conda environment
conda create --name tmkit python=3.11

# activate the conda environment
conda activate tmkit

conda install -c 2003100127 -c conda-forge -c bioconda tmkit
```



## Docker
To ensure a successful use of TMKit in its stable version, we make it accessible in a Docker image. Once being correctly configured, the Docker image will allow you to use TMKit without installation.

You can first choose which type of operating system (OS) you would like to install Docker software. Please refer to [here{octicon}`link-external;1em;sd-text-info`](https://docs.docker.com/engine/install). For example, if your computational work is based on a Windows OS, you can choose to install a Desktop version of Docker. Please refer to [here{octicon}`link-external;1em;sd-text-info`](https://docs.docker.com/desktop/install/windows-install).

If you have your Docker software installed on your OS, you can open a terminal to test whether the installation is successfully accomplished by typing `docker info`, where you should not be notified by something like "command is not found". Please take a look at [here{octicon}`link-external;1em;sd-text-info`](https://stackoverflow.com/questions/57108228/how-to-check-if-docker-is-running-on-windows).

After successful installation of Docker, you can put the following command in the terminal. You are prompted by a link. You can include your integrated development environment ([IDE{octicon}`link-external;1em;sd-text-info`](https://en.wikipedia.org/wiki/Integrated_development_environment)), such as [Visual Studio Code{octicon}`link-external;1em;sd-text-info`](https://code.visualstudio.com/). You can follow [the official instruction{octicon}`link-external;1em;sd-text-info`](https://learn.microsoft.com/en-us/visualstudio/docker/tutorials/docker-tutorial) on their cooperation. Then, you can explore with TMKit.

```{code} python
docker pull 2003100127/tmkit
```
