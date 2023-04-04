from datetime import timedelta

from fastapi import APIRouter, Cookie, Depends, HTTPException, Response
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_db
from app.core.security import decode_token, verify_password, create_token
from app.models import User
from app.schemas import Token
from app.schemas.user import UserCreate

router = APIRouter()


@router.post("/access-token", response_model=Token)
async def login_access_token(response: Response, login_data: UserCreate, db: AsyncSession = Depends(get_db)):
    queryset = await db.execute(select(User).where(User.email == login_data.email))
    user = queryset.scalars().first()
    if not user:
        raise HTTPException(status_code=404, detail={"field": "username", "msg": "User does not exists"})
    elif not verify_password(login_data.password, user.password):
        raise HTTPException(status_code=400, detail={"field": "password", "msg": "Password is incorrect"})

    access_token_expires = timedelta(minutes=10)
    response.set_cookie(
        key="refresh_token",
        value=create_token(user.pk, timedelta(days=7)),
        httponly=True,
        expires=3600 * 24 * 7,
        samesite="lax",
        secure=False,
    )

    return {
        "access_token": create_token(user.pk, access_token_expires),
        "token_type": "bearer",
    }


@router.get("/refresh-token")
async def refresh_token(refresh_token: str | None = Cookie(default=None)):
    token_data = decode_token(refresh_token)
    new_access_token = create_token(token_data.subject, expires_delta=timedelta(seconds=20))
    return {"access_token": new_access_token, "token_type": "bearer"}
