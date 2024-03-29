from fastapi import APIRouter

from app.api.api_routes.endpoints import login, user, task

api_router = APIRouter()


api_router.include_router(login.router, tags=["login"])
api_router.include_router(task.router, prefix="/my-tasks", tags=["tasks"])
api_router.include_router(user.router, prefix="/users", tags=["users"])
