from sqlalchemy.orm import Session
from app.models.post import Post
from app.schemas.v1.posts import PostCreate, PostUpdate
from app.exceptions import AppException

def create_post(db: Session, post_in: PostCreate, owner_id: int) -> Post:
    # construct a Post ORM instance
    post = Post(
        content=post_in.content,
        owner_id=owner_id,
        type_of_post=post_in.type_of_post,
        group_id=post_in.group_id,
    )
    # add the post to the Session
    db.add(post)
    # commit the transaction
    db.commit()
    # refresh the post to load DB-generated fields
    db.refresh(post)
    # return the post
    return post

def get_post_by_id(db: Session, post_id: int) -> Post:
    # query the post by id
    # if not found, raise APPException
    # return the post
    post = db.query(Post).filter(Post.id == post_id, Post.is_deleted == False).first()
    if not post:
        raise AppException(
            code="POST_NOT_FOUND",
            message=f"Post with id {post_id} not found",
            status_code=404,
        )
    return post

def get_all_posts(db: Session, skip: int = 0, limit: int = 100) -> list[Post]:
    # query posts with pagination
    # return list of posts
    return db.query(Post).filter(Post.is_deleted == False).offset(skip).limit(limit).all()


def update_post(db: Session, post_id: int, post_in: PostUpdate) -> Post:
    # query the post by id
    post = db.query(Post).filter(Post.id == post_id, Post.is_deleted == False).first()
    # if not found, raise APPException
    if not post:
        raise AppException(
            code="POST_NOT_FOUND",
            message=f"Post with id {post_id} not found",
            status_code=404,
        )
    # update the post fields if provided in post_in
    if post_in.content is not None:
        post.content = post_in.content
    if post_in.group_id is not None:
        post.group_id = post_in.group_id
    if post_in.type_of_post is not None:
        post.type_of_post = post_in.type_of_post
    # commit the transaction
    db.commit()
    # refresh the post to load updated fields
    db.refresh(post)
    # return the post
    return post

def delete_post(db: Session, post_id: int) -> None:
    # query the post by id
    # if not found, raise APPException
    # mark the post as deleted (soft delete)
    # commit the transaction
    post = db.query(Post).filter(Post.id == post_id, Post.is_deleted == False).first()
    if not post:
        raise AppException(
            code="POST_NOT_FOUND",
            message=f"Post with id {post_id} not found",
            status_code=404,
        )
    post.is_deleted = True
    db.commit()
