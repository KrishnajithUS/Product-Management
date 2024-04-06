from fastapi import APIRouter

from app.api.routers import products, users, login


api_router = APIRouter()


api_router.include_router(products.router)
api_router.include_router(users.router)
api_router.include_router(login.router)
