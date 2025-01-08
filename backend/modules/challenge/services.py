from typing import List, Optional
from modules.challenge.repositories import ChallengeRepository
from modules.challenge.schemas import ChallengeCreate, ChallengeUpdate, ChallengeResponse
from uuid import UUID


class ChallengeService:
    def __init__(self, challenge_repository: ChallengeRepository):
        self.challenge_repository = challenge_repository

    def get_challenge(self, challenge_id: UUID) -> Optional[ChallengeResponse]:
        return self.challenge_repository.get_challenge(challenge_id)

    def get_challenges(self, skip: int = 0, limit: int = 10) -> List[ChallengeResponse]:
        return self.challenge_repository.get_challenges(skip, limit)

    def create_challenge(self, challenge: ChallengeCreate) -> ChallengeResponse:
        return self.challenge_repository.create_challenge(challenge)

    def update_challenge(self, challenge_id: UUID, update_data: ChallengeUpdate) -> Optional[ChallengeResponse]:
        return self.challenge_repository.update_challenge(challenge_id, update_data)

    def delete_challenge(self, challenge_id: UUID) -> bool:
        return self.challenge_repository.delete_challenge(challenge_id)
