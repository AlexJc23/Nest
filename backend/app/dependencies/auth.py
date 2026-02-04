from typing import Optional
from fastapi import Header, HTTPException, status, Depends
from app.models.user import UserModel
from app.schemas.users import UserResponse
from app.services.users import get_user_by_token
from app.exceptions import AppException

def get_current_user(x_token: Optional[str] = Header(default=None)) -> UserResponse:
    print("AUTH FUNC ID:", id(get_current_user))

    if x_token != "secret":
        raise AppException(
            code="UNAUTHORIZED",
            message="Invalid or missing authentication token",
            status_code=401
        )


    return get_user_by_token(x_token)

def get_authenticated_user(
    user: UserResponse = Depends(get_current_user),
) -> UserResponse:
    return user
