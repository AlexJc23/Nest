from fastapi import APIRouter, Depends, Request
from app.dependencies.auth import get_authenticated_user, get_current_user
from app.dependencies.permissions import required_role
from app.schemas.v1.users import UserResponse, UserCreate
from app.exceptions import AppException
from datetime import datetime

# user_router = APIRouter(prefix="/users", dependencies=[Depends(get_current_user)])
user_router = APIRouter(prefix="/v1/users")

@user_router.get("/me")
def read_me(user: UserResponse = Depends(get_authenticated_user)):
    return user


@user_router.post("/create", response_model=UserResponse)
def create_user(user_in: UserCreate):

    now = datetime.utcnow()

    fake_user = {
        "id": 2,
        "email": user_in.email,
        "password": user_in.password,
        "first_name": user_in.first_name,
        "last_name": user_in.last_name,
        "title": user_in.title,
        "profile_img_url": user_in.profile_img_url,
        "google_chat_email": user_in.google_chat_email,
        "driving_score": 100,
        "nps_score": 100,
        "branch_id": 1,

        # server-owned fields
        "role": "user",
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    return fake_user

@user_router.get("/admin-only")
def admin_only(
    user: UserResponse = Depends(required_role("admin")),
):
    return {"message": f"Welcome {user.first_name}!"}
