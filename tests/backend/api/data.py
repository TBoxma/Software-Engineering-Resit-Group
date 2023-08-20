from uuid import uuid4

prefix_category = "TestCategory_"
prefix_task = "TestTask_"

def category_test_name() -> str:
    """
    :returns: Unique name of category prefixed with "TestCategory_" and postfixed with uuid4
    """
    return f"{prefix_category}{uuid4()}"

def task_test_name() -> str:
    """
    :returns: Unique name of task prefixed with "TestTask_" and postfixed with uuid4
    """
    return f"{prefix_task}{uuid4()}"