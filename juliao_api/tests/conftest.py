import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from typing import AsyncGenerator, Generator
import asyncio

from app.core.config import settings
from app.db.session import get_async_session # Original get_async_session
from app.main import app as main_app # The main FastAPI app instance

# Use a separate test database if possible, or ensure transactions roll back.
# For now, we'll mock the session for most tests.
TEST_DATABASE_URL_STR = settings.ASYNC_DATABASE_URL.unicode_string().replace(
    path=f"/{settings.POSTGRES_DB}_test" # e.g. /juliao_db_test (ensure leading slash)
) if settings.ASYNC_DATABASE_URL and settings.POSTGRES_DB else "postgresql+asyncpg://test:test@localhost/test_db"


test_engine = create_async_engine(TEST_DATABASE_URL_STR, echo=False) # Use the string directly
test_session_maker = sessionmaker(
    bind=test_engine, class_=AsyncSession, expire_on_commit=False
)

# This fixture can be used if you want to test against a real (test) DB
# For many unit tests, mocking the session dependency is better.
async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with test_session_maker() as session:
        try:
            yield session
            # For tests, we often want to rollback any changes
            # await session.rollback() # Or let test transactions handle it
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

@pytest.fixture(scope="session")
def event_loop(request) -> Generator[asyncio.AbstractEventLoop, None, None]:
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="function")
async def app() -> FastAPI:
    # If you need to override dependencies for testing:
    # main_app.dependency_overrides[get_async_session] = override_get_async_session
    return main_app

@pytest.fixture(scope="function")
async def client(app: FastAPI) -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as c:
        yield c

@pytest.fixture(scope="function")
async def db_session() -> AsyncGenerator[AsyncSession, None]:
    # This provides a session that can be used to set up test data
    # if not mocking the entire get_async_session dependency.
    async with test_session_maker() as session:
        # Ideally, you'd use transactional tests or ensure cleanup.
        # For now, we just provide a session.
        yield session
        await session.rollback() # Ensure changes are rolled back
        await session.close()
