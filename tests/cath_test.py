import tmkit as tmk


def test_cath_summary_by_id():
    res = tmk.cath.summary_by_id(id="1cukA01")
    assert (
        res["domain"]
        == "http://www.cathdb.info/version/v4_2_0/api/rest/domain_summary/1cukA01"
    )
