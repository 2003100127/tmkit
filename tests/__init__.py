import os

# get absolate path of the current file
dir_testdir = os.path.dirname(os.path.abspath(__file__))
# set working directory to the two levels up
wd = os.path.dirname(dir_testdir)

# Jinlong test data
dir_data = os.path.join(wd, "tests/test_data/")
fin_fasta = os.path.join(dir_data, "1xqfA.fasta")
fin_pdb = os.path.join(dir_data, "1xqfA.pdb")

# Jianfeng's example data
exp_data = os.path.join(wd, "tests/example_data/")
tmp_data = os.path.join(wd, "tmp/")
