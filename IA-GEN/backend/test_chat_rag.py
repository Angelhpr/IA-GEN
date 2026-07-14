from app.services.chat_service import ChatService

service = ChatService()

response = service.chat(
    "¿Qué cursos ofrece IA-GEN?"
)

print(response)