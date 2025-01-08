from pydantic import BaseModel, UUID4
from typing import Optional, Any

# User Schemas
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: UUID4

    class Config:
        orm_mode = True