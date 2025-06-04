import pytest
from httpx import AsyncClient
from fastapi import status
from uuid import uuid4, UUID
from unittest import mock
from typing import Optional, Dict, Any # Not strictly needed for these tests but good for general use
from datetime import datetime

from app.schemas.user_schemas import UserProfileRead, UserProfileUpdate
from app.models.user_profile import UserProfile # Needed for mock return types
from app.core.config import settings # For creating test tokens

# Helper to create tokens (can be shared or redefined if not using conftest for it)
from jose import jwt
from datetime import timedelta

# Using the DUMMY_USER_ID from test_auth or define a new one for clarity
PROFILE_TEST_USER_ID = uuid4()

def create_profile_test_token(user_id: UUID, expires_delta_seconds: int = 3600):
    to_encode = {"sub": str(user_id), "aud": "authenticated"}
    expire = datetime.utcnow() + timedelta(seconds=expires_delta_seconds)
    to_encode["exp"] = expire
    encoded_jwt = jwt.encode(to_encode, settings.SUPABASE_JWT_SECRET, algorithm="HS256")
    return encoded_jwt

@pytest.mark.asyncio
async def test_read_current_user_profile_success(client: AsyncClient):
    token = create_profile_test_token(user_id=PROFILE_TEST_USER_ID)
    headers = {"Authorization": f"Bearer {token}"}

    # Mock the CRUD function
    mock_profile_data = UserProfile(
        id=PROFILE_TEST_USER_ID,
        full_name="Test User",
        whatsapp_number="1234567890",
        avatar_url="http://example.com/avatar.png",
        default_currency_code="USD",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    with mock.patch("app.crud.get_user_profile", return_value=mock_profile_data) as mock_get:
        response = await client.get("/api/v1/profiles/me", headers=headers)

        assert response.status_code == status.HTTP_200_OK
        json_response = response.json()
        assert json_response["id"] == str(PROFILE_TEST_USER_ID)
        assert json_response["full_name"] == "Test User"
        assert json_response["default_currency_code"] == "USD"
        mock_get.assert_called_once()
        # Check if the db session and user_id were passed correctly if more detail is needed for mock
        # For example: mock_get.assert_called_once_with(db=mock.ANY, user_id=PROFILE_TEST_USER_ID)
        # However, db is harder to assert without more complex mocking of Depends(get_async_session)

@pytest.mark.asyncio
async def test_read_current_user_profile_not_found(client: AsyncClient):
    token = create_profile_test_token(user_id=PROFILE_TEST_USER_ID)
    headers = {"Authorization": f"Bearer {token}"}

    with mock.patch("app.crud.get_user_profile", return_value=None) as mock_get:
        response = await client.get("/api/v1/profiles/me", headers=headers)

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json()["detail"] == "User profile not found. It may not have been initialized yet."
        mock_get.assert_called_once()

@pytest.mark.asyncio
async def test_read_current_user_profile_unauthenticated(client: AsyncClient):
    response = await client.get("/api/v1/profiles/me") # No token
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    # The detail message for OAuth2PasswordBearer dependency failure when no token is provided
    # is "Not authenticated" by default in FastAPI.
    assert response.json()["detail"] == "Not authenticated"


@pytest.mark.asyncio
async def test_update_current_user_profile_success(client: AsyncClient):
    token = create_profile_test_token(user_id=PROFILE_TEST_USER_ID)
    headers = {"Authorization": f"Bearer {token}"}

    update_data_dict = {
        "full_name": "Updated Test User",
        "whatsapp_number": "0987654321",
        "default_currency_code": "EUR"
    }
    # Create UserProfileUpdate from dict for validation if needed, or pass dict directly if endpoint handles it
    update_data_schema = UserProfileUpdate(**update_data_dict)


    # Original profile that get_user_profile will return
    original_profile = UserProfile(
        id=PROFILE_TEST_USER_ID,
        full_name="Test User",
        whatsapp_number="1234567890",
        avatar_url="http://example.com/avatar.png",
        default_currency_code="USD",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    # Profile that update_user_profile will return
    # Ensure all fields expected by UserProfileRead are present
    updated_db_profile = UserProfile(
        id=PROFILE_TEST_USER_ID,
        full_name=update_data_schema.full_name,
        whatsapp_number=update_data_schema.whatsapp_number,
        avatar_url=original_profile.avatar_url, # Assuming avatar_url is not updated by this payload
        default_currency_code=update_data_schema.default_currency_code,
        created_at=original_profile.created_at, # created_at should not change
        updated_at=datetime.utcnow() # updated_at should be new
    )

    # Mock CRUD functions
    with mock.patch("app.crud.get_user_profile", return_value=original_profile) as mock_get, \
         mock.patch("app.crud.update_user_profile", return_value=updated_db_profile) as mock_update:

        response = await client.put("/api/v1/profiles/me", headers=headers, json=update_data_dict)

        assert response.status_code == status.HTTP_200_OK
        json_response = response.json()
        assert json_response["id"] == str(PROFILE_TEST_USER_ID)
        assert json_response["full_name"] == "Updated Test User"
        assert json_response["whatsapp_number"] == "0987654321"
        assert json_response["default_currency_code"] == "EUR"

        mock_get.assert_called_once()
        # Ensure the obj_in passed to crud.update_user_profile matches the schema instance
        # This requires comparing the schema instance, not just the dict.
        # For simplicity, we'll check that the mock was called. A more robust check
        # would involve an argument captor or a custom assertion.
        mock_update.assert_called_once()


@pytest.mark.asyncio
async def test_update_current_user_profile_not_found(client: AsyncClient):
    token = create_profile_test_token(user_id=PROFILE_TEST_USER_ID)
    headers = {"Authorization": f"Bearer {token}"}
    update_data = {"full_name": "Updated Test User"} # Using dict directly for json

    with mock.patch("app.crud.get_user_profile", return_value=None) as mock_get:
        response = await client.put("/api/v1/profiles/me", headers=headers, json=update_data)

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json()["detail"] == "User profile not found. Cannot update."
        mock_get.assert_called_once()

@pytest.mark.asyncio
async def test_update_current_user_profile_unauthenticated(client: AsyncClient):
    update_data = {"full_name": "Updated Test User"} # Using dict directly for json
    response = await client.put("/api/v1/profiles/me", json=update_data) # No token
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json()["detail"] == "Not authenticated"

@pytest.mark.asyncio
async def test_update_current_user_profile_invalid_data(client: AsyncClient):
    token = create_profile_test_token(user_id=PROFILE_TEST_USER_ID)
    headers = {"Authorization": f"Bearer {token}"}

    invalid_update_data = {
        "full_name": "Valid Name",
        "default_currency_code": "TOOLONGCODE" # More than 3 chars
    }

    response = await client.put("/api/v1/profiles/me", headers=headers, json=invalid_update_data)

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    json_response = response.json()
    assert "detail" in json_response
    # Check that the error detail mentions 'default_currency_code'
    found_error_for_field = False
    for error in json_response["detail"]:
        if "default_currency_code" in error.get("loc", []):
            found_error_for_field = True
            break
    assert found_error_for_field, "Validation error for 'default_currency_code' not found in details."
