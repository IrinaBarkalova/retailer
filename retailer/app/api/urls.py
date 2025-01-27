from fastapi import APIRouter, FastAPI

from .auth.controllers import router as auth_router
from .profile.controllers import router as profile_router


_router = APIRouter(
    prefix="/api",
    tags=["root"],
)


def setup_routes(app: FastAPI):
    _router.include_router(auth_router)
    _router.include_router(profile_router)
    app.include_router(_router)
