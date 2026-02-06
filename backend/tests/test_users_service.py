from app.services.users import get_user_by_token
from app.schemas.v1.users import UserResponse

def test_get_current_user_valid_token():
    user = get_user_by_token("secret")

    assert isinstance(user, UserResponse)
    assert user.id == 1
    assert user.role == "admin"
