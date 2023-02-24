from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class User(Base):
    __tablename__ = "user"
    email: Mapped[str]
    password: Mapped[str]
    is_verified: Mapped[bool] = mapped_column(default=True)
