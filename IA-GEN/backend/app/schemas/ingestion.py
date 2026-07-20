from pydantic import BaseModel, Field


class IngestionResponse(BaseModel):

    success: bool

    message: str


class DocumentsResponse(BaseModel):

    documents: list[str]


class DocumentInfoResponse(BaseModel):

    filename: str = Field(
        ...,
        description="Nombre del documento.",
    )

    chunks: int = Field(
        ...,
        description="Cantidad de fragmentos almacenados.",
    )

    content_hash: str = Field(
        ...,
        description="Hash SHA-256 del documento.",
    )

    source: str = Field(
        ...,
        description="Ruta original del documento.",
    )