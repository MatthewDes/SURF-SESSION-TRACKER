from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from . import Base


class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True)
    spot_id = Column(Integer, ForeignKey("spots.id"), nullable=False)
    session_time = Column(DateTime, nullable=False)
    rating = Column(Float, nullable=False)
    wave_height = Column(Float, nullable=False)
    tide = Column(Enum("low", "mid", "high", name="tide_enum"), nullable=False)
    waves_caught = Column(Integer, nullable=False)
    notes = Column(String, nullable=True)  # optional

    spot = relationship("Spot", back_populates="sessions")