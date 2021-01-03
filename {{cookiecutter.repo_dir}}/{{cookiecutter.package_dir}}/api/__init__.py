from fastapi import APIRouter

from .dummy import router as dummy_router

api_router = APIRouter()

api_router.include_router(dummy_router, prefix="/dummies", tags=["dummies"])
