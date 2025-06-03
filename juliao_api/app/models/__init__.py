from sqlmodel import SQLModel # type: ignore # Re-export SQLModel itself

# Import and re-export models from their respective files
from .base import BaseUUIDModel, TimestampModel
from .user_models import UserProfile
from .finance_models import (
    Account,
    AccountType,
    CreditCard,
    CreditCardBrand,
    Category,
    Transaction,
    TransactionType,
    Installment,
    RecurringTransaction,
    RecurringTransactionFrequency
)

# It's good practice to define __all__ to specify what gets imported with 'from .models import *'
# However, for Alembic autodiscovery, direct imports in env.py or ensuring modules are loaded is key.
# SQLModel.metadata relies on models being imported somewhere to be registered.
# This __init__.py helps in organizing imports for the application code.

__all__ = [
    "SQLModel", # From sqlmodel library
    "BaseUUIDModel",
    "TimestampModel",
    "UserProfile",
    "Account",
    "AccountType",
    "CreditCard",
    "CreditCardBrand",
    "Category",
    "Transaction",
    "TransactionType",
    "Installment",
    "RecurringTransaction",
    "RecurringTransactionFrequency",
]
