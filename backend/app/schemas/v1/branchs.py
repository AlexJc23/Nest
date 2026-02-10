from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


class BranchCreate(BaseModel):
    name: str
    location: str

class BranchUpdate(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None

class BranchResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    location: Optional[str] = None
    created_at: datetime
    updated_at: datetime
