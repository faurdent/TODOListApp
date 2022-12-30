from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from backend.app.api.dependencies import get_db
from backend.app.core.security import hash_password
from backend.app.models import User

router = APIRouter()


@router.post("/sign-up/")
async def sign_up(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    if db.query(User).filter(User.email == form_data.username).first():
        raise HTTPException(status_code=400, detail="User with this email already exists")
    new_user = User(email=form_data.username, password=hash_password(form_data.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
