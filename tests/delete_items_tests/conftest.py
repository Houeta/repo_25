import pytest

@pytest.fixture(scope="session")
def delete_test(db_test):
    db_test.create_shop('shop')
    db_test.add_item(path='items_and_price.json')