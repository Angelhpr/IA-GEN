from fastapi import FastAPI

from app.api.routes import router
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    description="Backend oficial del Instituto IA-GEN",
    version="1.0.0"
)

app.include_router(router)