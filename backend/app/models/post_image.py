from typing import TYPE_CHECKING
from sqlalchemy import String, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base

if TYPE_CHECKING:
    from app.models.post import Post

class PostImage(Base):
    __tablename__ = "post_images"
    id: Mapped[int] = mapped_column(primary_key=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"), nullable=False, index=True)
    image_url: Mapped[str] = mapped_column(String(2048), nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)


    # Relationships can be defined here if needed
    post: Mapped["Post"] = relationship("Post", back_populates="images")

    def __repr__(self) -> str:
        return f"<PostImage id={self.id} post_id={self.post_id}>"
