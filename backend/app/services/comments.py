from sqlalchemy.orm import Session, selectinload
from app.models.comment import Comment
from app.models.post import Post
from app.schemas.v1.comments import CommentCreate, CommentUpdate
from app.exceptions import AppException

def create_comment(db: Session, comment_in: CommentCreate, owner_id: int, post_id: int) -> Comment:
    # construct a Comment ORM instance
    post = (db.query(Post).filter(Post.id == post_id, Post.is_deleted == False).first())
    if not post:
        raise AppException(
            code="POST_NOT_FOUND",
            message=f"Post with id {post_id} not found",
            status_code=404
        )

    comment = Comment(
        content=comment_in.content,
        owner_id=owner_id,
        post_id=post_id,
    )
    # add the comment to the Session
    db.add(comment)
    # commit the transaction
    db.commit()
    # refresh the comment to load DB-generated fields
    db.refresh(comment)
    # return the comment
    return comment

def get_comment_by_id(db: Session, comment_id: int) -> Comment:
    # query the comment by id
    # if not found, raise APPException
    # return the comment
    comment = db.query(Comment).filter(Comment.id == comment_id, Comment.is_deleted == False).first()
    if not comment:
        raise AppException(
            code="COMMENT_NOT_FOUND",
            message=f"Comment with id {comment_id} not found",
            status_code=404,
        )
    return comment

def get_comments_by_post_id(db: Session, post_id: int, skip: int = 0, limit: int = 50) -> list[Comment]:
    comments = (db.query(Comment).filter(Comment.post_id == post_id, Comment.is_deleted == False)).options(selectinload(Comment.owner)).offset(skip).limit(limit).all()
    return comments

def update_comment(db: Session, user_id: int, comment_id: int, comment_in: CommentUpdate) -> Comment:
    # query the comment by id
    comment = db.query(Comment).filter(Comment.id == comment_id, Comment.is_deleted == False).first()
    # if not found, raise APPException
    if not comment:
        raise AppException(
            code="COMMENT_NOT_FOUND",
            message=f"Comment with id {comment_id} not found",
            status_code=404,
        )
    if comment.owner_id != user_id:
        raise AppException(
            code="NOT_AUTHORIZED",
            message="YOU ARE NOT PERMITTED TO EDIT THIS COMMENT",
            status_code=403
        )
    # update the comment fields if provided in comment_in
    if comment_in.content is not None:
        comment.content = comment_in.content
    # commit the transaction
    db.commit()
    # refresh the comment to load updated fields
    db.refresh(comment)
    # return the updated comment
    return comment

def delete_comment(db: Session, user_id: int, comment_id: int) -> None:
    # query the comment by id
    comment = db.query(Comment).filter(Comment.id == comment_id, Comment.is_deleted == False).first()
    # if not found, raise APPException
    if not comment:
        raise AppException(
            code="COMMENT_NOT_FOUND",
            message=f"Comment with id {comment_id} not found",
            status_code=404,
        )
    if comment.owner_id != user_id:
        raise AppException(
            code="NOT_AUTHORIZED",
            message="YOU ARE NOT PERMITTED TO DELETE THIS COMMENT",
            status_code=403
        )
    # mark the comment as deleted
    comment.is_deleted = True
    # commit the transaction
    db.commit()
