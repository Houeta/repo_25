import pytest
from script.main import ShopMysql
from contextlib import nullcontext as not_raise

@pytest.mark.usefixtures()
class TestDBandTable():
    def test_create_database(self, db_test):
        db_test.create_shop('test')
        assert 'db_shop' in str(db_test.show_databases())
        
    @pytest.mark.parametrize(
        'name_table, expectation',
        [('abcd', not_raise()),
         ('ABCD', not_raise()),
         ('123', pytest.raises(ValueError)),
         ('A3D5b', not_raise()),
         ('/45ppo', pytest.raises(ValueError)),
         ('calc.py', pytest.raises(ValueError)),
         ]
        )
    def test_create_table(self, db_test, name_table, expectation):
        with expectation:
            db_test.create_shop(name_table)
            tables = db_test.execute_query('SHOW TABLES')
            assert name_table.lower() in str(tables)
    