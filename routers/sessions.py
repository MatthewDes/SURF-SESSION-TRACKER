from fastapi import APIRouter, HTTPException
from models import SessionCreate, SessionResponse #only works when running from project root
from routers.spots import temp_spot_list #temp import, will change when using db

router = APIRouter(prefix="/sessions", tags=["sessions"])

temp_session_list = []

#add session
@router.post("/", response_model=SessionResponse)
def add_session(session: SessionCreate):
    for spot in temp_spot_list:
        if session.spot_id == spot.spot_id:
            session_id = len(temp_session_list) + 1
            new_session = SessionResponse(session_id=session_id, **session.dict())
            temp_session_list.append(new_session)
            return new_session
    raise HTTPException(status_code = 404, detail="Spot not found")

#get spots (list)
@router.get("/", response_model=list[SessionResponse])
def get_session_list():
    return temp_session_list


#get spot by ID
@router.get("/{session_id}", response_model=SessionResponse)
def get_session(session_id: int):
    for session in temp_session_list:
        if session.session_id == session_id:
            return session
    raise HTTPException(status_code=404, detail="Session with the given ID does not exist. ")