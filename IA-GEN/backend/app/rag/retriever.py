from app.rag.embedding import EmbeddingGenerator
from app.rag.vector_store import VectorStore


class Retriever:

    def __init__(self):

        self.embedding = EmbeddingGenerator()
        self.store = VectorStore()

    def search(self, question: str, k: int = 3):

        query_embedding = self.embedding.generate(question)

        results = self.store.query(
            embedding=query_embedding,
            k=k
        )

        return results