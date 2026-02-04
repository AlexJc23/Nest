from fastapi import Depends
from app.schemas.users import UserResponse
from app.exceptions import AppException
from app.dependencies.auth import get_authenticated_user

def required_role(required_role: str):
    def checker(
        user: UserResponse = Depends(get_authenticated_user),
    ) -> UserResponse:
        if user.role != required_role:
            raise AppException(
                code="NOT_AUTHORIZED",
                message="Forbidden",
                status_code=403,
            )
        return user

    return checker
