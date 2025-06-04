from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from typing import AsyncGenerator

from app.core.config import settings

# Create an async SQLAlchemy engine
async_engine = create_async_engine(
    settings.ASYNC_DATABASE_URL.unicode_string(), # Use .unicode_string() for pydantic v2 DSNs
    pool_pre_ping=True, # Good practice to check connections before use
    # echo=True, # Uncomment for debugging SQL queries
)

# Create an async session factory
async_session_maker = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False, # Good practice for FastAPI background tasks
)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency to get an async database session.
    Ensures the session is closed after the request.
    """
    async with async_session_maker() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
