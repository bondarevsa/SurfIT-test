from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    password: str


class UserCreate(UserBase):
    email: EmailStr


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    username: str


class TokenBase(BaseModel):
    access_token: str
    token_type: str
