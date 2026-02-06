from fastapi import APIRouter
from app.schemas.v1.auth import LoginRequest, LoginResponse
from app.services.auth_services import login_user


router = APIRouter(prefix="/v1/auth", tags=["auth"])

@router.post("/login", response_model=LoginResponse)
def login(payload: LoginRequest):
    return login_user(payload)
