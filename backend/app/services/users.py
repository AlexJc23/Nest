from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.v1.users import UserCreate
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
