from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    DATABASE_URL: str
    SUPABASE_URL: str
    SUPABASE_KEY: str
    SUPABASE_JWT_SECRET: str = "your_supabase_jwt_secret" # Default or from env
    SUPABASE_JWKS_URL: Optional[str] = None # Example: "https://<project_ref>.supabase.co/auth/v1/.well-known/jwks.json"


    class Config:
        env_file = ".env"

settings = Settings()
