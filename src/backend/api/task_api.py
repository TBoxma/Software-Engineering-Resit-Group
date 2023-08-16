from datetime import date, datetime
from typing import Sequence
from database.session_wrapper import query
from sqlalchemy.orm import Session
from sqlalchemy import select
from src.backend.api.base_api import BaseModelApi
from src.backend.model.category import Category

from src.backend.model.task import Task
from src.backend.model.task_time import TaskTime

class TaskApi(BaseModelApi):
    """
    API class for performing operations related to Task model.
    Inherits from BaseModelApi for common CRUD operations.
    """

    def __init__(self) -> None:
        """
        Initializes the TaskApi instance with the Task model.
        """
        super().__init__(Task)

    @classmethod
    @query
    def add(cls, name: str, category_names: list[str], session: Session) -> int:
        """
        Add a new task with the given name and associated with a specific category.

        Args:
            name (str): The name of the task to be added.
            category_name (str): The name of the category to associate the task with.
        """
        stm = select(Category).where(Category.name.in_(category_names))
        categories: list[Category] = session.scalars(stm).all()

        task: Task = Task(name=name)
        task.categories.extend(categories)

        session.add(task)
        session.commit()

        return task.id  

    @classmethod
    @query
    def add_duration(cls, day: date, duration: int, task_id: int, session: Session):
        """
        Add a task duration entry to the database.

        This function creates a TaskTime entry with the specified duration and associates it
        with the given task. The TaskTime entry is added to the database along with the task.

        Args:
            duration (int): The duration of the task in minutes.
            task_id (int): The ID of the task to which the duration will be added.
        """

        task: Task = session.get(Task, task_id)
        task_time: TaskTime = TaskTime(task_day=day, task_id=task_id, duration=duration)

        task.durations.append(task_time)

        session.add(task)
        session.add(task_time)
        session.commit()

    @classmethod
    @query
    def add_duration_by_start_end_time(cls, start: str, end: str, task_id: int, session: Session):
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

        task: Task = session.get(Task, task_id)

        duration = cls._calculate_duration(start, end)
        task_time: TaskTime = TaskTime(task_day=date.today(), task_id=task_id, duration=duration)

        task.durations.append(task_time)

        session.add(task)
        session.add(task_time)
        session.commit()

    @classmethod
    @query
    def update_task_duration(cls, day: date, task_id: int, duration: int, session: Session):
        """
        Update the duration of a task for a specific day using the provided session.

        Args:
            day (date): The date for which the task duration should be updated.
            task_id (int): The ID of the task for which the duration should be updated.
            duration (int): The amount by which to increase the task's duration.
        """

        task_time: TaskTime = session.get(TaskTime, (day, task_id))
        task_time.duration += duration

        session.commit()

    @staticmethod
    def _calculate_duration(start_time: str, end_time: str):
        time_format = "%H:%M"

        start_datetime = datetime.strptime(start_time, time_format)
        end_datetime = datetime.strptime(end_time, time_format)

        time_difference = (end_datetime - start_datetime).total_seconds() / 60

        return int(time_difference)