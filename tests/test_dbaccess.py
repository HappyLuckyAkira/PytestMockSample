import sys

sys.path.append('../')
import src.db_access as db


def test_DBアクセスがある関数をmockで差し替える(mocker):

    mocker.patch("src.db_access.db_access_body", return_value="mock_access")
    assert "mock_access" == db.db_access_func()
# TODO 引数が正しく呼び出されているか
# 回数が正しく呼び出されているか

def test_DBアクセスがある引数ありの関数を正しく呼び出されているか(mocker):
    m = mocker.patch("src.db_access.db_access_body_with_parameters")
    db.db_access_func_with_parameters("abc", 123)
    m.assert_called_with("abc", 123)

def test_DBアクセスがある引数ありの関数を正しい回数呼び出せているか(mocker):
    m = mocker.patch("src.db_access.db_access_body_with_parameters")
    db.db_access_func_with_parameters("def", 456)
    m.assert_called_once_with("def", 456)
