from typing import Generic, TypeVar, Type

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get(self, db: AsyncSession, **kwargs):
        queryset = await db.scalars(select(self.model).filter_by(**kwargs))
        return queryset.first()

    async def get_all(self, db: AsyncSession):
        queryset = await db.execute(select(self.model))
        return queryset.scalars().all()

    async def update(self, db: AsyncSession, obj_in: Type[UpdateSchemaType] | dict, obj_db):
        old_obj_data = jsonable_encoder(obj_db)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in old_obj_data:
            if field in update_data:
                setattr(obj_db, field, update_data[field])

        await db.commit()
        # await db.refresh(obj_db)
        return obj_db

    async def create(self, db: AsyncSession, obj_in):
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        await db.flush()
        await db.refresh(db_obj)
        return db_obj

    async def delete(self, db: AsyncSession, pk: int):
        obj = await self.get(db, pk=pk)
        if not obj:
            return
        await db.delete(obj)
        await db.commit()
        return obj
