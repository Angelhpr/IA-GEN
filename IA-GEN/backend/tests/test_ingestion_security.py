import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

from fastapi.testclient import TestClient
from pydantic import SecretStr

from app.core.config import settings
from app.core.exceptions import IngestionSourceUnavailableError
from app.main import app
from app.services.ingestion_service import IngestionService


class IngestionSecurityTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

    @classmethod
    def tearDownClass(cls):
        cls.client.close()

    def setUp(self):
        self.original_enabled = settings.INGESTION_ENABLED
        self.original_api_key = settings.INGESTION_API_KEY
        app.dependency_overrides.clear()

    def tearDown(self):
        settings.INGESTION_ENABLED = self.original_enabled
        settings.INGESTION_API_KEY = self.original_api_key
        app.dependency_overrides.clear()

    def test_disabled_endpoint_returns_404(self):
        settings.INGESTION_ENABLED = False
        settings.INGESTION_API_KEY = SecretStr(
            "test-ingestion-key"
        )

        with patch(
            "app.dependencies.services.get_ingestion_service"
        ) as get_service:
            response = self.client.post("/api/ingest")

        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            response.json(),
            {"detail": "Recurso no encontrado."},
        )
        get_service.assert_not_called()

    def test_enabled_without_configured_key_returns_503(self):
        settings.INGESTION_ENABLED = True
        settings.INGESTION_API_KEY = None

        with patch(
            "app.dependencies.services.get_ingestion_service"
        ) as get_service:
            response = self.client.post("/api/ingest")

        self.assertEqual(response.status_code, 503)
        self.assertEqual(
            response.json(),
            {
                "detail": (
                    "Servicio de ingestion no disponible."
                )
            },
        )
        get_service.assert_not_called()

    def test_empty_configured_key_returns_503(self):
        settings.INGESTION_ENABLED = True
        settings.INGESTION_API_KEY = SecretStr("")

        with patch(
            "app.dependencies.services.get_ingestion_service"
        ) as get_service:
            response = self.client.post("/api/ingest")

        self.assertEqual(response.status_code, 503)
        get_service.assert_not_called()

    def test_missing_or_invalid_key_returns_403(self):
        settings.INGESTION_ENABLED = True
        settings.INGESTION_API_KEY = SecretStr(
            "correct-test-key"
        )

        requests = (
            {},
            {
                "headers": {
                    "X-Ingestion-API-Key": "wrong-test-key",
                }
            },
        )

        for request_kwargs in requests:
            with self.subTest(request_kwargs=request_kwargs):
                with patch(
                    (
                        "app.dependencies.services."
                        "get_ingestion_service"
                    )
                ) as get_service:
                    response = self.client.post(
                        "/api/ingest",
                        **request_kwargs,
                    )

                self.assertEqual(response.status_code, 403)
                self.assertEqual(
                    response.json(),
                    {"detail": "Acceso denegado."},
                )
                get_service.assert_not_called()

    def test_valid_key_executes_configured_ingestion(self):
        settings.INGESTION_ENABLED = True
        settings.INGESTION_API_KEY = SecretStr(
            "correct-test-key"
        )

        fake_service = MagicMock()

        with patch(
            "app.dependencies.services.get_ingestion_service",
            return_value=fake_service,
        ) as get_service:
            response = self.client.post(
                "/api/ingest",
                headers={
                    "X-Ingestion-API-Key": (
                        "correct-test-key"
                    ),
                },
                json={
                    "folder": "C:/una/ruta/no-autorizada",
                },
            )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "success": True,
                "message": (
                    "Documentos indexados correctamente."
                ),
            },
        )
        get_service.assert_called_once_with()
        fake_service.ingest_configured_source.assert_called_once_with()

    def test_missing_source_raises_controlled_error(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            service = IngestionService.__new__(
                IngestionService
            )
            service.source_path = (
                Path(temp_dir) / "missing-source"
            )

            with self.assertRaises(
                IngestionSourceUnavailableError
            ):
                service.ingest_configured_source()

    def test_source_error_returns_controlled_503(self):
        settings.INGESTION_ENABLED = True
        settings.INGESTION_API_KEY = SecretStr(
            "correct-test-key"
        )

        fake_service = MagicMock()
        fake_service.ingest_configured_source.side_effect = (
            IngestionSourceUnavailableError()
        )

        with patch(
            "app.dependencies.services.get_ingestion_service",
            return_value=fake_service,
        ):
            response = self.client.post(
                "/api/ingest",
                headers={
                    "X-Ingestion-API-Key": (
                        "correct-test-key"
                    ),
                },
            )

        self.assertEqual(response.status_code, 503)
        self.assertEqual(
            response.json(),
            {
                "success": False,
                "error": {
                    "code": (
                        "INGESTION_SOURCE_UNAVAILABLE"
                    ),
                    "message": (
                        "La fuente documental configurada "
                        "no esta disponible."
                    ),
                    "retryable": False,
                },
            },
        )


if __name__ == "__main__":
    unittest.main()