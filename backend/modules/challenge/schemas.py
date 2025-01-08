from pydantic import BaseModel, UUID4
from typing import Optional, Any

class ChallengeBase(BaseModel):
    user_id: UUID4
    name: str
    collection: str
    rarity: str
    description: str
    reward: str
    additional_info: Optional[Any] = None

class ChallengeCreate(ChallengeBase):
    pass

class ChallengeUpdate(BaseModel):
    name: Optional[str]
    collection: Optional[str]
    rarity: Optional[str]
    description: Optional[str]
    reward: Optional[str]
    additional_info: Optional[Any]

class ChallengeResponse(ChallengeBase):
    id: UUID4

    class Config:
        orm_mode = True
