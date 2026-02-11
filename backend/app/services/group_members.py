from sqlalchemy.orm import Session
from app.models.group import Group
from app.models.user import User
from app.models.group_members import GroupMembers
from app.exceptions import AppException


def add_user_to_group(
    db: Session,
    acting_user_id: int,
    group_id: int,
) -> GroupMembers:

    group = db.query(Group).filter(Group.id == group_id).first()
    if not group:
        raise AppException(
            code="GROUP_NOT_FOUND",
            message=f"Group with id {group_id} not found",
            status_code=404,
        )

    existing = (
        db.query(GroupMembers)
        .filter(
            GroupMembers.group_id == group_id,
            GroupMembers.user_id == acting_user_id,
        )
        .first()
    )
    if existing:
        raise AppException(
            code="ALREADY_MEMBER",
            message="You are already a member of this group",
            status_code=400,
        )

    membership = GroupMembers(
        group_id=group_id,
        user_id=acting_user_id,
    )

    db.add(membership)
    db.commit()
    db.refresh(membership)

    return membership


def remove_user_from_group(
    db: Session,
    acting_user_id: int,
    group_id: int,
) -> None:

    membership = (
        db.query(GroupMembers)
        .filter(
            GroupMembers.group_id == group_id,
            GroupMembers.user_id == acting_user_id,
        )
        .first()
    )

    if not membership:
        raise AppException(
            code="MEMBERSHIP_NOT_FOUND",
            message="You are not a member of this group",
            status_code=404,
        )

    db.delete(membership)
    db.commit()

