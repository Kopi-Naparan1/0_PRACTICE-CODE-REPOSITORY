# core/config.py

from pydantic import BaseSettings
from functools import lru_cache

# 🔐 1. Inherit from BaseSettings to make it pull values from env vars or .env file
class Settings(BaseSettings):
    # ✅ Application settings
    PROJECT_NAME: str = "Secure FastAPI App"
    DEBUG: bool = False

    # ✅ Security settings
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # ✅ Database settings
    DATABASE_URL: str

    # ✅ Additional settings (optional)
    API_VERSION: str = "v1"

    # ⚙️ 2. Meta config to specify .env file (auto-loaded if it exists)
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# ♻️ 3. Use lru_cache to only load settings once (even if imported multiple times)
@lru_cache()
def get_settings() -> Settings:
    return Settings()
