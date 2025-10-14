from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session

from app.schemas import SessionCreate, SessionResponse #only works when running from project root
from app.database import get_db
from app.crud import create_session, get_session, get_all_sessions, update_session, delete_session
from app.routers.helpers import get_spot_endpoint_or_404


router = APIRouter(prefix="/sessions", tags=["sessions"])

def get_session_not_found_exception(session_id: int):
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Session with ID {session_id} does not exist." # Dynamic message
    )

#add session
@router.post("/", response_model=SessionResponse, status_code=status.HTTP_201_CREATED)
def create_session_endpoint(session: SessionCreate, db: Session = Depends(get_db)):
    get_spot_endpoint_or_404(db, session.spot_id)
    return create_session(db, session)

#get sessions (list)
@router.get("/", response_model=list[SessionResponse])
def get_all_sessions_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_all_sessions(db, skip, limit)


#get session by ID
@router.get("/{session_id}", response_model=SessionResponse)
def get_session_endpoint(session_id: int, db: Session = Depends(get_db)):
    session = get_session(db, session_id)
    if session is None:
        raise get_session_not_found_exception(session_id)
    return session


#update session
@router.put("/{session_id}", response_model=SessionResponse)
def update_session_endpoint(session_id: int, session: SessionCreate, db: Session = Depends(get_db)):
    get_spot_endpoint_or_404(db, session.spot_id)   #check that entered spot id exists
    updated_session = update_session(db, session_id, session)
    if updated_session is None:
        raise get_session_not_found_exception(session_id)
    return updated_session


#delete session
@router.delete("/{session_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_session_endpoint(session_id: int, db: Session = Depends(get_db)):
    if delete_session(db, session_id):
        return {"message": "Successfully deleted spot"}
    raise get_session_not_found_exception(session_id)