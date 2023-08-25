import sys

sys.path.append('../')
import src.db_access as db


def test_DBアクセスがある関数をmockで差し替える(mocker):

    mocker.patch("src.db_access.db_access_body", return_value="mock_access")
    assert "mock_access" == db.db_access_func()
