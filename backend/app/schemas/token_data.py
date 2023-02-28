from pydantic import BaseModel

from app.schemas.user import UserSchema


class Token(BaseModel):
    access_token: str
    token_type: str
    user_data: UserSchema


class TokenData(BaseModel):
    subject: int | None = None
