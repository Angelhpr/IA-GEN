from dataclasses import dataclass
from datetime import date
from typing import Literal

import yaml
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    ValidationError,
    field_validator,
)


Course = Literal[
    "general",
    "python",
    "machine_learning",
    "ia_generativa_rag",
    "oracle_cloud",
    "shared",
]

Level = Literal[
    "principiante",
    "intermedio",
    "avanzado",
    "general",
]

DocumentType = Literal[
    "welcome",
    "catalog",
    "course_description",
    "lesson",
    "exercise",
    "summary",
    "project",
    "faq",
    "glossary",
    "resource",
]

DocumentStatus = Literal[
    "draft",
    "review",
    "published",
    "deprecated",
]

TECHNICAL_NAME_PATTERN = r"^[a-z0-9]+(?:_[a-z0-9]+)*$"


class DocumentMetadataError(ValueError):
    """Error producido por metadatos documentales inválidos."""


class DocumentMetadata(BaseModel):
    """Metadatos editoriales de un documento de IA-GEN."""

    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
    )

    id: str = Field(
        min_length=1,
        pattern=TECHNICAL_NAME_PATTERN,
    )
    title: str = Field(min_length=1)
    course: Course
    module: str = Field(
        min_length=1,
        pattern=TECHNICAL_NAME_PATTERN,
    )
    lesson: str = Field(
        min_length=1,
        pattern=TECHNICAL_NAME_PATTERN,
    )
    topic: str = Field(
        min_length=1,
        pattern=TECHNICAL_NAME_PATTERN,
    )
    level: Level
    document_type: DocumentType
    language: Literal["es"]
    version: str = Field(
        pattern=r"^\d+\.\d+$",
    )
    status: DocumentStatus

    prerequisites: str | None = None
    estimated_minutes: int | None = Field(
        default=None,
        ge=1,
    )
    keywords: str | None = None
    source_reference: str | None = None
    updated_at: str | None = Field(
        default=None,
        pattern=r"^\d{4}-\d{2}-\d{2}$",
    )

    @field_validator("version", mode="before")
    @classmethod
    def normalize_version(cls, value):
        if value is None:
            return value

        return str(value)

    @field_validator("updated_at", mode="before")
    @classmethod
    def normalize_updated_at(cls, value):
        if isinstance(value, date):
            return value.isoformat()

        return value

    def to_chroma_metadata(self) -> dict:
        """Devuelve metadatos compatibles con ChromaDB."""

        return self.model_dump(
            mode="json",
            exclude_none=True,
        )


@dataclass(frozen=True)
class ParsedDocument:
    """Resultado de separar metadatos y contenido educativo."""

    metadata: DocumentMetadata
    content: str


def parse_document_text(text: str) -> ParsedDocument:
    """
    Lee un documento con front matter YAML delimitado por ---.

    El bloque debe encontrarse al inicio del archivo.
    """

    normalized_text = (
        text.replace("\r\n", "\n")
        .replace("\r", "\n")
    )
    lines = normalized_text.split("\n")

    if not lines or lines[0].strip() != "---":
        raise DocumentMetadataError(
            "El documento debe comenzar con un bloque de "
            "metadatos delimitado por ---."
        )

    closing_index = None

    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            closing_index = index
            break

    if closing_index is None:
        raise DocumentMetadataError(
            "No se encontró el delimitador de cierre "
            "del bloque de metadatos."
        )

    metadata_text = "\n".join(
        lines[1:closing_index]
    )

    try:
        raw_metadata = yaml.safe_load(metadata_text)
    except yaml.YAMLError as exc:
        raise DocumentMetadataError(
            "El bloque de metadatos contiene YAML inválido."
        ) from exc

    if not isinstance(raw_metadata, dict):
        raise DocumentMetadataError(
            "El bloque de metadatos debe contener "
            "un objeto de claves y valores."
        )

    try:
        metadata = DocumentMetadata.model_validate(
            raw_metadata
        )
    except ValidationError as exc:
        details = []

        for error in exc.errors():
            location = ".".join(
                str(part)
                for part in error["loc"]
            )
            details.append(
                f"{location}: {error['msg']}"
            )

        raise DocumentMetadataError(
            "Metadatos inválidos: "
            + "; ".join(details)
        ) from exc

    content = "\n".join(
        lines[closing_index + 1:]
    ).lstrip("\n")

    return ParsedDocument(
        metadata=metadata,
        content=content,
    )