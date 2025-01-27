from sqlalchemy import (
    Column,
    Integer,
    Identity,
    Text,
)
from app.base.models import BaseModel


class Shops(BaseModel):
    __tablename__ = "shops"

    id = Column(Integer, Identity(), primary_key=True)
    city = Column(Text, nullable=False, index=True)
    street = Column(Text, nullable=False, index=True)
    house = Column(Text, nullable=False)
    floor = Column(Integer, nullable=True)
