# juliao_api/app/auth/jwt.py
from fastapi import HTTPException, Security, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from jose import jwt, JWTError, jwk
from jose.utils import base64url_decode
from datetime import datetime, timedelta
import httpx
from typing import Dict, Optional, Any

from juliao_api.app.core.config import settings

# Global cache for JWKS
jwks_cache: Optional[Dict[str, Any]] = None
# TODO: Add a TTL for the cache in a real-world scenario

async def fetch_jwks(jwks_url: str) -> Dict[str, Any]:
    global jwks_cache
    # In a real app, consider a more robust caching mechanism with TTL
    if jwks_cache:
        return jwks_cache

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(jwks_url)
            response.raise_for_status() # Raise an exception for HTTP errors
            jwks_cache = response.json()
            return jwks_cache
        except httpx.HTTPStatusError as e:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail=f"Could not fetch JWKS: {e}",
            )
        except httpx.RequestError as e:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail=f"Request to JWKS endpoint failed: {e}",
            )

def get_signing_key(token: str, jwks: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    try:
        unverified_header = jwt.get_unverified_header(token)
    except JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid token header: {e}",
        )

    kid = unverified_header.get("kid")
    if not kid:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token header missing 'kid' (Key ID)",
        )

    for key_dict in jwks.get("keys", []):
        if key_dict.get("kid") == kid:
            # Ensure key has necessary components for RS256
            if key_dict.get("kty") == "RSA" and key_dict.get("n") and key_dict.get("e"):
                return key_dict
            else:
                # Log the problematic key for debugging
                # print(f"Found key with kid={kid} but it's not a valid RSA key: {key_dict}")
                pass # Continue searching if this key is not suitable

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f"Signing key not found for kid '{kid}' in JWKS",
    )

async def decode_and_validate_jwt(token: str) -> Dict[str, Any]:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    if settings.SUPABASE_JWKS_URL:
        try:
            jwks = await fetch_jwks(settings.SUPABASE_JWKS_URL)
            signing_key_dict = get_signing_key(token, jwks)

            if not signing_key_dict:
                 raise credentials_exception # Should have been raised by get_signing_key

            # Construct the key in the format python-jose expects for RSA
            # This might involve converting from JWK format if not directly usable
            # For RSA, python-jose typically uses a dict like {'kty': 'RSA', 'n': ..., 'e': ...}
            # which is what `get_signing_key` should return from the JWKS.

            payload = jwt.decode(
                token,
                signing_key_dict, # The key itself, not the kid
                algorithms=["RS256"],
                audience=settings.SUPABASE_URL + "/auth/v1", # Example audience, adjust if needed. Supabase default is 'authenticated'
                issuer=settings.SUPABASE_URL + "/auth/v1" # Example issuer, adjust as per Supabase config
            )
            return payload
        except JWTError as e:
            # print(f"JWTError during RS256 decoding: {e}") # For debugging
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Invalid token: {e}",
                headers={"WWW-Authenticate": "Bearer"},
            )
        except HTTPException as e: # Re-raise HTTPExceptions from fetch_jwks or get_signing_key
            raise e
        except Exception as e: # Catch any other unexpected errors
            # print(f"Unexpected error during RS256 JWT decoding: {e}") # For debugging
            raise credentials_exception

    elif settings.SUPABASE_JWT_SECRET:
        try:
            payload = jwt.decode(
                token,
                settings.SUPABASE_JWT_SECRET,
                algorithms=["HS256"]
            )
            return payload
        except JWTError as e:
            # print(f"JWTError during HS256 decoding: {e}") # For debugging
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Invalid token: {e}",
                headers={"WWW-Authenticate": "Bearer"},
            )
        except Exception as e: # Catch any other unexpected errors
            # print(f"Unexpected error during HS256 JWT decoding: {e}") # For debugging
            raise credentials_exception
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="JWT validation configuration is missing (JWKS_URL or JWT_SECRET).",
        )

# Example of a Pydantic model for token claims (optional, but good practice)
class TokenData(BaseModel):
    sub: Optional[str] = None # Subject (usually user ID)
    user_id: Optional[str] = None # Custom claim if present
    exp: Optional[int] = None
    # Add other claims you expect, e.g., email, role

# Placeholder for a dependency to get current user (will be refined)
# async def get_current_user(token: HTTPAuthorizationCredentials = Security(HTTPBearer())):
#     if token is None:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Not authenticated",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     try:
#         payload = await decode_and_validate_jwt(token.credentials)
#         # You might want to map 'sub' to 'user_id' or fetch user from DB here
#         user_id = payload.get("sub")
#         if user_id is None:
#             raise HTTPException(status_code=401, detail="User ID not in token")
#         return TokenData(**payload) # Or return a User model instance
#     except HTTPException as e:
#         raise e # Re-raise if decode_and_validate_jwt raised an HTTPException
#     except Exception as e:
#         # print(f"Error in get_current_user: {e}") # For debugging
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Could not validate credentials",
#             headers={"WWW-Authenticate": "Bearer"},
#         )

# Note: The actual `get_current_user` dependency that integrates with FastAPI's
#       security schemes and potentially fetches user details from the database
#       will be implemented in a later step when User models and services are in place.
#       This file focuses on the JWT decoding and validation logic.
