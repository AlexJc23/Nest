from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class BranchCreate(BaseModel):
    name: str
    location: Optional[str] = None

class BranchUpdate(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None

class BranchResponse(BaseModel):
    id: int
    name: str
    location: Optional[str] = None
    created_at: datetime
    updated_at: datetime
