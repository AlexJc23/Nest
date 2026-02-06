import app.dependencies.auth as auth_module
from app.schemas.v1.users import UserResponse
from fastapi.testclient import TestClient
from app.main import create_app


def fake_user():
    return UserResponse(
        id=99,
        email="test@example.com",
        first_name="Test",
        last_name="User",
        role="admin",
        is_active=True,
        branch_id=99,
    )


app = create_app()

app.dependency_overrides[auth_module.get_authenticated_user] = fake_user
app.dependency_overrides[auth_module.get_current_user] = fake_user

client = TestClient(app)


def test_users_me(fake_user):
    app = create_app()

    # 🔥 THIS is the important line
    app.dependency_overrides[auth_module.get_authenticated_user] = lambda: fake_user

    client = TestClient(app)

    response = client.get("/users/me")
    assert response.status_code == 200
    assert response.json()["branch_id"] == 99


app.dependency_overrides.clear()
