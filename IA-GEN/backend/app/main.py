from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router
from app.core.config import settings
from app.core.exceptions import register_exception_handlers
from app.core.logger import logger
from app.services.ingestion_service import IngestionService


@asynccontextmanager
async def lifespan(_app: FastAPI):
    if settings.AUTO_INGEST_ON_STARTUP:
        logger.info(
            "Iniciando ingestión automática de documentos..."
        )

        ingestion_service = IngestionService(
            source_path=settings.resolved_ingestion_source_path
        )
        ingestion_service.ingest_configured_source()

        logger.info(
            "Ingestión automática completada correctamente."
        )

    yield


app = FastAPI(
    title=settings.APP_NAME,
    description="Backend oficial del Instituto IA-GEN",
    version=settings.APP_VERSION,
    lifespan=lifespan,
    openapi_tags=[
        {
            "name": "General",
            "description": "Endpoints generales del sistema.",
        },
        {
            "name": "Chat",
            "description": "Comunicación con el asistente IA.",
        },
        {
            "name": "Admin",
            "description": "Administración del sistema.",
        },
    ],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_exception_handlers(app)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "Bienvenido a IA-GEN API",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }
