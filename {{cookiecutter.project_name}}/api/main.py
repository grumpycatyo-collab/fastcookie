"""API routes."""
from fastapi import APIRouter

from .health import router as health_router
from routes.cookies import router as cookies_router

router = APIRouter()

router.include_router(health_router)
router.include_router(cookies_router) # Example of routes usage