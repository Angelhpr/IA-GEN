from google import genai

from app.core.config import settings


class EmbeddingGenerator:

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    def generate(self, text: str) -> list[float]:

        response = self.client.models.embed_content(
            model="models/gemini-embedding-2",
            contents=text
        )

        return response.embeddings[0].values