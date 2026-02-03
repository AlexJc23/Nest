from pydantic import BaseModel, EmailStr

class AuthUser(BaseModel):
    id: int
    email: EmailStr
    role: str
    is_active: bool
