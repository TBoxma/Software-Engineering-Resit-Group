from src.backend.model.category import Category
from src.backend.model.task import Task


def having_created_category(name: str = None) -> Category:
    return Category(name="Test Category") if not name else Category(name=name)

def having_created_task(name: str = None) -> Task:
    return Task(name="Test task") if not name else Task(name=name)