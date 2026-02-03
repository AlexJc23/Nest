from fastapi import Depends, HTTPException, status
from app.dependencies.auth import get_current_user
from app.schemas.users import UserResponse

def required_role(required_role: str):
    def role_checker(user: UserResponse = Depends(get_current_user)):
        if user.role != required_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions"
            )
        return user
    return role_checker
