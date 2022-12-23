from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .dependencies import get_db
from .models import Task
from .schemas import TaskIn, TaskDBOut

app = FastAPI()


@app.get("/")
async def main_page():
    return {"hello": "world"}


@app.post("/my-tasks/add-task/", response_model=TaskDBOut)
async def add_task(task: TaskIn, db: Session = Depends(get_db)):
    task_obj = Task(**task.dict())
    print(task_obj)
    db.add(task_obj)
    db.commit()
    db.refresh(task_obj)
    return task_obj


@app.get("/my-tasks/{pk}", response_model=TaskDBOut)
async def get_one_task(pk: int, db: Session = Depends(get_db)):
    task_obj = db.query(Task).get(pk)
    if not task_obj:
        raise HTTPException(status_code=404, detail="Task does not exists")
    return task_obj


@app.get("/my-tasks/", response_model=list[TaskDBOut])
async def get_all_tasks(db: Session = Depends(get_db)):
    queryset = db.query(Task).all()
    print(queryset)
    return queryset
