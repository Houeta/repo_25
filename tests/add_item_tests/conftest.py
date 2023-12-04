import pytest

@pytest.fixture(scope="session")
def table_test(db_test):
    db_test.create_shop('shop')