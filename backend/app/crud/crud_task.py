from datetime import date

from sqlalchemy.orm import Session

from backend.app.crud.base import CRUDBase
from backend.app.models import Task
from backend.app.models.task import Week, Day
from backend.app.schemas import TaskCreate


class CRUDTask(CRUDBase[Task]):
    def create_task_with_day(self, db: Session, day_id: int, task_obj: TaskCreate):
        db_obj = self.model(day_id=day_id, **task_obj.dict()) # noqa
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


class CRUDWeek(CRUDBase[Week]):
    def create_week_with_owner(self, db: Session, start_day: date, owner_id: int):
        db_obj = self.model(start_day=start_day, owner_id=owner_id) # noqa
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_week_with_owner(self, db: Session, start_day: date, owner_id: int):
        return db.query(self.model).filter(self.model.start_day == start_day, self.model.owner_id == owner_id).first()


class CRUDDay(CRUDBase[Day]):
    def create_day_with_week(self, db: Session, week_id: int):
        db_obj = self.model(weekday="Monday", week_id=week_id) # noqa
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


task = CRUDTask(Task)
week = CRUDWeek(Week)
day = CRUDDay(Day)
