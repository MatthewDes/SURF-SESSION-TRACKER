from sqlalchemy.orm import declarative_base
Base = declarative_base()


from .spots_models import Spot
from .sessions_models import Session