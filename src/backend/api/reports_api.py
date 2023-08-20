from datetime import date
from decimal import Decimal

from sqlalchemy import and_, func, select
from database.session_wrapper import query

from src.backend.model.category import Category
from src.backend.model.task import Task
from src.backend.model.task_time import TaskTime

from sqlalchemy.orm import Session


class ReportsApi:

    """
    A utility class for generating reports related to task time tracking.
    """

    @staticmethod
    @query
    def report_total_time(start: date, end: date, session: Session) -> Decimal:
        """
        Calculates the total time spent on all tasks within a specified time period.

        :param start: The start date of the time period.
        :param end: The end date of the time period.
        :return: The total time spent in minutes.
        """
        stm = select(func.sum(TaskTime.duration)).where(
            and_(
                    TaskTime.task_day >= start,
                    TaskTime.task_day <= end
                )
            )

        return session.scalar(stm)

    @staticmethod
    @query
    def report_total_time_categories(start: date, end: date, category_names: list[str], session: Session) -> dict[Category.name, Decimal]:
        """
        Calculates the total time spent on tasks belonging to specified categories within a specified time period.

        :param start: The start date of the time period.
        :param end: The end date of the time period.
        :param category_names: List of category names to consider.
        :return: A dictionary containing categories as keys and their total times as values.
        """
        stm = select(Category.name, func.sum(TaskTime.duration))\
            .join(Category.tasks)\
            .join(Task.durations)\
            .where(
                and_(
                    Category.name.in_(category_names),
                    TaskTime.task_day >= start,
                    TaskTime.task_day <= end
                )
            )\
            .group_by(Category.name)
        

        total_category_times = session.execute(stm).all()
        result = {}

        for category_name, total_duration in total_category_times:
            result[category_name] = total_duration
        
        return result

    @staticmethod
    @query
    def report_total_time_tasks(start: date, end: date, task_names: list[str], session: Session) -> dict[Task.name, Decimal]:
        """
        Calculates the total time spent on specified tasks within a specified time period.

        :param start: The start date of the time period.
        :param end: The end date of the time period.
        :param task_names: List of task names to consider.
        :return: A dictionary containing task names as keys and their total times as values.
        """
        stm = select(Task.name, func.sum(TaskTime.duration))\
            .join(Task.durations)\
            .where(
                and_(
                    Task.name.in_(task_names),
                    TaskTime.task_day >= start,
                    TaskTime.task_day <= end
                )
            )\
            .group_by(Task.name)
        
        total_task_times = session.execute(stm).all()
        result = {}

        for task_name, total_duration in total_task_times:
            result[task_name] = total_duration
        
        return result

    @staticmethod
    def report_percentage_categories(start: date, end: date, category_names: list[str]) -> dict[Category.name, Decimal]:
        """
        Calculates the percentage of total time spent on each category within a specified time period.

        :param start: The start date of the time period.
        :param end: The end date of the time period.
        :param category_names: List of category names to consider.
        :return: A dictionary containing categories as keys and their percentage of total time as values.
        """
        total_time = ReportsApi.report_total_time(start, end)
        total_by_categories = ReportsApi.report_total_time_categories(start, end, category_names)

        result = {}

        for category in total_by_categories:
            result[category] = ((total_by_categories[category] / total_time) * 100).quantize(Decimal('0.0'))
        
        return result

    @staticmethod
    def report_percentage_tasks(start: date, end: date, task_names: list[str]) -> dict[Task.name, Decimal]:
        """
        Calculates the percentage of total time spent on each task within a specified time period.

        :param start: The start date of the time period.
        :param end: The end date of the time period.
        :param task_names: List of task names to consider.
        :return: A dictionary containing task names as keys and their percentage of total time as values.
        """
        total_time = ReportsApi.report_total_time(start, end)
        total_by_tasks = ReportsApi.report_total_time_tasks(start, end, task_names)

        result = {}

        for category in total_by_tasks:
            result[category] = ((total_by_tasks[category] / total_time) * 100).quantize(Decimal('0.0'))
        
        return result