from datetime import timedelta

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .core.security import verify_password, create_access_token, hash_password
from .crud import task
from .dependencies import get_db, get_current_user
from .models import User
from .schemas import TaskSchema, TaskCreate, Token

app = FastAPI()


@app.get("/")
async def main_page():
    return {"hello": "world"}


@app.post("/my-tasks/add-task/", response_model=TaskSchema)
async def create_task(task_obj: TaskCreate, owner: User = Depends(get_current_user), db: Session = Depends(get_db)):
    created_task = task.create_with_owner(db=db, obj_in=task_obj, owner_id=owner.pk)
    print(created_task)
    return created_task


# @app.post("/my-tasks/add-task/", response_model=TaskDBOut)
# async def add_task(task: TaskIn, db: Session = Depends(get_db), owner: User = Depends(get_current_user)):
#     task_info = task.dict()
#     task_info.update({"owner_id": owner.pk})
#     task_obj = Task(**task_info)
#     print(task_obj)
#     db.add(task_obj)
#     db.commit()
#     db.refresh(task_obj)
#     return task_obj


# @app.get("/my-tasks/{pk}", response_model=TaskDBOut)
# async def get_one_task(pk: int, db: Session = Depends(get_db), owner: User = Depends(get_current_user)):
#     task_obj = db.query(Task).get(pk)
#     print(owner)
#     if not task_obj:
#         raise HTTPException(status_code=404, detail="Task does not exists")
#     return task_obj
#
#
# @app.get("/my-tasks/", response_model=list[TaskDBOut])
# async def get_all_tasks(db: Session = Depends(get_db), owner: User = Depends(get_current_user)):
#     queryset = owner.owner_tasks
#     print(queryset)
#     return queryset


@app.post("/sign-up/")
async def sign_up(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = db.query(User).filter(User.email == form_data.username).first()
    if user:
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
