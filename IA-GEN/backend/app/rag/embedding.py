from collections.abc import Sequence

from google import genai

from app.core.config import settings
from google.genai import types

class EmbeddingGenerator:

    DEFAULT_BATCH_SIZE = 50

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    def generate(self, text: str) -> list[float]:
        return self.generate_batch([text])[0]

    def generate_batch(
        self,
        texts: Sequence[str],
        batch_size: int = DEFAULT_BATCH_SIZE,
    ) -> list[list[float]]:
        normalized_texts = list(texts)

        if not normalized_texts:
            return []

        if batch_size < 1:
            raise ValueError(
                "El tamaño del lote debe ser mayor que cero."
            )

        vectors: list[list[float]] = []

        for start in range(
            0,
            len(normalized_texts),
            batch_size,
        ):
            batch = normalized_texts[
                start:start + batch_size
            ]

            batch_contents = [
                types.Content(
                    role="user",
                    parts=[
                        types.Part.from_text(text=text)
                    ],
                )
                for text in batch
            ]

            response = self.client.models.embed_content(
                model="models/gemini-embedding-2",
                contents=batch_contents,
            )

            batch_vectors = [
                list(embedding.values or [])
                for embedding in (
                    response.embeddings or []
                )
            ]

            if len(batch_vectors) != len(batch):
                raise ValueError(
                    "Gemini devolvió una cantidad inesperada "
                    "de embeddings."
                )

            vectors.extend(batch_vectors)

        return vectors
