from backend.app.db import SessionLocal


def get_db():
    try:
        db_obj = SessionLocal()
        yield db_obj
    finally:
        db_obj.close()
