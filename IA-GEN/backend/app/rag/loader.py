from pathlib import Path

from langchain_core.documents import Document

from app.core.config import settings
from app.core.hashing import calculate_file_hash
from app.core.logger import logger
from app.rag.document_metadata import parse_document_text


class DocumentLoader:

    def __init__(
        self,
        source_root: str | Path | None = None,
    ):
        configured_root = (
            source_root
            if source_root is not None
            else settings.resolved_ingestion_source_path
        )

        self.source_root = (
            Path(configured_root)
            .expanduser()
            .resolve()
        )

    def load(self, file_path: str) -> Document:

        path = Path(file_path).expanduser().resolve()

        if not path.exists():
            raise FileNotFoundError(
                f"No existe el archivo: {file_path}"
            )

        if not path.is_file():
            raise ValueError(
                f"La ruta no corresponde a un archivo: {file_path}"
            )

        suffix = path.suffix.lower()

        if suffix == ".txt":
            return self._load_txt(path)

        if suffix == ".pdf":
            return self._load_pdf(path)

        if suffix == ".docx":
            return self._load_docx(path)

        raise ValueError(
            f"Formato no soportado: {suffix}"
        )

    def _load_txt(self, path: Path) -> Document:

        logger.info(
            "Leyendo archivo TXT: %s",
            path.name,
        )

        with path.open(
            "r",
            encoding="utf-8",
        ) as file:
            raw_text = file.read()

        parsed_document = parse_document_text(
            raw_text
        )

        relative_path = self._get_relative_path(
            path
        )

        metadata = (
            parsed_document.metadata
            .to_chroma_metadata()
        )

        metadata.update(
            {
                "source": str(path),
                "filename": path.name,
                "relative_path": relative_path,
                "content_hash": calculate_file_hash(
                    str(path)
                ),
            }
        )

        return Document(
            page_content=parsed_document.content,
            metadata=metadata,
        )

    def _get_relative_path(
        self,
        path: Path,
    ) -> str:

        try:
            relative_path = path.relative_to(
                self.source_root
            )
        except ValueError as exc:
            raise ValueError(
                "El archivo está fuera de la fuente "
                f"documental configurada: {path}"
            ) from exc

        return relative_path.as_posix()

    def _load_pdf(self, path: Path):
        ...

    def _load_docx(self, path: Path):
        ...