import pytest

from uuid import uuid4

from src.backend.api.category_api import CategoryApi
from src.backend.exception import CategoryNotFoundException
from src.backend.model.category import Category


def test_should_create_category():
    category_name = f"TestCategory_{uuid4()}"
    CategoryApi.add(category_name)

    category: Category = CategoryApi.get_by_name(category_name)

    assert category.name == category_name

def test_should_update_category():
    category_name = f"TestCategory_{uuid4()}"
    new_name = f"TestCategory_{uuid4()}"
    
    CategoryApi.add(category_name)
    CategoryApi.update_by_name(category_name, new_name)

    category: Category = CategoryApi.get_by_name(new_name)

    assert category.name == new_name

def test_should_delete_category():
    category_name = f"TestCategory_{uuid4()}"

    CategoryApi.add(category_name)
    CategoryApi.delete_by_name(category_name)

    # assert raises exception
    with pytest.raises(CategoryNotFoundException, match=category_name):
        CategoryApi.get_by_name(category_name)

def test_should_list_categories():
    c1 = f"TestCategory_{uuid4()}"
    c2 = f"TestCategory_{uuid4()}"
    c3 = f"TestCategory_{uuid4()}"

    CategoryApi.add(c1)
    CategoryApi.add(c2)
    CategoryApi.add(c3)

    cats = CategoryApi.list_all()
    c_names = [c.name for c in cats]

    assert set([c1, c2, c3]) <= set(c_names)

