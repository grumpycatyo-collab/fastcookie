"""API routes."""
from fastapi import APIRouter

from .health import router as healthcheck_router
from .version import router as version_router
from routes.cookies import router as cookies_router

router = APIRouter()

router.include_router(healthcheck_router)
router.include_router(version_router)
router.include_router(cookies_router) # Example of routes usage