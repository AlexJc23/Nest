from sqlalchemy.orm import Session
from app.models.reaction import Reaction
from app.models.post import Post
from app.models.comment import Comment
from app.exceptions import AppException


def add_reaction(
    db: Session,
    owner_id: int,
    name: str,
    post_id: int | None = None,
    comment_id: int | None = None,
) -> Reaction:
    # validate exactly one target
    if (post_id is None and comment_id is None) or (
        post_id is not None and comment_id is not None
    ):
        raise AppException(
            code="INVALID_TARGET",
            message="Reaction must target exactly one of post or comment",
            status_code=400,
        )

    # ensure target exists
    if post_id is not None:
        target_exists = db.query(Post).filter(Post.id == post_id).first()
        if not target_exists:
            raise AppException(
                code="POST_NOT_FOUND",
                message=f"Post with id {post_id} not found",
                status_code=404,
            )
    else:
        target_exists = db.query(Comment).filter(Comment.id == comment_id).first()
        if not target_exists:
            raise AppException(
                code="COMMENT_NOT_FOUND",
                message=f"Comment with id {comment_id} not found",
                status_code=404,
            )

    # enforce uniqueness
    existing = (
        db.query(Reaction)
        .filter(
            Reaction.owner_id == owner_id,
            Reaction.post_id == post_id,
            Reaction.comment_id == comment_id,
        )
        .first()
    )
    if existing:
        raise AppException(
            code="ALREADY_REACTED",
            message="User has already reacted to this target",
            status_code=400,
        )

    # create reaction
    reaction = Reaction(
        owner_id=owner_id,
        name=name,
        post_id=post_id,
        comment_id=comment_id,
    )

    db.add(reaction)
    db.commit()
    db.refresh(reaction)
    return reaction


def remove_reaction(
    db: Session,
    owner_id: int,
    post_id: int | None = None,
    comment_id: int | None = None,
) -> None:
    # validate target
    if (post_id is None and comment_id is None) or (
        post_id is not None and comment_id is not None
    ):
        raise AppException(
            code="INVALID_TARGET",
            message="Reaction must target exactly one of post or comment",
            status_code=400,
        )

    reaction = (
        db.query(Reaction)
        .filter(
            Reaction.owner_id == owner_id,
            Reaction.post_id == post_id,
            Reaction.comment_id == comment_id,
        )
        .first()
    )

    if not reaction:
        raise AppException(
            code="REACTION_NOT_FOUND",
            message="Reaction does not exist",
            status_code=404,
        )

    db.delete(reaction)
    db.commit()
