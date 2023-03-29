from datetime import datetime

from sqlalchemy import UUID, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from app.db import Base
from .user import User


class VerificationCode(Base):
    __tablename__ = "verification_ids"
    verification_code = mapped_column(UUID(as_uuid=True))
    valid_until: Mapped[datetime]
    user_id: Mapped[int] = mapped_column(ForeignKey("user.pk"))
    user: Mapped["User"] = relationship(backref="verification_code", uselist=False)
