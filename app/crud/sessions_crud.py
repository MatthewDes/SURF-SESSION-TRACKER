from sqlalchemy.orm import Session
from app import db_models, schemas #SessionCreate, Session

#POST
def create_session(db: Session, session_in: schemas.SessionCreate):
    db_session = db_models.Session(**session_in.model_dump())
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    return db_session

#GET
def get_session(db: Session, session_id: int):
    return db.query(db_models.Session).filter(db_models.Session.id == session_id).first()


def get_all_sessions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(db_models.Session).offset(skip).limit(limit).all()