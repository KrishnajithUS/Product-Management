import secrets

from pydantic import (
    HttpUrl,
    PostgresDsn,
    computed_field,
)
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict




class Settings(BaseSettings):
    """Helps to load env variables and set appropriate types"""
    
    model_config = SettingsConfigDict(
        env_file="app/.env", env_ignore_empty=True, extra="ignore"
    )
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    DOMAIN: str = "localhost"

    PROJECT_NAME: str = ''
    POSTGRES_SERVER: str = ''
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = ''
    POSTGRES_PASSWORD: str = ''
    POSTGRES_DB: str = ''
    IS_POSTGRES_SET : bool = False
    
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> PostgresDsn:
        if self.IS_POSTGRES_SET:
            return MultiHostUrl.build(
                scheme="postgresql+psycopg",
                username=self.POSTGRES_USER,
                password=self.POSTGRES_PASSWORD,
                host=self.POSTGRES_SERVER,
                port=self.POSTGRES_PORT,
                path=self.POSTGRES_DB,
            )
            
    FIRST_SUPERUSER: str = "admin@gmail.com"
    FIRST_SUPERUSER_PASSWORD: str = "test@pass"




settings = Settings()  # type: ignore
