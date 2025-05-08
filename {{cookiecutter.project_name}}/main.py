"""Main application module."""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from api.main import router
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

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", include_in_schema=False)
async def root_redirect():
    """Redirect root path to docs."""
    return RedirectResponse(url="/docs")


app.include_router(router, prefix="/api")

logger.info(f"Application {settings.app_name} initialized")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
