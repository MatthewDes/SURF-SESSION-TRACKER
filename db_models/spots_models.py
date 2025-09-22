from sqlalchemy import Column, Integer, String, Float
from database import Base


class Spot(Base):
    __tablename__ = "spots"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    description = Column(String, nullable=True)  # optional