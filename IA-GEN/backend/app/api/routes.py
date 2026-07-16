from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import ChatService

router = APIRouter(
    prefix="/api",
    tags=["Chat"]
)

chat_service = ChatService()


@router.post(
    "/chat",
    response_model=ChatResponse,
    summary="Consultar al asistente IA",
    description=(
        "Recibe una pregunta del usuario y devuelve una respuesta"
        "utilizando el sistema RAG de IA-GEN."
    )
)
def chat(request: ChatRequest):

    result = chat_service.chat(
        request.message
    )

    return ChatResponse(
        **result
    )
