from typing import NoReturn

from google import genai
from google.genai import errors as genai_errors

from app.core.config import settings
from app.core.exceptions import AIServiceUnavailableError
from app.core.logger import logger


TRANSIENT_SERVER_STATUS_CODES = {
    500,
    503,
    504,
}


class GeminiClient:

    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    @staticmethod
    def _provider_status(
        exc: genai_errors.APIError,
    ) -> int | None:
        status_code = getattr(
            exc,
            "code",
            None,
        )

        if status_code is not None:
            return status_code

        return getattr(
            exc,
            "status_code",
            None,
        )

    @staticmethod
    def _fallback_model() -> str | None:
        fallback_model = (
            settings.FALLBACK_MODEL_NAME or ""
        ).strip()

        if (
            not fallback_model
            or fallback_model == settings.MODEL_NAME
        ):
            return None

        return fallback_model

    def _generate_with_model(
        self,
        prompt: str,
        model_name: str,
    ) -> str:
        logger.info(
            "Generando respuesta con %s",
            model_name,
        )

        response = self.client.models.generate_content(
            model=model_name,
            contents=prompt,
        )

        if not response.text:
            raise AIServiceUnavailableError(
                (
                    "El asistente no generó una "
                    "respuesta válida."
                ),
                code="AI_EMPTY_RESPONSE",
                retryable=True,
            )

        return response.text.strip()

    def _raise_provider_error(
        self,
        exc: genai_errors.APIError,
    ) -> NoReturn:
        status_code = self._provider_status(exc)

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
                (
                    "El asistente no está disponible "
                    "temporalmente."
                ),
                code="AI_CONFIGURATION_ERROR",
                retryable=False,
            ) from exc

        if status_code in TRANSIENT_SERVER_STATUS_CODES:
            raise AIServiceUnavailableError(
                (
                    "El servicio de IA no está "
                    "disponible temporalmente."
                ),
                code="AI_SERVICE_UNAVAILABLE",
                retryable=True,
            ) from exc

        raise AIServiceUnavailableError(
            (
                "No fue posible comunicarse con "
                "el asistente."
            ),
            code="AI_PROVIDER_ERROR",
            retryable=True,
        ) from exc

    def generate(self, prompt: str) -> str:
        try:
            return self._generate_with_model(
                prompt,
                settings.MODEL_NAME,
            )

        except AIServiceUnavailableError:
            raise

        except genai_errors.APIError as exc:
            status_code = self._provider_status(exc)
            fallback_model = self._fallback_model()

            if (
                status_code
                in TRANSIENT_SERVER_STATUS_CODES
                and fallback_model
            ):
                logger.warning(
                    (
                        "Modelo principal no disponible. "
                        "status=%s fallback=%s"
                    ),
                    status_code,
                    fallback_model,
                )

                try:
                    return self._generate_with_model(
                        prompt,
                        fallback_model,
                    )

                except AIServiceUnavailableError:
                    raise

                except genai_errors.APIError as fallback_exc:
                    self._raise_provider_error(
                        fallback_exc
                    )

                except Exception as fallback_exc:
                    raise AIServiceUnavailableError(
                        (
                            "No fue posible comunicarse "
                            "con el asistente."
                        ),
                        code="AI_SERVICE_UNAVAILABLE",
                        retryable=True,
                    ) from fallback_exc

            self._raise_provider_error(exc)

        except Exception as exc:
            raise AIServiceUnavailableError(
                (
                    "No fue posible comunicarse "
                    "con el asistente."
                ),
                code="AI_SERVICE_UNAVAILABLE",
                retryable=True,
            ) from exc
