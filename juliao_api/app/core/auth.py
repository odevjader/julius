from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pydantic import ValidationError
from uuid import UUID

from app.core.config import settings

# This scheme can be used in Swagger UI for testing, but token extraction is manual
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") # tokenUrl is a dummy here, not actually used for auth

async def get_current_user_id(token: str = Depends(oauth2_scheme)) -> UUID:
    """
    Dependency to get the current user ID from a Supabase JWT.
    Verifies the token and extracts the user ID (sub claim).
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token,
            settings.SUPABASE_JWT_SECRET,
            algorithms=["HS256"], # Supabase typically uses HS256 for its JWTs
            audience="authenticated" # Default audience for Supabase JWTs
        )
        user_id_str: str = payload.get("sub")
        if user_id_str is None:
            raise credentials_exception

        # Validate that user_id_str is a valid UUID
        try:
            user_id = UUID(user_id_str)
        except ValueError:
            raise credentials_exception # Or a more specific error for invalid UUID format

    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except JWTError: # Catches other JWT errors (e.g., invalid signature, invalid token format)
        raise credentials_exception
    except Exception: # Catch any other unexpected error during token processing
             raise credentials_exception

    return user_id
