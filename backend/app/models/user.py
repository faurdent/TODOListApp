from sqlalchemy import Column, String

from backend.app.db import Base


class User(Base):
    email = Column(String(100))
    password = Column(String(60))
