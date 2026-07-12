from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def root():
    return {
        "message": "Bienvenido a IA-GEN API"
    }


@router.get("/health")
def health():
    return {
        "status": "ok",
        "project": "IA-GEN API",
        "version": "1.0.0"
    }


from app.services.chat_service import ChatService

chat_service = ChatService()


@router.get("/chat")
def chat(message: str):
    return chat_service.chat(message)