from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from app import crud
from app.schemas.user_schemas import UserProfileRead, UserProfileUpdate
from app.db.session import get_async_session
from app.core.auth import get_current_user_id

router = APIRouter()

@router.get("/me", response_model=UserProfileRead)
async def read_current_user_profile(
    *,
    db: AsyncSession = Depends(get_async_session),
    current_user_id: UUID = Depends(get_current_user_id)
):
    """
    Retrieve the profile of the currently authenticated user.
    """
    user_profile = await crud.get_user_profile(db=db, user_id=current_user_id)
    if not user_profile:
        # This case should ideally not happen if profile creation trigger works correctly.
        # However, it's good practice to handle it.
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User profile not found. It may not have been initialized yet.",
        )
    return user_profile

@router.put("/me", response_model=UserProfileRead)
async def update_current_user_profile(
    *,
    db: AsyncSession = Depends(get_async_session),
    profile_in: UserProfileUpdate,
    current_user_id: UUID = Depends(get_current_user_id)
):
    """
    Update the profile of the currently authenticated user.
    """
    db_user_profile = await crud.get_user_profile(db=db, user_id=current_user_id)
    if not db_user_profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User profile not found. Cannot update.",
        )

    updated_user_profile = await crud.update_user_profile(
        db=db, db_obj=db_user_profile, obj_in=profile_in
    )
    return updated_user_profile
