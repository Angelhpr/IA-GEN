from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


BACKEND_ROOT = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):

    APP_NAME: str
    GEMINI_API_KEY: str
    MODEL_NAME: str
    APP_VERSION: str
    DEBUG: bool = False
    LOG_LEVEL: str = "INFO"
    CORS_ORIGINS: str = "http://localhost:3000"

    VECTOR_DB_PATH: str = "data/vector_db"

    INGESTION_ENABLED: bool = False
    INGESTION_API_KEY: SecretStr | None = None
    INGESTION_SOURCE_PATH: Path = Path("data/documentos")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def cors_origins(self) -> list[str]:
        return [
            origin.strip()
            for origin in self.CORS_ORIGINS.split(",")
            if origin.strip()
        ]

    @property
    def resolved_ingestion_source_path(self) -> Path:
        """
        Devuelve la carpeta documental configurada como ruta absoluta.

        Las rutas relativas se resuelven desde la raiz del backend,
        independientemente del directorio desde el que arranque Uvicorn.
        """

        source_path = self.INGESTION_SOURCE_PATH.expanduser()

        if source_path.is_absolute():
            return source_path.resolve()

        return (BACKEND_ROOT / source_path).resolve()


settings = Settings()