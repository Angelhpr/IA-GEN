from fastapi import FastAPI
from fastapi.responses import JSONResponse


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(RuntimeError)
    async def runtime_error_handler(request, exc):

        return JSONResponse(
            status_code=500,
            content={
                "detail": str(exc)
            }
        )

    @app.exception_handler(Exception)
    async def generic_error_handler(request, exc):

        return JSONResponse(
            status_code=500,
            content={
                "detail": "Ha ocurrido un error interno."
            }
        )