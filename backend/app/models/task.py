from sqlalchemy import Column, String, Text, ForeignKey, BigInteger
from sqlalchemy.orm import relationship

from backend.app.db import Base


# class Week(Base):
#     pass
#
#
# class Day(Base):
#     weekday = Column(String(15))
#     week = Column(Integer, ForeignKey(Week.pk))
#     tasks = relationship("Task", backref="day")


class Task(Base):
    title = Column(String(60))
    description = Column(Text)
    owner_id = Column(BigInteger, ForeignKey("user.pk"), nullable=False, index=True)
    owner = relationship("User", backref="owner_tasks", foreign_keys=[owner_id])
