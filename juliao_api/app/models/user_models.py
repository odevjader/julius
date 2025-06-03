import uuid
from typing import TYPE_CHECKING, List

from sqlmodel import Field, Relationship # type: ignore # TODO: remove type: ignore when pydantic v2 is supported by sqlmodel

from .base import BaseUUIDModel # Import the BaseUUIDModel

if TYPE_CHECKING:
    from .finance_models import Account, CreditCard, Category, Transaction, RecurringTransaction

class UserProfile(BaseUUIDModel, table=True):
    __tablename__ = "user_profiles" # type: ignore

    # id: inherited from BaseUUIDModel, will mirror auth.users.id
    # created_at, updated_at: inherited from BaseUUIDModel

    # Relationships to finance models
    # These will be populated by the back_populates in the finance_models
    accounts: List["Account"] = Relationship(back_populates="user_profile")
    credit_cards: List["CreditCard"] = Relationship(back_populates="user_profile")
    categories: List["Category"] = Relationship(back_populates="user_profile")
    transactions: List["Transaction"] = Relationship(back_populates="user_profile")
    recurring_transactions: List["RecurringTransaction"] = Relationship(back_populates="user_profile")
