from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    APP_NAME: str
    GEMINI_API_KEY: str
    MODEL_NAME: str
    APP_VERSION: str
    DEBUG: bool = False
    LOG_LEVEL: str = "INFO"

    VECTOR_DB_PATH: str = "data/vector_db"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()