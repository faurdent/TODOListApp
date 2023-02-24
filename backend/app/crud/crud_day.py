from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Day, Week


class CRUDDay(CRUDBase[Day]):
    async def create_days_for_week(self, db: AsyncSession, week_id: int):
        weekdays = ("Monday", "Tuesday", "Wednesday", "Tuesday", "Friday", "Saturday", "Sunday")
        day_objs = [
            self.model(weekday=day_name, week_id=week_id, tasks=[]) for day_name in weekdays
        ]
        db.add_all(day_objs)
        await db.flush()
        return day_objs

    async def get_day_with_owner(self, db: AsyncSession, pk, owner_id):
        query = select(self.model).where(Week.owner_id == owner_id, self.model.pk == pk).join(Week)
        day_obj = await db.scalars(query)

        return day_obj.first()


day = CRUDDay(Day)
