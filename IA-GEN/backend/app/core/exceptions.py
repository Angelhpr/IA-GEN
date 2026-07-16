from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


from app.core.logger import logger


def register_exception_handlers(app: FastAPI):
    """Registra los manejadores globales de excepciones de la API."""

    @app.exception_handler(RuntimeError)
    async def runtime_error_handler(
        request: Request,
        exc: RuntimeError
    ):

        logger.error(
            f"RuntimeError: {exc}"
        )

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "detail": str(exc)
            }
        )

    @app.exception_handler(Exception)
    async def generic_error_handler(
        request: Request,
        exc: Exception
    ):

        logger.exception(
            "Error interno no controlado."
        )

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "detail": "Ha ocurrido un error interno."
            }
        )