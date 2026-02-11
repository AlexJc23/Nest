# data contracts and validation for authentication-related operations

from pydantic import BaseModel, EmailStr

class LoginRequest(BaseModel):
    # Data contract for login request
    email: EmailStr
    password: str

class LoginResponse(BaseModel):
    # Data contract for login response
    access_token: str
    token_type: str = "bearer"
