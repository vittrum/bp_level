from sqlalchemy import Column, String, ForeignKey, Text, types, text
from sqlalchemy.dialects.postgresql import UUID, JSONB

import uuid

from sqlalchemy.orm import Mapped, mapped_column

from db.db import Base


class Challenge(Base):
    __tablename__ = "challenges"

    id: Mapped[UUID] = mapped_column(types.Uuid, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(nullable=False)
    collection: Mapped[str] = mapped_column(nullable=False)
    rarity: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    reward: Mapped[int] = mapped_column(nullable=False)
    additional_info = Column(JSONB, nullable=True)  # Todo: understand how to work with json in mapped

    # user_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
