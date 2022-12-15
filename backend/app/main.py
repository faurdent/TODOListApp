from fastapi import FastAPI

from .schemas import TaskOut

app = FastAPI()


@app.get("/")
async def main_page():
    return {"hello": "world"}


@app.get("/my-tasks/", response_model=dict[int, TaskOut])
async def get_all_tasks():
    return {1: TaskOut(title="First", description="My first task")}
