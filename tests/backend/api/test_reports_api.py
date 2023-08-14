from src.backend.api import reports_api
from src.backend.api.category_api import CategoryApi
from src.backend.api.task_api import TaskApi
from src.backend.model.category import Category
from src.backend.model.task import Task
from datetime import date
from src.backend.api.reports_api import ReportsApi


def create_testdata_temp():
    category1: int = CategoryApi.add("TestCategory1")
    category2: int = CategoryApi.add("TestCategory2")
    category3: int = CategoryApi.add("TestCategory3")
    
    task11: int = TaskApi.add("TestTask11", category1)
    task12: int = TaskApi.add("TestTask12", category1)
    task13: int = TaskApi.add("TestTask13", category1)

    TaskApi.add_duration(date(2023, 8, 4), 10, task11)
    TaskApi.add_duration(date(2023, 8, 5), 20, task11)
    TaskApi.add_duration(date(2023, 8, 6), 40, task12)
    TaskApi.add_duration(date(2023, 8, 7), 15, task13)
    TaskApi.add_duration(date(2023, 8, 8), 16, task13)


    task21: int = TaskApi.add("TestTask21", category1)
    task22: int = TaskApi.add("TestTask22", category2)
    task23: int = TaskApi.add("TestTask23", category2)

    TaskApi.add_duration(date(2023, 8, 5), 60, task21)
    TaskApi.add_duration(date(2023, 8, 6), 70, task22)
    TaskApi.add_duration(date(2023, 7, 7), 10, task23)


    task31: int = TaskApi.add("TestTask31", category3)
    task32: int = TaskApi.add("TestTask32", category3)
    task33: int = TaskApi.add("TestTask33", category3)

    TaskApi.add_duration(date(2023, 8, 6), 67, task31)
    TaskApi.add_duration(date(2023, 8, 9), 50, task32)
    TaskApi.add_duration(date(2023, 7, 4), 10, task33)

def test_me():
    names = ["TestTask11", "TestTask12", "TestTask13"]
    tmp = ReportsApi.report_percentage_tasks(date(2023, 8, 1), date(2023, 8, 31), names)
    print(tmp)

test_me()