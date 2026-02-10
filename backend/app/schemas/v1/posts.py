from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class PostCreate(BaseModel):
    content: str
    group_id: Optional[int] = None # None = company-wide feed
    type_of_post: str # e.g. "announcement", "DT Update", "general"

class PostUpdate(BaseModel):
    content: Optional[str] = None
    group_id: Optional[int] = None
    type_of_post: Optional[str] = None

class PostResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    content: str
    owner_id: int
    group_id: Optional[int] = None
    type_of_post: str
    created_at: datetime
    updated_at: datetime
