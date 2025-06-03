import uuid
import enum
from datetime import datetime, date
from decimal import Decimal
from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import Column, func
from sqlalchemy.dialects.postgresql import TIMESTAMP, NUMERIC # For specific PG types
from sqlmodel import Field, Relationship, SQLModel # type: ignore

from .base import BaseUUIDModel # Import the BaseUUIDModel

if TYPE_CHECKING:
    from .user_models import UserProfile

# --- Enums (Consider moving to a separate enums.py if they grow) ---
class AccountType(str, enum.Enum):
    CHECKING = "checking"
    SAVINGS = "savings"
    INVESTMENT = "investment"
    WALLET = "wallet"
    OTHER = "other"

class CreditCardBrand(str, enum.Enum):
    VISA = "visa"
    MASTERCARD = "mastercard"
    AMEX = "amex"
    ELO = "elo"
    HIPERCARD = "hipercard"
    OTHER = "other"

class TransactionType(str, enum.Enum):
    INCOME = "income"
    EXPENSE = "expense"
    TRANSFER = "transfer"

class RecurringTransactionFrequency(str, enum.Enum):
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    BIMONTHLY = "bimonthly" # Every two months
    QUARTERLY = "quarterly"
    SEMI_ANNUALLY = "semi_annually" # Every six months
    ANNUALLY = "annually"

# --- Models ---

class Account(BaseUUIDModel, table=True):
    __tablename__ = "accounts" # type: ignore

    name: str = Field(index=True)
    type: AccountType = Field(default=AccountType.CHECKING)
    balance: Decimal = Field(default=0, sa_column=Column(NUMERIC(15, 2)))
    user_id: uuid.UUID = Field(foreign_key="user_profiles.id", index=True, nullable=False)

    user_profile: "UserProfile" = Relationship(back_populates="accounts")
    transactions: List["Transaction"] = Relationship(back_populates="account")
    # For transfers
    transfer_from_transactions: List["Transaction"] = Relationship(back_populates="from_account")
    transfer_to_transactions: List["Transaction"] = Relationship(back_populates="to_account")


class CreditCard(BaseUUIDModel, table=True):
    __tablename__ = "credit_cards" # type: ignore

    name: str
    brand: Optional[CreditCardBrand] = Field(default=None)
    limit: Decimal = Field(sa_column=Column(NUMERIC(15, 2)))
    due_day: int = Field(ge=1, le=31) # Day of the month the bill is due
    closing_day: int = Field(ge=1, le=31) # Day of the month the bill closes
    user_id: uuid.UUID = Field(foreign_key="user_profiles.id", index=True, nullable=False)

    user_profile: "UserProfile" = Relationship(back_populates="credit_cards")
    transactions: List["Transaction"] = Relationship(back_populates="credit_card")


class Category(BaseUUIDModel, table=True):
    __tablename__ = "categories" # type: ignore

    name: str = Field(index=True, unique=True) # Consider if unique per user or globally
    description: Optional[str] = Field(default=None)
    # If categories are user-specific, add user_id
    user_id: uuid.UUID = Field(foreign_key="user_profiles.id", index=True, nullable=False)

    user_profile: "UserProfile" = Relationship(back_populates="categories")
    transactions: List["Transaction"] = Relationship(back_populates="category")


class Transaction(BaseUUIDModel, table=True):
    __tablename__ = "transactions" # type: ignore

    description: str = Field(index=True)
    amount: Decimal = Field(sa_column=Column(NUMERIC(15, 2)))
    transaction_date: date = Field(sa_column=Column(TIMESTAMP(timezone=True), default=func.now())) # Date of transaction
    type: TransactionType = Field(default=TransactionType.EXPENSE)
    notes: Optional[str] = Field(default=None)

    user_id: uuid.UUID = Field(foreign_key="user_profiles.id", index=True, nullable=False)
    account_id: Optional[uuid.UUID] = Field(default=None, foreign_key="accounts.id", index=True)
    credit_card_id: Optional[uuid.UUID] = Field(default=None, foreign_key="credit_cards.id", index=True)
    category_id: Optional[uuid.UUID] = Field(default=None, foreign_key="categories.id", index=True)

    # For transfers
    from_account_id: Optional[uuid.UUID] = Field(default=None, foreign_key="accounts.id", index=True)
    to_account_id: Optional[uuid.UUID] = Field(default=None, foreign_key="accounts.id", index=True)

    user_profile: "UserProfile" = Relationship(back_populates="transactions")
    account: Optional[Account] = Relationship(back_populates="transactions", sa_relationship_kwargs=dict(foreign_keys="[Transaction.account_id]"))
    credit_card: Optional[CreditCard] = Relationship(back_populates="transactions")
    category: Optional[Category] = Relationship(back_populates="transactions")

    from_account: Optional[Account] = Relationship(back_populates="transfer_from_transactions", sa_relationship_kwargs=dict(foreign_keys="[Transaction.from_account_id]"))
    to_account: Optional[Account] = Relationship(back_populates="transfer_to_transactions", sa_relationship_kwargs=dict(foreign_keys="[Transaction.to_account_id]"))

    installments: List["Installment"] = Relationship(back_populates="transaction")


class Installment(BaseUUIDModel, table=True):
    __tablename__ = "installments" # type: ignore

    transaction_id: uuid.UUID = Field(foreign_key="transactions.id", index=True, nullable=False)
    installment_number: int
    total_installments: int
    amount: Decimal = Field(sa_column=Column(NUMERIC(15, 2)))
    due_date: date
    is_paid: bool = Field(default=False)

    transaction: Transaction = Relationship(back_populates="installments")


class RecurringTransaction(BaseUUIDModel, table=True):
    __tablename__ = "recurring_transactions" # type: ignore

    description: str
    amount: Decimal = Field(sa_column=Column(NUMERIC(15, 2)))
    frequency: RecurringTransactionFrequency
    start_date: date
    end_date: Optional[date] = Field(default=None)
    transaction_type: TransactionType = Field(default=TransactionType.EXPENSE) # To determine if it's income or expense
    notes: Optional[str] = Field(default=None)

    user_id: uuid.UUID = Field(foreign_key="user_profiles.id", index=True, nullable=False)
    account_id: Optional[uuid.UUID] = Field(default=None, foreign_key="accounts.id") # For recurring debits/credits to an account
    credit_card_id: Optional[uuid.UUID] = Field(default=None, foreign_key="credit_cards.id") # For recurring credit card charges
    category_id: Optional[uuid.UUID] = Field(default=None, foreign_key="categories.id")

    user_profile: "UserProfile" = Relationship(back_populates="recurring_transactions")
    # Relationships to account, credit_card, category if needed can be added here,
    # similar to Transaction model, but might be simpler to just store IDs if not heavily queried via ORM relationships.
