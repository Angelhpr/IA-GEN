from app.ai.gemini_client import GeminiClient
from app.core.logger import logger
from app.rag.prompt_builder import PromptBuilder
from app.rag.retriever import Retriever


class ChatService:

    def __init__(self):
        self.gemini = GeminiClient()
        self.retriever = Retriever()
        self.prompt_builder = PromptBuilder()

    @staticmethod
    def _build_retrieval_query(
        message: str,
        history: list[dict[str, str]],
    ) -> str:
        previous_user_messages = [
            history_message["content"]
            for history_message in history
            if history_message.get("role") == "user"
            and history_message.get("content")
        ]

        if not previous_user_messages:
            return message

        recent_user_messages = previous_user_messages[-2:]

        return "\n".join([
            *recent_user_messages,
            message,
        ])

    def chat(
        self,
        message: str,
        history: list[dict[str, str]] | None = None,
    ) -> dict:
        conversation_history = history or []

        logger.info(
            "Mensaje recibido: %s",
            message,
        )

        retrieval_query = self._build_retrieval_query(
            message=message,
            history=conversation_history,
        )

        logger.info(
            "Buscando contexto en ChromaDB..."
        )

        results = self.retriever.search(retrieval_query)

        logger.info(
            "Contexto recuperado correctamente"
        )

        logger.info(
            "Construyendo prompt..."
        )

        prompt = self.prompt_builder.build(
            question=message,
            retrieval_result=results,
            history=conversation_history,
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