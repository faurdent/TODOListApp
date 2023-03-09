from datetime import date

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from app.api.dependencies import get_db, get_current_verified_user
from app.crud import task, week, day, relationship_collectors
from app.models import User
from app.schemas import TaskSchema, TaskUpdate, TaskCreate, DaySchema, WeekSchema

router = APIRouter()


@router.put("/{pk}", response_model=TaskSchema)
async def update_task(
    pk: int,
    task_obj: TaskUpdate,
    # owner: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    task_to_update = await task.get(db, pk=pk)
    if not task_to_update:
        raise HTTPException(status_code=404, detail="Task not found")
    return await task.update(db=db, obj_in=task_obj, obj_db=task_to_update)


@router.delete("/{pk}", response_model=TaskSchema)
async def delete_task(
    pk: int,
    # owner: User = Depends(get_current_verified_user),
    db: Session = Depends(get_db),
):
    deleted_task = await task.delete(db, pk=pk)
    if not deleted_task:
        raise HTTPException(status_code=404, detail="Instance not found")
    return deleted_task


@router.get("/{pk}", response_model=TaskSchema)
async def get_task(
    pk: int,
    # owner: User = Depends(get_current_verified_user),
    db: Session = Depends(get_db),
):
    task_obj = await task.get(db, pk=pk)
    if not task_obj:
        raise HTTPException(status_code=404, detail="Task not found")
    return task_obj


@router.post("/{day_pk}", response_model=TaskSchema)
async def add_task(
    task_in: TaskCreate,
    day_pk: int,
    db: Session = Depends(get_db),
    # owner: User = Depends(get_current_verified_user),
):
    day_obj = await day.get_day_with_owner(db, pk=day_pk, owner_id=1)
    if not day_obj:
        raise HTTPException(status_code=404, detail="Day not found")
    return await task.create_task_with_day(db=db, day_id=day_pk, task_obj=task_in)


@router.get("/day/{pk}", response_model=DaySchema)
async def get_tasks_for_day(
    pk: int, db: AsyncSession = Depends(get_db), owner: User = Depends(get_current_verified_user)
):
    day_obj = await day.get_day_with_owner(db, pk=pk, owner_id=owner.pk)

    if not day_obj:
        raise HTTPException(status_code=404, detail="Day not found")

    return day_obj


@router.get("/week/{week_start}", response_model=WeekSchema)
async def get_tasks_for_week(
    week_start: date,
    db: AsyncSession = Depends(get_db),
    # owner: User = Depends(get_current_verified_user)
):
    current_week = await week.get_week_with_owner(db=db, start_day=week_start, owner_id=1)
    # weekdays = current_week.week_days or await day.create_days_for_week(db, current_week.pk, week_start)
    tasks = []
    if current_week.week_days:
        weekdays = current_week.week_days
        tasks = relationship_collectors.collect_tasks(weekdays)
    else:
        weekdays = await day.create_days_for_week(db, current_week.pk, week_start)
    # if not current_week.week_days:
    #     weekdays = current_week
    # weekdays = await day.create_days_for_week(db, current_week.pk, week_start)
    return WeekSchema(start_day=current_week.start_day, week_days=weekdays, tasks=tasks)
