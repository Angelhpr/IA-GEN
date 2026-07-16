from pathlib import Path

from chromadb import PersistentClient
from chromadb.config import Settings

from app.core.config import settings

from app.core.logger import logger


class VectorStore:

    def __init__(self):

        db_path = Path(settings.VECTOR_DB_PATH)

        db_path.mkdir(parents=True, exist_ok=True)

        self.client = PersistentClient(
            path=str(db_path),
            settings=Settings(anonymized_telemetry=False)
        )

        self.collection = self.client.get_or_create_collection(
            name="ia_gen_documents"
        )

    def _generate_chunk_id(self, chunk, index: int) -> str:
            
        filename = Path(
            chunk.metadata["filename"]
        ).stem

        content_hash = chunk.metadata["content_hash"][:8]

        return f"{filename}_{content_hash}_chunk_{index}"

    def add_documents(self, chunks, embeddings):

        ids = []
        documents = []
        metadatas = []

        for i, chunk in enumerate(chunks):

            chunk_id = self._generate_chunk_id(
                chunk,
                i
            )
            ids.append(chunk_id)

            documents.append(chunk.page_content)
            metadatas.append(chunk.metadata)

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas
        )

        logger.info(
            f"IDs almacenados: {ids}"
        )
        
        logger.info(
            f"{len(ids)} documentos almacenados en ChromaDB"
        )

    def query(self, embedding, k: int = 3):

        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=k
        )

        return results
    
    def count(self):

        return self.collection.count()
    
    def document_exists(self, source: str) -> bool:

        results = self.collection.get(
            where={
                "source": source}
        )

        return len(results["ids"]) > 0
    
    def get_document(self, source: str):

        source = str(Path(source).resolve())

        results = self.collection.get(
            where={
                "source": source
            }
        )

        return results
    
    def delete_document(self, source: str):

        source = str(Path(source).resolve())

        self.collection.delete(
            where={
                "source": source
            }
        )

        logger.info(
            f"Documento eliminado: {source}"
        )
    
    def needs_update(self, source: str, new_hash: str) -> bool:

        results = self.get_document(source)

        if len(results["ids"]) == 0:
            return True

        stored_hash = results["metadatas"][0]["content_hash"]

        return stored_hash != new_hash
    
    def show_all(self):

        return self.collection.get()