from fastapi import APIRouter
from models import SpotCreate, Spot #only works when running from project root

router = APIRouter(prefix="/spots", tags=["spots"])

temp_spot_list = []


@router.post("/", response_model=Spot)
def add_spot(spot: SpotCreate):
    spot_id = len(temp_spot_list) + 1
    new_spot = Spot(spot_id=spot_id, **spot.dict())
    temp_spot_list.append(new_spot)
    return new_spot

