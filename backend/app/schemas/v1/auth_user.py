from pydantic import BaseModel, EmailStr

class AuthUser(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    last_name: str
    role: str
    is_active: bool
