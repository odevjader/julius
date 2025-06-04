from typing import Optional
from uuid import UUID

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import SQLModel # Required for update logic

from app.models.user_profile import UserProfile
from app.schemas.user_schemas import UserProfileUpdate, UserProfileCreateInternal


async def get_user_profile(db: AsyncSession, user_id: UUID) -> Optional[UserProfile]:
    """
    Retrieve a user profile by their ID.
    """
    result = await db.execute(select(UserProfile).where(UserProfile.id == user_id))
    return result.scalar_one_or_none()

async def create_user_profile(db: AsyncSession, *, obj_in: UserProfileCreateInternal) -> UserProfile:
    """
    Create a new user profile.
    The 'id' is provided by obj_in, matching Supabase auth.users.id.
    """
    # Create an instance of the UserProfile model from the input schema
    db_obj = UserProfile.model_validate(obj_in) # SQLModel v2 style

    db.add(db_obj)
    await db.commit()
    await db.refresh(db_obj)
    return db_obj

async def update_user_profile(
    db: AsyncSession, *, db_obj: UserProfile, obj_in: UserProfileUpdate
) -> UserProfile:
    """
    Update an existing user profile.
    """
    # Get the dictionary of the input data, excluding unset values
    update_data = obj_in.model_dump(exclude_unset=True) # SQLModel v2 style

    # Update the database object's fields
    for field, value in update_data.items():
        setattr(db_obj, field, value)

    db.add(db_obj)
    await db.commit()
    await db.refresh(db_obj)
    return db_obj
