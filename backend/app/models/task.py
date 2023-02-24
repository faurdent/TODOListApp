from datetime import time, date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db import Base


class Week(Base):
    __tablename__ = "week"
    start_day: Mapped[date]
    owner_id: Mapped[int] = mapped_column(ForeignKey("user.pk"))
    week_days: Mapped[list["Day"]] = relationship(
        cascade="all, delete-orphan",
        passive_deletes=True,
        lazy="joined"
    )


class Day(Base):
    __tablename__ = "day"
    weekday: Mapped[str]
    week_id: Mapped[int] = mapped_column(ForeignKey("week.pk"))
    tasks: Mapped[list["Task"]] = relationship(
        cascade="all, delete-orphan",
        passive_deletes=True,
        lazy="joined"
    )


class Task(Base):
    __tablename__ = "task"
    title: Mapped[str]
    description: Mapped[str] = mapped_column(nullable=True)
    deadline: Mapped[time]
    is_done: Mapped[bool] = mapped_column(default=False)
    day_id: Mapped[int] = mapped_column(ForeignKey("day.pk"))
