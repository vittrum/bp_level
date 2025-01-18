from pydantic import BaseModel, UUID4
from typing import Optional, Any


class RegisterUser(BaseModel):
    username: str
    full_name: str
    email: str
    password_first_time: str
    password_confirmation: str


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: UUID4

    class Config:
        orm_mode = True
