from pydantic import BaseModel, conint, confloat
from typing import Optional


class SpotCreate(BaseModel):
    name: str
    latitude: confloat(ge=-90, le=90)
    longitude: confloat(ge=-180, le=180)
    description: Optional[str] = None

class SpotResponse(SpotCreate):
    spot_id: conint(gt=0)