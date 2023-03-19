from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.db import SessionLocal
from app.models import User
from app.core.security import decode_token

oauth2 = OAuth2PasswordBearer(tokenUrl="access-token")


async def get_db():
    async with SessionLocal() as session:
        async with session.begin():
            try:
                yield session
            except Exception as e:
                await session.rollback()
                raise e


async def get_current_user(db: AsyncSession = Depends(get_db), token: str = Depends(oauth2)) -> User:
    token_data = decode_token(token)
    queryset = await db.execute(select(User).where(User.pk == token_data.subject))
    user = queryset.scalars().first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


def get_current_verified_user(current_user: User = Depends(get_current_user)):
    if not current_user.is_verified:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user. Verify your account",
        )
    return current_user
