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


def register_exception_handlers(app: FastAPI):
    """Registra los manejadores globales de excepciones de la API."""

    @app.exception_handler(AIServiceUnavailableError)
    async def ai_service_unavailable_handler(
        request: Request,
        exc: AIServiceUnavailableError,
    ):
        provider_status = getattr(
            exc.__cause__,
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