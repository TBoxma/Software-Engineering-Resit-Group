from datetime import date, datetime
from database.session_wrapper import query
from sqlalchemy.orm import Session
from sqlalchemy import and_, select
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
    def add(cls, name: str, category_names: list[str], session: Session):
        """
        Add a new task with the given name and associated with a specific category.

        :param name: The name of the task to be added.
        :param category_name: The name of the category to associate the task with.
        """
        stm = select(Category).where(Category.name.in_(category_names))
        categories: list[Category] = session.scalars(stm).all()

        task: Task = Task(name=name)
        task.categories.extend(categories)

        session.add(task)
        session.commit()

    @classmethod
    @query
    def add_duration(cls, day: date, duration: int, task_name: str, session: Session):
        """
        Add a task duration entry to the database.

        This function creates a TaskTime entry with the specified duration and associates it
        with the given task. The TaskTime entry is added to the database along with the task.

        :param duration: The duration of the task in minutes.
        :param task_id: The ID of the task to which the duration will be added.
        """

        task: Task = cls()._get_model_by_name(task_name, session)
        task_time: TaskTime = TaskTime(task_day=day, task_id=task.id, duration=duration)

        task.durations.append(task_time)

        session.add(task)
        session.add(task_time)
        session.commit()

    @classmethod
    @query
    def add_duration_by_start_end_time(cls, day: date, start: str, end: str, task_name: str, session: Session):
        """
        Add a task duration to the database based on start and end times.

        This function calculates the duration between the provided start and end times,
        then adds the calculated duration as a TaskTime entry associated with the given task.

        :param start: The start time in "hh:mm" format.
        :param end: The end time in "hh:mm" format.
        :param task_id: The ID of the task to which the duration will be added.
        :raises ValueError: If either start or end time is in an invalid format.

        Note:
            The start and end times should be in the "hh:mm" format. This function calculates
            the time difference based on these times and adds the calculated duration as a TaskTime
            entry to the provided task.
        """
        duration = cls._calculate_duration(start, end)

        task: Task = cls()._get_model_by_name(task_name, session)
        task_time: TaskTime = TaskTime(task_day=day, task_id=task.id, duration=duration)

        task.durations.append(task_time)

        session.add(task)
        session.add(task_time)
        session.commit()

    @classmethod
    @query
    def get_task_time(cls, day: date, task_name: str, session: Session) -> TaskTime:
        """
        Returns task time entry by specific date and task name

        :param day: date of interest
        :param task_name: name of the task for which to return time entry
        :returns: TaskTime object with the duration of specified task at specifed day
        """
        task: Task = cls()._get_model_by_name(task_name, session)

        task_time: TaskTime = session.scalar(select(TaskTime)
                                             .where(and_(TaskTime.task_id == task.id, TaskTime.task_day == day)))
        return task_time

    @classmethod
    @query
    def list_all_task_times(cls, task_name: str, session: Session) -> list[TaskTime]:
        """
        Returns all task time entries for specific task

        :param task_name: name of the task for which to display all time entries
        :returns: a list of TaskTime objects
        """
        task: Task = cls()._get_model_by_name(task_name, session)

        task_times: list[TaskTime] = session.scalars(select(TaskTime)
                                             .where(TaskTime.task_id == task.id))
        return task_times        

    @classmethod
    @query
    def update_task_duration(cls, day: date, task_name: str, duration: int, session: Session):
        """
        Update the duration of a task for a specific day.

        :param day: The date for which the task duration should be updated.
        :param task_id: The ID of the task for which the duration should be updated.
        :param duration: The amount by which to increase the task's duration.
        """
        task: Task = cls()._get_model_by_name(task_name, session)
        task_time: TaskTime = session.get(TaskTime, (day, task.id))
        task_time.duration += duration

        session.commit()

    @staticmethod
    def _calculate_duration(start_time: str, end_time: str) -> int:
        """
        Private function which calculates difference between 2 points in time
        """
        time_format = "%H:%M"

        start_datetime = datetime.strptime(start_time, time_format)
        end_datetime = datetime.strptime(end_time, time_format)

        time_difference = (end_datetime - start_datetime).total_seconds() / 60

        return int(time_difference)
    
    @classmethod
    def exists(cls, name: str) -> bool:
        all_tasks = cls().list_all()
        names = [c.name for c in all_tasks]

        return name in names