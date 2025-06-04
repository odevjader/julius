from logging.config import fileConfig

from sqlalchemy.ext.asyncio import create_async_engine # Use async engine
from sqlalchemy import pool

from alembic import context

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Import your models' MetaData object here
# For SQLModel, you might need to import all models that define tables
# and then access a common SQLModel.metadata
# For simplicity, assuming all models are imported somewhere that populates SQLModel.metadata
# If not, you might need to explicitly import them:
# from app.models.user_profile import UserProfile # Example
from sqlmodel import SQLModel # Import SQLModel
from app.models.user_profile import UserProfile # Ensure UserProfile is imported to be part of metadata

target_metadata = SQLModel.metadata # Use SQLModel's metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

def get_url():
    from app.core.config import settings # Import settings here to avoid circular imports at global scope
    return settings.DATABASE_URL.render_as_string(hide_password=False) # Use sync URL for migrations

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

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


async def run_migrations_online() -> None: # Make this function async
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = create_async_engine( # Use create_async_engine
        get_url(), # Get the database URL
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection: # Use async connect
        await connection.run_sync(do_run_migrations) # Run migrations synchronously within the async connection

    await connectable.dispose() # Dispose of the engine

def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    import asyncio
    asyncio.run(run_migrations_online()) # Run the async function
