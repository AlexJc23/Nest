from app.schemas.auth import LoginRequest, LoginResponse

def login_user(payload: LoginRequest) -> LoginResponse:
    # Here you would add the logic to authenticate the user
    # For demonstration, we return a dummy token
    return LoginResponse(
        access_token="dummy_token",
    )
