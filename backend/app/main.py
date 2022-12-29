from datetime import timedelta

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .core.security import verify_password, create_access_token, hash_password
from .crud import task
from .dependencies import get_db, get_current_user
from .models import User
from .schemas import TaskSchema, TaskCreate, Token, TaskUpdate

app = FastAPI()


@app.get("/")
async def main_page():
    return {"hello": "world"}


@app.post("/my-tasks/add-task/", response_model=TaskSchema)
async def create_task(task_obj: TaskCreate, owner: User = Depends(get_current_user), db: Session = Depends(get_db)):
    created_task = task.create_with_owner(db=db, obj_in=task_obj, owner_id=owner.pk)
    return created_task


@app.put("/my-tasks/{pk}", response_model=TaskSchema)
async def update_task(
        pk: int, task_obj: TaskUpdate, owner: User = Depends(get_current_user), db: Session = Depends(get_db)
):
    task_to_update = task.get_with_owner(db=db, pk=pk, owner_id=owner.pk)
    if not task_to_update:
        raise HTTPException(status_code=404, detail="Task not found")
    updated_task = task.update(db=db, obj_in=task_obj, obj_db=task_to_update)
    return updated_task


@app.delete("/my-tasks/{pk}")
async def delete_task(
        pk: int, owner: User = Depends(get_current_user), db: Session = Depends(get_db)
):
    task_to_delete = task.get_with_owner(db=db, pk=pk, owner_id=owner.pk)
    if not task_to_delete:
        raise HTTPException(status_code=404, detail="Task not found")
    task.delete_by_instance(db, task_to_delete)
    return {"msg": "Deleted"}


@app.get("/my-tasks/{pk}", response_model=TaskSchema)
async def get_task(pk: int, owner: User = Depends(get_current_user), db: Session = Depends(get_db)):
    task_obj = task.get_with_owner(db=db, pk=pk, owner_id=owner.pk)
    print(task_obj)
    return task_obj


@app.get("/my-tasks/", response_model=list[TaskSchema])
async def get_my_tasks(owner: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return task.get_all_by_owner(db=db, owner_id=owner.pk)


@app.post("/sign-up/")
async def sign_up(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    if db.query(User).filter(User.email == form_data.username).first():
        raise HTTPException(status_code=400, detail="User with this email already exists")
    new_user = User(email=form_data.username, password=hash_password(form_data.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.post("/login/access-token", response_model=Token)
async def login_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User does not exists")
    elif not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=400)

    access_token_expires = timedelta(minutes=30)
    return {
        "access_token": create_access_token(user.pk, access_token_expires),
        "token_type": "bearer",
    }
