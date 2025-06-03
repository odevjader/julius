import os
from dotenv import load_dotenv
from sqlmodel import SQLModel # Assuming your models will use SQLModel as a base
# Import your models so Alembic can see them.
# You'll need to create these model files in subsequent steps.
# For now, we'll prepare for them. Example:
# from app.models.base import SQLModel # If you have a central SQLModel export
# from app.models.user_models import UserProfile # Example
# from app.models.finance_models import Account # Example

# It's crucial that all your SQLModel table models are imported
# directly or indirectly before `target_metadata` is accessed.
# A common pattern is to import a base model that itself imports all other models,
# or import all model modules here.
# For now, we just need SQLModel itself for SQLModel.metadata

from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Load .env.dev or .env for database URL
# Assuming alembic commands are run from juliao_api directory
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env.dev')
if not os.path.exists(dotenv_path):
    dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env') # Fallback to .env
load_dotenv(dotenv_path=dotenv_path)

DATABASE_URL = os.getenv("DATABASE_URL_LOCAL")
if DATABASE_URL is None:
    raise ValueError("DATABASE_URL_LOCAL not found in environment variables. Ensure .env.dev or .env is correctly set up.")

# Interpret the config file for Python logging.
# This line needs to be called before config.set_main_option.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

config.set_main_option("sqlalchemy.url", DATABASE_URL)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
# Import your models here or ensure they are imported via a base model
# For now, this assumes all models will be children of SQLModel directly or indirectly
# and SQLModel.metadata will collect them.
# You will create app.models.finance_models and app.models.user_models later.
# These imports will be necessary for Alembic to detect your tables.
# For this step, we ensure SQLModel.metadata is the target.
# The actual model imports will be added to these files later.
from app.models import SQLModel # This will be from juliao_api/app/models/__init__.py eventually

target_metadata = SQLModel.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
