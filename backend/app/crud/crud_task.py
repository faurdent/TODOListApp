from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Task
from app.schemas import TaskCreate


class CRUDTask(CRUDBase[Task]):
    async def create_task_with_day(self, db: AsyncSession, day_id: int, task_obj: TaskCreate):
        db_obj = self.model(day_id=day_id, **task_obj.dict())  # noqa
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj


task = CRUDTask(Task)
