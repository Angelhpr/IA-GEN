from app.ai.gemini_client import GeminiClient
from app.core.logger import logger
from app.rag.retriever import Retriever
from app.rag.prompt_builder import PromptBuilder

class ChatService:

    def __init__(self):
        self.gemini = GeminiClient()
        self.retriever = Retriever()
        self.prompt_builder = PromptBuilder()

    def chat(self, message: str):

        logger.info(f"Mensaje recibido: {message}")

        try:

            logger.info("Buscando contexto en ChromaDB...")
           
            results = self.retriever.search(message)

            logger.info(f"Contexto recuperado correctamente")

            logger.info("Construyendo prompt...")

            prompt = self.prompt_builder.build(
                message,
                results
            )

            logger.info("Enviando prompt a Gemini...")

            response = self.gemini.generate(prompt)

            logger.info("Respuesta generada correctamente")

            return {
                "response": response
            }

        except Exception:

            logger.exception("Error en ChatService")

            raise