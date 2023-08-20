from datetime import date

import pytest
from src.backend.api.category_api import CategoryApi
from src.backend.api.task_api import TaskApi
from src.backend.exception import TaskNotFoundException
from src.backend.model.task import Task
from src.backend.model.task_time import TaskTime
from tests.backend.api.data import category_test_name, task_test_name

def test_should_add_task():
    cat_name1 = category_test_name()
    cat_name2 = category_test_name()
    task_name = task_test_name()
    CategoryApi.add(cat_name1)
    CategoryApi.add(cat_name2)

    TaskApi.add(task_name, [cat_name1, cat_name2])

    task: Task = TaskApi.get_by_name(task_name)
    task_cat_names = [c.name for c in task.categories]

    assert task.name == task_name
    assert set(task_cat_names) == set([cat_name1, cat_name2]) 

def test_should_add_time_to_task():
    task_name = task_test_name()    
    TaskApi.add(task_name, [])
    TaskApi.add_duration(date.today(), 60, task_name)

    task: Task = TaskApi.get_by_name(task_name)

    task_time: TaskTime = TaskApi.get_task_time(date.today(), task_name)

    assert task_time.task_id == task.id
    assert task_time.duration == 60

def test_should_add_time_to_task_by_start_and_end_time():
    task_name = task_test_name()    
    TaskApi.add(task_name, [])
    TaskApi.add_duration_by_start_end_time(date.today(), '16:00', '17:00', task_name)

    task: Task = TaskApi.get_by_name(task_name)

    task_time: TaskTime = TaskApi.get_task_time(date.today(), task_name)

    assert task_time.task_id == task.id
    assert task_time.duration == 60

def test_should_update_task_duration():
    task_name = task_test_name()    
    TaskApi.add(task_name, [])
    TaskApi.add_duration(date.today(), 60, task_name)
    TaskApi.update_task_duration(date.today(), task_name, 20)

    task: Task = TaskApi.get_by_name(task_name)

    task_time: TaskTime = TaskApi.get_task_time(date.today(), task_name)

    assert task_time.task_id == task.id
    assert task_time.duration == 80

def test_should_delete_task():
    category_name = category_test_name()  
    task_name = task_test_name()    

    CategoryApi.add(category_name)
    TaskApi.add(task_name, [category_name])

    TaskApi.add_duration(date.today(), 20, task_name)
    TaskApi.add_duration(date(2023, 8, 18), 20, task_name)

    TaskApi.delete_by_name(task_name)

    with pytest.raises(TaskNotFoundException, match=task_name):
        TaskApi.get_by_name(task_name)