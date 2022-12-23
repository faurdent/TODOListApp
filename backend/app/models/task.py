from sqlalchemy import Column, String, Text

from backend.app.db import Base


class Task(Base):
    title = Column(String(60))
    description = Column(Text)
