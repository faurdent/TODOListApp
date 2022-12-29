from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from backend.app.crud.base import CRUDBase
from backend.app.models import Task
from backend.app.schemas import TaskCreate, TaskUpdate


class CRUDTask(CRUDBase[Task, TaskCreate, TaskUpdate]):
    def create_with_owner(self, db: Session, obj_in: TaskCreate, owner_id: int):
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


task = CRUDTask(Task)
