from pydantic import BaseModel


class UserBase(BaseModel):
    username: str | None = None


class UserCreate(UserBase):
    username: str
    password: str


class UserUpdate(UserBase):
    password: str | None = None


class UserInDBBase(UserBase):
    pk: int
    email: str

    class Config:
        orm_mode = True


class UserSchema(UserInDBBase):
    pass


class UserInDB(UserInDBBase):
    hashed_password: str


class User(UserInDBBase):
    pass
