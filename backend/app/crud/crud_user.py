from app.crud.base import CRUDBase
from app.models import User


class CRUDUser(CRUDBase[User]):
    async def activate_account(self, db, user_id):
        user_obj = await self.get(db, pk=user_id)
        user_obj.is_verified = True
        await db.flush()
        return user_obj


user = CRUDUser(User)
