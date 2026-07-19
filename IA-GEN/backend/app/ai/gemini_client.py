from google import genai
from google.genai import errors as genai_errors

from app.core.config import settings
from app.core.exceptions import AIServiceUnavailableError
from app.core.logger import logger


class GeminiClient:

    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    def generate(self, prompt: str) -> str:

        try:
            logger.info(
                "Generando respuesta con %s",
                settings.MODEL_NAME,
            )

            response = self.client.models.generate_content(
                model=settings.MODEL_NAME,
                contents=prompt,
            )

            if not response.text:
                raise AIServiceUnavailableError(
                    "El asistente no generó una respuesta válida.",
                    code="AI_EMPTY_RESPONSE",
                    retryable=True,
                )

            return response.text.strip()

        except AIServiceUnavailableError:
            raise

        except genai_errors.ClientError as exc:
            status_code = getattr(
                exc,
                "status_code",
                None,
            )

            if status_code == 429:
                raise AIServiceUnavailableError(
                    (
                        "El asistente alcanzó temporalmente "
                        "su límite de solicitudes."
                    ),
                    code="AI_RATE_LIMITED",
                    retryable=True,
                ) from exc

            if status_code in {401, 403}:
                raise AIServiceUnavailableError(
                    "El asistente no está disponible temporalmente.",
                    code="AI_CONFIGURATION_ERROR",
                    retryable=False,
                ) from exc

            raise AIServiceUnavailableError(
                "No fue posible comunicarse con el asistente.",
                code="AI_PROVIDER_ERROR",
                retryable=True,
            ) from exc

        except Exception as exc:
            raise AIServiceUnavailableError(
                "No fue posible comunicarse con el asistente.",
                code="AI_SERVICE_UNAVAILABLE",
                retryable=True,
            ) from exc