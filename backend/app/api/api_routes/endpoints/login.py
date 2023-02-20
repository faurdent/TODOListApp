from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.core.security import verify_password, create_access_token
from app.models import User
from app.schemas import Token

router = APIRouter()


@router.post("/access-token", response_model=Token)
async def login_access_token(
    db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()
):
    print()
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User does not exists")
    elif not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=400)

    access_token_expires = timedelta(minutes=30)
    return {
        "access_token": create_access_token(user.pk, access_token_expires),
        "token_type": "bearer",
    }
