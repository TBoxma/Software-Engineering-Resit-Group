import pytest

from datetime import date
from sqlalchemy.exc import IntegrityError

from database.connector import SQLite
from sqlalchemy.orm.session import Session
from src.backend.model.category import Category
from src.backend.model.task import Task
from src.backend.model.task_category import TaskCategory
from src.backend.model.task_time import TaskTime

def sample_category(name: str = None) -> Category:
    return Category(name="Test Category") if not name else Category(name=name)

def sample_task(name: str = None) -> Task:
    return Task(name="Test task") if not name else Task(name=name)

@pytest.fixture
def session():
    engine = SQLite.get_engine()
    session = Session(bind=engine)
    session.begin_nested()

    yield session

    session.rollback()
    session.close()

def test_should_create_category(session: Session):
    category = sample_category()
    
    session.add(category)
    session.flush()

    category_returned: Category = session.get(Category, category.id)

    assert category_returned == category

def test_should_create_task(session: Session):
   task = sample_task()

   session.add(task)
   session.flush()

   task_returned: Task = session.get(Task, task.id)
   
   assert task_returned == task

def test_should_create_task_correct_category(session: Session):
   
   category = sample_category()
   task = sample_task()

   task.categories.append(category)

   session.add(category)
   session.add(task)
   session.flush()

   task_returned: Task = session.get(Task, task.id)
   category_name = task_returned.categories[0].name
   
   assert category_name == "Test Category"

def test_should_create_task_multiple_categories(session: Session):
    category1 = sample_category(name="First category")
    category2 = sample_category(name="Second category")
    task = sample_task()

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

def test_should_correctly_add_durations_to_task(session: Session):
    task = sample_task()
    duration1 = TaskTime(task_day=date.today(), task_id=task.id, duration=60)
    duration2 = TaskTime(task_day=date(2023, 8, 10), task_id=task.id, duration=60)

    task.durations.append(duration1)
    task.durations.append(duration2)

    session.add(task)
    session.add(duration1)
    session.add(duration2)
    session.flush()

    task_time: TaskTime = session.get(TaskTime, (date.today(), task.id))
    task_time_another: TaskTime = session.get(TaskTime, (date(2023, 8, 10), task.id))

    assert task_time != None and task_time_another != None

    task_with_duration = session.get(Task, task.id)

    task_id_equals = task_with_duration.durations[0].task_id == task.id
    date_is_today = task_with_duration.durations[0].task_day == date.today()

    assert duration1.duration == task_time.duration == 60
    assert task_id_equals and date_is_today

def test_should_fail_to_add_duration_same_day_same_task(session: Session):
    with pytest.raises(IntegrityError, match='UNIQUE constraint failed'):
        task = sample_task()
        duration1 = TaskTime(task_day=date.today(), task_id=task.id, duration=60)
        duration2 = TaskTime(task_day=date.today(), task_id=task.id, duration=10)

        task.durations.append(duration1)
        task.durations.append(duration2)

        session.add(task)
        session.add(duration1)
        session.add(duration2)
        session.flush()