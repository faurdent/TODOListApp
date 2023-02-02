from fastapi import FastAPI

from app.api.api_routes.api_register import api_router

app = FastAPI()

app.include_router(api_router)


@app.get("/")
async def main_page():
    return {"hello": "world"}
