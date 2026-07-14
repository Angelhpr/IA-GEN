from pathlib import Path

from chromadb import PersistentClient
from chromadb.config import Settings

from app.core.logger import logger


class VectorStore:

    def __init__(self):

        db_path = Path("data/vector_db")

        db_path.mkdir(parents=True, exist_ok=True)

        self.client = PersistentClient(
            path=str(db_path),
            settings=Settings(anonymized_telemetry=False)
        )

        self.collection = self.client.get_or_create_collection(
            name="ia_gen_documents"
        )

    def add_documents(self, chunks, embeddings):

        ids = []
        documents = []
        metadatas = []

        for i, chunk in enumerate(chunks):

            ids.append(f"doc_{i}")
            documents.append(chunk.page_content)
            metadatas.append(chunk.metadata)

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas
        )

        logger.info(f"{len(ids)} documentos almacenados en ChromaDB")

    def query(self, embedding, k: int = 3):

        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=k
        )

        return results