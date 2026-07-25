class PromptBuilder:

    @staticmethod
    def _format_history(
        history: list[dict[str, str]],
    ) -> str:
        if not history:
            return "No hay mensajes anteriores."

        formatted_messages = []

        for message in history:
            role = (
                "Usuario"
                if message.get("role") == "user"
                else "IA-GEN"
            )

            content = message.get("content", "").strip()

            if content:
                formatted_messages.append(
                    f"{role}: {content}"
                )

        if not formatted_messages:
            return "No hay mensajes anteriores."

        return "\n\n".join(formatted_messages)

    def build(
        self,
        question: str,
        retrieval_result,
        history: list[dict[str, str]] | None = None,
    ):
        documents = retrieval_result["documents"][0]
        context = "\n\n".join(documents)

        conversation_history = self._format_history(
            history or []
        )

        prompt = f"""
Eres el tutor educativo oficial de IA-GEN.

Tu tarea es responder la pregunta actual utilizando la información académica recuperada y el historial reciente de la conversación.

Reglas obligatorias:

- Responde siempre en español.
- No saludes ni te presentes en cada respuesta.
- No repitas que eres el asistente oficial de IA-GEN.
- No cierres con despedidas automáticas.
- No escribas frases como "según el contexto", "el contexto proporcionado" o "el texto proporcionado".
- Responde directamente a la pregunta.
- Usa el historial para comprender referencias, continuaciones y preguntas incompletas.
- No trates el historial como una fuente académica; úsalo solamente para conservar el hilo de la conversación.
- Basa la explicación académica en la información recuperada.
- Si no existe información suficiente, indícalo de manera natural sin mencionar documentos ni contexto interno.
- Sé claro, educativo y adecuado para estudiantes principiantes.
- Incluye ejemplos cuando estén respaldados por la información disponible.
- Usa Markdown limpio.
- Escribe nombres de funciones, tipos y operadores entre comillas invertidas, por ejemplo: `input()`, `int` y `**`.
- No añadas un saludo al principio ni una despedida al final.

=========================
HISTORIAL RECIENTE
=========================

{conversation_history}

=========================
INFORMACIÓN ACADÉMICA
=========================

{context}

=========================
PREGUNTA ACTUAL
=========================

{question}

=========================
RESPUESTA
=========================
"""

        return prompt