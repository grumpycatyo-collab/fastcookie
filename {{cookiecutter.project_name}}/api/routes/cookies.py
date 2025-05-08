from fastapi import APIRouter

router = APIRouter(tags=["cookies"])

""" Example endpoint to get `cookies`. """


@router.get("/cookies")
async def get_cookies():
    """Get cookies."""
    return {"cookies": ["cookie1", "cookie2", "cookie3"]}
