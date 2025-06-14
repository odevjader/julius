from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from uuid import UUID
from jose import jwt as jose_jwt, JWTError # Use 'jose_jwt' to avoid conflict if 'jwt' module name is used elsewhere

# Assuming TokenData is correctly defined in app.auth.jwt to include 'sub'
from juliao_api.app.auth.jwt import decode_and_validate_jwt, TokenData
from juliao_api.app.core.config import Settings
# It's common to have a get_settings dependency if settings are needed in various places
# For now, directly using settings from config, or passing settings if needed by decode_and_validate_jwt
# The current signature of decode_and_validate_jwt in jwt.py doesn't take settings, it imports them directly.

bearer_scheme = HTTPBearer(auto_error=True)

async def get_current_supabase_user_id(
    token: HTTPAuthorizationCredentials = Depends(bearer_scheme)
    # settings: Settings = Depends(get_settings) # get_settings would be a dependency that provides Settings instance
                                                # decode_and_validate_jwt currently imports settings directly
) -> UUID:
    """
    FastAPI dependency to extract and validate Supabase User ID (UUID) from a JWT token.
    Relies on `decode_and_validate_jwt` to handle the actual decoding and validation logic.
    """
    try:
        # decode_and_validate_jwt is expected to raise HTTPException on failure.
        # It internally uses settings from juliao_api.app.core.config
        payload = await decode_and_validate_jwt(token=token.credentials)

        # Ensure payload is not None if decode_and_validate_jwt could return None on some paths
        if payload is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token: payload is null", # Should not happen if decode_and_validate_jwt is robust
                headers={"WWW-Authenticate": "Bearer"},
            )

        token_data = TokenData(**payload)

        if token_data.sub is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token: User ID (sub) missing",
                headers={"WWW-Authenticate": "Bearer"},
            )

        try:
            user_uuid = UUID(token_data.sub)
            return user_uuid
        except ValueError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, # Or 400 Bad Request if sub is present but not UUID
                detail="Invalid token: User ID (sub) is not a valid UUID",
                headers={"WWW-Authenticate": "Bearer"},
            )

    except JWTError as e: # This might be redundant if decode_and_validate_jwt catches all JWTError
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid token: {str(e)}",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except HTTPException as e: # Re-raise HTTPExceptions raised by decode_and_validate_jwt
        raise e
    except Exception as e: # Catch any other unexpected errors during processing
        # Log the exception e for server-side review
        # print(f"Unexpected error in get_current_supabase_user_id: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred while processing the token.",
            headers={"WWW-Authenticate": "Bearer"},
        )
