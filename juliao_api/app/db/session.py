from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel, Session

from juliao_api.app.core.config import settings

engine = create_engine(settings.DATABASE_URL)

def get_db_session():
    with Session(engine) as session:
        yield session
