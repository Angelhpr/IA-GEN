from app.ai.gemini_client import GeminiClient


class ChatService:

    def __init__(self):

        self.gemini = GeminiClient()

    def chat(self, message: str):

        response = self.gemini.generate(message)

        return {
            "response": response
        }