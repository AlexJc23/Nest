from typing import Optional
from fastapi import Header, HTTPException, status
from app.schemas.auth_user import AuthUser

def get_current_user(x_token: Optional[str] = Header(default=None)) -> AuthUser:
    if x_token != "secret":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated"
        )

    return AuthUser(
        id=1,
        email="fake@example.com",
        role="admin",
        is_active=True
    )
