from pathlib import Path

from app.core.exceptions import IngestionSourceUnavailableError
from app.core.hashing import calculate_file_hash
from app.core.logger import logger
from app.rag.ingestion import IngestionPipeline
from app.rag.vector_store import VectorStore


class IngestionService:

    def __init__(self, source_path: Path):

        self.source_path = source_path.resolve()
        self.pipeline = IngestionPipeline()
        self.vector_store = VectorStore()

    def ingest_file(self, file_path: str):
        """
        Procesa un unico documento y actualiza la base vectorial
        si ha cambiado.
        """

        file = Path(file_path)

        logger.info(
            "Procesando: %s",
            file.name,
        )

        content_hash = calculate_file_hash(
            file_path
        )

        if not self.vector_store.needs_update(
            file_path,
            content_hash,
        ):

            logger.info(
                "%s no ha cambiado. Se omite.",
                file.name,
            )

            return

        if self.vector_store.get_document(
            file_path
        )["ids"]:

            logger.info(
                "%s fue modificado. Actualizando...",
                file.name,
            )

            self.vector_store.delete_document(
                file_path
            )

        chunks, embeddings = self.pipeline.run(
            file_path
        )

        self.vector_store.add_documents(
            chunks,
            embeddings,
        )

    def ingest_configured_source(self):
        """
        Procesa los archivos TXT de la fuente configurada
        por el servidor.
        """

        folder_path = self.source_path

        if not folder_path.exists() or not folder_path.is_dir():
            logger.error(
                "Fuente documental invalida: %s",
                folder_path,
            )

            raise IngestionSourceUnavailableError()

        txt_files = sorted(
            file
            for file in folder_path.glob("*.txt")
            if file.is_file()
        )

        logger.info(
            "Se encontraron %s archivos TXT",
            len(txt_files),
        )

        for file in txt_files:
            self.ingest_file(str(file))

    def list_documents(self):
        """Devuelve los documentos indexados."""

        return self.vector_store.list_documents()

    def get_document_by_filename(
        self,
        filename: str,
    ):

        return self.vector_store.get_document_by_filename(
            filename
        )