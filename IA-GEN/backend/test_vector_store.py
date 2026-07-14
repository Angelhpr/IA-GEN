from app.rag.ingestion import IngestionPipeline
from app.rag.vector_store import VectorStore

pipeline = IngestionPipeline()
chunks, embeddings = pipeline.run("data/documentos/bienvenida.txt")

store = VectorStore()

store.add_documents(chunks, embeddings)

print("Documentos guardados correctamente.")