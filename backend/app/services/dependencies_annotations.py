from typing import Annotated

from fastapi import Depends

from app.api.dependencies import get_current_verified_user
from app.models import User

CurrentVerifiedUser = Annotated[User, Depends(get_current_verified_user)]
