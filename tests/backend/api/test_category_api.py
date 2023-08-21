import pytest

from src.backend.api.category_api import CategoryApi
from src.backend.exception import CategoryNotFoundException
from src.backend.model.category import Category
from tests.backend.api.data import category_test_name


def test_should_create_category():
    category_name = category_test_name()
    CategoryApi.add(category_name)

    category: Category = CategoryApi.get_by_name(category_name)

    assert category.name == category_name

def test_should_update_category():
    category_name = category_test_name()
    new_name = category_test_name()
    
    CategoryApi.add(category_name)
    CategoryApi.update_by_name(category_name, new_name)

    category: Category = CategoryApi.get_by_name(new_name)

    assert category.name == new_name

def test_should_delete_category():
    category_name = category_test_name()

    CategoryApi.add(category_name)
    CategoryApi.delete_by_name(category_name)

    # assert raises exception
    with pytest.raises(CategoryNotFoundException, match=category_name):
        CategoryApi.get_by_name(category_name)

def test_should_list_categories():
    c1 = category_test_name()
    c2 = category_test_name()
    c3 = category_test_name()

    CategoryApi.add(c1)
    CategoryApi.add(c2)
    CategoryApi.add(c3)

    cats = CategoryApi.list_all()
    c_names = [c.name for c in cats]

    assert set([c1, c2, c3]) <= set(c_names)

