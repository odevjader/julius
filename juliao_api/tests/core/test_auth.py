import pytest
from fastapi import HTTPException, Depends, FastAPI
from fastapi.testclient import TestClient # Can use for simple dependency tests too
from jose import jwt, JWTError
from unittest import mock
from uuid import uuid4, UUID
from datetime import datetime, timedelta

from app.core.auth import get_current_user_id
from app.core.config import settings

# A dummy FastAPI app to test the dependency in isolation if needed
# Or can be tested via client requests to a protected endpoint later
mock_app = FastAPI()
DUMMY_USER_ID = uuid4()

@mock_app.get("/test-auth")
async def test_auth_route(user_id: UUID = Depends(get_current_user_id)):
    return {"user_id": user_id}

# Use TestClient for these dependency unit tests for simplicity
# AsyncClient would be for testing the actual endpoints
client = TestClient(mock_app)

def create_test_token(payload: dict, expires_delta_seconds: int = 3600):
    to_encode = payload.copy()
    expire = datetime.utcnow() + timedelta(seconds=expires_delta_seconds)
    to_encode.update({"exp": expire, "aud": "authenticated"}) # Add audience
    encoded_jwt = jwt.encode(to_encode, settings.SUPABASE_JWT_SECRET, algorithm="HS256")
    return encoded_jwt

@pytest.mark.asyncio
async def test_get_current_user_id_valid_token():
    token_payload = {"sub": str(DUMMY_USER_ID)}
    token = create_test_token(token_payload)

    # Mock settings for the dependency if it's not using the global one directly
    # In this case, get_current_user_id directly imports settings

    # Direct call test (more unit-style)
    # Need to mock the oauth2_scheme dependency behavior for direct call
    async def mock_oauth2_scheme_valid(): # Renamed to avoid conflict
        return token

    # Patch within the test function to ensure it's scoped
    with mock.patch("app.core.auth.oauth2_scheme", new=mock_oauth2_scheme_valid):
         # Call get_current_user_id with the token it would receive from Depends(oauth2_scheme)
         user_id = await get_current_user_id(token=await mock_oauth2_scheme_valid())
         assert user_id == DUMMY_USER_ID

    # Test via route
    response = client.get("/test-auth", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json()["user_id"] == str(DUMMY_USER_ID)


@pytest.mark.asyncio
async def test_get_current_user_id_expired_token():
    token_payload = {"sub": str(DUMMY_USER_ID)}
    token = create_test_token(token_payload, expires_delta_seconds=-3600) # Expired

    response = client.get("/test-auth", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Token has expired"

@pytest.mark.asyncio
async def test_get_current_user_id_invalid_signature():
    token_payload = {"sub": str(DUMMY_USER_ID)}
    # Tamper with the secret for this token only
    invalid_secret = settings.SUPABASE_JWT_SECRET + "tampered"
    expire = datetime.utcnow() + timedelta(seconds=3600)
    to_encode = token_payload.copy()
    to_encode.update({"exp": expire, "aud": "authenticated"})
    token = jwt.encode(to_encode, invalid_secret, algorithm="HS256")

    response = client.get("/test-auth", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Could not validate credentials"

@pytest.mark.asyncio
async def test_get_current_user_id_missing_sub():
    token_payload = {} # Missing "sub"
    token = create_test_token(token_payload)
    response = client.get("/test-auth", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Could not validate credentials"

@pytest.mark.asyncio
async def test_get_current_user_id_invalid_sub_uuid():
    token_payload = {"sub": "not-a-uuid"}
    token = create_test_token(token_payload)
    response = client.get("/test-auth", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Could not validate credentials"

@pytest.mark.asyncio
async def test_get_current_user_id_no_token():
    response = client.get("/test-auth") # No Authorization header
    assert response.status_code == 401
    assert response.json()["detail"] == "Not authenticated"

@pytest.mark.asyncio
async def test_get_current_user_id_wrong_audience():
    payload = {"sub": str(DUMMY_USER_ID), "exp": datetime.utcnow() + timedelta(seconds=30), "aud": "wrong_audience"}
    token = jwt.encode(payload, settings.SUPABASE_JWT_SECRET, algorithm="HS256")
    response = client.get("/test-auth", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Could not validate credentials"
