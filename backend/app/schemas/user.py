from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr | None = None


class UserCreate(UserBase):
    email: str
    password: str


class UserUpdate(UserBase):
    password: str | None = None


class UserInDBBase(UserBase):
    pk: int

    class Config:
        orm_mode = True


class UserSchema(UserInDBBase):
    pass


class UserInDB(UserInDBBase):
    hashed_password: str


class User(UserInDBBase):
    pass
