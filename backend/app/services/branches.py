from sqlalchemy.orm import Session
from app.models.branch import Branch
from app.schemas.v1.branches import BranchCreate, BranchUpdate
from app.exceptions import AppException

def create_branch(db: Session, branch_in: BranchCreate) -> Branch:
    branch = Branch(
        name=branch_in.name,
        location=branch_in.location
    )

    db.add(branch)
    db.commit()
    db.refresh(branch)
    return branch

def get_branch_by_id(db: Session, branch_id: int) -> Branch:
    branch = db.query(Branch).filter(Branch.id == branch_id).first()

    if not branch:
        raise AppException(
            code="BRANCH_NOT_FOUND",
            message=f"Branch with id {branch_id} not found",
            status_code=404
        )
    return branch

def get_all_branches(db: Session) -> list[Branch]:
    return db.query(Branch).all()



def update_branch(db: Session, branch_id: int, branch_in: BranchUpdate) -> Branch:
    branch = db.query(Branch).filter(Branch.id == branch_id).first()

    if not branch:
        raise AppException(
            code="BRANCH_NOT_FOUND",
            message=f"Branch with id {branch_id} not found",
            status_code=404
        )

    if branch_in.name is not None:
        branch.name = branch_in.name
    if branch_in.location is not None:
        branch.location = branch_in.location

    db.commit()
    db.refresh(branch)
    return branch

def delete_branch(db: Session, branch_id: int) -> None:
    branch = db.query(Branch).filter(Branch.id == branch_id).first()

    if not branch:
        raise AppException(
            code= "BRANCH_NOT_FOUND",
            message=f"Branch with id {branch_id} not found",
            status_code=404
        )
    db.delete(branch)
    db.commit()
