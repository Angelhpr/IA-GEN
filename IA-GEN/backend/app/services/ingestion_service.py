from pathlib import Path

from app.core.exceptions import (
    IngestionSourceUnavailableError,
)
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
        Procesa un documento y actualiza la base
        vectorial de forma segura.

        La nueva versión se almacena antes de retirar
        los chunks de la versión anterior.
        """

        file = Path(file_path).resolve()

        logger.info(
            "Procesando: %s",
            file.name,
        )

        document = self.pipeline.loader.load(
            str(file)
        )

        source = document.metadata["source"]
        content_hash = document.metadata[
            "content_hash"
        ]
        status = document.metadata["status"]

        existing_document = (
            self.vector_store.get_document(source)
        )
        old_ids = list(
            existing_document.get("ids") or []
        )

        if status != "published":
            logger.info(
                (
                    "%s no está publicado "
                    "(status=%s). Se omite."
                ),
                file.name,
                status,
            )

            if old_ids:
                self.vector_store.delete_ids(
                    old_ids
                )

                logger.info(
                    (
                        "Se eliminó la versión indexada "
                        "de %s."
                    ),
                    file.name,
                )

            return

        if not self.vector_store.needs_update(
            source,
            content_hash,
        ):
            logger.info(
                "%s no ha cambiado. Se omite.",
                file.name,
            )
            return

        chunks, embeddings = (
            self.pipeline.run_document(document)
        )

        new_ids = self.vector_store.add_documents(
            chunks,
            embeddings,
        )

        if not new_ids:
            raise ValueError(
                "El documento no generó chunks "
                f"indexables: {file.name}"
            )

        if not old_ids:
            logger.info(
                "Nuevo documento indexado: %s",
                file.name,
            )
            return

        try:
            self.vector_store.delete_ids(
                old_ids
            )
        except Exception:
            logger.exception(
                (
                    "No se pudieron retirar los chunks "
                    "anteriores de %s. Revirtiendo la "
                    "nueva versión."
                ),
                file.name,
            )

            try:
                self.vector_store.delete_ids(
                    new_ids
                )
            except Exception:
                logger.exception(
                    (
                        "No se pudieron revertir los "
                        "chunks nuevos de %s."
                    ),
                    file.name,
                )

            raise

        logger.info(
            "Documento actualizado de forma segura: %s",
            file.name,
        )

    def _remove_orphaned_documents(
        self,
        current_sources: set[str],
    ) -> None:
        """
        Elimina de ChromaDB documentos cuyo archivo
        fuente ya no existe dentro de la Knowledge Base.
        """

        indexed_sources = set(
            self.vector_store.list_sources()
        )

        orphaned_sources = sorted(
            indexed_sources - current_sources
        )

        for source in orphaned_sources:
            logger.info(
                "Eliminando documento huérfano: %s",
                source,
            )

            self.vector_store.delete_document(
                source
            )

        logger.info(
            "Documentos huérfanos eliminados: %s",
            len(orphaned_sources),
        )

    def ingest_configured_source(self):
        """
        Procesa recursivamente los archivos TXT de la
        fuente documental configurada.

        La limpieza de huérfanos se ejecuta únicamente
        cuando todos los archivos terminan sin errores.
        """

        folder_path = self.source_path

        if (
            not folder_path.exists()
            or not folder_path.is_dir()
        ):
            logger.error(
                "Fuente documental inválida: %s",
                folder_path,
            )

            raise IngestionSourceUnavailableError()

        txt_files = sorted(
            (
                file.resolve()
                for file in folder_path.rglob("*.txt")
                if file.is_file()
            ),
            key=lambda file: file.as_posix(),
        )

        logger.info(
            "Se encontraron %s archivos TXT",
            len(txt_files),
        )

        current_sources = {
            str(file)
            for file in txt_files
        }

        for file in txt_files:
            self.ingest_file(str(file))

        self._remove_orphaned_documents(
            current_sources
        )

    def list_documents(self):
        """Devuelve los documentos indexados."""

        return self.vector_store.list_documents()

    def get_document_by_filename(
        self,
        filename: str,
    ):
        return (
            self.vector_store
            .get_document_by_filename(filename)
        )
