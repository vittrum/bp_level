from typing import Type
from uuid import UUID

from passlib.hash import bcrypt
from sqlalchemy.orm import Session

from modules.user.models import User
from modules.user.schemas import RegisterUser


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: RegisterUser) -> User:
        hashed_password = bcrypt.hash(user.password_first_time)
        db_user = User(
            username=user.username,
            email=user.email,
            full_name=user.full_name,
            hashed_password=hashed_password
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_user_by_username(self, username: str) -> Type[User] | None:
        return self.db.query(User).filter(User.username == username).first()

    def get_user(self, user_id: UUID) -> Type[User] | None:
        return self.db.query(User).filter(User.id == user_id).first()
