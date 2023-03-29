from datetime import datetime, timedelta
import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import VerificationCode


class CRUDVerificationCode(CRUDBase[VerificationCode]):
    async def create_or_update_verification_code(self, db: AsyncSession, user_id: int):
        new_code = uuid.uuid4()
        valid_until = datetime.now() + timedelta(minutes=5)
        code_obj = await self.get(db, user_id=user_id)
        if code_obj:
            update_data = {"verification_code": new_code, "valid_until": valid_until}
            return await self.update(db, code_obj, update_data)
        new_code_obj = self.model(verification_code=new_code, valid_until=valid_until, user_id=user_id)
        db.add(new_code_obj)
        await db.flush()
        await db.refresh(new_code_obj)
        return new_code_obj


verification_code = CRUDVerificationCode(VerificationCode)
