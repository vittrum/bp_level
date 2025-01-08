from typing import Type

from sqlalchemy.orm import Session
from modules.challenge.models import Challenge
from modules.challenge.schemas import ChallengeCreate, ChallengeUpdate
from uuid import UUID


class ChallengeRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_challenge(self, challenge_id: UUID) -> Type[Challenge] | None:
        return self.db.query(Challenge).filter(Challenge.id == challenge_id).first()

    def get_challenges(self, skip: int = 0, limit: int = 10):
        return self.db.query(Challenge).offset(skip).limit(limit).all()

    def create_challenge(self, challenge: ChallengeCreate) -> Challenge:
        db_challenge = Challenge(**challenge.dict())
        self.db.add(db_challenge)
        self.db.commit()
        self.db.refresh(db_challenge)
        return db_challenge

    def update_challenge(self, challenge_id: UUID, update_data: ChallengeUpdate) -> Type[Challenge] | None:
        db_challenge = self.get_challenge(challenge_id)
        if not db_challenge:
            return None

        for key, value in update_data.dict(exclude_unset=True).items():
            setattr(db_challenge, key, value)

        self.db.commit()
        self.db.refresh(db_challenge)
        return db_challenge

    def delete_challenge(self, challenge_id: UUID) -> bool:
        db_challenge = self.get_challenge(challenge_id)
        if not db_challenge:
            return False

        self.db.delete(db_challenge)
        self.db.commit()
        return True
