from pathlib import Path

from langchain_core.documents import Document

from app.core.logger import logger

from app.core.hashing import calculate_file_hash

class DocumentLoader:

    def load(self, file_path: str) -> Document:

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"No existe el archivo: {file_path}")

        suffix = path.suffix.lower()

        if suffix == ".txt":
            return self._load_txt(path)

        elif suffix == ".pdf":
            return self._load_pdf(path)

        elif suffix == ".docx":
            return self._load_docx(path)

        raise ValueError(f"Formato no soportado: {suffix}")

    def _load_txt(self, path: Path) -> Document:

        logger.info(f"Leyendo archivo TXT: {path.name}")

        with path.open("r", encoding="utf-8") as file:
            text = file.read()

        return Document(
            page_content=text,
            metadata={
                "source": str(path.resolve()),
                "filename": path.name,
                "content_hash": calculate_file_hash(
                    str(path.resolve())
                )
            }
        )

    def _load_pdf(self, path: Path):
        ...

    def _load_docx(self, path: Path):
        ...