from datetime import date

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.api.dependencies import get_current_user, get_db, get_current_verified_user
from backend.app.crud import task, week, day
from backend.app.models import User
from backend.app.schemas import TaskSchema, TaskUpdate, TaskCreate
from backend.app.schemas.task import DaySchema

router = APIRouter()


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
async def delete_task(pk: int, owner: User = Depends(get_current_verified_user), db: Session = Depends(get_db)):
    task_to_delete = task.get_with_owner(db=db, pk=pk, owner_id=owner.pk)
    if not task_to_delete:
        raise HTTPException(status_code=404, detail="Task not found")
    task.delete_by_instance(db, task_to_delete)
    return {"msg": "Deleted"}


@router.get("/{pk}", response_model=TaskSchema)
async def get_task(pk: int, owner: User = Depends(get_current_verified_user), db: Session = Depends(get_db)):
    if task_obj := task.get_with_owner(db=db, pk=pk, owner_id=owner.pk):
        return task_obj
    raise HTTPException(status_code=404, detail="Task not found")


@router.get("/", response_model=list[TaskSchema])
async def get_my_tasks(owner: User = Depends(get_current_verified_user), db: Session = Depends(get_db)):
    return task.get_all_by_owner(db=db, owner_id=owner.pk)


@router.get("/test-week/{week_start}")
async def get_week(week_start: date, db: Session = Depends(get_db), owner: User = Depends(get_current_user)):
    current_week = week.get_week_with_owner(db=db, start_day=week_start, owner_id=owner.pk)
    if current_week:
        return current_week
    return week.create_week_with_owner(db=db, start_day=week_start, owner_id=owner.pk)


@router.post("/add-day/", deprecated=True)
async def add_day(week_start: date, db: Session = Depends(get_db), owner: User = Depends(get_current_verified_user)):
    current_week = week.get_week_with_owner(db=db, start_day=week_start, owner_id=owner.pk)
    day_obj = day.create_day_with_week(db=db, week_id=current_week.pk)
    print(day_obj)
    return day_obj


@router.post("/add-task/{day_pk}")
async def add_task(
        task_in: TaskCreate,
        day_pk: int, db: Session = Depends(get_db),
        owner: User = Depends(get_current_verified_user)
):
    # current_week = week.get_week_with_owner(db=db, start_day=week_start, owner_id=owner.pk)
    day_obj = day.get(db=db, pk=day_pk)
    if not day_obj:
        raise HTTPException(status_code=404, detail="Day not found")
    task_obj = task.create_task_with_day(db=db, day_id=day_pk, task_obj=task_in)
    return task_obj


@router.get("/test-tasks/{week_start}", response_model=list[DaySchema])
async def get_tasks_for_week(
        week_start: date,
        db: Session = Depends(get_db),
        owner: User = Depends(get_current_verified_user)
):
    current_week = week.get_week_with_owner(db=db, start_day=week_start, owner_id=owner.pk)
    return current_week.week_days

