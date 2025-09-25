from sqlalchemy import Column, Integer, String, Float, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True)
    spot_id = Column(Integer, ForeignKey("spots.id"), nullable=False)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    rating = Column(Float, nullable=False)
    wave_height = Column(Float, nullable=False)
    tide = Column(String, nullable=False)
    waves_caught = Column(Integer, nullable=False)
    notes = Column(String, nullable=True)  # optional

    spot = relationship("Spot", back_populates="sessions")