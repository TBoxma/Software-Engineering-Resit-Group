from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

# Importing each model, so sqlalchemy can pick them up
from .category import Category
from .task import Task
from .task_category import TaskCategory