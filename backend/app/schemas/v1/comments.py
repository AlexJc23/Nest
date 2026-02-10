from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class CommentCreate(BaseModel):
    content: str


class CommentUpdate(BaseModel):
    content: Optional[str] = None

class CommentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    content: str
    owner_id: int
    post_id: int
    created_at: datetime
    updated_at: datetime
