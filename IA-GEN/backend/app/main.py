from fastapi import FastAPI
from app.api.routes import router
from app.core.exceptions import register_exception_handlers

app = FastAPI(
    title="IA-GEN API",
    description="Backend oficial del Instituto IA-GEN",
    version="0.1.0",
)

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