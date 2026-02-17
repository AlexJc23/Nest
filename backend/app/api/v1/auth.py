from fastapi import APIRouter, Depends
from app.schemas.v1.auth import LoginRequest, LoginResponse
from app.services.auth_services import login_user
from sqlalchemy.orm import Session
from app.db.database import get_db


router = APIRouter(prefix="/v1/auth", tags=["auth"])

@router.post("/login", response_model=LoginResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    return login_user(db, payload)
