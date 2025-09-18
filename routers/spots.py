from fastapi import APIRouter, HTTPException
from models import SpotCreate, SpotResponse, SessionResponse #only works when running from project root
from storage import temp_spot_list, temp_session_list #temp import, will change when using db

router = APIRouter(prefix="/spots", tags=["spots"])


#helper function for @get routes
def get_spot_or_404(spot_id: int) -> SpotResponse:
    spot = next((s for s in temp_spot_list if s.spot_id == spot_id), None)
    if spot is None:
        raise HTTPException(status_code=404, detail="Spot with the given ID does not exist.")
    return spot


#add spots
@router.post("/", response_model=SpotResponse, status_code=201)
def add_spot(spot: SpotCreate):
    spot_id = len(temp_spot_list) + 1. #will change once using db
    new_spot = SpotResponse(spot_id=spot_id, **spot.model_dump())
    temp_spot_list.append(new_spot)
    return new_spot

#get spots (list)
@router.get("/", response_model=list[SpotResponse])
def get_spot_list():
    return temp_spot_list

#get spot by ID
@router.get("/{spot_id}", response_model=SpotResponse)
def get_spot(spot_id: int):
    return get_spot_or_404(spot_id)


#get sessions at a certain spot
@router.get("/{spot_id}/sessions", response_model=list[SessionResponse])
def get_sessions_at_spot(spot_id: int):
    spot = get_spot_or_404(spot_id)
    return [session for session in temp_session_list if session.spot_id == spot_id]
