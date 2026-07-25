from typing import Literal

from pydantic import BaseModel, Field


class ChatHistoryMessage(BaseModel):
    """Mensaje previo incluido como contexto conversacional."""

    role: Literal["user", "assistant"] = Field(
        ...,
        description="Rol del mensaje dentro de la conversación",
    )

    content: str = Field(
        ...,
        min_length=1,
        max_length=5000,
        description="Contenido del mensaje previo",
    )


class ChatRequest(BaseModel):
    """Solicitud enviada por el usuario al asistente IA."""

    message: str = Field(
        ...,
        min_length=1,
        max_length=5000,
        description="Mensaje actual del usuario",
    )

    history: list[ChatHistoryMessage] = Field(
        default_factory=list,
        max_length=8,
        description="Últimos mensajes de la conversación",
    )


class ChatResponse(BaseModel):
    """Respuesta generada por el asistente IA."""

    response: str = Field(
        ...,
        description="Respuesta generada por el asistente IA",
    )