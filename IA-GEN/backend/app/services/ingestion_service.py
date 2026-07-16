from pathlib import Path

from app.core.hashing import calculate_file_hash
from app.core.logger import logger
from app.rag.ingestion import IngestionPipeline
from app.rag.vector_store import VectorStore


class IngestionService:

    def __init__(self):

        self.pipeline = IngestionPipeline()
        self.vector_store = VectorStore()

    def ingest_folder(self, folder: str):

        folder_path = Path(folder)

        if not folder_path.exists():
            raise FileNotFoundError(
                f"No existe la carpeta: {folder}"
            )

        txt_files = list(folder_path.glob("*.txt"))

        logger.info(
            f"Se encontraron {len(txt_files)} archivos TXT"
        )

        for file in txt_files:

            logger.info(
                f"Procesando: {file.name}"
            )

            content_hash = calculate_file_hash(
                str(file)
            )

            if not self.vector_store.needs_update(
                str(file),
                content_hash
            ):

                logger.info(
                    f"{file.name} no ha cambiado. Se omite."
                )

                continue

            if self.vector_store.get_document(
                str(file)
            )["ids"]:

                logger.info(
                    f"{file.name} fue modificado. Actualizando..."
                )

                self.vector_store.delete_document(
                    str(file)
                )

            chunks, embeddings = self.pipeline.run(
                str(file)
            )

            self.vector_store.add_documents(
                chunks,
                embeddings
            )