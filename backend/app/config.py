# app/config.py

# app/config.py

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    HOST: str = "127.0.0.1"
    PORT: int = 8000
    OUTLOOK_CLIENT_ID: str = ""
    OUTLOOK_CLIENT_SECRET: str = ""
    OUTLOOK_TENANT_ID: str = ""

class Config:
    env_file = ".env"
    extra = "ignore"  # Add this line

settings = Settings()
