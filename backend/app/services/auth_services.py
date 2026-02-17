from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import verify_password
from app.exceptions import AppException
from app.schemas.v1.auth import LoginResponse, LoginRequest


def login_user(db: Session, payload: LoginRequest) -> LoginResponse:

    user = db.query(User).filter(User.email == payload.email).first()

    if not user:
        raise AppException(
            code="INVALID_CREDENTIALS",
            message="Invalid email or password",
            status_code=401,
        )

    if not verify_password(payload.password, user.hashed_password):
        raise AppException(
            code="INVALID_CREDENTIALS",
            message="Invalid email or password",
            status_code=401,
        )

    if not user.is_active:
        raise AppException(
            code="FORBIDDEN",
            message="User account is inactive",
            status_code=403,
        )

    # temporary fake token encoding identity
    token = f"user-{user.id}"

    return LoginResponse(
        access_token=token,
        token_type="bearer",
    )
