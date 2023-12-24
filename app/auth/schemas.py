from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    id: int
    email: EmailStr
    username: str
    is_admin: bool
