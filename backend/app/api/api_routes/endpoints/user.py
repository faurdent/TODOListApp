from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_db
from app.core.security import hash_password
from app.models import User
from app.schemas import UserCreate

router = APIRouter()


@router.post("/sign-up/")
async def sign_up(user_data: UserCreate, db: AsyncSession = Depends(get_db)):
    queryset = await db.execute(select(User).where(User.email == user_data.email))
    if queryset.scalars().first():
        raise HTTPException(status_code=400, detail="User with this email already exists")
    new_user = User(email=user_data.email, password=hash_password(user_data.password))
    db.add(new_user)
    await db.flush()
    await db.refresh(new_user)
    return new_user
