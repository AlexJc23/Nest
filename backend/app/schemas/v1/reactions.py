from pydantic import BaseModel, ConfigDict
from datetime import datetime

class ReactionCreate(BaseModel):
    name: str

class ReactionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str | None
    post_id: int
    comment_id: int | None
    owner_id: int
    created_at: datetime
    updated_at: datetime
