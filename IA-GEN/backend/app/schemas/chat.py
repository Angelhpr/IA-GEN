from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Solicitud enviada por el usuario al asistente IA."""

    message: str = Field(
        ...,
        min_length=1,
        max_length=5000,
        description="Mensaje del usuario"
    )


class ChatResponse(BaseModel):
   """Respuesta generada por el asistente IA."""

   response: str = Field(
        ...,
        description="Respuesta generada por el asistente IA"
)