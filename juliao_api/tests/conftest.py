# juliao_api/tests/conftest.py
import pytest
from fastapi.testclient import TestClient
from sqlmodel import create_engine, Session, SQLModel
from sqlalchemy.pool import StaticPool # Recommended for SQLite in-memory for testing
from uuid import uuid4, UUID

# Adjust imports to match the project structure
from juliao_api.app.main import app # Main FastAPI app
from juliao_api.app.db.session import get_db_session
from juliao_api.app.core.config import Settings #, get_settings # get_settings might not exist or be needed here yet
# Import all models that might be created or queried during tests
from juliao_api.app.models.user_models import UserProfile
# Add other models here if they are used in tests, e.g.
# from juliao_api.app.models.transaction_models import Transaction

# Use a SQLite in-memory database for testing
# Using StaticPool as recommended for SQLite in-memory with SQLAlchemy for tests
DATABASE_URL_TEST = "sqlite:///:memory:"
engine_test = create_engine(
    DATABASE_URL_TEST,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)

@pytest.fixture(scope="session", autouse=True)
def create_test_db_and_tables():
    """
    Fixture to create all tables in the test database once per session.
    It yields control to the tests and then drops all tables after the session.
    """
    # SQLModel.metadata.create_all should ideally be called after all models are imported
    # Ensure all model files are imported somewhere before this runs,
    # or that SQLModel.metadata correctly collected all table metadata.
    SQLModel.metadata.create_all(engine_test)
    yield
    SQLModel.metadata.drop_all(engine_test)

@pytest.fixture(scope="function")
def db_session_test(create_test_db_and_tables):
    """
    Fixture to provide a database session for each test function.
    It starts a transaction, yields the session, and then rolls back the transaction.
    This ensures test isolation.
    """
    connection = engine_test.connect()
    transaction = connection.begin()
    session = Session(bind=connection)
    yield session
    session.close() # Close the session to release resources
    transaction.rollback() # Rollback any changes made during the test
    connection.close() # Close the connection

# Store original dependencies to restore them later
original_dependencies = {}

@pytest.fixture(scope="function")
def client_test(db_session_test):
    """
    Fixture to provide a FastAPI TestClient with overridden dependencies for testing.
    It overrides `get_db_session` to use the test database session.
    It also demonstrates how to override settings if needed.
    """
    global original_dependencies

    # Override get_db_session dependency
    if get_db_session not in original_dependencies:
        original_dependencies[get_db_session] = app.dependency_overrides.get(get_db_session)

    def override_get_db_session():
        yield db_session_test
    app.dependency_overrides[get_db_session] = override_get_db_session

    # Example: Override settings if necessary for specific test scenarios
    # This is useful if your app behavior changes based on settings (e.g., JWT keys)
    # from juliao_api.app.core.config import get_settings # Assuming you have a get_settings dependency
    # if get_settings not in original_dependencies:
    #     original_dependencies[get_settings] = app.dependency_overrides.get(get_settings)

    # def override_get_settings_for_test():
    #     return Settings(
    #         DATABASE_URL="sqlite:///:memory:", # Or any other test-specific setting
    #         SUPABASE_URL="https://test.supabase.co",
    #         SUPABASE_KEY="test_supabase_key",
    #         SUPABASE_JWT_SECRET="test_jwt_secret",
    #         SUPABASE_JWKS_URL="https://test.supabase.co/auth/v1/.well-known/jwks.json"
    #         # Add other settings as needed
    #     )
    # app.dependency_overrides[get_settings] = override_get_settings_for_test

    test_client = TestClient(app)
    yield test_client

    # Restore original dependencies
    if get_db_session in app.dependency_overrides:
        app.dependency_overrides[get_db_session] = original_dependencies[get_db_session]
    # if get_settings in app.dependency_overrides:
    #     app.dependency_overrides[get_settings] = original_dependencies[get_settings]

    # Clean up any remaining overrides if they were set to None originally
    if app.dependency_overrides.get(get_db_session) is None:
        del app.dependency_overrides[get_db_session]
    # if get_settings in original_dependencies and original_dependencies[get_settings] is None and get_settings in app.dependency_overrides:
    #     del app.dependency_overrides[get_settings]

# It's good practice to also have a fixture for test user IDs or tokens if needed across multiple tests.
@pytest.fixture(scope="session")
def test_user_id() -> UUID:
    return uuid4()

# Add more fixtures as needed, e.g., for creating mock JWT tokens.
# Consider using a library like `pytest-mock` for easier mocking.
