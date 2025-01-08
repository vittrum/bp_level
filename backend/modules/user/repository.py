from sqlalchemy.orm import Session
from models import User, Challenge
from schemas import UserCreate
from uuid import UUID
from passlib.hash import bcrypt

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: UserCreate) -> User:
        hashed_password = bcrypt.hash(user.password)
        db_user = User(username=user.username, hashed_password=hashed_password)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_user_by_username(self, username: str) -> User:
        return self.db.query(User).filter(User.username == username).first()

    def get_user(self, user_id: UUID) -> User:
        return self.db.query(User).filter(User.id == user_id).first()
