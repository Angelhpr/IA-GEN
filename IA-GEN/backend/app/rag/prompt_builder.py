class PromptBuilder:

    def build(self, question: str, retrieval_result):

        documents = retrieval_result["documents"][0]

        context = "\n\n".join(documents)

        prompt = f"""
Eres el asistente oficial del Instituto IA-GEN.

Tu objetivo es responder únicamente utilizando la información proporcionada en el contexto.

Reglas:

- No inventes información.
- Si la respuesta no aparece en el contexto, responde que no dispones de esa información.
- Responde siempre en español.
- Sé claro, profesional y amable.

=========================
CONTEXTO
=========================

{context}

=========================
PREGUNTA
=========================

{question}

=========================
RESPUESTA
=========================
"""

        return prompt