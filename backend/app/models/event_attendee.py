# from typing import TYPE_CHECKING
from sqlalchemy import DateTime, func, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base

class EventAttendee(Base):
    __tablename__ = "event_attendees"

    __table_args__ = (
        UniqueConstraint("event_id", "user_id", name="uq_event_user"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id"), nullable=False, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, index=True)
    responded_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    def __repr__(self) -> str:
        return f"<EventAttendee id={self.id} event_id={self.event_id} user_id={self.user_id}>"
