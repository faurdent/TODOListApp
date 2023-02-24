from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_db
from app.core.security import hash_password
from app.models import User

router = APIRouter()


@router.post("/sign-up/")
async def sign_up(db: AsyncSession = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    queryset = await db.execute(select(User).where(User.email == form_data.username))
    if queryset.scalars().first():
        raise HTTPException(status_code=400, detail="User with this email already exists")
    new_user = User(email=form_data.username, password=hash_password(form_data.password))
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user
