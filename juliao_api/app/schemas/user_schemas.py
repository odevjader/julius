from sqlmodel import SQLModel
from typing import Optional
from uuid import UUID
from datetime import datetime

# Properties to receive via API on update
class UserProfileUpdate(SQLModel):
    full_name: Optional[str] = None
    whatsapp_number: Optional[str] = None
    avatar_url: Optional[str] = None
    default_currency_code: Optional[str] = None

# Properties to return via API, inherits from SQLModel for ORM mode
# This schema will be based on the UserProfile model fields
class UserProfileRead(SQLModel):
    id: UUID
    full_name: Optional[str] = None
    whatsapp_number: Optional[str] = None
    avatar_url: Optional[str] = None
    default_currency_code: str
    created_at: datetime
    updated_at: datetime


# Schema for creating a user profile internally, e.g., by a trigger or system process
# It expects the id to be provided directly.
class UserProfileCreateInternal(SQLModel):
    id: UUID
    full_name: Optional[str] = None
    whatsapp_number: Optional[str] = None
    avatar_url: Optional[str] = None
    default_currency_code: str = "BRL"
