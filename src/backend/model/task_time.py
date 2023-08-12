from datetime import date
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from . import Base

class TaskTime(Base):
    __tablename__ = "task_time"

    task_day: Mapped[date] = mapped_column(primary_key=True)
    task_id: Mapped[int] = mapped_column(ForeignKey('task.id'), primary_key=True)
    duration: Mapped[int]