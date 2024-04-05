from fastapi import FastAPI
from app.models.database import init_db
from app.api.main import api_router


server = FastAPI()

@server.on_event("startup")
def on_startup():
    init_db()

server.include_router(api_router)
