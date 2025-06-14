# juliao_api/app/api/v1/endpoints/users.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from uuid import UUID

# Assuming UserProfile model is defined and user_service is implemented
from juliao_api.app.models.user_models import UserProfile # Will be created in model definition step
from juliao_api.app.services.user_service import sync_user_profile
from juliao_api.app.db.session import get_db_session

from juliao_api.app.auth.dependencies import get_current_supabase_user_id


router = APIRouter()

@router.post(
    "/sync_profile",
    response_model=UserProfile,
    summary="Synchronize User Profile",
    description="Retrieves the current user's profile. If no profile exists for the user ID "
                "obtained from the authentication token, a new profile is created and returned. "
                "This endpoint effectively ensures a user profile exists after login/authentication.",
    status_code=status.HTTP_200_OK, # Returns 200 if existing or 201 if created, but FastAPI handles this.
                                    # Default is 200 for POST if no specific success code for creation is set.
                                    # To be more explicit, one could return a Response with 201 on creation.
    responses={
        status.HTTP_200_OK: {"description": "User profile retrieved or created successfully."},
        status.HTTP_401_UNAUTHORIZED: {"description": "Not authenticated or token is invalid."},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid user ID format in token (should be rare if token validation is robust)."},
        status.HTTP_403_FORBIDDEN: {"description": "Token is valid but lacks necessary permissions (not typically used for 'sub' check, but for roles/scopes)."},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"description": "An unexpected error occurred on the server."},
    }
)
async def sync_current_user_profile(
    db: Session = Depends(get_db_session),
    current_user_id: UUID = Depends(get_current_supabase_user_id)
):
    """
    Synchronizes the user profile based on the Supabase User ID from the JWT token.
    If the profile exists, it's returned. If not, it's created.
    """
    if not current_user_id: # Should be handled by the dependency, but as a safeguard
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not identify user from token."
        )

    user_profile = sync_user_profile(db=db, user_id=current_user_id)

    # Determine if the profile was newly created to set status code to 201
    # This requires checking creation time or if it was just inserted.
    # For simplicity, FastAPI will default to 200 unless we manually craft a Response.
    # If UserProfile.created_at is very recent, it's likely new.
    # However, `sync_user_profile` handles the create/get logic.
    # The primary goal here is to ensure the profile exists and return it.

    return user_profile

# Note: The `UserProfile` model and the `sync_user_profile` service function must be correctly
# implemented and available for this endpoint to work.
# The `get_current_user_id_from_token` is a placeholder and needs to be replaced with
# the actual JWT authentication dependency that extracts user information from a valid token.
