from app.rag.loader import DocumentLoader
from app.rag.chunker import DocumentChunker
from app.rag.embedding import EmbeddingGenerator
from app.core.logger import logger


class IngestionPipeline:

    def __init__(self):
        self.loader = DocumentLoader()
        self.chunker = DocumentChunker()
        self.embedding = EmbeddingGenerator()

    def run(self, file_path: str) -> tuple[list, list]:

        logger.info("===== INICIO DEL PIPELINE =====")

        document = self.loader.load(file_path)

        logger.info("Documento cargado correctamente")

        chunks = self.chunker.split(document)

        logger.info(f"Chunks generados: {len(chunks)}")

        embeddings = []

        for chunk in chunks:

            vector = self.embedding.generate(chunk.page_content)

            embeddings.append(vector)

        logger.info(f"Embeddings creados: {len(embeddings)}")

        logger.info("===== PIPELINE FINALIZADO =====")

        return chunks, embeddings