from pydantic import BaseModel


class BaseTask(BaseModel):
    title: str | None
    description: str | None


class TaskOut(BaseTask):
    title: str


class TaskDBBase(BaseTask):
    pk: int | None


class TaskDBIn(TaskDBBase):
    pass

