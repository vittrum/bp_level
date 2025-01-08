from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from modules.challenge.schemas import ChallengeCreate, ChallengeUpdate, ChallengeResponse
from db.db import get_db  # Assume you have a database.py to provide a session
from modules.challenge.repositories import ChallengeRepository
from modules.challenge.services import ChallengeService
from uuid import UUID

router = APIRouter()


def get_challenge_service(db: Session = Depends(get_db)):
    return ChallengeService(ChallengeRepository(db))


@router.get("/challenges", response_model=List[ChallengeResponse])
def get_challenges(skip: int = 0, limit: int = 10, service: ChallengeService = Depends(get_challenge_service)):
    return service.get_challenges(skip, limit)


@router.get("/challenges/{challenge_id}", response_model=ChallengeResponse)
def get_challenge(challenge_id: UUID, service: ChallengeService = Depends(get_challenge_service)):
    challenge = service.get_challenge(challenge_id)
    if not challenge:
        raise HTTPException(status_code=404, detail="Challenge not found")
    return challenge


@router.post("/challenges", response_model=ChallengeResponse)
def create_challenge(challenge: ChallengeCreate, service: ChallengeService = Depends(get_challenge_service)):
    return service.create_challenge(challenge)


@router.put("/challenges/{challenge_id}", response_model=ChallengeResponse)
def update_challenge(challenge_id: UUID, update_data: ChallengeUpdate,
                     service: ChallengeService = Depends(get_challenge_service)):
    updated_challenge = service.update_challenge(challenge_id, update_data)
    if not updated_challenge:
        raise HTTPException(status_code=404, detail="Challenge not found")
    return updated_challenge


@router.delete("/challenges/{challenge_id}", response_model=bool)
def delete_challenge(challenge_id: UUID, service: ChallengeService = Depends(get_challenge_service)):
    deleted = service.delete_challenge(challenge_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Challenge not found")
    return deleted
