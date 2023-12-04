import pytest
from script.main import ShopMysql
from contextlib import nullcontext as not_raise

@pytest.fixture(scope="session")
def db_test():
    CONNECT = {  ##needed to modify
            "host": 'localhost',
            "user": 'root',
            "password": 'password'
    }
    db_test = ShopMysql(**CONNECT)
    yield db_test
    db_test.delete_shop()