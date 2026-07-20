import unittest

from fastapi import HTTPException
from pydantic import SecretStr

from app.core.config import settings
from app.dependencies.security import require_ingestion_access


class IngestionUnicodeSecurityTests(unittest.TestCase):

    def setUp(self):
        self.original_enabled = settings.INGESTION_ENABLED
        self.original_api_key = settings.INGESTION_API_KEY

    def tearDown(self):
        settings.INGESTION_ENABLED = self.original_enabled
        settings.INGESTION_API_KEY = self.original_api_key

    def test_unicode_secret_is_compared_without_type_error(self):
        settings.INGESTION_ENABLED = True
        settings.INGESTION_API_KEY = SecretStr("clave-á")

        require_ingestion_access("clave-á")

        with self.assertRaises(HTTPException) as raised:
            require_ingestion_access("wrong-key")

        self.assertEqual(raised.exception.status_code, 403)
        self.assertEqual(
            raised.exception.detail,
            "Acceso denegado.",
        )


if __name__ == "__main__":
    unittest.main()
