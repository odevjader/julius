# juliao_api/app/services/user_service.py
from uuid import UUID
from sqlmodel import Session, select

# Assuming UserProfile will be defined in app.models.user_models
# If UserProfile is not yet defined, this will cause an import error at runtime.
# This subtask focuses on the service logic. Model creation is separate.
from juliao_api.app.models.user_models import UserProfile
from juliao_api.app.db.session import get_db_session

def sync_user_profile(db: Session, user_id: UUID) -> UserProfile:
    """
    Retrieves a user profile by user_id. If it doesn't exist, it creates one.
    """
    statement = select(UserProfile).where(UserProfile.id == user_id)
    db_user_profile = db.exec(statement).first()

    if db_user_profile:
        # Optionally, update fields like last_seen_at here if needed.
        # For now, just returning the existing profile.
        # If any changes were made and db.commit() was called,
        # BaseUUIDModel's updated_at would be handled.
        return db_user_profile
    else:
        # Create a new profile if one doesn't exist
        new_profile = UserProfile(id=user_id)
        db.add(new_profile)
        db.commit()
        db.refresh(new_profile) # To get DB-generated values like created_at, updated_at
        return new_profile

# Example usage (for testing or integration, not part of the service itself):
# if __name__ == "__main__":
#     # This is a simplified example and needs a running DB and proper setup
#     # from app.db.session import engine # Assuming engine is defined in session.py
#     # from app.models.base import SQLModel # Assuming SQLModel is your base for models
#
#     # SQLModel.metadata.create_all(engine) # Create tables if they don't exist (for local testing)
#
#     # test_user_id = UUID("a1b2c3d4-e5f6-7890-1234-567890abcdef") # Example UUID
#
#     # with Session(engine) as session:
#         # profile = sync_user_profile(session, test_user_id)
#         # print(f"Synced profile for user {test_user_id}: {profile}")
#
#         # profile_again = sync_user_profile(session, test_user_id)
#         # print(f"Fetched profile again for user {test_user_id}: {profile_again}")
#         # assert profile.id == profile_again.id
#         # assert profile.created_at == profile_again.created_at
#
#         # another_user_id = UUID("b2c3d4e5-f6a7-8901-2345-67890abcdef0")
#         # another_profile = sync_user_profile(session, another_user_id)
#         # print(f"Synced profile for another user {another_user_id}: {another_profile}")
#         # assert another_profile.id == another_user_id

# Note: The UserProfile model (from app.models.user_models) and its table
#       must exist in the database for this service to function correctly.
#       Alembic migrations should handle table creation in a production setup.
#       The import `from juliao_api.app.models.user_models import UserProfile` assumes
#       that this model will be defined in that location by a subsequent step.
