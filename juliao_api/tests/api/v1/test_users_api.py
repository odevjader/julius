import pytest
from fastapi.testclient import TestClient
from uuid import uuid4, UUID
from sqlmodel import Session, select
from unittest.mock import patch # For mocking dependencies

from juliao_api.app.models.user_models import UserProfile
from juliao_api.app.main import app # Ensure app is imported for dependency override
from juliao_api.app.auth.dependencies import get_current_supabase_user_id # Import the actual dependency

# Endpoint URL
SYNC_PROFILE_URL = "/api/v1/users/sync_profile"

# --- Test Cases for POST /sync_profile ---

def test_sync_profile_new_user_success(client_test: TestClient, db_session_test: Session, test_user_id: UUID):
    # Mock the dependency to return our test_user_id
    async def mock_get_user_id():
        return test_user_id

    app.dependency_overrides[get_current_supabase_user_id] = mock_get_user_id

    response = client_test.post(SYNC_PROFILE_URL)

    assert response.status_code == 200 # Default for POST if not specified otherwise
    profile_data = response.json()
    assert profile_data["id"] == str(test_user_id)
    assert "created_at" in profile_data
    assert "updated_at" in profile_data

    # Verify in DB
    db_profile = db_session_test.exec(select(UserProfile).where(UserProfile.id == test_user_id)).first()
    assert db_profile is not None
    assert db_profile.id == test_user_id

    # Clean up override
    del app.dependency_overrides[get_current_supabase_user_id]


def test_sync_profile_existing_user_success(client_test: TestClient, db_session_test: Session, test_user_id: UUID):
    # Pre-create user in DB
    existing_profile = UserProfile(id=test_user_id)
    db_session_test.add(existing_profile)
    db_session_test.commit()
    db_session_test.refresh(existing_profile)

    # Mock the dependency
    async def mock_get_user_id():
        return test_user_id
    app.dependency_overrides[get_current_supabase_user_id] = mock_get_user_id

    response = client_test.post(SYNC_PROFILE_URL)

    assert response.status_code == 200
    profile_data = response.json()
    assert profile_data["id"] == str(test_user_id)
    # Ensure it's the same user (e.g., created_at should match)
    assert profile_data["created_at"] == existing_profile.created_at.isoformat().replace('+00:00', 'Z') # Ensure ISO format matches

    # Verify in DB (no new user created)
    profiles_in_db = db_session_test.exec(select(UserProfile).where(UserProfile.id == test_user_id)).all()
    assert len(profiles_in_db) == 1

    del app.dependency_overrides[get_current_supabase_user_id]


def test_sync_profile_unauthorized_simulated(client_test: TestClient):
    # Mock the dependency to raise HTTPException similar to what happens with an invalid token
    async def mock_auth_failure():
        from fastapi import HTTPException, status
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Simulated auth error")

    app.dependency_overrides[get_current_supabase_user_id] = mock_auth_failure

    response = client_test.post(SYNC_PROFILE_URL)

    assert response.status_code == 401
    assert "Simulated auth error" in response.json()["detail"]

    del app.dependency_overrides[get_current_supabase_user_id]

def test_sync_profile_token_sub_not_uuid(client_test: TestClient):
    # Mock the dependency to raise HTTPException for invalid UUID format
    async def mock_invalid_uuid_in_sub():
        from fastapi import HTTPException, status
        # This specific error is raised by get_current_supabase_user_id if UUID(token_data.sub) fails
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, # Or 400 depending on where it's caught
            detail="Invalid token: User ID (sub) is not a valid UUID"
        )
    app.dependency_overrides[get_current_supabase_user_id] = mock_invalid_uuid_in_sub

    response = client_test.post(SYNC_PROFILE_URL)
    assert response.status_code == 401 # Based on current dependency implementation
    json_response = response.json()
    assert "User ID (sub) is not a valid UUID" in json_response["detail"]

    del app.dependency_overrides[get_current_supabase_user_id]


# Additional tests could include:
# - What happens if the database operation in sync_user_profile fails for some reason?
#   (This would likely result in a 500 error, TestClient usually catches these).
# - Testing with different valid UUIDs for user_id.
# - If `get_current_supabase_user_id` could return `None` (it shouldn't based on its code, as it raises HTTPException),
#   how the endpoint handles it (currently, there's a `if not current_user_id:` check, but it's defensive).

# Note on dependency overrides:
# It's crucial to clean up `app.dependency_overrides` after each test or test suite
# to prevent interference between tests. Pytest fixtures with `yield` can manage this,
# or manual deletion as shown. The `client_test` fixture in `conftest.py` was updated
# to try and manage this, but direct manipulation in tests like this is also common.
# Ensure that the override is specific to the test function's scope.
# The `client_test` fixture in `conftest.py` should ideally handle the override and cleanup
# if the mocked dependency is passed to it or configured within it.
# For this example, explicit override and cleanup in the test functions are shown for clarity.
# A more robust fixture could accept the mock function to use for the dependency.

# Example of how a fixture could manage the override:
# @pytest.fixture
# def client_with_mocked_auth(client_test: TestClient, test_user_id: UUID, mocker):
#     async def mock_get_user_id():
#         return test_user_id
#
#     original_dependency = app.dependency_overrides.get(get_current_supabase_user_id)
#     app.dependency_overrides[get_current_supabase_user_id] = mock_get_user_id
#     yield client_test # The client now uses the mocked dependency
#     # Restore:
#     if original_dependency is None:
#         del app.dependency_overrides[get_current_supabase_user_id]
#     else:
#         app.dependency_overrides[get_current_supabase_user_id] = original_dependency

# Then tests would use `client_with_mocked_auth` instead of `client_test`.
# The current `conftest.py` client_test fixture does basic override restoration.
# If a test needs a *specific* mock for a dependency, it often has to set it up itself
# and ensure cleanup, as done in these test functions.
