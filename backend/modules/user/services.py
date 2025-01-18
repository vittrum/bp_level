from typing import Type

from modules.user.exceptions import PasswordsDoNotMatchException
from modules.user.models import User
from modules.user.repository import UserRepository
from modules.user.schemas import UserCreate, UserResponse, RegisterUser
from passlib.hash import bcrypt
from uuid import UUID


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, user: RegisterUser) -> UserResponse:
        if user.password_first_time != user.password_confirmation:
            print("Passwords do not match!")
            raise PasswordsDoNotMatchException
        return self.user_repository.create_user(user)

    def authenticate_user(self, username: str, password: str) -> Type[User] | None:
        user = self.user_repository.get_user_by_username(username)
        if user and bcrypt.verify(password, user.hashed_password):
            return user
        return None

    def get_user(self, user_id: UUID) -> Type[User] | None:
        return self.user_repository.get_user(user_id)

    def get_user_by_name(self, username: str) -> Type[User] | None:
        return self.user_repository.get_user_by_username(username)
