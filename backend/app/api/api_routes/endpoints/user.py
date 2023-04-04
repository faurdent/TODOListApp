from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_db, get_current_user
from app.core.security import hash_password
from app.crud import user, verification_code
from app.models import User
from app.schemas import UserCreate, UserSchema
from app.services.email_operations import send_verification_code

router = APIRouter()


@router.post("/sign-up/")
async def sign_up(user_data: UserCreate, background_tasks: BackgroundTasks, db: AsyncSession = Depends(get_db)):
    queryset = await db.execute(select(User).where(User.email == user_data.email))
    if queryset.scalars().first():
        raise HTTPException(status_code=400, detail="User with this email already exists")
    new_user_object = User(email=user_data.email, password=hash_password(user_data.password))
    new_user = await user.create(db, new_user_object)
    background_tasks.add_task(send_verification_code, db, new_user.pk, new_user.email)
    return new_user


@router.get("/verify/{verification_user_code}")
async def verify_account(verification_user_code: str, db: AsyncSession = Depends(get_db)):
    verification_code_obj = await verification_code.get(db, verification_code=verification_user_code)
    if not verification_code_obj:
        raise HTTPException(status_code=400, detail="Incorrect verification code")
    return await user.activate_account(db, verification_code_obj.user_id)


@router.post("/send-verification-email")
async def send_verification_email(
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db),
    user_info: UserSchema = Depends(get_current_user),
):
    background_tasks.add_task(send_verification_code, db, user_info.pk, user_info.email)
    return {"msg": "Email sent successfully"}
