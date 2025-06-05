import os
import sys
from logging.config import fileConfig

# Use create_engine for migrations, even if the app uses an async engine.
# Alembic operations are typically synchronous.
from sqlalchemy import engine_from_config 
from sqlalchemy import pool

from alembic import context

# --- Add this block at the beginning ---
# This adds the project root directory (which is /app in the container,
# and it contains the 'app' package at /app/app) to the Python path.
# This allows imports like 'from app.models...' or 'from app.core.config...'
# os.path.dirname(__file__) will be /app/alembic
# os.path.join(os.path.dirname(__file__), '..') will be /app/alembic/.. which is /app
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
# --- End of block to add ---

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Import your SQLModel base and all models to populate SQLModel.metadata
from sqlmodel import SQLModel # Import SQLModel
# Ensure all your models are imported.
# Your app/app/models/__init__.py should import all individual model files
# (e.g., user_models.py, finance_models.py)
import app.models # This now refers to /app/app/models

target_metadata = SQLModel.metadata # Use SQLModel's global metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

def get_url():
    # Import settings here, now that PROJECT_ROOT is in sys.path
    from app.core.config import settings 
    # For Alembic, it's generally recommended to use a synchronous DSN.
    # If settings.DATABASE_URL is an async DSN (e.g., "postgresql+asyncpg://..."),
    # you might need a separate sync DSN or to convert it.
    # Assuming settings.DATABASE_URL can provide a sync version or is already sync for Alembic.
    # If settings.DATABASE_URL is from Pydantic's PostgresDsn, render_as_string(hide_password=False) is good.
    # If it is an AsyncPostgresDsn, you need to ensure it's convertible to a sync URL for Alembic.
    # For simplicity, let's assume your settings.DATABASE_URL can be used directly or converted.
    # The original code used settings.DATABASE_URL.render_as_string(hide_password=False)
    # Let's stick to that, assuming it produces a sync URL.
    db_url = settings.DATABASE_URL.render_as_string(hide_password=False)
    # Override with DATABASE_URL_LOCAL if present, for docker-compose context
    local_db_url = os.getenv("DATABASE_URL_LOCAL")
    return local_db_url if local_db_url else db_url


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.
    """
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

# Your async setup for migrations online:
# It's kept as you had it, but note that Alembic itself doesn't run async operations.
# The `connection.run_sync(do_run_migrations)` is the key part that bridges async and sync.
# For the engine, Alembic traditionally uses a sync engine.
# If create_async_engine is used, it must be handled carefully with run_sync.
# A simpler approach for Alembic is often to use a synchronous engine directly.
# However, let's try with your async setup first, as the main error was ModuleNotFound.

def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()

async def run_migrations