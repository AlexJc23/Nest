from pydantic import BaseModel, ConfigDict
from datetime import datetime

class EventAttendeeCreate(BaseModel):
    pass


class EventAttendeeResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    user_id: int
    event_id: int
    responded_at: datetime
