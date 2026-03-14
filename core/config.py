from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    db_url: str
    db_max_connections: int = 5
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

settings = Settings()