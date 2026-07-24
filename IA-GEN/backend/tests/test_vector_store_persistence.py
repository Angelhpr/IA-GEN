import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

from langchain_core.documents import Document

import app.core.config as config_module
from app.core.config import settings
from app.rag.vector_store import VectorStore


def create_chunk(
    *,
    document_id: str,
    filename: str = "leccion.txt",
    content_hash: str = "abcdef1234567890",
    chunk_index: int = 0,
):
    return Document(
        page_content="Contenido educativo.",
        metadata={
            "id": document_id,
            "filename": filename,
            "relative_path": filename,
            "source": str(
                Path(filename).resolve()
            ),
            "content_hash": content_hash,
            "chunk_index": chunk_index,
        },
    )


class ConfigPathTests(unittest.TestCase):

    def test_resolves_relative_vector_path_from_backend(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            backend_root = Path(temp_dir)

            with patch.object(
                config_module,
                "BACKEND_ROOT",
                backend_root,
            ):
                with patch.object(
                    settings,
                    "VECTOR_DB_PATH",
                    "data/vector_db",
                ):
                    result = (
                        settings
                        .resolved_vector_db_path
                    )

            self.assertEqual(
                result,
                (
                    backend_root
                    / "data"
                    / "vector_db"
                ).resolve(),
            )

    def test_preserves_absolute_vector_path(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            absolute_path = (
                Path(temp_dir)
                / "persistent"
                / "vector_db"
            ).resolve()

            with patch.object(
                settings,
                "VECTOR_DB_PATH",
                str(absolute_path),
            ):
                result = (
                    settings
                    .resolved_vector_db_path
                )

            self.assertEqual(
                result,
                absolute_path,
            )


class VectorStorePersistenceTests(unittest.TestCase):

    def create_store(self):
        store = VectorStore.__new__(
            VectorStore
        )
        store.collection = MagicMock()

        return store

    def test_generates_id_from_editorial_document_id(self):
        store = self.create_store()
        chunk = create_chunk(
            document_id=(
                "python_modulo_01_leccion_01"
            ),
            chunk_index=3,
        )

        chunk_id = store._generate_chunk_id(
            chunk,
            0,
        )

        self.assertEqual(
            chunk_id,
            (
                "python_modulo_01_leccion_01_"
                "abcdef12_chunk_3"
            ),
        )

    def test_same_filename_can_belong_to_different_courses(self):
        store = self.create_store()

        python_chunk = create_chunk(
            document_id=(
                "python_descripcion_curso"
            ),
            filename="00_descripcion_curso.txt",
        )
        machine_learning_chunk = create_chunk(
            document_id=(
                "machine_learning_descripcion_curso"
            ),
            filename="00_descripcion_curso.txt",
        )

        python_id = store._generate_chunk_id(
            python_chunk,
            0,
        )
        machine_learning_id = (
            store._generate_chunk_id(
                machine_learning_chunk,
                0,
            )
        )

        self.assertNotEqual(
            python_id,
            machine_learning_id,
        )

    def test_add_documents_returns_stored_ids(self):
        store = self.create_store()

        chunks = [
            create_chunk(
                document_id=(
                    "python_modulo_01_leccion_01"
                ),
                chunk_index=0,
            ),
            create_chunk(
                document_id=(
                    "python_modulo_01_leccion_01"
                ),
                chunk_index=1,
            ),
        ]
        embeddings = [
            [0.1, 0.2],
            [0.3, 0.4],
        ]

        ids = store.add_documents(
            chunks,
            embeddings,
        )

        self.assertEqual(
            ids,
            [
                (
                    "python_modulo_01_leccion_01_"
                    "abcdef12_chunk_0"
                ),
                (
                    "python_modulo_01_leccion_01_"
                    "abcdef12_chunk_1"
                ),
            ],
        )

        store.collection.add.assert_called_once_with(
            ids=ids,
            documents=[
                "Contenido educativo.",
                "Contenido educativo.",
            ],
            embeddings=embeddings,
            metadatas=[
                chunks[0].metadata,
                chunks[1].metadata,
            ],
        )

    def test_rejects_mismatched_chunks_and_embeddings(self):
        store = self.create_store()

        with self.assertRaisesRegex(
            ValueError,
            "debe coincidir",
        ):
            store.add_documents(
                [
                    create_chunk(
                        document_id="python_leccion"
                    )
                ],
                [],
            )

        store.collection.add.assert_not_called()

    def test_deletes_records_by_explicit_ids(self):
        store = self.create_store()

        store.delete_ids(
            ["old_chunk_0", "old_chunk_1"]
        )

        store.collection.delete.assert_called_once_with(
            ids=[
                "old_chunk_0",
                "old_chunk_1",
            ]
        )

    def test_empty_id_list_does_not_delete(self):
        store = self.create_store()

        store.delete_ids([])

        store.collection.delete.assert_not_called()

    def test_lists_unique_sources(self):
        store = self.create_store()

        store.collection.get.return_value = {
            "ids": ["1", "2", "3"],
            "metadatas": [
                {
                    "source": (
                        "C:/knowledge/python.txt"
                    )
                },
                {
                    "source": (
                        "C:/knowledge/python.txt"
                    )
                },
                {
                    "source": (
                        "C:/knowledge/ml.txt"
                    )
                },
            ],
        }

        sources = store.list_sources()

        self.assertEqual(
            sources,
            [
                "C:/knowledge/ml.txt",
                "C:/knowledge/python.txt",
            ],
        )


if __name__ == "__main__":
    unittest.main()
