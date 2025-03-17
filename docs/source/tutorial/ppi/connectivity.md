# Connectivity

Protein connectivity reflects how many known biological processes in which a protein is involved if known protein-protein interaction (PPI) databases are used. TMKit is powerful in studying protein connectivity as it not only detect the interaction partners but also confirm how many subunits in a protein complex (where it resides) interact with it.

In tutorials [BioGRID{octicon}`link-external;1em;sd-text-info`](./biogrid.md) and [IntAct{octicon}`link-external;1em;sd-text-info`](./intact.md), we have shown how to access the PPI databases. We can now use the combination of them to study protein connectivity.

TMKit offers an interface, `tmkit.ppi`, to access the database. In this tutorial, we will show how we can use this database in Python, starting from downloading it.



## {octicon}`file-code;1em;sd-text-info` **Example usage**

First, we can define some file paths in `ppi_db_fpns` as shown below, where BioGRID (`BIOGRID-ALL-4.4.212.biogrid`) and IntAct (`interA_B.intact`) can be found.

```{code} python
ppi_db_fpns = {
    'biogrid': 'data/ppi/BIOGRID-ALL-4.4.212.biogrid',
    'intact': 'data/ppi/interA_B.intact',
}
```

Then, using the following codes, you can generate the interaction partners of a given protein `3pux` chain `G` whose UniProt accession code is `P68183`. In the PDB structure, there are other 4 chains, `A`, `B`, `E`, and `F`.

The `tmk.ppi.connectivity` module will first return all interaction partners of protein `3pux` chain `G` in BioGRID and IntAct, and then return how many chains interact with it. We need to specify a dictionary called interacting_partner_idmap where a PDB code matches an UniProt accession code (e.g., `3pux.A`: `P68187`). Of course, protein `3pux` chain `G` itself is needed to do so `3pux.G`: `P68183` in `prot_idmap`.

Their complex structures are needed and the paths to them can be specified using parameters `pdb_rcsb_fp` and `pdb_pdbtm_fp`.

Finally, the results will be saved in `./data/ppi/indepdata.ppidb` using parameter `sv_fpn`. It will be like this below.


```{code} python
import tmkit as tmk

df = tmk.ppi.connectivity(
    prot_name='3pux',
    seq_chain='G',
    prot_idmap={'3pux.G': 'P68183'},
    interacting_partner_idmap={
        '3pux.A': 'P68187',
        '3pux.B': 'P68187',
        '3pux.E': 'P0AEX9',
        '3pux.F': 'P02916',
    },
    pdb_rcsb_fp='./data/pdb/rcsb/',
    pdb_pdbtm_fp='./data/pdb/pdbtm/',
    sv_fpn='./data/ppi/indepdata.ppidb',
    ppi_db_fpns=ppi_db_fpns,
)
print(df)
```



## {octicon}`key;1em;sd-text-info` **Attributes**

| **Attribute**             | **Description**                                                                                                 |
|---------------------------|-----------------------------------------------------------------------------------------------------------------|
| prot_name                 | name of a protein in the prefix of a PDB file name (e.g., `1xqf` in `1xqfA.pdb`)                                |
| seq_chain                 | chain of a protein in the prefix of a PDB file name (e.g., `A` in `1xqfA.pdb`) (biological purpose)             |
| sv_fp                     | path to where you want to save files                                                                            |
| prot_idmap                | a Python dict with key -> value for PDB ID -> UniProt accession code (please see the command below for details) |
| interacting_partner_idmap | a Python dict with key -> value for PDB ID -> UniProt accession code (please see the command below for details) |
| pdb_rcsb_fp               | path where a target PDB file is placed                                                                          |
| pdb_pdbtm_fp              | path where a target PDB file is placed                                                                          |
| ppi_db_fpns               | paths where interaction databases are placed (e.g., `BIOGRID-ALL-4.4.212.biogrid` and `interA_B.intact`)        |




## {octicon}`file-added;1em;sd-text-info` **Output**

Finally, you will see the following output. By searching two interaction databases, all interaction partners of protein `3pux` chain `G` are in the second column below.

```{code} python
 ['3pux.G' 'P02916']
 ['3pux.G' 'P02943']
 ['3pux.G' 'P0A8N3']
 ['3pux.G' 'P0AEX9']
 ['3pux.G' 'P0AGH8']
 ['3pux.G' 'P10907']
 ['3pux.G' 'P19576']
 ['3pux.G' 'P33650']
 ['3pux.G' 'P37019']
 ['3pux.G' 'P42907']
 ['3pux.G' 'P68187']
 ['3pux.G' 'P76084']
 ['3pux.G' 'Q46832']
 ['3pux.G' 'chebi:"CHEBI:15422"']
 ['3pux.G' 'chebi:"CHEBI:47785"']
```

In the same time, the output also tells you that the 4 chains in the complex are all its interacting partners, which you can find via key `num_ip_overlapped_db` in file `./data/ppi/indepdata.ppidb`.


```{code} python
======>basic info:
  prot_name chain pdbtm_chains rcsb_chains source diff   same
0      3pux     G        EFGAB       EFGAB   rcsb       EFGBA
===>UniProt protein id: {'3pux.G': 'P68183'}
===>protein 1 chain 3pux
======>scanning ppi db: biogrid
=========>Record(s) for P68183 found in the left column.
=========>Record(s) for P68183 found in the left column.
======>scanning ppi db: intact
=========>No record(s) for P68183 found in the left column.
=========>Record(s) for P68183 found in the left column.
======>interacting partners from the ppi databases:
[['3pux.G' 'P02916']
 ['3pux.G' 'P02943']
 ['3pux.G' 'P0A8N3']
 ['3pux.G' 'P0AEX9']
 ['3pux.G' 'P0AGH8']
 ['3pux.G' 'P10907']
 ['3pux.G' 'P19576']
 ['3pux.G' 'P33650']
 ['3pux.G' 'P37019']
 ['3pux.G' 'P42907']
 ['3pux.G' 'P68187']
 ['3pux.G' 'P76084']
 ['3pux.G' 'Q46832']
 ['3pux.G' 'chebi:"CHEBI:15422"']
 ['3pux.G' 'chebi:"CHEBI:47785"']]
======>interacting partner idmap: {'3pux.A': 'P68187', '3pux.B': 'P68187', '3pux.E': 'P0AEX9', '3pux.F': 'P02916'}
======>interacting partners from its complex: ['3pux.A', '3pux.B', '3pux.E', '3pux.F']
======>uniprot ids of interacting partners from its complex:['P68187', 'P68187', 'P0AEX9', 'P02916']
======>15 records found from the ppi databases
======>4 interacting partners from its complex
======>4 interacting partners from its complex and found in the ppi databases as well
  prot_name chain pdbtm_chains  ... num_ip ip_chains num_ip_overlapped_db
0      3pux     G        EFGAB  ...    4.0      ABEF                  4.0

[1 rows x 11 columns]
```
