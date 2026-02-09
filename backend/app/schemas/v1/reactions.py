from pydantic import BaseModel
from datetime import datetime

class ReactionCreate(BaseModel):
    name: str

class ReactionResponse(BaseModel):
    id: int
    name: str | None
    post_id: int
    comment_id: int | None
    owner_id: int
    created_at: datetime
    updated_at: datetime
