from sqlalchemy.orm import Session
from app import db_models, schemas #SpotCreate, Spot, Session

#POST
def create_spot(db: Session, spot_in: schemas.SpotCreate):
    db_spot = db_models.Spot(**spot_in.model_dump())
    db.add(db_spot)
    db.commit() #as application grows may need to move commit() out of function incase I want to group multiple operations together
    db.refresh(db_spot)
    return db_spot
    #db errors are handeled in get_db() function (database.py)

#GET
def get_spot(db:Session, spot_id: int):
    return db.query(db_models.Spot).filter(db_models.Spot.id == spot_id).first()


def get_all_spots(db:Session, skip: int = 0, limit: int = 100):
    return db.query(db_models.Spot).offset(skip).limit(limit).all()


def get_sessions_at_spot(db: Session, spot_id: int, skip: int = 0, limit: int = 100):
    return db.query(db_models.Session).filter(db_models.Session.spot_id == spot_id).offset(skip).limit(limit).all()
    #placed this function under spots because the endpoint function is in routers/spots.py 