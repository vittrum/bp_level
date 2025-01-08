from sqlalchemy import Column, String, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID, JSONB

import uuid

from db.db import Base


class Challenge(Base):
    __tablename__ = "challenges"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    user_id = Column(UUID(as_uuid=True), nullable=False)
    name = Column(String, nullable=False)
    collection = Column(String, nullable=False)
    rarity = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    reward = Column(String, nullable=False)
    additional_info = Column(JSONB, nullable=True)
