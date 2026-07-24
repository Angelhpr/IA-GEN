import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, call

from langchain_core.documents import Document

from app.services.ingestion_service import (
    IngestionService,
)


def create_document(
    file_path: Path,
    *,
    status: str = "published",
    content_hash: str = "hash-actual",
):
    return Document(
        page_content="Contenido educativo.",
        metadata={
            "id": "python_modulo_01_leccion_01",
            "source": str(file_path.resolve()),
            "filename": file_path.name,
            "relative_path": file_path.name,
            "content_hash": content_hash,
            "status": status,
        },
    )


class IngestionKnowledgeBaseTests(unittest.TestCase):

    def create_service(self, source_path: Path):
        service = IngestionService.__new__(
            IngestionService
        )
        service.source_path = source_path.resolve()
        service.pipeline = MagicMock()
        service.vector_store = MagicMock()

        return service

    def test_discovers_txt_files_recursively(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            source_root = Path(temp_dir)

            first_folder = (
                source_root / "00_general"
            )
            second_folder = (
                source_root
                / "01_python"
                / "01_fundamentos"
            )

            first_folder.mkdir(parents=True)
            second_folder.mkdir(parents=True)

            first_file = (
                first_folder / "bienvenida.txt"
            )
            second_file = (
                second_folder / "leccion.txt"
            )
            ignored_file = (
                second_folder / "notas.md"
            )

            first_file.write_text(
                "general",
                encoding="utf-8",
            )
            second_file.write_text(
                "python",
                encoding="utf-8",
            )
            ignored_file.write_text(
                "ignorado",
                encoding="utf-8",
            )

            service = self.create_service(
                source_root
            )
            service.ingest_file = MagicMock()
            service.vector_store.list_sources.return_value = []

            service.ingest_configured_source()

            service.ingest_file.assert_has_calls(
                [
                    call(str(first_file.resolve())),
                    call(str(second_file.resolve())),
                ]
            )
            self.assertEqual(
                service.ingest_file.call_count,
                2,
            )
            service.vector_store.delete_document.assert_not_called()

    def test_skips_draft_without_embeddings(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            source_root = Path(temp_dir)
            file_path = source_root / "borrador.txt"

            service = self.create_service(
                source_root
            )
            document = create_document(
                file_path,
                status="draft",
            )

            service.pipeline.loader.load.return_value = (
                document
            )
            service.vector_store.get_document.return_value = {
                "ids": []
            }

            service.ingest_file(str(file_path))

            service.pipeline.run_document.assert_not_called()
            service.vector_store.add_documents.assert_not_called()
            service.vector_store.delete_ids.assert_not_called()

    def test_removes_previous_version_when_unpublished(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            source_root = Path(temp_dir)
            file_path = source_root / "revision.txt"

            service = self.create_service(
                source_root
            )
            document = create_document(
                file_path,
                status="review",
            )

            service.pipeline.loader.load.return_value = (
                document
            )
            service.vector_store.get_document.return_value = {
                "ids": ["old-chunk"]
            }

            service.ingest_file(str(file_path))

            service.vector_store.delete_ids.assert_called_once_with(
                ["old-chunk"]
            )
            service.pipeline.run_document.assert_not_called()
            service.vector_store.add_documents.assert_not_called()

    def test_skips_unchanged_published_document(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            source_root = Path(temp_dir)
            file_path = source_root / "publicado.txt"

            service = self.create_service(
                source_root
            )
            document = create_document(file_path)

            service.pipeline.loader.load.return_value = (
                document
            )
            service.vector_store.get_document.return_value = {
                "ids": ["existing-chunk"]
            }
            service.vector_store.needs_update.return_value = (
                False
            )

            service.ingest_file(str(file_path))

            service.vector_store.needs_update.assert_called_once_with(
                str(file_path.resolve()),
                "hash-actual",
            )
            service.pipeline.run_document.assert_not_called()
            service.vector_store.add_documents.assert_not_called()
            service.vector_store.delete_ids.assert_not_called()

    def test_indexes_new_published_document(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            source_root = Path(temp_dir)
            file_path = source_root / "nuevo.txt"

            service = self.create_service(
                source_root
            )
            document = create_document(file_path)
            chunks = [MagicMock()]
            embeddings = [[0.1, 0.2]]

            service.pipeline.loader.load.return_value = (
                document
            )
            service.vector_store.get_document.return_value = {
                "ids": []
            }
            service.vector_store.needs_update.return_value = (
                True
            )
            service.pipeline.run_document.return_value = (
                chunks,
                embeddings,
            )
            service.vector_store.add_documents.return_value = [
                "new-chunk"
            ]

            service.ingest_file(str(file_path))

            service.vector_store.add_documents.assert_called_once_with(
                chunks,
                embeddings,
            )
            service.vector_store.delete_ids.assert_not_called()

    def test_stores_new_version_before_deleting_old(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            source_root = Path(temp_dir)
            file_path = source_root / "actualizado.txt"

            service = self.create_service(
                source_root
            )
            document = create_document(
                file_path,
                content_hash="nuevo-hash",
            )
            chunks = [MagicMock()]
            embeddings = [[0.3, 0.4]]

            service.pipeline.loader.load.return_value = (
                document
            )
            service.vector_store.get_document.return_value = {
                "ids": ["old-chunk"]
            }
            service.vector_store.needs_update.return_value = (
                True
            )
            service.pipeline.run_document.return_value = (
                chunks,
                embeddings,
            )
            service.vector_store.add_documents.return_value = [
                "new-chunk"
            ]

            service.ingest_file(str(file_path))

            add_call = call.add_documents(
                chunks,
                embeddings,
            )
            delete_call = call.delete_ids(
                ["old-chunk"]
            )

            vector_calls = (
                service.vector_store.mock_calls
            )

            self.assertLess(
                vector_calls.index(add_call),
                vector_calls.index(delete_call),
            )

    def test_keeps_old_version_when_storage_fails(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            source_root = Path(temp_dir)
            file_path = (
                source_root / "fallo_guardado.txt"
            )

            service = self.create_service(
                source_root
            )
            document = create_document(
                file_path,
                content_hash="nuevo-hash",
            )

            service.pipeline.loader.load.return_value = (
                document
            )
            service.vector_store.get_document.return_value = {
                "ids": ["old-chunk"]
            }
            service.vector_store.needs_update.return_value = (
                True
            )
            service.pipeline.run_document.return_value = (
                [MagicMock()],
                [[0.1, 0.2]],
            )
            service.vector_store.add_documents.side_effect = (
                RuntimeError("storage failed")
            )

            with self.assertRaisesRegex(
                RuntimeError,
                "storage failed",
            ):
                service.ingest_file(str(file_path))

            service.vector_store.delete_ids.assert_not_called()

    def test_rolls_back_new_version_when_old_delete_fails(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            source_root = Path(temp_dir)
            file_path = (
                source_root / "fallo_eliminacion.txt"
            )

            service = self.create_service(
                source_root
            )
            document = create_document(
                file_path,
                content_hash="nuevo-hash",
            )

            service.pipeline.loader.load.return_value = (
                document
            )
            service.vector_store.get_document.return_value = {
                "ids": ["old-chunk"]
            }
            service.vector_store.needs_update.return_value = (
                True
            )
            service.pipeline.run_document.return_value = (
                [MagicMock()],
                [[0.1, 0.2]],
            )
            service.vector_store.add_documents.return_value = [
                "new-chunk"
            ]
            service.vector_store.delete_ids.side_effect = [
                RuntimeError("delete failed"),
                None,
            ]

            with self.assertRaisesRegex(
                RuntimeError,
                "delete failed",
            ):
                service.ingest_file(str(file_path))

            self.assertEqual(
                service.vector_store.delete_ids.call_args_list,
                [
                    call(["old-chunk"]),
                    call(["new-chunk"]),
                ],
            )

    def test_does_not_delete_old_when_no_new_ids_exist(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            source_root = Path(temp_dir)
            file_path = source_root / "sin_chunks.txt"

            service = self.create_service(
                source_root
            )
            document = create_document(
                file_path,
                content_hash="nuevo-hash",
            )

            service.pipeline.loader.load.return_value = (
                document
            )
            service.vector_store.get_document.return_value = {
                "ids": ["old-chunk"]
            }
            service.vector_store.needs_update.return_value = (
                True
            )
            service.pipeline.run_document.return_value = (
                [],
                [],
            )
            service.vector_store.add_documents.return_value = []

            with self.assertRaisesRegex(
                ValueError,
                "chunks indexables",
            ):
                service.ingest_file(str(file_path))

            service.vector_store.delete_ids.assert_not_called()

    def test_removes_orphan_after_successful_scan(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            source_root = Path(temp_dir)
            current_file = source_root / "actual.txt"

            current_file.write_text(
                "contenido",
                encoding="utf-8",
            )

            orphan_source = str(
                (
                    source_root / "eliminado.txt"
                ).resolve()
            )

            service = self.create_service(
                source_root
            )
            service.ingest_file = MagicMock()
            service.vector_store.list_sources.return_value = [
                str(current_file.resolve()),
                orphan_source,
            ]

            service.ingest_configured_source()

            service.vector_store.delete_document.assert_called_once_with(
                orphan_source
            )

    def test_does_not_clean_orphans_after_ingestion_failure(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            source_root = Path(temp_dir)
            file_path = source_root / "invalido.txt"

            file_path.write_text(
                "contenido",
                encoding="utf-8",
            )

            service = self.create_service(
                source_root
            )
            service.ingest_file = MagicMock(
                side_effect=RuntimeError(
                    "ingestion failed"
                )
            )

            with self.assertRaisesRegex(
                RuntimeError,
                "ingestion failed",
            ):
                service.ingest_configured_source()

            service.vector_store.list_sources.assert_not_called()
            service.vector_store.delete_document.assert_not_called()


if __name__ == "__main__":
    unittest.main()
