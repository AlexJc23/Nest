from sqlalchemy.orm import Session
from app.models.comment import Comment
from app.schemas.v1.comments import CommentCreate, CommentUpdate
from app.exceptions import AppException

def create_comment(db: Session, comment_in: CommentCreate, owner_id: int, post_id: int) -> Comment:
    # construct a Comment ORM instance
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

def update_comment(db: Session, comment_id: int, comment_in: CommentUpdate) -> Comment:
    # query the comment by id
    comment = db.query(Comment).filter(Comment.id == comment_id, Comment.is_deleted == False).first()
    # if not found, raise APPException
    if not comment:
        raise AppException(
            code="COMMENT_NOT_FOUND",
            message=f"Comment with id {comment_id} not found",
            status_code=404,
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

def delete_comment(db: Session, comment_id: int) -> None:
    # query the comment by id
    comment = db.query(Comment).filter(Comment.id == comment_id, Comment.is_deleted == False).first()
    # if not found, raise APPException
    if not comment:
        raise AppException(
            code="COMMENT_NOT_FOUND",
            message=f"Comment with id {comment_id} not found",
            status_code=404,
        )
    # mark the comment as deleted
    comment.is_deleted = True
    # commit the transaction
    db.commit()
