from fastapi import Depends, HTTPException, BackgroundTasks
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.core.security import decode_token
from app.db import SessionLocal
from app.models import User
from app.services.email_operations import send_verification_code

oauth2 = OAuth2PasswordBearer(tokenUrl="access-token")


async def get_db():
    async with SessionLocal() as session:
        async with session.begin():
            try:
                yield session
            except Exception as e:
                await session.rollback()
                raise e


async def get_current_user(
        db: AsyncSession = Depends(get_db),
        token: str = Depends(oauth2)
) -> User:
    token_data = decode_token(token)
    queryset = await db.execute(select(User).where(User.pk == token_data.subject))
    user = queryset.scalars().first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def get_current_verified_user(
        background_tasks: BackgroundTasks,
        db: AsyncSession = Depends(get_db),
        current_user: User = Depends(get_current_user),
):
    print(background_tasks.__dict__)
    if not current_user.is_verified:
        background_tasks.add_task(send_verification_code, db, current_user.pk, current_user.email)
        print(background_tasks.__dict__)
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive user. Verify your account",
        )
    yield current_user
