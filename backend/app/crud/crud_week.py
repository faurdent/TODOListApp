from datetime import date

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Week


class CRUDWeek(CRUDBase[Week]):
    async def create_week_with_owner(self, db: AsyncSession, start_day: date, owner_id: int):
        db_obj = self.model(start_day=start_day, owner_id=owner_id)  # noqa
        db.add(db_obj)
        await db.flush()
        await db.refresh(db_obj)
        return db_obj

    async def get_week_with_owner(self, db: AsyncSession, start_day: date, owner_id: int):
        queryset = await db.execute(
            select(self.model).where(self.model.start_day == start_day, self.model.owner_id == owner_id)
        )
        week_obj = queryset.scalars().first()
        return week_obj or await self.create_week_with_owner(
            db=db, start_day=start_day, owner_id=owner_id
        )

    async def get_weekdays(self, db: AsyncSession, week_object: Week):
        pass


week = CRUDWeek(Week)
