from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "sqlite:///./dev.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}) 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 


def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        print(f"Database error detected, rolling back: {e}") 
        db.rollback()
        raise
    finally:
        db.close()