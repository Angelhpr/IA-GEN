from fastapi import APIRouter, Depends, HTTPException

from app.core.config import settings
from app.dependencies.services import (
    get_authorized_ingestion_service,
    get_chat_service,
    get_ingestion_service,
)
from app.schemas.chat import ChatRequest, ChatResponse
from app.schemas.ingestion import (
    DocumentInfoResponse,
    DocumentsResponse,
    IngestionResponse,
)
from app.services.chat_service import ChatService
from app.services.ingestion_service import IngestionService


router = APIRouter(
    prefix="/api",
    tags=["IA-GEN API"],
)


@router.post(
    "/chat",
    response_model=ChatResponse,
)
def chat(
    request: ChatRequest,
    chat_service: ChatService = Depends(get_chat_service),
):

    result = chat_service.chat(request.message)

    return ChatResponse(**result)


@router.post(
    "/ingest",
    response_model=IngestionResponse,
    summary="Indexar documentos",
    description=(
        "Procesa los documentos de la carpeta configurada "
        "por el servidor. Requiere acceso administrativo."
    ),
    include_in_schema=settings.INGESTION_ENABLED,
)
def ingest(
    ingestion_service: IngestionService = Depends(
        get_authorized_ingestion_service
    ),
):

    ingestion_service.ingest_configured_source()

    return IngestionResponse(
        success=True,
        message="Documentos indexados correctamente.",
    )


@router.get(
    "/documents",
    response_model=DocumentsResponse,
    summary="Listar documentos indexados",
    description=(
        "Devuelve la lista de documentos actualmente "
        "almacenados en la base vectorial."
    ),
)
def list_documents(
    ingestion_service: IngestionService = Depends(
        get_ingestion_service
    ),
):
    documents = ingestion_service.list_documents()

    return DocumentsResponse(
        documents=documents
    )


@router.get(
    "/documents/{filename}",
    response_model=DocumentInfoResponse,
    summary="Consultar documento",
    description=(
        "Devuelve la informacion de un documento "
        "almacenado en la base vectorial."
    ),
)
def get_document(
    filename: str,
    ingestion_service: IngestionService = Depends(
        get_ingestion_service
    ),
):
    result = ingestion_service.get_document_by_filename(
        filename
    )

    if not result["ids"]:
        raise HTTPException(
            status_code=404,
            detail=f"Documento no encontrado: {filename}",
        )

    metadata = result["metadatas"][0]

    return DocumentInfoResponse(
        filename=metadata["filename"],
        chunks=len(result["ids"]),
        content_hash=metadata["content_hash"],
        source=metadata["source"],
    )