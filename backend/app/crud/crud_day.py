from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Day, Week


class CRUDDay(CRUDBase[Day]):
    def create_day_with_week(self, db: AsyncSession, week_id: int):
        db_obj = self.model(weekday="Monday", week_id=week_id)  # noqa
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    async def create_days_for_week(self, db: AsyncSession, week_id: int):
        weekdays = ("Monday", "Sunday", "Wednesday", "Tuesday", "Friday", "Saturday", "Sunday")
        day_objs = [
            self.model(weekday=day_name, week_id=week_id) for day_name in weekdays  # noqa
        ]
        db.add_all(day_objs)
        await db.flush()
        return day_objs

    async def get_day_with_owner(self, db: AsyncSession, pk, owner_id):
        query = select(self.model).where(Week.owner_id == owner_id, self.model.pk == pk).join(Week)
        res = await db.scalars(query)
        day_obj = res.first()
        return day_obj


day = CRUDDay(Day)
