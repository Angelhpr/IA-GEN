from app.ai.gemini_client import GeminiClient
from app.core.logger import logger


class ChatService:

    def __init__(self):
        self.gemini = GeminiClient()

    def chat(self, message: str):

        logger.info(f"Mensaje recibido: {message}")

        try:

            response = self.gemini.generate(message)

            logger.info("Respuesta generada correctamente")

            return {
                "response": response
            }

        except Exception:

            logger.exception("Error en ChatService")

            raise