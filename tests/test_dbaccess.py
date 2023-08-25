import sys

sys.path.append('../')
import src.db_access as db


def test_DBアクセスがある関数をmockで差し替える():
    assert "db_access" == db.db_access_func()
