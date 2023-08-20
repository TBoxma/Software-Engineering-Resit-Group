import pytest
from sqlalchemy import select
from database.session_wrapper import query
from src.backend.model.category import Category
from src.backend.model.task import Task

from sqlalchemy.orm import Session
from tests.backend.api.data import prefix_task, prefix_category

@pytest.fixture(autouse=True)
def clean_database():
    yield

    _cleanup()


@query
def _cleanup(session: Session):
    get_test_categories = select(Category).where(Category.name.like(f"{prefix_category}%"))
    get_test_tasks = select(Task).where(Task.name.like(f"{prefix_task}%"))

    test_categories = session.scalars(get_test_categories)
    test_tasks = session.scalars(get_test_tasks)

    for category in test_categories:
        category.tasks.clear()
    
        session.delete(category)
    
    session.commit()
   

    for task in test_tasks:
        task.categories.clear()
        task.durations.clear()

        session.delete(task)
    
    session.commit()