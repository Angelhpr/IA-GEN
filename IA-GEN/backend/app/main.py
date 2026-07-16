from fastapi import FastAPI

from app.api.routes import router
from app.core.exceptions import register_exception_handlers

app = FastAPI(
    title="IA-GEN API",
    description="Backend oficial del Instituto IA-GEN",
    version="0.4.0-dev",
    openapi_tags=[
        {
            "name": "General",
            "description": "Endpoints generales del sistema."
        },
        {
            "name": "Chat",
            "description": "Comunicación con el asistente IA."
        },
        {
            "name": "Admin",
            "description": "Administración del sistema."
        }
    ]
)

# Registrar los manejadores de excepciones
register_exception_handlers(app)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "Bienvenido a IA-GEN API"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }