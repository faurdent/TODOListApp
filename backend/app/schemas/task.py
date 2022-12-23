from pydantic import BaseModel


class BaseTask(BaseModel):
    title: str | None
    description: str | None


class TaskIn(BaseTask):
    title: str


class TaskOut(BaseTask):
    title: str


class TaskDBBase(BaseTask):
    pk: int | None


class TaskDBOut(TaskDBBase):
    class Config:
        orm_mode = True
