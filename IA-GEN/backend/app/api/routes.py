from fastapi import APIRouter, Depends

from app.dependencies.services import get_chat_service
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import ChatService

router = APIRouter(
    prefix="/api",
    tags=["Chat"]
)


@router.post(
    "/chat",
    response_model=ChatResponse,
    summary="Consultar al asistente IA",
    description=(
        "Recibe una pregunta del usuario y devuelve una respuesta "
        "utilizando el sistema RAG de IA-GEN."
    )
)
def chat(
    request: ChatRequest,
    chat_service: ChatService = Depends(get_chat_service),
):
    result = chat_service.chat(request.message)

    return ChatResponse(**result)
