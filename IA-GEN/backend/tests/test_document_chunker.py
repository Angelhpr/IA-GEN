import unittest

from langchain_core.documents import Document

from app.rag.chunker import DocumentChunker


class DocumentChunkerTests(unittest.TestCase):

    def test_preserves_document_metadata(self):
        document = Document(
            page_content="Texto educativo breve.",
            metadata={
                "id": "python_modulo_01_leccion_01",
                "course": "python",
                "status": "published",
            },
        )

        chunks = DocumentChunker(
            chunk_size=100,
            chunk_overlap=20,
        ).split(document)

        self.assertEqual(len(chunks), 1)
        self.assertEqual(
            chunks[0].metadata["id"],
            "python_modulo_01_leccion_01",
        )
        self.assertEqual(
            chunks[0].metadata["course"],
            "python",
        )
        self.assertEqual(
            chunks[0].metadata["status"],
            "published",
        )

    def test_adds_sequential_chunk_index(self):
        document = Document(
            page_content=(
                "Primer bloque de contenido educativo. "
                "Segundo bloque de contenido educativo. "
                "Tercer bloque de contenido educativo."
            ),
            metadata={
                "id": "python_modulo_01_leccion_01",
            },
        )

        chunks = DocumentChunker(
            chunk_size=45,
            chunk_overlap=5,
        ).split(document)

        self.assertGreater(len(chunks), 1)

        self.assertEqual(
            [
                chunk.metadata["chunk_index"]
                for chunk in chunks
            ],
            list(range(len(chunks))),
        )

    def test_does_not_modify_original_metadata(self):
        original_metadata = {
            "id": "python_modulo_01_leccion_01",
            "course": "python",
        }

        document = Document(
            page_content=(
                "Contenido suficientemente largo para "
                "producir varios fragmentos de prueba."
            ),
            metadata=original_metadata.copy(),
        )

        DocumentChunker(
            chunk_size=30,
            chunk_overlap=5,
        ).split(document)

        self.assertNotIn(
            "chunk_index",
            document.metadata,
        )
        self.assertEqual(
            document.metadata,
            original_metadata,
        )


if __name__ == "__main__":
    unittest.main()