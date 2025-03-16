# Feature
TMKit supports researchers to analyze the problems involving transmembrane proteins by offering both commonly-used and bespoke methods that access their sequences, structures, topologies, etc. It has many features from both technical and biological perspectives.


## {octicon}`code-square;1em;sd-text-info` **Language style**
Technically, the library is written by an object-oriented programming (OOP) manner with its specific system for naming parameters. Biologically, we have been focusing on sorting out problems that are infested in a whole analysis process, regardless of whether they are small or big.



## {octicon}`table;1em;sd-text-info` **Nomenclature**
In the TMKit package, {bdg-primary-line}`attributes` are named and written proper to this tool. Specifically, TMKit primarily uses the way of acronyms as its naming system.


Technically, `fp` stands for file path, while `fpn` refers to file path + file name. These abbreviations are commonly used throughout the codebase, often concatenated with an underscore (`_`) to indicate specific file types.

For example:

>`pdb_fp` represents the directory where a PDB file is stored.  
>`pdb_fpn` refers to the full path including the PDB file name.

Similarly, `fasta_fp` and `xml_fp` indicate directories containing **FASTA** and **XML** files, respectively.
Another frequently seen example is `sv_fpn`, where sv stands for save, indicating a file intended for storing results.
This convention helps maintain clarity and consistency when handling different file types within the project.


Biologically, protein-related file names, such as those for multiple sequence alignments (MSA), PDB structures, and FASTA sequences, typically follow a convention where the name consists of two parts: the RCSB structure name and the chain identifier.

For example, the MSA file for the crystal structure of the A3 domain of human von Willebrand factor, chain A, is named `1atzA.aln` in the CCMpred example dataset[^1]. The same naming convention is also used for data files in the PSICOV supplemental dataset[^2].

To maintain clarity, TMKit distinguishes between the protein structure name and the chain name in its file-naming system:

>`msa_fp`: Represents the file path to an MSA file of a protein.  
>`prot_name`: Denotes the name of the protein structure.  
>`file_chain`: Specifies the name of the specific chain within the protein.

In many cases, file_chain may not be applicable, particularly when working with protein files named using UniProt accession codes. However, if an operation in TMKit specifically targets a protein chain, you must specify it using `seq_chain`.

In addition, for a batch operation on multiple proteins, you can pass a Pandas dataframe containing two columns of protein names and chains, respectively onto TMKit. The parameter is prot_df in most of the cases.



## {octicon}`search;1em;sd-text-info` **Focus**
TMKit is designed to simplify the complexity of protein analysis by offering a high level of granularity and automation. For instance, when analyzing a protein, you may need to map its PDB identifier to a UniProt accession code (or vice versa) to retrieve more detailed biological information. However, performing this task in Python can be challenging due to the lack of well-prepared packages. R, on the other hand, provides more established methods for such operations. Even minor technical obstacles like this can slow down coding efficiency, which is why TMKit provides a streamlined solution through the `tmkit.collate` module.

:::{important}
**{octicon}`light-bulb;1em;sd-text-dark`Another challenge** arises with transmembrane proteins, which form oligomeric complexes to perform biological functions. In RCSB PDB, a transmembrane protein structure may contain only non-redundant subunits, whereas certain transmembrane protein databases store the full oligomeric complex (after transformation). The issue is that both versions of the structure share the same file name, and it's unclear how many new chains were added during transformation. TMKit’s `tmkit.collate` module efficiently resolves this by identifying structural differences with minimal effort.
:::

Additionally, TMKit integrates high-speed computing libraries optimized for machine learning applications. Extracting information about pairwise and single residues is crucial, as their relationships are fundamental to various biological studies, including feature extraction for machine learning models. The `tmkit.edge` module in TMKit allows users to perform this task seamlessly, supporting both pre-existing and custom-designed feature extraction schemes.

[^1]: https://github.com/soedinglab/CCMpred/tree/master/example
[^2]: http://bioinf.cs.ucl.ac.uk/downloads/PSICOV/suppdata
