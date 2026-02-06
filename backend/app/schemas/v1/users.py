from app.domain.user import UserModel
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    title: Optional[str] = None
    first_name: str
    last_name: str
    role: str
    driving_score: Optional[int] = None
    nps_score: Optional[int] = None
    branch_id: int
    profile_img_url: Optional[str] = None
    google_chat_email: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


    @classmethod
    def from_model(cls, user: UserModel):
        return cls(
            id=user.id,
            email=user.email,
            title=user.title,
            first_name=user.first_name,
            last_name=user.last_name,
            role=user.role,
            driving_score=user.driving_score,
            nps_score=user.nps_score,
            branch_id=user.branch_id,
            profile_img_url=user.profile_img_url,
            google_chat_email=user.google_chat_email,
            is_active=user.is_active,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    title: Optional[str]
    first_name: str
    last_name: str
    profile_img_url: Optional[str]
    google_chat_email: Optional[str]
