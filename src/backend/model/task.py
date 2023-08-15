from typing import List
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from src.backend.model.task_time import TaskTime

from . import Base

class Task(Base):
    __tablename__ = "task"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), unique=True)
    categories = relationship('Category', secondary='task_category', back_populates='tasks', lazy='selectin')
    durations: Mapped[List[TaskTime]] = relationship()