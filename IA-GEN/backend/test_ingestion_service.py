from app.services.ingestion_service import IngestionService

service = IngestionService()

service.ingest_folder(
    "data/documentos"
)

print("Ingestión completada correctamente.")

from app.rag.vector_store import VectorStore

store = VectorStore()

print(f"Documentos en ChromaDB: {store.count()}")

store = VectorStore()

print(store.show_all())