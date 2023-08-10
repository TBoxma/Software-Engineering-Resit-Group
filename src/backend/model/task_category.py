from unicodedata import category
from sqlalchemy import Column, ForeignKey, String, Table
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from . import Base

class TaskCategory(Base):
    __tablename__ = "task_category"

    category_id: Mapped[int] = mapped_column(ForeignKey('category.id'), primary_key=True)
    task_id: Mapped[int] = mapped_column(ForeignKey('task.id'), primary_key=True)