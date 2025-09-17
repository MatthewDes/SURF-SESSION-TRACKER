from fastapi import APIRouter, HTTPException
from models import SpotCreate, SpotResponse #only works when running from project root

router = APIRouter(prefix="/spots", tags=["spots"])

temp_spot_list = []

#add spots
@router.post("/", response_model=SpotResponse)
def add_spot(spot: SpotCreate):
    spot_id = len(temp_spot_list) + 1
    new_spot = SpotResponse(spot_id=spot_id, **spot.dict())
    temp_spot_list.append(new_spot)
    return new_spot

#get spots (list)
@router.get("/", response_model=list[SpotResponse])
def get_spot_list():
    return temp_spot_list

#get spot by ID
@router.get("/{spot_id}", response_model=SpotResponse)
def get_spot(spot_id: int):
    for spot in temp_spot_list:
        if spot.spot_id == spot_id: # model field
            return spot
    raise HTTPException(status_code=404, detail="Spot with the given ID does not exist. ") 



