from fastapi import APIRouter
from .endpoints import profiles

api_v1_router = APIRouter()
api_v1_router.include_router(profiles.router, prefix="/profiles", tags=["User Profiles"])
