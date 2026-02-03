from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    title: Optional[str]
    first_name: str
    last_name: str
    role: str
    driving_score: Optional[int]
    nps_score: Optional[int]
    branch_id: int
    profile_img_url: Optional[str]
    google_chat_email: Optional[str]
    is_active: bool
    created_at: datetime
    updated_at: datetime


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    title: Optional[str]
    first_name: str
    last_name: str
    profile_img_url: Optional[str]
    google_chat_email: Optional[str]

