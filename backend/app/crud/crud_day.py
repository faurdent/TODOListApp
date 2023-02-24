from datetime import date, timedelta

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Day, Week


class CRUDDay(CRUDBase[Day]):
    async def create_days_for_week(self, db: AsyncSession, week_id: int, week_start: date):
        weekdays = ("Monday", "Tuesday", "Wednesday", "Tuesday", "Friday", "Saturday", "Sunday")
        day_objs = []
        for weekday_number, weekday_name in enumerate(weekdays):
            day_date = week_start + timedelta(days=weekday_number)
            day_objs.append(self.model(weekday=weekday_name, day_date=day_date, week_id=week_id, tasks=[]))
        db.add_all(day_objs)
        await db.flush()
        return day_objs

    async def get_day_with_owner(self, db: AsyncSession, pk, owner_id):
        query = select(self.model).where(Week.owner_id == owner_id, self.model.pk == pk).join(Week)
        day_obj = await db.scalars(query)

        return day_obj.first()


day = CRUDDay(Day)
