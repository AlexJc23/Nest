from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db

from app.dependencies.auth import get_current_user
from app.dependencies.permissions import required_role
from app.models.user import User
from app.models.branch import Branch
from app.models.group import Group
from app.models.group_member import GroupMembers
from app.models.post import Post
from app.models.comment import Comment
from app.models.event import Event
from app.models.event_attendee import EventAttendee
from app.models.reaction import Reaction
from app.models.post_image import PostImage

from app.schemas.v1.users import UserResponse, UserUpdate
from app.services import users_service

router = APIRouter(prefix="/users", tags=['users'])

@router.get("/me", response_model=UserResponse)
def get_me(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return users_service.get_user_by_id(db, current_user.id)

@router.put("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    user_in: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return users_service.update_user(
        db=db,
        acting_user_id=current_user.id,
        user_id=user_id,
        user_in=user_in
    )
@router.delete("/{user_id}")
def deactivate_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    users_service.delete_user(
        db=db,
        acting_user_id=current_user.id,
        user_id=user_id
    )
    return {"message: User deactivated"}
