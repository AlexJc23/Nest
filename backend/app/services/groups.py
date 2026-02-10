from sqlalchemy.orm import Session
from app.models.group import Group
from app.schemas.v1.groups import GroupCreate, GroupUpdate
from app.exceptions import AppException

def create_group(db: Session, group_in: GroupCreate, owner_id: int) -> Group:
    # construct a Group ORM instance
    group = Group(
        name=group_in.name,
        description=group_in.description,
        owner_id=owner_id,
    )
    # add the group to the Session
    db.add(group)
    # commit the transaction
    db.commit()
    # refresh the group to load DB-generated fields
    db.refresh(group)
    # return the group
    return group

def get_group_by_id(db: Session, group_id: int) -> Group:
    # query the group by id
    # if not found, raise APPException
    # return the group
    group = db.query(Group).filter(Group.id == group_id).first()
    if not group:
        raise AppException(
            code="GROUP_NOT_FOUND",
            message=f"Group with id {group_id} not found",
            status_code=404,
        )
    return group

def get_all_groups(db: Session, skip: int = 0, limit: int = 100) -> list[Group]:
    # query all groups
    # return the list of groups
    return db.query(Group).offset(skip).limit(limit).all()

def update_group(db: Session, group_id: int, group_in: GroupUpdate) -> Group:
    # query the group by id
    group = db.query(Group).filter(Group.id == group_id).first()
    # if not found, raise APPException
    if not group:
        raise AppException(
            code="GROUP_NOT_FOUND",
            message=f"Group with id {group_id} not found",
            status_code=404,
        )
    # update the group fields if provided in group_in
    if group_in.name is not None:
        group.name = group_in.name
    if group_in.description is not None:
        group.description = group_in.description
    # commit the transaction
    db.commit()
    # refresh the group to load updated fields
    db.refresh(group)
    # return the updated group
    return group


def delete_group(db: Session, group_id: int) -> None:
    # query the group by id
    group = db.query(Group).filter(Group.id == group_id).first()
    # if not found, raise APPException
    if not group:
        raise AppException(
            code="GROUP_NOT_FOUND",
            message=f"Group with id {group_id} not found",
            status_code=404,
        )
    # delete the group
    db.delete(group)
    # commit the transaction
    db.commit()
