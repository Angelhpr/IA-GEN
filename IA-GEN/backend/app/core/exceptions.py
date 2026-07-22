from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.logger import logger


class AIServiceUnavailableError(RuntimeError):
    """
    Error controlado producido cuando el proveedor de IA
    no puede completar una solicitud.
    """

    def __init__(
        self,
        message: str,
        *,
        code: str = "AI_SERVICE_UNAVAILABLE",
        retryable: bool = True,
    ):
        super().__init__(message)

        self.code = code
        self.retryable = retryable


class IngestionSourceUnavailableError(RuntimeError):
    """
    Error controlado cuando la fuente documental configurada
    no existe o no es un directorio accesible.
    """

    def __init__(
        self,
        message: str = (
            "La fuente documental configurada no esta disponible."
        ),
        *,
        code: str = "INGESTION_SOURCE_UNAVAILABLE",
        retryable: bool = False,
    ):
        super().__init__(message)

        self.code = code
        self.retryable = retryable


def register_exception_handlers(app: FastAPI):
    """Registra los manejadores globales de excepciones de la API."""

    @app.exception_handler(AIServiceUnavailableError)
    async def ai_service_unavailable_handler(
        request: Request,
        exc: AIServiceUnavailableError,
    ):
        provider_error = exc.__cause__
        provider_status = getattr(
            provider_error,
            "code",
            None,
        )

        if provider_status is None:
            provider_status = getattr(
                provider_error,
                "status_code",
                None,
            )

        logger.warning(
            (
                "Servicio de IA no disponible. "
                "code=%s path=%s provider_status=%s"
            ),
            exc.code,
            request.url.path,
            provider_status,
        )

        return JSONResponse(
            status_code=503,
            content={
                "success": False,
                "error": {
                    "code": exc.code,
                    "message": str(exc),
                    "retryable": exc.retryable,
                },
            },
        )

    @app.exception_handler(IngestionSourceUnavailableError)
    async def ingestion_source_unavailable_handler(
        request: Request,
        exc: IngestionSourceUnavailableError,
    ):
        logger.error(
            "Fuente de ingestion no disponible. code=%s path=%s",
            exc.code,
            request.url.path,
        )

        return JSONResponse(
            status_code=503,
            content={
                "success": False,
                "error": {
                    "code": exc.code,
                    "message": str(exc),
                    "retryable": exc.retryable,
                },
            },
        )

    @app.exception_handler(RuntimeError)
    async def runtime_error_handler(
        request: Request,
        exc: RuntimeError,
    ):
        logger.error(
            "RuntimeError no controlado en %s",
            request.url.path,
            exc_info=(
                type(exc),
                exc,
                exc.__traceback__,
            ),
        )

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "error": {
                    "code": "INTERNAL_RUNTIME_ERROR",
                    "message": "Ha ocurrido un error interno.",
                    "retryable": False,
                },
            },
        )

    @app.exception_handler(Exception)
    async def generic_error_handler(
        request: Request,
        exc: Exception,
    ):
        logger.error(
            "Error interno no controlado en %s",
            request.url.path,
            exc_info=(
                type(exc),
                exc,
                exc.__traceback__,
            ),
        )

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "error": {
                    "code": "INTERNAL_SERVER_ERROR",
                    "message": "Ha ocurrido un error interno.",
                    "retryable": False,
                },
            },
        )
