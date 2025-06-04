from sqlmodel import SQLModel, Field
from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime
import sqlalchemy as sa

class UserProfile(SQLModel, table=True):
    __tablename__ = "user_profiles"

    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True, nullable=False, sa_column_kwargs={"server_default": sa.text("gen_random_uuid()")})
    full_name: Optional[str] = Field(default=None, max_length=255)
    whatsapp_number: Optional[str] = Field(default=None, max_length=30) # E.164 format can be up to 15, but allow some flexibility
    avatar_url: Optional[str] = Field(default=None, max_length=1024) # Standard URL lengths
    default_currency_code: str = Field(default="BRL", max_length=3, nullable=False) # ISO 4217 currency codes

    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False, sa_column_kwargs={"server_default": sa.func.now()})
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False, sa_column_kwargs={"server_default": sa.func.now(), "onupdate": sa.func.now()})

    # The 'id' field is intended to be the same as auth.users.id from Supabase.
    # We are not creating a direct foreign key constraint in this model to auth.users.id
    # as auth.users is in a separate schema managed by Supabase.
    # The trigger (to be implemented later) will handle linking these.
