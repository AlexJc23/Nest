from typing import TYPE_CHECKING, Optional
from sqlalchemy import String, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.group import Group
    from app.models.post_image import PostImage
    from app.models.comment import Comment
    from app.models.reaction import Reaction

class Post(Base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(primary_key=True)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, index=True)
    content: Mapped[str] = mapped_column(String, nullable=False)
    group_id: Mapped[Optional[int]] = mapped_column(ForeignKey("groups.id"), nullable=True, index=True)
    type_of_post: Mapped[str] = mapped_column(String, nullable=False)
    is_deleted: Mapped[bool] = mapped_column(default=False, nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    # Relationships can be defined here if needed
    owner: Mapped["User"] = relationship("User", back_populates="posts")
    group: Mapped[Optional["Group"]] = relationship("Group", back_populates="posts")
    images: Mapped[list["PostImage"]] = relationship("PostImage", back_populates="post", cascade="all, delete-orphan")
    comments: Mapped[list["Comment"]] = relationship("Comment", back_populates="post", cascade="all, delete-orphan")
    reactions: Mapped[list["Reaction"]] = relationship("Reaction", back_populates="post", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<Post id={self.id} owner_id={self.owner_id}>"
