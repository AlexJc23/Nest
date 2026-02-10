from sqlalchemy.orm import Session
from app.models.post_image import PostImage
from app.models.post import Post
from app.exceptions import AppException
from app.schemas.v1.post_images import PhotoImageCreate, PhotoImageUpdate

def create_post_image(db: Session, post_id: int, image_data: PhotoImageCreate) -> PostImage:
    post = (
        db.query(Post)
        .filter(Post.id == post_id)
        .first()
    )
    if not post:
        raise AppException(
            code="POST_NOT_FOUND",
            message=f"Post with id {post_id} not found",
            status_code=404,
        )

    post_image = PostImage(
        post_id=post_id,
        image_url=image_data.image_url,
    )

    db.add(post_image)
    db.commit()
    db.refresh(post_image)

    return post_image

def update_post_image(db: Session, image_id: int, image_data: PhotoImageUpdate) -> PostImage:
    post_image = db.query(PostImage).filter(PostImage.id == image_id).first()
    if not post_image:
        raise AppException(
            code="POST_IMAGE_NOT_FOUND",
            message=f"Post image with id {image_id} not found",
            status_code=404,
        )

    if image_data.image_url is not None:
        post_image.image_url = image_data.image_url

    db.commit()
    db.refresh(post_image)

    return post_image

def delete_post_image(db: Session, image_id: int) -> None:
    post_image = db.query(PostImage).filter(PostImage.id == image_id).first()
    if not post_image:
        raise AppException(
            code="POST_IMAGE_NOT_FOUND",
            message=f"Post image with id {image_id} not found",
            status_code=404,
        )

    db.delete(post_image)
    db.commit()
