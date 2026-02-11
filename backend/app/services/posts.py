from sqlalchemy.orm import Session
from app.models.post import Post
from app.schemas.v1.posts import PostCreate, PostUpdate
from app.exceptions import AppException


def create_post(db: Session, post_in: PostCreate, owner_id: int) -> Post:
    # Create a new Post ORM object from validated input data
    # NOTE: owner_id is injected by the service caller (auth layer),
    # not trusted from client input
    post = Post(
        content=post_in.content,
        owner_id=owner_id,
        type_of_post=post_in.type_of_post,
        group_id=post_in.group_id,
    )

    # Stage the object for insertion into the database
    db.add(post)

    # Persist the transaction (INSERT happens here)
    db.commit()

    # Reload the object so DB-generated fields (id, timestamps) are populated
    db.refresh(post)

    # Return ORM object (schemas will handle serialization)
    return post


def get_post_by_id(db: Session, post_id: int) -> Post:
    # Fetch a single post that is NOT soft-deleted
    post = (
        db.query(Post)
        .filter(Post.id == post_id, Post.is_deleted == False)
        .first()
    )

    # Explicit error instead of returning None
    # Keeps service behavior predictable
    if not post:
        raise AppException(
            code="POST_NOT_FOUND",
            message=f"Post with id {post_id} not found",
            status_code=404,
        )

    return post


def get_all_posts(db: Session, skip: int = 0, limit: int = 100) -> list[Post]:
    # Returns a paginated list of all non-deleted posts
    # Used for general feeds
    return (
        db.query(Post)
        .filter(Post.is_deleted == False)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_all_posts_by_type(
    db: Session,
    type_of_post: str | None,
    skip: int = 0,
    limit: int = 100,
) -> list[Post]:
    # Returns posts filtered by a specific post type
    # Example: "announcement", "general"
    return (
        db.query(Post)
        .filter(
            Post.is_deleted == False,
            Post.type_of_post == type_of_post,
        )
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_posts_by_group_id(
    db: Session,
    group_id: int,
    skip: int = 0,
    limit: int = 100,
) -> list[Post]:
    # Used for group-specific feeds
    # Only returns posts that belong to the given group
    return (
        db.query(Post)
        .filter(
            Post.is_deleted == False,
            Post.group_id == group_id,
        )
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_posts_by_owner_id(
    db: Session,
    owner_id: int,
    skip: int = 0,
    limit: int = 100,
) -> list[Post]:
    # Used for user profile pages
    # Shows posts authored by a specific user
    return (
        db.query(Post)
        .filter(
            Post.is_deleted == False,
            Post.owner_id == owner_id,
        )
        .offset(skip)
        .limit(limit)
        .all()
    )


def update_post(db: Session, user_id: int, post_id: int, post_in: PostUpdate) -> Post:
    # Fetch the post first to ensure it exists and is mutable
    post = (
        db.query(Post)
        .filter(Post.id == post_id, Post.is_deleted == False)
        .first()
    )

    if not post:
        raise AppException(
            code="POST_NOT_FOUND",
            message=f"Post with id {post_id} not found",
            status_code=404,
        )
    if post.owner_id != user_id:
        raise AppException(
            code='UNAUTHORIZED',
            message='You are not permitted to edit this post',
            status_code=403
        )

    # Partial update pattern:
    # only overwrite fields explicitly provided
    if post_in.content is not None:
        post.content = post_in.content
    if post_in.group_id is not None:
        post.group_id = post_in.group_id
    if post_in.type_of_post is not None:
        post.type_of_post = post_in.type_of_post

    # Persist changes
    db.commit()

    # Refresh to reflect updated timestamps
    db.refresh(post)

    return post


def delete_post(db: Session, user_id: int, post_id: int) -> None:
    # Soft-delete instead of physical delete
    # Preserves history and relationships
    post = (
        db.query(Post)
        .filter(Post.id == post_id, Post.is_deleted == False)
        .first()
    )

    if not post:
        raise AppException(
            code="POST_NOT_FOUND",
            message=f"Post with id {post_id} not found",
            status_code=404,
        )
    if post.owner_id != user_id:
            raise AppException(
                code='UNAUTHORIZED',
                message='You are not permitted to edit this post',
                status_code=403
            )

    post.is_deleted = True
    db.commit()
