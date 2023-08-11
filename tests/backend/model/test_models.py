from typing import List
from unicodedata import category
import pytest

from database.connector import MySQL
from sqlalchemy.orm.session import Session
from src.backend.model import task_category
from src.backend.model.category import Category
from src.backend.model.task import Task
from src.backend.model.task_category import TaskCategory

from tests.testdata import having_created_category, having_created_task

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

def test_should_create_task(session: Session):
   task = having_created_task()

   session.add(task)
   session.flush()

   task_returned: Task = session.get(Task, task.id)
   
   assert task_returned == task

def test_should_create_task_correct_category(session: Session):
   
   category = having_created_category()
   task = having_created_task()

   task.categories.append(category)

   session.add(category)
   session.add(task)
   session.flush()

   task_returned: Task = session.get(Task, task.id)
   category_name = task_returned.categories[0].name
   
   assert category_name == "Test Category"

def test_should_create_task_multiple_categories(session: Session):
    category1 = having_created_category(name="First category")
    category2 = having_created_category(name="Second category")
    task = having_created_task()

    task.categories.append(category1)
    task.categories.append(category2)

    session.add(category1)
    session.add(category2)
    session.add(task)
    session.flush()

    task_category1: TaskCategory = session.get(TaskCategory, (category1.id, task.id))
    task_category2: TaskCategory = session.get(TaskCategory, (category2.id, task.id))

    task_by_id: Task = session.get(Task, task_category1.task_id)

    assert task_by_id == task

    assert task_category1.task_id == task.id
    assert task_category1.category_id == category1.id
   
    assert task_category2.task_id == task.id
    assert task_category2.category_id == category2.id
