import asyncio
from pathlib import Path

from app.core.config import settings
from app.main import app, lifespan


def run_lifespan() -> None:
    async def execute() -> None:
        async with lifespan(app):
            pass

    asyncio.run(execute())


def test_startup_ingests_documents_when_enabled(
    monkeypatch,
):
    calls: dict[str, object] = {}

    class FakeIngestionService:
        def __init__(self, source_path: Path):
            calls["source_path"] = source_path

        def ingest_configured_source(self) -> None:
            calls["ingested"] = True

    monkeypatch.setattr(
        settings,
        "AUTO_INGEST_ON_STARTUP",
        True,
    )
    monkeypatch.setattr(
        "app.main.IngestionService",
        FakeIngestionService,
    )

    run_lifespan()

    assert calls["source_path"] == (
        settings.resolved_ingestion_source_path
    )
    assert calls["ingested"] is True


def test_startup_skips_ingestion_when_disabled(
    monkeypatch,
):
    def unexpected_ingestion_service(*args, **kwargs):
        raise AssertionError(
            "IngestionService no debe inicializarse."
        )

    monkeypatch.setattr(
        settings,
        "AUTO_INGEST_ON_STARTUP",
        False,
    )
    monkeypatch.setattr(
        "app.main.IngestionService",
        unexpected_ingestion_service,
    )

    run_lifespan()
