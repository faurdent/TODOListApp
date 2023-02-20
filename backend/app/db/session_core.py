from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from app.core.config import config

# path = pathlib.Path(__file__).parent.joinpath("storage/db_file.db")

# engine = create_engine(
#     f"sqlite:///{path}", connect_args={"check_same_thread": False}, pool_pre_ping=True
# )
# SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

engine = create_async_engine(config.get_db_url(), echo=True)

SessionLocal = AsyncSession(engine, expire_on_commit=False)
