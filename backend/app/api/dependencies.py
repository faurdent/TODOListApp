from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session
from starlette import status

from app.core.security import ALGORITHM
from app.db import SessionLocal
from app.models import User
from app.schemas import TokenData

oauth2 = OAuth2PasswordBearer(tokenUrl="access-token")


def get_db():
    db_obj = SessionLocal()
    try:
        yield db_obj
    finally:
        db_obj.close()


def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2)) -> User:
    try:
        payload = jwt.decode(token, "8ZIOl6Rcuh4X+/oK/iArCx4qWSBkGjG3nXGcSlC0xx8=", algorithms=[ALGORITHM])
        token_data = TokenData(**payload)
    except (jwt.JWTError, ValidationError) as exc:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        ) from exc

    user = db.query(User).filter(User.pk == token_data.subject).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


def get_current_verified_user(current_user: User = Depends(get_current_user)):
    if not current_user.is_verified:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Inactive user. Verify your account")
    return current_user
