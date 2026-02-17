from sqlalchemy.orm import Session
from app.db.database import get_db, SessionLocal
from app.models import User
from typing import Optional
from fastapi import Header, Depends
from app.schemas.v1.users import UserResponse
from app.exceptions import AppException
from datetime import datetime

def get_current_user(
    x_token: Optional[str] = Header(default=None),
    db: Session = Depends(get_db),
) -> User:

    if not x_token or not x_token.startswith("user-"):
        raise AppException(
            code="UNAUTHORIZED",
            message="Invalid tokens",
            status_code=401
        )

    user_id = int(x_token.split("-")[1])
    user = db.query(User).filter(User.id == user_id).first()


    if not user:
        raise AppException(
            code="USER_NOT_FOUND",
            message="Authenticated user not found",
            status_code=404,
        )

    if not user.is_active:
        raise AppException(
            code="FORBIDDEN",
            message="User account is inactive",
            status_code=403,
        )

    return user


def get_authenticated_user(
    user: UserResponse = Depends(get_current_user),
) -> UserResponse:
    return user
