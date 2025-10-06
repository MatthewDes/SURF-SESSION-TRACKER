from pydantic import BaseModel, conint, confloat
from typing import Optional
from datetime import datetime


class SessionCreate(BaseModel):
    spot_id: conint(gt=0)
    session_time: datetime
    rating: conint(ge=0, le=5)
    wave_height: confloat(ge=0)
    tide: str
    waves_caught: conint(ge=0)
    notes: Optional[str] = None

class SessionResponse(SessionCreate):
    id: conint(gt=0)