from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.schemas import SessionCreate, SessionResponse #only works when running from project root
from app.database import get_db
from app.crud import create_session, get_session, get_all_sessions, get_spot


router = APIRouter(prefix="/sessions", tags=["sessions"])

#add session
@router.post("/", response_model=SessionResponse, status_code=201)
def create_session_endpoint(session: SessionCreate, db: Session = Depends(get_db)):
    spot = get_spot(db, session.spot_id)
    if spot is None:       #could be replaced with a common dependancy later (get_spot_endpoint_or_404)
        raise HTTPException(status_code=404, detail="Spot with the given ID does not exist.")
    return create_session(db, session)

#get sessions (list)
@router.get("/", response_model=list[SessionResponse])
def get_all_sessions_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_all_sessions(db, skip, limit)


#get spot by ID
@router.get("/{session_id}", response_model=SessionResponse)
def get_session_endpoint(session_id: int, db: Session = Depends(get_db)):
    session = get_session(db, session_id)
    if session is None:
        raise HTTPException(status_code=404, detail="Session with the given ID does not exist.")
    return session