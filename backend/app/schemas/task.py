from datetime import date

from pydantic import BaseModel


class BaseTask(BaseModel):
    title: str | None = None
    description: str | None = None


class TaskCreate(BaseTask):
    title: str


class TaskUpdate(BaseTask):
    pass


class TaskInDBBase(BaseTask):
    pk: int
    title: str
    day_id: int

    class Config:
        orm_mode = True


class TaskInDB(TaskInDBBase):
    pass


class TaskSchema(TaskInDBBase):
    pass


class WeekBase(BaseModel):
    start_day: date | None = None
    owner_id: int | None = None


class WeekIn(WeekBase):
    start_day: date
    owner_id: int


class DaySchema(BaseModel):
    pk: int
    weekday: str
    tasks: list[TaskSchema] | None = None

    class Config:
        orm_mode = True
