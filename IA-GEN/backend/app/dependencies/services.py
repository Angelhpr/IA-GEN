from app.services.chat_service import ChatService
from app.services.ingestion_service import IngestionService


def get_chat_service() -> ChatService:
    return ChatService()


def get_ingestion_service() -> IngestionService:
    return IngestionService()