from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.crud.spots_crud import get_spot
from app.schemas import SpotResponse



#helper function for get_spot routes (get_spot_endpoint, get_sessions_at_spot_endpoint, update sessions)
def get_spot_endpoint_or_404(db: Session, spot_id: int) -> SpotResponse:
    spot = get_spot(db, spot_id)
    if spot is None:
        raise HTTPException(status_code=404, detail="Spot with the given ID does not exist.")
    return spot