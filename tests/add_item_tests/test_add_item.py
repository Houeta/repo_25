import pytest
from contextlib import nullcontext as not_raise

    
@pytest.mark.usefixtures("table_test")
class TestItems():
    def test_with_correct_argument(self, db_test):
        db_test.add_item("car", 1000)
        assert "'car', 1000" in str(db_test.execute_query('SELECT * FROM shop'))
    
    @pytest.mark.parametrize(
        'item, price, path, expectation',
        [
            ('xiaomi', 1000, '', not_raise()),
            ('','','items_and_price.json', not_raise()),
            ('', '', '', not_raise()),
            ('one', 1.34, '', not_raise()),
            ('','', 'unknowfile.txt', pytest.raises(FileNotFoundError)),
            ('one', '3.45', '', not_raise()),
            ('', 100, '', not_raise()),
            ('book', 356, 'items_and_price.json', not_raise()),
            ('comma', '2,34', '', not_raise()),
            ('comma', '2,3,4', '', pytest.raises(ValueError)),
        ]
    )
    def test_add_item(self, db_test, item, price, path, expectation):
        with expectation:
            db_test.add_item(item, price, path)
        