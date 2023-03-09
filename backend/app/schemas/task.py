from datetime import date, time

from pydantic import BaseModel


class BaseTask(BaseModel):
    title: str | None = None
    description: str | None = None
    deadline: time | None = None
    is_done: bool | None = None


class TaskCreate(BaseTask):
    title: str
    deadline: time


class TaskUpdate(BaseTask):
    pass


class TaskInDBBase(BaseTask):
    pk: int
    title: str
    deadline: time
    day_id: int

    class Config:
        orm_mode = True


class TaskSchema(TaskInDBBase):
    pass


class DaySchema(BaseModel):
    pk: int
    weekday: str
    day_date: date
    # tasks: list[TaskSchema] | None = None

    class Config:
        orm_mode = True


class WeekSchema(BaseModel):
    start_day: date
    week_days: list[DaySchema]
    tasks: list[TaskSchema]

    class Config:
        orm_mode = True
