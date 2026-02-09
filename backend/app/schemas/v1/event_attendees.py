from pydantic import BaseModel
from datetime import datetime

class EventAttendeeCreate(BaseModel):
    pass


class EventAttendeeResponse(BaseModel):
    id: int
    user_id: int
    event_id: int
    responded_at: datetime
