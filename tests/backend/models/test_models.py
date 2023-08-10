from unicodedata import category
import pytest

from database.connector import MySQL
from sqlalchemy.orm.session import Session
from src.backend.model.category import Category

from tests.testdata import having_created_category

@pytest.fixture(autouse=True)
def session():
    engine = MySQL.get_engine()
    session = Session(bind=engine)
    session.begin_nested()

    yield session

    session.rollback()
    session.close()

def test_should_create_category(session: Session):
    category = having_created_category()
    
    session.add(category)
    session.flush()

    category_returned: Category = session.get(Category, category.id)

    assert category_returned == category

