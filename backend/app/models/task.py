from sqlalchemy import Column, String, Text, ForeignKey, BigInteger, Date
from sqlalchemy.orm import relationship

from backend.app.db import Base


class Week(Base):
    start_day = Column(Date)
    owner_id = Column(BigInteger, ForeignKey("user.pk"), nullable=False, index=True)
    owner = relationship("User", backref="owner_tasks", foreign_keys=[owner_id])


class Day(Base):
    weekday = Column(String(15))
    week_id = Column(BigInteger, ForeignKey(Week.pk))
    week = relationship("Week", backref="week_days", foreign_keys=[week_id])


class Task(Base):
    title = Column(String(60))
    description = Column(Text)
    day_id = Column(BigInteger, ForeignKey(Day.pk))
    day = relationship("Day", backref="tasks", foreign_keys=[day_id])
