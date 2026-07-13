from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import ChatService

router = APIRouter()

chat_service = ChatService()


@router.post(
    "/chat",
    response_model=ChatResponse,
    tags=["Chat"]
)
def chat(request: ChatRequest):

    result = chat_service.chat(request.message)

    return ChatResponse(**result)