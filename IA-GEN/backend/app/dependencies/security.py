from secrets import compare_digest
from typing import Annotated

from fastapi import HTTPException, Security, status
from fastapi.security import APIKeyHeader

from app.core.config import settings
from app.core.logger import logger


ingestion_api_key_header = APIKeyHeader(
    name="X-Ingestion-API-Key",
    scheme_name="IngestionApiKey",
    description="Clave administrativa para ejecutar la ingestion.",
    auto_error=False,
)


def require_ingestion_access(
    provided_api_key: Annotated[
        str | None,
        Security(ingestion_api_key_header),
    ],
) -> None:
    """
    Protege la ingestion mediante un interruptor de configuracion
    y una clave administrativa dedicada.
    """

    if not settings.INGESTION_ENABLED:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Recurso no encontrado.",
        )

    configured_secret = settings.INGESTION_API_KEY

    if configured_secret is None:
        logger.error(
            "La ingestion esta habilitada sin INGESTION_API_KEY."
        )

        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Servicio de ingestion no disponible.",
        )

    configured_api_key = configured_secret.get_secret_value()

    if not configured_api_key.strip():
        logger.error(
            "INGESTION_API_KEY esta vacia."
        )

        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Servicio de ingestion no disponible.",
        )

    candidate_api_key = provided_api_key or ""

    if not compare_digest(
        candidate_api_key.encode("utf-8"),
        configured_api_key.encode("utf-8"),
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acceso denegado.",
        )
