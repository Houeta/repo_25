import pytest
from contextlib import nullcontext as not_raise

@pytest.mark.usefixtures('delete_test')
class TestDeleteItems():
    def test_if_delete_item_by_id(self, db_test):
        with pytest.raises(FileExistsError):
            db_test.delete_item(10)
            db_test.delete_item(0)
            db_test.delete_item(47)
            
    def test_delete_item_with_none_argument(self, db_test):
        db_test.delete_item()
            
    @pytest.mark.parametrize(
        "item",
        [
            ('Iron Flame'),
            ("Just Because"),
            ('the woman in me'),
            ("ENOUGH"),
            ('the Mysteries'),
            ("cOmmA")
        ]
    )
    def test_if_works_delete_item_with_different_case(self, db_test, item):
        db_test.delete_item(item)

    @pytest.mark.parametrize(
        "item",
        [
            (':Enough'),
            ('I``ron Flame'),
            ('Iron Flame/'),
            ("0ne"),
            ("Iron Flame."),
        ]
    )
    def test_if_works_delete_item_with_different_case(self, db_test, item, expectation=pytest.raises(FileExistsError)):
        with expectation:
            db_test.delete_item(item)