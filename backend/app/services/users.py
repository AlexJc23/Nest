from app.domain.user import UserModel
from app.schemas.v1.users import UserResponse

def get_user_by_token(token: str) -> UserResponse:
    # Dummy implementation for example purposes
    fake_db_user = UserModel(
        id=1,
        hashed_password="hashedpassword",
        email="fake@example.com",
        first_name="Fake",
        last_name="User",
        role="admin",
        is_active=True
    )
    return UserResponse.from_model(fake_db_user)
