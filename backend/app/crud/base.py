from typing import Generic, TypeVar, Type

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.app.db import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, db: Session, pk: int):
        return db.query(self.model).filter(self.model.pk == pk).first()

    def get_all(self, db: Session):
        return db.query(self.model).all()

    def update(self, db: Session, obj_in: Type[UpdateSchemaType], obj_db):
        old_obj_data = jsonable_encoder(obj_db)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in old_obj_data:
            if field in update_data:
                setattr(obj_db, field, update_data[field])

        db.add(obj_db)
        db.commit()
        db.refresh(obj_db)
        return obj_db

    def create(self, db: Session, obj_in):
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete_by_pk(self, db: Session, pk: int):
        obj = db.query(self.model).get(pk)
        db.delete(obj)
        db.commit()
        return

    def delete_by_instance(self, db: Session, db_obj: Type[ModelType]):
        db.delete(db_obj)
        db.commit()
        return
