import pathlib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

path = pathlib.Path(__file__).parent.joinpath("storage/db_file.db")

engine = create_engine(f'sqlite:///{path}', connect_args={'check_same_thread': False}, pool_pre_ping=True)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
