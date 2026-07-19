from app.ai.gemini_client import GeminiClient
from app.core.logger import logger
from app.rag.prompt_builder import PromptBuilder
from app.rag.retriever import Retriever


class ChatService:

    def __init__(self):
        self.gemini = GeminiClient()
        self.retriever = Retriever()
        self.prompt_builder = PromptBuilder()

    def chat(self, message: str) -> dict:

        logger.info(
            "Mensaje recibido: %s",
            message,
        )

        logger.info(
            "Buscando contexto en ChromaDB..."
        )

        results = self.retriever.search(message)

        logger.info(
            "Contexto recuperado correctamente"
        )

        logger.info(
            "Construyendo prompt..."
        )

        prompt = self.prompt_builder.build(
            message,
            results,
        )

        logger.info(
            "Enviando prompt a Gemini..."
        )

        response = self.gemini.generate(prompt)

        logger.info(
            "Respuesta generada correctamente"
        )

        return {
            "response": response,
        }