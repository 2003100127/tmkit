__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2022"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from tmkit.db.muthtp.Reader import reader as muthtpreader
from tmkit.db.predmuthtp.Reader import reader as predmuthtpreader


def read_muthtp_db(
        muthtp_fpn
):
    """

    Parameters
    ----------
    muthtp_fpn

    Returns
    -------

    """
    return muthtpreader().full(
        muthtp_fpn
    )


def read_predmuthtp_db(
        pred_muthtp_fpn
):
    """

    Parameters
    ----------
    pred_muthtp_fpn

    Returns
    -------

    """
    return predmuthtpreader().readall(
        pred_muthtp_fpn
    )


def split_predmuthtp(
        pred_muthtp_df,
        sv_fp,
):
    """

    Parameters
    ----------
    pred_muthtp_df
    sv_fp

    Returns
    -------

    """
    return predmuthtpreader().split(
        pred_muthtp_df=pred_muthtp_df,
        sv_fp=sv_fp
    )


def read_split_predmuthtp(
        pred_split_muthtp_fpn,
):
    """

    Parameters
    ----------
    pred_split_muthtp_fpn

    Returns
    -------

    """
    return predmuthtpreader().readsingle(
        pred_split_muthtp_fpn=pred_split_muthtp_fpn,
    )


if __name__ == "__main__":
    from tmkit.Path import to

    # print(read_muthtp_db(
    #     muthtp_fpn=to('data/example/mut/final_to_upload_17Mar_2020.txt')
    # ))

    # pred_muthtp_df = read_predmuthtp_db(
    #     pred_muthtp_fpn=to('data/example/mut/pred_varhtp_mut.csv')
    # )
    # print(pred_muthtp_df)

    # split_predmuthtp(
    #     pred_muthtp_df=pred_muthtp_df,
    #     sv_fp=to('data/example/mut/')
    # )

    pred_muthtp_df = read_split_predmuthtp(
        pred_split_muthtp_fpn=to('data/example/mut/W5XKT8.predmuthtp')
    )
    print(pred_muthtp_df)