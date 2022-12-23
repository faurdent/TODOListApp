from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///./storage/db_file.db')
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
