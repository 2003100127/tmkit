# Read

 TMKit can read biological sequences from a Fasta, PDB (both RCSB or PDBTM), or XML (PDBTM) file. To be exact, the tmk.seq module supports it. Due to the fact that residues in FASTA format can be imperfectly aligned with those from the PDB structure as experimentally resolved residues can be discontinuous in its crystal structure for a number of problems in crystallization processes (please refer to this paper), we provide the mapping and conversion from its Fasta IDs to PDB IDs. Please note that in both formats, the sequence is kept the same but we will know how the exact position of each residue in the PDB file corresponds to that in the Fasta file.

 Please make sure that the TMKit example dataset has been downloaded before you walk through the tutorial (please refer to here).
