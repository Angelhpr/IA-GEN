from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router
from app.core.config import settings
from app.core.exceptions import register_exception_handlers


app = FastAPI(
    title=settings.APP_NAME,
    description="Backend oficial del Instituto IA-GEN",
    version=settings.APP_VERSION,
    openapi_tags=[
        {
            "name": "General",
            "description": "Endpoints generales del sistema.",
        },
        {
            "name": "Chat",
            "description": "Comunicación con el asistente IA.",
        },
        {
            "name": "Admin",
            "description": "Administración del sistema.",
        },
    ],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_exception_handlers(app)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "Bienvenido a IA-GEN API",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }
