from datetime import date, datetime
from database.session_wrapper import query
from sqlalchemy.orm import Session
from sqlalchemy import select
from src.backend.exception import CategoryNotFoundException
from src.backend.model.category import Category

from src.backend.model.task import Task
from src.backend.model.task_time import TaskTime

@query
def add_task(name: str, category_name: str, session: Session):
    """
    Add a new task with the given name and associated with a specific category.

    Args:
        name (str): The name of the task to be added.
        category_name (str): The name of the category to associate the task with.
    
     Raises:
        CategoryNotFoundException: If category with provided name is not found in database
    """
    session.begin()

    category: Category = session.scalar(select(Category).where(Category.name == category_name))

    if not category:
        raise CategoryNotFoundException(f"Category with name '{category_name}' was not found")

    task: Task = Task(name=name)
    task.categories.append(category)

    session.add(task)
    session.commit()    

@query
def add_duration(duration: int, task_id: int, session: Session):
    """
    Add a task duration entry to the database.

    This function creates a TaskTime entry with the specified duration and associates it
    with the given task. The TaskTime entry is added to the database along with the task.

    Args:
        duration (int): The duration of the task in minutes.
        task_id (int): The ID of the task to which the duration will be added.
    """
    session.begin()

    task: Task = session.get(Task, task_id)
    task_time: TaskTime = TaskTime(task_day=date.today(), task_id=task_id, duration=duration)

    task.durations.append(task_time)

    session.add(task)
    session.add(task_time)
    session.commit()

@query
def add_duration_by_start_end_time(start: str, end: str, task_id: int, session: Session):
    """
    Add a task duration to the database based on start and end times.

    This function calculates the duration between the provided start and end times,
    then adds the calculated duration as a TaskTime entry associated with the given task.

    Args:
        start (str): The start time in "hh:mm" format.
        end (str): The end time in "hh:mm" format.
        task_id (int): The ID of the task to which the duration will be added.

    Raises:
        ValueError: If either start or end time is in an invalid format.

    Note:
        The start and end times should be in the "hh:mm" format. This function calculates
        the time difference based on these times and adds the calculated duration as a TaskTime
        entry to the provided task.
    """
    session.begin()

    task: Task = session.get(Task, task_id)

    duration = _calculate_duration(start, end)
    task_time: TaskTime = TaskTime(task_day=date.today(), task_id=task_id, duration=duration)

    task.durations.append(task_time)

    session.add(task)
    session.add(task_time)
    session.commit()

@query
def update_task_duration(day: date, task_id: int, duration: int, session: Session):
    """
    Update the duration of a task for a specific day using the provided session.

    Args:
        day (date): The date for which the task duration should be updated.
        task_id (int): The ID of the task for which the duration should be updated.
        duration (int): The amount by which to increase the task's duration.
    """
    session.begin()

    task_time: TaskTime = session.get(TaskTime, (day, task_id))
    task_time.duration += duration

    session.commit()

def _calculate_duration(start_time: str, end_time: str):
    # Define the format of the time strings
    time_format = "%H:%M"

    start_datetime = datetime.strptime(start_time, time_format)
    end_datetime = datetime.strptime(end_time, time_format)

    # Calculate the time difference in minutes
    time_difference = (end_datetime - start_datetime).total_seconds() / 60

    return int(time_difference)