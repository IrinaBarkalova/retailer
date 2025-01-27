from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from app.dto.user import UserSchema
from app.services import AuthService
from .errors import InactiveAccountError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth.login")


async def get_current_user(
    token: str = Depends(oauth2_scheme), auth_service: AuthService = Depends()
) -> UserSchema:
    return await auth_service.get_current_user(token)


async def get_current_active_user(
    current_user: UserSchema = Depends(get_current_user),
) -> UserSchema:
    if not current_user.is_active:
        raise InactiveAccountError

    return current_user
