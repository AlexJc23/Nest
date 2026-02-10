from sqlalchemy.orm import Session
from app.models.event import Event
from app.schemas.v1.events import EventCreate, EventUpdate
from app.exceptions import AppException

def create_event(db: Session, event_in: EventCreate, owner_id: int) -> Event:

    # construct an Event ORM instance
    event = Event(
        title=event_in.title,
        description=event_in.description,
        location=event_in.location,
        start_time=event_in.start_time,
        end_time=event_in.end_time,
        owner_id=owner_id,
        branch_id=event_in.branch_id,

    )
    # add the event to the Session
    db.add(event)
    # commit the transaction
    db.commit()
    # refresh the event to load DB-generated fields
    db.refresh(event)
    # return the event
    return event

def get_event_by_id(db: Session, event_id: int) -> Event:
    # query the event by id
    # if not found, raise APPException
    # return the event
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise AppException(
            code="EVENT_NOT_FOUND",
            message=f"Event with id {event_id} not found",
            status_code=404,

        )
    return event

def get_all_events(db: Session, skip: int = 0, limit: int = 100) -> list[Event]:
    # query events with pagination
    # return list of events
    return db.query(Event).offset(skip).limit(limit).all()

def update_event(db: Session, event_id: int, event_in: EventUpdate) -> Event:
    # query the event by id
    event = db.query(Event).filter(Event.id == event_id).first()
    # if not found, raise APPException
    if not event:
        raise AppException(
            code="EVENT_NOT_FOUND",
            message=f"Event with id {event_id} not found",
            status_code=404,
        )
    # update the event fields if provided in event_in
    if event_in.title is not None:
        event.title = event_in.title
    if event_in.description is not None:
        event.description = event_in.description
    if event_in.location is not None:
        event.location = event_in.location
    if event_in.start_time is not None:
        event.start_time = event_in.start_time
    if event_in.end_time is not None:
        event.end_time = event_in.end_time
    if event_in.branch_id is not None:
        event.branch_id = event_in.branch_id
    # commit the transaction
    db.commit()
    # refresh the event to load updated fields
    db.refresh(event)
    # return the updated event
    return event

def delete_event(db: Session, event_id: int) -> None:
    # query the event by id
    event = db.query(Event).filter(Event.id == event_id).first()
    # if not found, raise APPException
    if not event:
        raise AppException(
            code="EVENT_NOT_FOUND",
            message=f"Event with id {event_id} not found",
            status_code=404,
        )
    # delete the event
    db.delete(event)
    # commit the transaction
    db.commit()
