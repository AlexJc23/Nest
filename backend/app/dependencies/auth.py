from typing import Optional
from fastapi import Header, Depends
from app.schemas.v1.users import UserResponse
from app.exceptions import AppException
from datetime import datetime

def get_current_user(
    x_token: Optional[str] = Header(default=None),
) -> UserResponse:
    if x_token != "secret":
        raise AppException(
            code="UNAUTHORIZED",
            message="Invalid or missing authentication token",
            status_code=401,
        )

    # Placeholder user (Phase 3 auth skeleton)
    return UserResponse(
        id=1,
        email="placeholder@example.com",
        first_name="Placeholder",
        last_name="User",
        role="user",
        branch_id=None,
        is_active=True,
        driving_score=None,
        nps_score=None,
        profile_img_url=None,
        google_chat_email=None,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )


def get_authenticated_user(
    user: UserResponse = Depends(get_current_user),
) -> UserResponse:
    return user
