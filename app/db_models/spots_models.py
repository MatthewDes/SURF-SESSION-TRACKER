from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import relationship
from . import Base


class Spot(Base):
    __tablename__ = "spots"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True, nullable=False)
    latitude = Column(Numeric(10, 7), nullable=False)
    longitude = Column(Numeric(10, 7), nullable=False)
    description = Column(String, nullable=True)  # optional

    sessions = relationship("Session", back_populates="spot")

    