import pytest
from pydantic import ValidationError

from app.rag.prompt_builder import PromptBuilder
from app.schemas.chat import ChatRequest
from app.services.chat_service import ChatService


def test_chat_request_accepts_conversation_history():
    request = ChatRequest(
        message="¿Y cómo lo convierto?",
        history=[
            {
                "role": "user",
                "content": "¿Qué devuelve input()?",
            },
            {
                "role": "assistant",
                "content": "input() devuelve texto.",
            },
        ],
    )

    assert request.message == "¿Y cómo lo convierto?"
    assert len(request.history) == 2
    assert request.history[0].role == "user"
    assert request.history[1].role == "assistant"


def test_chat_request_rejects_more_than_eight_history_messages():
    history = [
        {
            "role": "user",
            "content": f"Mensaje {index}",
        }
        for index in range(9)
    ]

    with pytest.raises(ValidationError):
        ChatRequest(
            message="Pregunta actual",
            history=history,
        )


def test_retrieval_query_uses_last_two_user_messages():
    history = [
        {
            "role": "user",
            "content": "Primera pregunta",
        },
        {
            "role": "assistant",
            "content": "Primera respuesta",
        },
        {
            "role": "user",
            "content": "Segunda pregunta",
        },
        {
            "role": "assistant",
            "content": "Segunda respuesta",
        },
        {
            "role": "user",
            "content": "Tercera pregunta",
        },
    ]

    query = ChatService._build_retrieval_query(
        message="Pregunta actual",
        history=history,
    )

    assert query == (
        "Segunda pregunta\n"
        "Tercera pregunta\n"
        "Pregunta actual"
    )


def test_prompt_includes_history_and_conversational_rules():
    prompt = PromptBuilder().build(
        question="¿Y si necesito un entero?",
        retrieval_result={
            "documents": [
                [
                    "int() convierte texto compatible "
                    "en un número entero."
                ]
            ]
        },
        history=[
            {
                "role": "user",
                "content": "¿Qué devuelve input()?",
            },
            {
                "role": "assistant",
                "content": "input() devuelve texto.",
            },
        ],
    )

    assert "Usuario: ¿Qué devuelve input()?" in prompt
    assert "IA-GEN: input() devuelve texto." in prompt
    assert "¿Y si necesito un entero?" in prompt
    assert "No saludes ni te presentes en cada respuesta." in prompt
    assert "int() convierte texto compatible" in prompt