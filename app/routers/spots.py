from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.schemas import SpotCreate, SpotResponse, SessionResponse  #only works when running from project root
from app.database import get_db
from app.crud.spots_crud import create_spot, get_spot, get_all_spots, get_sessions_at_spot

#PHASE 1 - CAN BE REMOVED
#from app.storage_temp import temp_spot_list, temp_session_list #temp import, will change when using db

router = APIRouter(prefix="/spots", tags=["spots"])


#helper function for get_spot routes (get_spot_endpoint, get_sessions_at_spot_endpoint)
def get_spot_endpoint_or_404(db: Session, spot_id: int) -> SpotResponse:
    spot = get_spot(db, spot_id)
    if spot is None:
        raise HTTPException(status_code=404, detail="Spot with the given ID does not exist.")
    return spot


#add spots
@router.post("/", response_model=SpotResponse, status_code=201)
def create_spot_endpoint(spot: SpotCreate, db: Session = Depends(get_db)):
    return create_spot(db, spot)

#get spots (list)
@router.get("/", response_model=list[SpotResponse])
def get_all_spots_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_all_spots(db, skip, limit)

#get spot by ID
@router.get("/{spot_id}", response_model=SpotResponse)
def get_spot_endpoint(spot_id: int, db: Session = Depends(get_db)):
    return get_spot_endpoint_or_404(db, spot_id)


#get sessions at a certain spot
@router.get("/{spot_id}/sessions", response_model=list[SessionResponse])
def get_sessions_at_spot_endpoint(spot_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    get_spot_endpoint_or_404(db, spot_id)
    return get_sessions_at_spot(db, spot_id, skip, limit)
