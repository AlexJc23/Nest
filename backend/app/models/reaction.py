from typing import TYPE_CHECKING
from sqlalchemy import String, DateTime, func, ForeignKey, CheckConstraint, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base

if TYPE_CHECKING:
    from app.models.post import Post
    from app.models.comment import Comment
    from app.models.user import User

class Reaction(Base):
    __tablename__ = "reactions"

    __table_args__ = (
    CheckConstraint(
        "(post_id IS NOT NULL AND comment_id IS NULL) OR "
        "(post_id IS NULL AND comment_id IS NOT NULL)",
        name="ck_reaction_single_target"
    ),
    UniqueConstraint(
        "owner_id",
        "post_id",
        "comment_id",
        "name",
        name="uq_reaction_owner_target_name"
    ),
)


    id: Mapped[int] = mapped_column(primary_key=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"), nullable=True, index=True)
    comment_id: Mapped[int] = mapped_column(ForeignKey("comments.id"), nullable=True, index=True)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, index=True)
    name: Mapped[str] = mapped_column(String, index=True, nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)


    # Relationships can be defined here if needed
    post = relationship("Post", back_populates="reactions")
    comment = relationship("Comment", back_populates="reactions")
    owner = relationship("User", back_populates="reactions")

    def __repr__(self) -> str:
        return f"<Reaction id={self.id} post_id={self.post_id} comment_id={self.comment_id} owner_id={self.owner_id}>"
