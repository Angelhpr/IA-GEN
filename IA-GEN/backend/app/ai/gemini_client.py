from google import genai

from app.core.config import settings
from app.core.logger import logger


class GeminiClient:

    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    def generate(self, prompt: str) -> str:

        try:

            logger.info(
                f"Generando respuesta con {settings.MODEL_NAME}"
            )

            response = self.client.models.generate_content(
                model=settings.MODEL_NAME,
                contents=prompt
            )

            if not response.text:

                raise RuntimeError(
                    "Gemini no devolvió ningún contenido."
                )

            return response.text.strip()

        except Exception as e:

            logger.exception(
                "Error comunicándose con Gemini"
            )

            raise RuntimeError(
                "No fue posible comunicarse con Gemini."
            ) from e