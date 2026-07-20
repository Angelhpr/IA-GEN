from typing import Annotated

from fastapi import Depends

from app.core.config import settings
from app.dependencies.security import require_ingestion_access
from app.services.chat_service import ChatService
from app.services.ingestion_service import IngestionService


def get_chat_service() -> ChatService:
    return ChatService()


def get_ingestion_service() -> IngestionService:
    return IngestionService(
        source_path=settings.resolved_ingestion_source_path
    )


def get_authorized_ingestion_service(
    _: Annotated[
        None,
        Depends(require_ingestion_access),
    ],
) -> IngestionService:
    """
    Autoriza primero la operacion y crea el servicio
    de ingestion unicamente si el acceso es valido.
    """

    return get_ingestion_service()