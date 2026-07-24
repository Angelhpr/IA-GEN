from collections.abc import Sequence
from pathlib import Path

from chromadb import PersistentClient
from chromadb.config import Settings

from app.core.config import settings
from app.core.logger import logger


class VectorStore:

    def __init__(self):

        db_path = settings.resolved_vector_db_path

        db_path.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.client = PersistentClient(
            path=str(db_path),
            settings=Settings(
                anonymized_telemetry=False
            ),
        )

        self.collection = (
            self.client.get_or_create_collection(
                name="ia_gen_documents"
            )
        )

    def _generate_chunk_id(
        self,
        chunk,
        index: int,
    ) -> str:

        document_id = chunk.metadata["id"]
        content_hash = (
            chunk.metadata["content_hash"][:8]
        )
        chunk_index = chunk.metadata.get(
            "chunk_index",
            index,
        )

        return (
            f"{document_id}_"
            f"{content_hash}_"
            f"chunk_{chunk_index}"
        )

    def add_documents(
        self,
        chunks,
        embeddings,
    ) -> list[str]:

        if len(chunks) != len(embeddings):
            raise ValueError(
                "La cantidad de chunks y embeddings "
                "debe coincidir."
            )

        if not chunks:
            return []

        ids = []
        documents = []
        metadatas = []

        for index, chunk in enumerate(chunks):
            chunk_id = self._generate_chunk_id(
                chunk,
                index,
            )

            ids.append(chunk_id)
            documents.append(
                chunk.page_content
            )
            metadatas.append(
                chunk.metadata
            )

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
        )

        logger.info(
            "IDs almacenados: %s",
            ids,
        )
        logger.info(
            "%s chunks almacenados en ChromaDB",
            len(ids),
        )

        return ids

    def query(
        self,
        embedding,
        k: int = 3,
    ):

        return self.collection.query(
            query_embeddings=[embedding],
            n_results=k,
        )

    def count(self):

        return self.collection.count()

    def document_exists(
        self,
        source: str,
    ) -> bool:

        results = self.get_document(source)

        return bool(results["ids"])

    def get_document(
        self,
        source: str,
    ):

        normalized_source = str(
            Path(source).resolve()
        )

        return self.collection.get(
            where={
                "source": normalized_source,
            }
        )

    def delete_ids(
        self,
        ids: Sequence[str],
    ) -> None:
        """
        Elimina únicamente los registros indicados.

        Se utiliza durante el reemplazo seguro para
        retirar los chunks de una versión anterior.
        """

        normalized_ids = list(ids)

        if not normalized_ids:
            return

        self.collection.delete(
            ids=normalized_ids
        )

        logger.info(
            "%s chunks eliminados por ID",
            len(normalized_ids),
        )

    def delete_document(
        self,
        source: str,
    ) -> None:

        normalized_source = str(
            Path(source).resolve()
        )

        self.collection.delete(
            where={
                "source": normalized_source,
            }
        )

        logger.info(
            "Documento eliminado: %s",
            normalized_source,
        )

    def needs_update(
        self,
        source: str,
        new_hash: str,
    ) -> bool:

        results = self.get_document(source)

        if not results["ids"]:
            return True

        stored_hash = (
            results["metadatas"][0]
            ["content_hash"]
        )

        return stored_hash != new_hash

    def show_all(self):

        return self.collection.get()

    def list_sources(self) -> list[str]:
        """
        Devuelve las rutas fuente únicas almacenadas
        en la colección.
        """

        results = self.collection.get()
        metadatas = (
            results.get("metadatas") or []
        )

        sources = {
            metadata["source"]
            for metadata in metadatas
            if metadata
            and metadata.get("source")
        }

        return sorted(sources)

    def list_documents(self):

        results = self.collection.get()

        if not results["metadatas"]:
            return []

        filenames = {
            metadata["filename"]
            for metadata in results["metadatas"]
        }

        return sorted(filenames)

    def get_document_by_filename(
        self,
        filename: str,
    ):

        return self.collection.get(
            where={
                "filename": filename,
            }
        )
