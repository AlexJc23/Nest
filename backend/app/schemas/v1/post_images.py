from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PhotoImageCreate(BaseModel):
    image_url: str

class PhotoImageUpdate(BaseModel):
    image_url: Optional[str] = None

class PhotoImageResponse(BaseModel):
    id: int
    image_url: str
    post_id: int
    created_at: datetime
    updated_at: datetime
