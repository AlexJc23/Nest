from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.v1.users import UserCreate, UserUpdate
from app.core.security import hash_password
from app.exceptions import AppException


def create_user(db: Session, user_in: UserCreate) -> User:
    # hash the plaintext password
    hashed_password = hash_password(user_in.password)
    # construct a User ORM instance
    user = User(
        email=user_in.email,
        first_name=user_in.first_name,
        last_name=user_in.last_name,
        title=user_in.title,
        profile_img_url=user_in.profile_img_url,
        google_chat_email=user_in.google_chat_email,
        hashed_password=hashed_password,
    )
    # add the user to the Session
    db.add(user)
    # commit the transaction
    db.commit()
    # refresh the user to load DB-generated fields
    db.refresh(user)
    # return the user
    return user

def get_user_by_id(db: Session, user_id: int) -> User:
    # query the user by id
    # if not found, raise APPException
    # return the user
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise AppException(
            code="USER_NOT_FOUND",
            message=f"User with id {user_id} not found",
            status_code=404,
        )
    return user

def get_user_by_email(db: Session, email: str) -> User:
    # query the user by email
    # if not found, raise APPException
    # return the user
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise AppException(
            code="USER_NOT_FOUND",
            message=f"User with email {email} not found",
            status_code=404,
        )
    return user

def update_user(
    db: Session,
    acting_user_id: int,
    user_id: int,
    user_in: UserUpdate,
) -> User:

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise AppException(
            code="USER_NOT_FOUND",
            message=f"User with id {user_id} not found",
            status_code=404,
        )

    if acting_user_id != user_id:
        raise AppException(
            code="FORBIDDEN",
            message="You are not authorized to update this user",
            status_code=403,
        )

    if user_in.first_name is not None:
        user.first_name = user_in.first_name
    if user_in.last_name is not None:
        user.last_name = user_in.last_name
    if user_in.title is not None:
        user.title = user_in.title
    if user_in.profile_img_url is not None:
        user.profile_img_url = user_in.profile_img_url

    db.commit()
    db.refresh(user)

    return user


def delete_user(
    db: Session,
    acting_user_id: int,
    user_id: int,
) -> None:

    # fetch acting user
    acting_user = db.query(User).filter(User.id == acting_user_id).first()
    if not acting_user:
        raise AppException(
            code="USER_NOT_FOUND",
            message=f"User with id {acting_user_id} not found",
            status_code=404,
        )

    # only admin allowed
    if acting_user.role != "admin":
        raise AppException(
            code="FORBIDDEN",
            message="Only admins can deactivate users",
            status_code=403,
        )

    # fetch target user
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise AppException(
            code="USER_NOT_FOUND",
            message=f"User with id {user_id} not found",
            status_code=404,
        )

    # prevent admin from deactivating themselves (optional but smart)
    if acting_user_id == user_id:
        raise AppException(
            code="INVALID_OPERATION",
            message="Admin cannot deactivate themselves",
            status_code=400,
        )

    user.is_active = False
    db.commit()
