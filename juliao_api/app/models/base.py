import uuid
from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel, func # type: ignore # TODO: remove type: ignore when pydantic v2 is supported by sqlmodel
from sqlalchemy import Column, DateTime # Import DateTime for timezone=True

# Define a base class for common timestamp fields
class TimestampModel(SQLModel):
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False,
        sa_column_kwargs={
            "server_default": func.now()
        }
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False,
        sa_column_kwargs={
            "server_default": func.now(),
            "onupdate": func.now()
        }
    )

# Example of a base model with a UUID primary key and timestamps
# Models can inherit from this or directly from SQLModel and TimestampModel
class BaseUUIDModel(TimestampModel):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )

# Re-export SQLModel and Field for convenience in other model files
# This way, other models can do `from .base import SQLModel, Field, BaseUUIDModel`
__all__ = ["SQLModel", "Field", "TimestampModel", "BaseUUIDModel", "func"]
