__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from tmkit.base import PDB


class pdb(PDB.structure):

    def __init__(
            self,
            pdb_fp,
            prot_name,
            seq_chain='',
            file_chain='',
    ):
        super(pdb, self).__init__(pdb_fp, prot_name, seq_chain, file_chain)

    def read(self, ):
        import warnings
        from Bio import BiopythonWarning
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', BiopythonWarning)
            from biopandas.pdb import PandasPdb
            df = PandasPdb().read_pdb(self.pdb_fpn).df
        return df

    def search_foldseek(self, sv_fp: str) -> None:
        """
        Search Foldseek database for a given PDB file.

        Args:
            sv_fp (str): The path to save the output Foldseek file (gzip .m8 format).

        Examples:
            >>> search_foldseek("Q5VSL9.pdb", "Q5VSL9.m8.gz")
        """
        import requests
        from time import sleep
        import sys
        databases = ['afdb50', 'afdb-swissprot', 'afdb-proteome', 'cath50', 'mgnify_esm30', 'pdb100', 'gmgcl_id']
        self.file_chain = '' if self.file_chain == None else self.file_chain
        with open(self.pdb_fp + self.prot_name + self.file_chain + '.pdb', "r") as pdb_file:
            print('===>Searching databases by foldseek...')
            pdb_content = pdb_file.read()
            ticket = requests.post(
                'https://search.foldseek.com/api/ticket',
                files={'q': (pdb_content, pdb_content, 'application/octet-stream')},
                data={
                    'mode': '3diaa',
                    'database[]': databases,
                }
            ).json()
        # poll until the job was successful or failed
        repeat = True
        while repeat:
            status = requests.get('https://search.foldseek.com/api/ticket/' + ticket['id']).json()
            if status['status'] == "ERROR":
                # handle error
                sys.exit(0)
            # wait a short time between poll requests
            sleep(1)
            repeat = status['status'] != "COMPLETE"
        # get all hits for the first query (0)
        result = requests.get('https://search.foldseek.com/api/result/' + ticket['id'] + '/0').json()
        # download blast compatible result archive
        download = requests.get('https://search.foldseek.com/api/result/download/' + ticket['id'], stream=True)
        with open(sv_fp + self.prot_name + self.file_chain + '_foldseek_result.gz', 'wb') as fd:
            for chunk in download.iter_content(chunk_size=128):
                fd.write(chunk)
        from tmkit.util.Kit import ungz
        ungz(
            file_path=sv_fp,
            file_name=self.prot_name + self.file_chain + '_foldseek_result',
            sv_fp=sv_fp,
            new_suffix='.csv',
        )
        print('===>Results have been saved!')
        return result