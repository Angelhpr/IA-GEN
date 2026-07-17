from pathlib import Path

from app.core.hashing import calculate_file_hash
from app.core.logger import logger
from app.rag.ingestion import IngestionPipeline
from app.rag.vector_store import VectorStore


class IngestionService:

    def __init__(self):

        self.pipeline = IngestionPipeline()
        self.vector_store = VectorStore()

    def ingest_file(self, file_path: str):
        """Procesa un único documento y actualiza la base vectorial si ha cambiado."""

        file = Path(file_path)

        logger.info(
            f"Procesando: {file.name}"
        )

        content_hash = calculate_file_hash(
            file_path 
        )

        if not self.vector_store.needs_update(
            file_path,
            content_hash
        ):

            logger.info(
                f"{file.name} no ha cambiado. Se omite."
            )

            return

        if self.vector_store.get_document(
            file_path
        )["ids"]:

            logger.info(
                f"{file.name} fue modificado. Actualizando..."
            )

            self.vector_store.delete_document(
                file_path
            )

        chunks, embeddings = self.pipeline.run(
            file_path
        )

        self.vector_store.add_documents(
            chunks,
            embeddings
        )

    def ingest_folder(self, folder: str):
        """Procesa todos los archivos TXT de una carpeta."""

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
            self.ingest_file(str(file))

    def list_documents(self):
        """Devuelve los documentos indexados."""

        return self.vector_store.list_documents()
    
    def get_document_by_filename(
        self,
        filename: str
    ):
        
        return self.vector_store.get_document_by_filename(
            filename
        )