__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2022"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import sys
sys.path.append('../../../')
from tmkit.util.Reader import reader as greader
from tmkit.util.Writer import writer as gwriter
from tmkit.util.Console import console


class reader(object):

    def __init__(
            self,
            verbose=True,
    ):
        self.greader = greader()
        self.gwriter = gwriter()

        self.console = console()
        self.console.verbose = verbose

    def readall(self, pred_muthtp_fpn):
        self.console.print('======>reading Pred-MutHTP...')
        all = self.greader.generic(pred_muthtp_fpn, df_sep=',')
        all = all.rename(columns={
            0: 'uniprot_id',
            1: 'protein_mutation_site',
            2: 'topology',
            3: 'mutation_type',
            4: 'mut_prob',
        })
        self.console.print('======>Pred-MutHTP features are: '.format())
        for i, e in enumerate(all.columns):
            self.console.print('=========>No.{}: {}'.format(i + 1, e))
        return all

    def readsingle(self, pred_split_muthtp_fpn):
        self.console.print('======>reading split Pred-MutHTP...')
        all = self.greader.generic(pred_split_muthtp_fpn, header=0)
        return all

    def split(self, pred_muthtp_df, sv_fp):
        """

        Parameters
        ----------
        pred_muthtp_df
        sv_fp

        Returns
        -------

        """
        pred_muthtp_df = pred_muthtp_df[[
            'uniprot_id',
            'protein_mutation_site',
            'mut_prob',
        ]]
        # uniprot_ids = pd.unique(muthtp_df['uniprot_id'])
        # pred_muthtp_uniprot_ids = pd.unique(pred_muthtp_df['uniprot_id'])
        pred_muthtp_df_gp = pred_muthtp_df.groupby(['uniprot_id'])
        pred_muthtp_df_gp_keys = pred_muthtp_df_gp.groups.keys()
        self.console.print('======>{} uniprot proteins'.format(len(pred_muthtp_df_gp_keys)))
        for i, prot_id in enumerate(pred_muthtp_df_gp_keys):
            self.console.print('=========>Splitting No.{} protein from Pred-MutHTP'.format(i))
            cc = pred_muthtp_df_gp.get_group(prot_id)
            self.gwriter.generic(
                df=cc, sv_fpn=sv_fp + prot_id + '.predmuthtp',
                header=True,
            )
        return 0


if __name__ == "__main__":
    from tmkit.Path import to

    p = reader()
    from tmkit.db.muthtp.Reader import reader as muthtpreader

    pred_muthtp_df = p.readall(
        pred_muthtp_fpn=to('data/example/mut/pred_varhtp_mut.csv')
    )
    print(pred_muthtp_df)

    muthtp_df = muthtpreader().full(
        muthtp_fpn=to('data/example/mut/final_to_upload_17Mar_2020.txt')
    )

    print(p.split(
        pred_muthtp_df,
        sv_fp=to('data/example/mut/')
    ))