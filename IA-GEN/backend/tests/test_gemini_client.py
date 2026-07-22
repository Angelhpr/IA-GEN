import unittest
from types import SimpleNamespace
from unittest.mock import MagicMock

from google.genai import errors as genai_errors

from app.ai.gemini_client import GeminiClient
from app.core.config import settings
from app.core.exceptions import AIServiceUnavailableError


class GeminiClientTests(unittest.TestCase):

    def setUp(self):
        self.original_model = settings.MODEL_NAME
        self.original_fallback = settings.FALLBACK_MODEL_NAME

        settings.MODEL_NAME = "primary-model"
        settings.FALLBACK_MODEL_NAME = "fallback-model"

        self.client = GeminiClient.__new__(GeminiClient)
        self.client.client = MagicMock()
        self.generate_content = (
            self.client.client.models.generate_content
        )

    def tearDown(self):
        settings.MODEL_NAME = self.original_model
        settings.FALLBACK_MODEL_NAME = self.original_fallback

    @staticmethod
    def server_error(code):
        return genai_errors.ServerError(
            code,
            {"error": {"message": "Server unavailable"}},
        )

    @staticmethod
    def client_error(code):
        return genai_errors.ClientError(
            code,
            {"error": {"message": "Client error"}},
        )

    def test_success_uses_primary_model(self):
        self.generate_content.return_value = SimpleNamespace(
            text="  Primary response  "
        )

        result = self.client.generate("question")

        self.assertEqual(result, "Primary response")
        self.generate_content.assert_called_once_with(
            model="primary-model",
            contents="question",
        )

    def test_transient_errors_use_fallback(self):
        for status_code in (500, 503, 504):
            with self.subTest(status_code=status_code):
                self.generate_content.reset_mock()
                self.generate_content.side_effect = [
                    self.server_error(status_code),
                    SimpleNamespace(text="Fallback response"),
                ]

                result = self.client.generate("question")

                self.assertEqual(result, "Fallback response")
                models = [
                    call.kwargs["model"]
                    for call
                    in self.generate_content.call_args_list
                ]
                self.assertEqual(
                    models,
                    ["primary-model", "fallback-model"],
                )

    def test_rate_limit_does_not_use_fallback(self):
        self.generate_content.side_effect = (
            self.client_error(429)
        )

        with self.assertRaises(
            AIServiceUnavailableError
        ) as raised:
            self.client.generate("question")

        self.assertEqual(
            raised.exception.code,
            "AI_RATE_LIMITED",
        )
        self.assertTrue(raised.exception.retryable)
        self.assertEqual(self.generate_content.call_count, 1)

    def test_auth_errors_do_not_use_fallback(self):
        for status_code in (401, 403):
            with self.subTest(status_code=status_code):
                self.generate_content.reset_mock()
                self.generate_content.side_effect = (
                    self.client_error(status_code)
                )

                with self.assertRaises(
                    AIServiceUnavailableError
                ) as raised:
                    self.client.generate("question")

                self.assertEqual(
                    raised.exception.code,
                    "AI_CONFIGURATION_ERROR",
                )
                self.assertFalse(
                    raised.exception.retryable
                )
                self.assertEqual(
                    self.generate_content.call_count,
                    1,
                )

    def test_both_models_unavailable(self):
        self.generate_content.side_effect = [
            self.server_error(503),
            self.server_error(503),
        ]

        with self.assertRaises(
            AIServiceUnavailableError
        ) as raised:
            self.client.generate("question")

        self.assertEqual(
            raised.exception.code,
            "AI_SERVICE_UNAVAILABLE",
        )
        self.assertTrue(raised.exception.retryable)
        self.assertEqual(self.generate_content.call_count, 2)
        self.assertEqual(
            raised.exception.__cause__.code,
            503,
        )

    def test_empty_response_is_controlled(self):
        self.generate_content.return_value = (
            SimpleNamespace(text="")
        )

        with self.assertRaises(
            AIServiceUnavailableError
        ) as raised:
            self.client.generate("question")

        self.assertEqual(
            raised.exception.code,
            "AI_EMPTY_RESPONSE",
        )
        self.assertTrue(raised.exception.retryable)
        self.assertEqual(self.generate_content.call_count, 1)


if __name__ == "__main__":
    unittest.main()
