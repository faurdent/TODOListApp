from sqlalchemy import Column, String, Boolean

from app.db import Base


class User(Base):
    email = Column(String(100))
    password = Column(String(60))
    is_verified = Column(Boolean)
