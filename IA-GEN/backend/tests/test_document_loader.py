import tempfile
import unittest
from pathlib import Path
from textwrap import dedent

from app.core.hashing import calculate_file_hash
from app.rag.document_metadata import (
    DocumentMetadataError,
)
from app.rag.loader import DocumentLoader


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


class DocumentLoaderTests(unittest.TestCase):

    def test_loads_txt_with_editorial_metadata(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            source_root = Path(temp_dir)

            lesson_folder = (
                source_root
                / "01_python"
                / "01_fundamentos"
            )
            lesson_folder.mkdir(
                parents=True
            )

            file_path = (
                lesson_folder
                / "01_introduccion_a_python.txt"
            )
            file_path.write_text(
                VALID_DOCUMENT,
                encoding="utf-8",
            )

            loader = DocumentLoader(
                source_root=source_root
            )
            document = loader.load(
                str(file_path)
            )

            self.assertEqual(
                document.metadata["id"],
                "python_modulo_01_leccion_01",
            )
            self.assertEqual(
                document.metadata["title"],
                "Introducción a Python",
            )
            self.assertEqual(
                document.metadata["course"],
                "python",
            )
            self.assertEqual(
                document.metadata["status"],
                "published",
            )
            self.assertEqual(
                document.metadata[
                    "estimated_minutes"
                ],
                20,
            )

    def test_removes_front_matter_from_content(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            source_root = Path(temp_dir)
            file_path = (
                source_root / "leccion.txt"
            )
            file_path.write_text(
                VALID_DOCUMENT,
                encoding="utf-8",
            )

            document = DocumentLoader(
                source_root=source_root
            ).load(str(file_path))

            self.assertTrue(
                document.page_content.startswith(
                    "# Introducción a Python"
                )
            )
            self.assertNotIn(
                "status: published",
                document.page_content,
            )
            self.assertIn(
                "programación",
                document.page_content,
            )

    def test_adds_technical_metadata(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            source_root = Path(temp_dir)

            nested_folder = (
                source_root
                / "01_python"
                / "01_fundamentos"
            )
            nested_folder.mkdir(
                parents=True
            )

            file_path = (
                nested_folder
                / "01_introduccion_a_python.txt"
            )
            file_path.write_text(
                VALID_DOCUMENT,
                encoding="utf-8",
            )

            document = DocumentLoader(
                source_root=source_root
            ).load(str(file_path))

            self.assertEqual(
                document.metadata["source"],
                str(file_path.resolve()),
            )
            self.assertEqual(
                document.metadata["filename"],
                file_path.name,
            )
            self.assertEqual(
                document.metadata["relative_path"],
                (
                    "01_python/01_fundamentos/"
                    "01_introduccion_a_python.txt"
                ),
            )
            self.assertEqual(
                document.metadata["content_hash"],
                calculate_file_hash(
                    str(file_path)
                ),
            )

    def test_accepts_valid_non_published_document(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            source_root = Path(temp_dir)
            file_path = (
                source_root / "borrador.txt"
            )

            file_path.write_text(
                VALID_DOCUMENT.replace(
                    "status: published",
                    "status: draft",
                ),
                encoding="utf-8",
            )

            document = DocumentLoader(
                source_root=source_root
            ).load(str(file_path))

            self.assertEqual(
                document.metadata["status"],
                "draft",
            )

    def test_rejects_invalid_metadata(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            source_root = Path(temp_dir)
            file_path = (
                source_root / "invalido.txt"
            )

            file_path.write_text(
                VALID_DOCUMENT.replace(
                    "course: python\n",
                    "",
                ),
                encoding="utf-8",
            )

            loader = DocumentLoader(
                source_root=source_root
            )

            with self.assertRaises(
                DocumentMetadataError
            ):
                loader.load(str(file_path))

    def test_rejects_file_outside_source_root(self):
        with tempfile.TemporaryDirectory() as source_dir:
            with tempfile.TemporaryDirectory() as external_dir:
                source_root = Path(source_dir)
                external_file = (
                    Path(external_dir)
                    / "externo.txt"
                )

                external_file.write_text(
                    VALID_DOCUMENT,
                    encoding="utf-8",
                )

                loader = DocumentLoader(
                    source_root=source_root
                )

                with self.assertRaisesRegex(
                    ValueError,
                    "fuera de la fuente documental",
                ):
                    loader.load(
                        str(external_file)
                    )

    def test_rejects_missing_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            source_root = Path(temp_dir)
            missing_file = (
                source_root / "no_existe.txt"
            )

            loader = DocumentLoader(
                source_root=source_root
            )

            with self.assertRaises(
                FileNotFoundError
            ):
                loader.load(
                    str(missing_file)
                )

    def test_rejects_unsupported_extension(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            source_root = Path(temp_dir)
            file_path = (
                source_root / "documento.md"
            )

            file_path.write_text(
                "Contenido",
                encoding="utf-8",
            )

            loader = DocumentLoader(
                source_root=source_root
            )

            with self.assertRaisesRegex(
                ValueError,
                "Formato no soportado",
            ):
                loader.load(str(file_path))


if __name__ == "__main__":
    unittest.main()