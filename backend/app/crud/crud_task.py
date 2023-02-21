from datetime import date

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import Task
from app.models.task import Week, Day
from app.schemas import TaskCreate


class CRUDTask(CRUDBase[Task]):
    async def create_task_with_day(self, db: AsyncSession, day_id: int, task_obj: TaskCreate):
        db_obj = self.model(day_id=day_id, **task_obj.dict())  # noqa
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj


class CRUDWeek(CRUDBase[Week]):
    async def create_week_with_owner(self, db: AsyncSession, start_day: date, owner_id: int):
        db_obj = self.model(start_day=start_day, owner_id=owner_id)  # noqa
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def get_week_with_owner(self, db: AsyncSession, start_day: date, owner_id: int):
        week_obj = db.execute(
            select(self.model).where(self.model.start_day == start_day, self.model.owner_id == owner_id)
        )
        return week_obj or self.create_week_with_owner(
            db=db, start_day=start_day, owner_id=owner_id
        )


class CRUDDay(CRUDBase[Day]):
    def create_day_with_week(self, db: Session, week_id: int):
        db_obj = self.model(weekday="Monday", week_id=week_id)  # noqa
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    async def create_days_for_week(self, db: AsyncSession, week_id: int):
        weekdays = ["Monday", "Sunday", "Wednesday", "Tuesday", "Friday"]
        day_objs = [
            self.model(weekday=day_name, week_id=week_id) for day_name in weekdays  # noqa
        ]
        db.add_all(day_objs)
        await db.commit()
        return day_objs


task = CRUDTask(Task)
week = CRUDWeek(Week)
day = CRUDDay(Day)
