"""Health check endpoint."""

from fastapi import APIRouter, status

router = APIRouter(tags=["health"])


@router.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}


@router.get("/readiness", status_code=status.HTTP_200_OK)
async def readiness():
    """Readiness endpoint."""
    return {"status": "ready"}
