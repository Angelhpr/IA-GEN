import unittest
from textwrap import dedent

from app.rag.document_metadata import (
    DocumentMetadataError,
    parse_document_text,
)


VALID_DOCUMENT = dedent(
    """\
    ---
    id: python_modulo_01_leccion_01
    title: Introducción a Python
    course: python
    module: fundamentos
    lesson: introduccion_a_python
    topic: conceptos_basicos
    level: principiante
    document_type: lesson
    language: es
    version: 1.0
    status: published
    prerequisites: ninguno
    estimated_minutes: 20
    keywords: python, programacion, sintaxis
    source_reference: documentacion_oficial_python
    updated_at: 2026-07-24
    ---

    # Introducción a Python

    Python es un lenguaje de programación.
    """
)


class DocumentMetadataTests(unittest.TestCase):

    def test_parses_valid_document(self):
        result = parse_document_text(
            VALID_DOCUMENT
        )

        self.assertEqual(
            result.metadata.id,
            "python_modulo_01_leccion_01",
        )
        self.assertEqual(
            result.metadata.title,
            "Introducción a Python",
        )
        self.assertEqual(
            result.metadata.course,
            "python",
        )
        self.assertEqual(
            result.metadata.version,
            "1.0",
        )
        self.assertEqual(
            result.metadata.status,
            "published",
        )
        self.assertEqual(
            result.metadata.estimated_minutes,
            20,
        )
        self.assertEqual(
            result.metadata.updated_at,
            "2026-07-24",
        )
        self.assertTrue(
            result.content.startswith(
                "# Introducción a Python"
            )
        )
        self.assertNotIn(
            "status: published",
            result.content,
        )

    def test_preserves_unicode_content(self):
        result = parse_document_text(
            VALID_DOCUMENT
        )

        self.assertIn(
            "programación",
            result.content,
        )

    def test_accepts_approved_non_published_status(self):
        document = VALID_DOCUMENT.replace(
            "status: published",
            "status: review",
        )

        result = parse_document_text(document)

        self.assertEqual(
            result.metadata.status,
            "review",
        )

    def test_exports_chroma_compatible_metadata(self):
        result = parse_document_text(
            VALID_DOCUMENT
        )

        metadata = (
            result.metadata.to_chroma_metadata()
        )

        self.assertEqual(
            metadata["course"],
            "python",
        )
        self.assertEqual(
            metadata["version"],
            "1.0",
        )
        self.assertEqual(
            metadata["updated_at"],
            "2026-07-24",
        )

    def test_rejects_missing_opening_delimiter(self):
        document = VALID_DOCUMENT.removeprefix(
            "---\n"
        )

        with self.assertRaises(
            DocumentMetadataError
        ):
            parse_document_text(document)

    def test_rejects_missing_closing_delimiter(self):
        document = VALID_DOCUMENT.replace(
            "\n---\n\n# Introducción",
            "\n\n# Introducción",
            1,
        )

        with self.assertRaises(
            DocumentMetadataError
        ):
            parse_document_text(document)

    def test_rejects_invalid_yaml(self):
        document = VALID_DOCUMENT.replace(
            "title: Introducción a Python",
            "title: [Introducción a Python",
        )

        with self.assertRaises(
            DocumentMetadataError
        ):
            parse_document_text(document)

    def test_rejects_non_mapping_metadata(self):
        document = dedent(
            """\
            ---
            - python
            - fundamentos
            ---

            Contenido.
            """
        )

        with self.assertRaises(
            DocumentMetadataError
        ):
            parse_document_text(document)

    def test_rejects_missing_required_field(self):
        document = VALID_DOCUMENT.replace(
            "course: python\n",
            "",
        )

        with self.assertRaisesRegex(
            DocumentMetadataError,
            "course",
        ):
            parse_document_text(document)

    def test_rejects_invalid_controlled_value(self):
        document = VALID_DOCUMENT.replace(
            "level: principiante",
            "level: experto",
        )

        with self.assertRaisesRegex(
            DocumentMetadataError,
            "level",
        ):
            parse_document_text(document)

    def test_rejects_unknown_metadata_field(self):
        document = VALID_DOCUMENT.replace(
            "status: published",
            (
                "status: published\n"
                "unknown_field: value"
            ),
        )

        with self.assertRaisesRegex(
            DocumentMetadataError,
            "unknown_field",
        ):
            parse_document_text(document)

    def test_rejects_invalid_technical_name(self):
        document = VALID_DOCUMENT.replace(
            "module: fundamentos",
            "module: Fundamentos Básicos",
        )

        with self.assertRaisesRegex(
            DocumentMetadataError,
            "module",
        ):
            parse_document_text(document)


if __name__ == "__main__":
    unittest.main()