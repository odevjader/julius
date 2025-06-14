import pytest
from uuid import uuid4, UUID
from sqlmodel import Session, select

from juliao_api.app.services.user_service import sync_user_profile
from juliao_api.app.models.user_models import UserProfile

# Test case for creating a new user profile
def test_sync_user_profile_creates_new_profile(db_session_test: Session):
    user_id = uuid4()

    # Ensure profile does not exist
    statement = select(UserProfile).where(UserProfile.id == user_id)
    profile = db_session_test.exec(statement).first()
    assert profile is None

    # Sync profile
    created_profile = sync_user_profile(db=db_session_test, user_id=user_id)

    assert created_profile is not None
    assert created_profile.id == user_id

    # Verify it's in the database
    retrieved_profile = db_session_test.exec(select(UserProfile).where(UserProfile.id == user_id)).first()
    assert retrieved_profile is not None
    assert retrieved_profile.id == user_id
    assert retrieved_profile.created_at is not None
    assert retrieved_profile.updated_at is not None

# Test case for retrieving an existing user profile
def test_sync_user_profile_retrieves_existing_profile(db_session_test: Session):
    user_id = uuid4()

    # Pre-create a profile
    existing_profile = UserProfile(id=user_id)
    db_session_test.add(existing_profile)
    db_session_test.commit()
    db_session_test.refresh(existing_profile)

    # Sync profile
    retrieved_profile = sync_user_profile(db=db_session_test, user_id=user_id)

    assert retrieved_profile is not None
    assert retrieved_profile.id == user_id
    assert retrieved_profile.created_at == existing_profile.created_at
    # updated_at might change if the model auto-updates it, but sync_user_profile doesn't modify it.
    # So, it should ideally be the same if no actual update logic is present.
    # If BaseUUIDModel updates updated_at on any access/save, this might need adjustment.
    # For now, assuming updated_at remains same if no data changed.
    assert retrieved_profile.updated_at == existing_profile.updated_at

    # Verify it's the same record
    statement = select(UserProfile).where(UserProfile.id == user_id)
    profile_from_db = db_session_test.exec(statement).first()
    assert profile_from_db is not None
    assert profile_from_db.id == user_id

# Test case to ensure retrieving an existing profile doesn't create a new one
def test_sync_user_profile_retrieves_existing_profile_does_not_duplicate(db_session_test: Session):
    user_id = uuid4()

    # Create and sync once
    sync_user_profile(db=db_session_test, user_id=user_id)

    # Count profiles before second sync
    count_before = db_session_test.exec(select(UserProfile)).all()
    assert len(count_before) >= 1 # Should be at least 1, could be more if other tests ran in same session (not with rollback)

    # Sync again
    sync_user_profile(db=db_session_test, user_id=user_id)

    # Count profiles after second sync
    count_after = db_session_test.exec(select(UserProfile).where(UserProfile.id == user_id)).all()
    assert len(count_after) == 1 # Should only be one profile with this ID

    all_profiles = db_session_test.exec(select(UserProfile)).all()
    # This assertion depends on test isolation. If db_session_test is truly isolated per test function,
    # then len(all_profiles) should be 1.
    # If the session fixture had 'module' scope and no rollbacks, this would be different.
    # With function scope and rollbacks, this should be fine.
    assert len(all_profiles) == 1


# Consider edge cases:
# - What if user_id is None? (sync_user_profile type hints prevent this, but defensive checks?)
#   The endpoint dependency get_current_supabase_user_id should ensure UUID is passed.
# - Concurrency: (Hard to test here) What if two requests try to sync the same non-existent profile?
#   One might fail due to unique constraint if not handled carefully (current logic should be okay:
#   first select, then insert. If another inserts between select and current insert, commit will fail).
#   This is usually handled by DB unique constraints. The first commit wins, the second fails unique constraint.
#   The current code doesn't explicitly handle that failure but relies on DB for integrity.
#   For a simple sync/create, this is often acceptable. More complex "upsert" might use DB features.
#   A try-except around db.commit() could catch IntegrityError if needed.

# This service is simple, so tests are straightforward.
# They rely on the db_session_test fixture from conftest.py for database interaction.
