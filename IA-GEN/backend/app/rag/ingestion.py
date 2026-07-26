from langchain_core.documents import Document

from app.core.logger import logger
from app.rag.chunker import DocumentChunker
from app.rag.embedding import EmbeddingGenerator
from app.rag.loader import DocumentLoader


class IngestionPipeline:

    def __init__(self):
        self.loader = DocumentLoader()
        self.chunker = DocumentChunker()
        self.embedding = EmbeddingGenerator()

    def run(self, file_path: str) -> tuple[list, list]:
        """Carga y procesa un documento desde una ruta."""

        document = self.loader.load(file_path)

        return self.run_document(document)

    def run_document(
        self,
        document: Document,
    ) -> tuple[list, list]:
        """Procesa un documento que ya fue cargado."""

        logger.info("===== INICIO DEL PIPELINE =====")
        logger.info("Documento cargado correctamente")

        chunks = self.chunker.split(document)

        logger.info(
            "Chunks generados: %s",
            len(chunks),
        )

        embeddings = []

        embeddings = self.embedding.generate_batch(
            [
                chunk.page_content
                for chunk in chunks
            ]
        )

        logger.info(
            "Embeddings creados: %s",
            len(embeddings),
        )
        logger.info("===== PIPELINE FINALIZADO =====")

        return chunks, embeddings