from datetime import date

from sqlalchemy import and_, func, select
from database.session_wrapper import query

from src.backend.model.category import Category
from src.backend.model.task import Task
from src.backend.model.task_time import TaskTime

from sqlalchemy.orm import Session


class ReportsApi:

    @staticmethod
    @query
    def report_total_time(start: date, end: date, session: Session) -> int:
        stm = select(func.sum(TaskTime.duration)).where(
            and_(
                TaskTime.task_day >= start,
                TaskTime.task_day <= end
                )
            )

        return session.scalar(stm)

    @staticmethod
    @query
    def report_total_time_categories(start: date, end: date, category_ids: list[int], session: Session) -> dict[Category, int]:
        pass

    @staticmethod
    @query
    def report_total_time_tasks(start: date, end: date, task_ids: list[int], session: Session) -> dict[Task, int]:
        pass

    @staticmethod
    @query
    def report_percentage_categories(start: date, end: date, category_ids: list[int], session: Session) -> dict[Category, int]:
        pass

    @staticmethod
    @query
    def report_percentage_tasks(start: date, end: date, task_ids: list[int], session: Session) -> dict[Task, int]:
        pass