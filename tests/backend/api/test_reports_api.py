from datetime import date
from decimal import Decimal
from src.backend.api.category_api import CategoryApi
from src.backend.api.reports_api import ReportsApi

from src.backend.api.task_api import TaskApi
from tests.backend.api.data import category_test_name, task_test_name

def test_should_calculate_total_time():
    category_name = category_test_name()
    task_name1 = task_test_name()
    task_name2 = task_test_name()
    task_name3 = task_test_name()

    CategoryApi.add(category_name)

    TaskApi.add(task_name1, [category_name])
    TaskApi.add(task_name2, [category_name])
    TaskApi.add(task_name3, [category_name])

    TaskApi.add_duration(date(2023, 8, 18), 60, task_name1)
    TaskApi.add_duration(date(2023, 8, 18), 50, task_name2)
    TaskApi.add_duration(date(2023, 8, 18), 70, task_name3)

    TaskApi.add_duration(date(2023, 8, 12), 60, task_name1)
    TaskApi.add_duration(date(2023, 8, 13), 50, task_name2)
    TaskApi.add_duration(date(2023, 8, 14), 70, task_name3)

    total_time_1day = ReportsApi.report_total_time(date(2023, 8, 18), date(2023, 8, 18))
    total_time_range = ReportsApi.report_total_time(date(2023, 8, 11), date(2023, 8, 13))
    total_time_none = ReportsApi.report_total_time(date(3023, 1, 1), date(3023, 1, 1))

    assert total_time_1day == 180
    assert total_time_range == 110
    assert total_time_none == None

def test_should_report_total_time_by_categories():
    cn1 = category_test_name()
    cn2 = category_test_name()
    cn3 = category_test_name()

    tn1 = task_test_name()
    tn2 = task_test_name()

    CategoryApi.add(cn1)
    CategoryApi.add(cn2)
    CategoryApi.add(cn3)

    TaskApi.add(tn1, [cn1, cn2, cn3])
    TaskApi.add(tn2, [cn1])
    
    TaskApi.add_duration(date(2023, 8, 12), 60, tn1)
    TaskApi.add_duration(date(2023, 8, 12), 60, tn2)
    TaskApi.add_duration(date(2023, 8, 13), 60, tn2)
    TaskApi.add_duration(date(2023, 8, 14), 60, tn1)

    time_14 = ReportsApi.report_total_time_categories(date(2023, 8, 14), date(2023, 8, 14), [cn1, cn2, cn3])
    time_12_13 = ReportsApi.report_total_time_categories(date(2023, 8, 12), date(2023, 8, 13), [cn1, cn2, cn3])

    assert time_14[cn1] == time_14[cn2] == time_14[cn3] == 60
    assert time_12_13[cn1] == 180
    assert time_12_13[cn2] == time_12_13[cn3] == 60

def test_should_report_total_time_by_tasks():
    cn = category_test_name()

    tn1 = task_test_name()
    tn2 = task_test_name()
    tn3 = task_test_name()

    CategoryApi.add(cn)

    TaskApi.add(tn1, [cn])
    TaskApi.add(tn2, [cn])
    TaskApi.add(tn3, [cn])

    TaskApi.add_duration(date(2023, 8, 12), 60, tn1)
    TaskApi.add_duration(date(2023, 8, 12), 60, tn2)
    TaskApi.add_duration(date(2023, 8, 13), 60, tn3)
    TaskApi.add_duration(date(2023, 8, 14), 60, tn1)

    time_spent = ReportsApi.report_total_time_tasks(date(2023, 8, 12), date(2023, 8, 14), [tn1, tn2, tn3])

    assert time_spent[tn1] == 120
    assert time_spent[tn2] == time_spent[tn3] == 60

def test_should_report_percentage_by_categories():
    cn1 = category_test_name()
    cn2 = category_test_name()
    cn3 = category_test_name()

    tn1 = task_test_name()
    tn2 = task_test_name()

    CategoryApi.add(cn1)
    CategoryApi.add(cn2)
    CategoryApi.add(cn3)

    TaskApi.add(tn1, [cn1, cn2])
    TaskApi.add(tn2, [cn1])
    
    # total time: 240
    TaskApi.add_duration(date(2023, 8, 12), 60, tn1)
    TaskApi.add_duration(date(2023, 8, 12), 50, tn2)
    TaskApi.add_duration(date(2023, 8, 13), 10, tn2)
    TaskApi.add_duration(date(2023, 8, 14), 120, tn1)

    time_spent = ReportsApi.report_percentage_categories(date(2023, 8, 12), date(2023, 8, 14), [cn1, cn2, cn3])

    assert time_spent[cn1] == 100
    assert time_spent[cn2] == 75

    # no time should be spent on third category
    assert cn3 not in time_spent.keys()

def test_should_report_percentage_by_tasks():
    cn = category_test_name()

    tn1 = task_test_name()
    tn2 = task_test_name()
    tn3 = task_test_name()

    CategoryApi.add(cn)

    TaskApi.add(tn1, [cn])
    TaskApi.add(tn2, [cn])
    TaskApi.add(tn3, [cn])

    # total time: 214
    TaskApi.add_duration(date(2023, 8, 12), 50, tn1)
    TaskApi.add_duration(date(2023, 8, 12), 102, tn2)
    TaskApi.add_duration(date(2023, 8, 13), 47, tn3)
    TaskApi.add_duration(date(2023, 8, 14), 15, tn1)

    time_spent = ReportsApi.report_percentage_tasks(date(2023, 8, 12), date(2023, 8, 14), [tn1, tn2, tn3])

    assert time_spent[tn1] == round(((50 + 15) / 214) * 100, 2)
    assert time_spent[tn2] == round((102 / 214) * 100, 2)
    assert time_spent[tn3] == round((47 / 214) * 100, 2)