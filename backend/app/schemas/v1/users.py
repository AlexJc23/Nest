from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    title: Optional[str] = None
    profile_img_url: Optional[str] = None
    google_chat_email: Optional[str] = None

class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    title: Optional[str] = None
    profile_img_url: Optional[str] = None


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    email: EmailStr
    first_name: str
    last_name: str
    title: Optional[str] = None
    role: str
    branch_id: Optional[int] = None
    is_active: bool
    driving_score: Optional[int] = None
    nps_score: Optional[int] = None
    profile_img_url: Optional[str] = None
    google_chat_email: Optional[str] = None
    created_at: datetime
    updated_at: datetime
