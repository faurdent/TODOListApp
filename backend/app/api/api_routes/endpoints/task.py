from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.api.dependencies import get_current_user, get_db
from backend.app.crud import task
from backend.app.models import User
from backend.app.schemas import TaskSchema, TaskUpdate, TaskCreate

router = APIRouter()


@router.post("/add-task/", response_model=TaskSchema)
async def create_task(task_obj: TaskCreate, owner: User = Depends(get_current_user), db: Session = Depends(get_db)):
    created_task = task.create_with_owner(db=db, obj_in=task_obj, owner_id=owner.pk)
    return created_task


@router.put("/{pk}", response_model=TaskSchema)
async def update_task(
    pk: int, task_obj: TaskUpdate, owner: User = Depends(get_current_user), db: Session = Depends(get_db)
):
    task_to_update = task.get_with_owner(db=db, pk=pk, owner_id=owner.pk)
    if not task_to_update:
        raise HTTPException(status_code=404, detail="Task not found")
    updated_task = task.update(db=db, obj_in=task_obj, obj_db=task_to_update)
    return updated_task


@router.delete("/{pk}")
async def delete_task(pk: int, owner: User = Depends(get_current_user), db: Session = Depends(get_db)):
    task_to_delete = task.get_with_owner(db=db, pk=pk, owner_id=owner.pk)
    if not task_to_delete:
        raise HTTPException(status_code=404, detail="Task not found")
    task.delete_by_instance(db, task_to_delete)
    return {"msg": "Deleted"}


@router.get("/{pk}", response_model=TaskSchema)
async def get_task(pk: int, owner: User = Depends(get_current_user), db: Session = Depends(get_db)):
    # task_obj = task.get_with_owner(db=db, pk=pk, owner_id=owner.pk)
    if task_obj := task.get_with_owner(db=db, pk=pk, owner_id=owner.pk):
        return task_obj
    raise HTTPException(status_code=404, detail="Task not found")
    # print(task_obj)
    # return task_obj


@router.get("/", response_model=list[TaskSchema])
async def get_my_tasks(owner: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return task.get_all_by_owner(db=db, owner_id=owner.pk)