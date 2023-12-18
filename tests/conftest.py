import pytest
from script.main import ShopMysql
from contextlib import nullcontext as not_raise
from os import getenv

@pytest.fixture(scope="session")
def db_test():
    CONNECT = { 
            "host": getenv('MYSQL_HOST'),
            "user": getenv('MYSQL_USER'),
            "password": getenv('MYSQL_PASSWORD')
    }
    db_test = ShopMysql(**CONNECT)
    yield db_test
    db_test.delete_shop()