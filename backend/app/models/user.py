from typing import TYPE_CHECKING
from sqlalchemy import String, Boolean, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.branch import Branch
    from app.models.post import Post
    from app.models.group import Group
    from app.models.comment import Comment
    from app.models.reaction import Reaction
    from app.models.event import Event

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    last_name: Mapped[str] = mapped_column(String, nullable=False)
    title: Mapped[str] = mapped_column(String, nullable=True)
    profile_img_url: Mapped[str] = mapped_column(String, nullable=True)
    google_chat_email: Mapped[str] = mapped_column(String, nullable=True)
    role: Mapped[str] = mapped_column(String, default="user", nullable=False)
    driving_score: Mapped[int] = mapped_column(nullable=True)
    nps_score: Mapped[int] = mapped_column(nullable=True)
    branch_id: Mapped[int] = mapped_column(ForeignKey("branches.id"), nullable=True, index=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    # Relationship to Branch model
    branch: Mapped["Branch"] = relationship("Branch", back_populates="users")
    posts: Mapped[list["Post"]] = relationship("Post", back_populates="owner",cascade="all, delete-orphan")
    owned_groups: Mapped[list["Group"]] = relationship("Group", back_populates="owner")
    comments: Mapped[list["Comment"]] = relationship("Comment", back_populates="owner", cascade="all, delete-orphan")
    reactions: Mapped[list["Reaction"]] = relationship("Reaction", back_populates="owner", cascade="all, delete-orphan")
    events: Mapped[list["Event"]] = relationship("Event", back_populates="owner", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<User id={self.id} email={self.email}>"
