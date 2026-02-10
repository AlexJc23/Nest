from sqlalchemy.orm import Session
from app.models.event_attendee import EventAttendee
from models.user import User
from models.event import Event
from app.schemas.v1.event_attendees import EventAttendeeCreate
from app.exceptions import AppException

def add_user_to_event_attending(db:Session, event_id: int, user_id: int) -> EventAttendee:
    event = db.query(Event).filter(Event.id == event_id).first()

    if not event:
        raise AppException(
            code="EVENT_NOT_FOUND",
            message=f"Event with id {event_id} not found",
            status_code=404
        )

    
