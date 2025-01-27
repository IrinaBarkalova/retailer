from sqlalchemy import (
    Column,
    Integer,
    Identity,
    Text,
    ForeignKey,
)
from app.base.models import BaseModel


class Addresses(BaseModel):
    __tablename__ = "addresses"

    id = Column(Integer, Identity(), primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    city = Column(Text, nullable=False, index=True)
    street = Column(Text, nullable=False, index=True)
    house = Column(Text, nullable=False)
    entrance = Column(Integer, nullable=False)
    floor = Column(Integer, nullable=True)
    flat = Column(Text, nullable=True)
