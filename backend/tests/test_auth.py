import pytest
from app.dependencies.auth import get_current_user
from app.exceptions import AppException

def test_get_current_user_invalid_token():
    with pytest.raises(AppException):
        get_current_user(x_token="invalid_token")

def test_get_current_user_valid_token():
    user = get_current_user(x_token="secret")
    assert user.role == "admin"
