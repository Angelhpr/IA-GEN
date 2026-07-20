from app.core.config import settings
from app.rag.vector_store import VectorStore
from app.services.ingestion_service import IngestionService


service = IngestionService(
    source_path=settings.resolved_ingestion_source_path
)

service.ingest_configured_source()

print("Ingestion completada correctamente.")

store = VectorStore()

print(f"Documentos en ChromaDB: {store.count()}")
print(store.show_all())