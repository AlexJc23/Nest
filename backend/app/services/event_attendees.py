from sqlalchemy.orm import Session
from app.models.event_attendee import EventAttendee
from app.models.user import User
from app.models.event import Event
from app.exceptions import AppException


def add_user_to_event_attending(
    db: Session,
    event_id: int,
    user_id: int,
) -> EventAttendee:

    # Ensure event exists
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise AppException(
            code="EVENT_NOT_FOUND",
            message=f"Event with id {event_id} not found",
            status_code=404,
        )

    # Ensure user exists
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise AppException(
            code="USER_NOT_FOUND",
            message=f"User with id {user_id} not found",
            status_code=404,
        )

    # Prevent duplicate attendance
    existing = (
        db.query(EventAttendee)
        .filter(
            EventAttendee.event_id == event_id,
            EventAttendee.user_id == user_id,
        )
        .first()
    )
    if existing:
        raise AppException(
            code="ALREADY_ATTENDING",
            message="User is already attending this event",
            status_code=400,
        )

    attendance = EventAttendee(
        event_id=event_id,
        user_id=user_id,
    )

    db.add(attendance)
    db.commit()
    db.refresh(attendance)

    return attendance


def remove_user_attendance(
    db: Session,
    event_id: int,
    user_id: int,
) -> None:

    attendance = (
        db.query(EventAttendee)
        .filter(
            EventAttendee.event_id == event_id,
            EventAttendee.user_id == user_id,
        )
        .first()
    )

    if not attendance:
        raise AppException(
            code="ATTENDANCE_NOT_FOUND",
            message="User is not attending this event",
            status_code=404,
        )

    db.delete(attendance)
    db.commit()
