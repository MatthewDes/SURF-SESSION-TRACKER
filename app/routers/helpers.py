from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.crud.spots_crud import get_spot
from app.schemas import SpotResponse




def get_session_not_found_exception(session_id: int):
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Session with ID {session_id} does not exist." # Dynamic message
    )

def get_spot_not_found_exception(spot_id: int):
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Spot with ID {spot_id} does not exist." # Dynamic message
    )


#helper function for get_spot routes (get_spot_endpoint, get_sessions_at_spot_endpoint, update sessions)
def get_spot_endpoint_or_404(db: Session, spot_id: int) -> SpotResponse:
    spot = get_spot(db, spot_id)
    if spot is None:
        raise get_spot_not_found_exception(spot_id)
    return spot