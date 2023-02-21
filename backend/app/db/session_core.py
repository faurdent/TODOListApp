from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.core.config import app_config

engine = create_async_engine(app_config.get_db_url(), echo=True)

SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)
