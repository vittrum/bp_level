from repository import UserRepository
from schemas import UserCreate, UserResponse
from passlib.hash import bcrypt
from uuid import UUID

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, user: UserCreate) -> UserResponse:
        return self.user_repository.create_user(user)

    def authenticate_user(self, username: str, password: str) -> UserResponse:
        user = self.user_repository.get_user_by_username(username)
        if user and bcrypt.verify(password, user.hashed_password):
            return user
        return None

    def get_user(self, user_id: UUID) -> UserResponse:
        return self.user_repository.get_user(user_id)
