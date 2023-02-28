from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_db
from app.core.security import verify_password, create_access_token
from app.models import User
from app.schemas import Token, UserCreate

router = APIRouter()


@router.post("/access-token", response_model=Token)
async def login_access_token(login_data: UserCreate, db: AsyncSession = Depends(get_db)):
    queryset = await db.execute(select(User).where(User.email == login_data.username))
    user = queryset.scalars().first()
    if not user:
        raise HTTPException(status_code=404, detail="User does not exists")
    elif not verify_password(login_data.password, user.password):
        raise HTTPException(status_code=400)

    access_token_expires = timedelta(days=7)
    return {
        "access_token": create_access_token(user.pk, access_token_expires),
        "user_data": user,
        "token_type": "bearer",
    }
