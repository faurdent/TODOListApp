from datetime import timedelta, datetime, timezone

from jose import jwt
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = "HS256"


def create_access_token(subject: int, expires_delta: timedelta):
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode_data = {"subject": subject, "exp": expire}
    return jwt.encode(
        to_encode_data,
        "8ZIOl6Rcuh4X+/oK/iArCx4qWSBkGjG3nXGcSlC0xx8=",
        algorithm=ALGORITHM,
    )


def hash_password(plain_password: str):
    return pwd_context.hash(plain_password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)
