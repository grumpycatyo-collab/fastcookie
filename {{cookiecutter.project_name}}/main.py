"""Main application module."""
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from api.routes import router
from core.config import get_settings
from core.logger import logger

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Handle startup and shutdown events.

    Args:
        app: FastAPI application
    """
    # Startup
    logger.info("Starting up application")
    yield
    # Shutdown
    logger.info("Shutting down application")


app = FastAPI(
    title=settings.app_name,
    description=settings.app_description,
    debug=settings.debug,
    lifespan=lifespan,
)


# @app.middleware("http")
# async def log_requests(request: Request, call_next):
#     """Log all requests with endpoint path and method."""
#     logger.info(f"Request: {request.method} {request.url.path}")
#     response = await call_next(request)
#     logger.info(f"Response: {request.method} {request.url.path} - Status: {response.status_code}")
#     return response

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(router, prefix="/api")

logger.info(f"Application {settings.app_name} initialized")