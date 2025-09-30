from sqlalchemy.orm import Session
from app import db_models, schemas

def create_spot(db: Session, spot_in: schemas.SpotCreate):
    db_spot = db_models.Spot(**spot_in.model_dump())
    db.add(db_spot)
    #finish off function (commit refresh, or add in exception handling?)