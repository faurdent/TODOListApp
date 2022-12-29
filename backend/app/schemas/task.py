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
    owner_id: int

    class Config:
        orm_mode = True


class TaskInDB(TaskInDBBase):
    pass


class TaskSchema(TaskInDBBase):
    pass


# class TaskIn(BaseTask):
#     title: str
#
#
# class TaskOut(BaseTask):
#     title: str
#
#
# class TaskDBBase(BaseTask):
#     pk: int | None
#
#
# class TaskDBOut(TaskDBBase):
#     class Config:
#         orm_mode = True
