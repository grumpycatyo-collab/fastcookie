"""Version endpoint."""
from fastapi import APIRouter

import {{cookiecutter.project_slug}}

router = APIRouter(tags=["version"])


@router.get("/version", status_code=200)
async def version():
    """Return the API version."""
    return {"version": {{cookiecutter.project_slug}}.__version__}
