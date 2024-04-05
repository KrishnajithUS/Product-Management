from fastapi import APIRouter

from app.api.routers import products


api_router = APIRouter()


api_router.include_router(products.router)