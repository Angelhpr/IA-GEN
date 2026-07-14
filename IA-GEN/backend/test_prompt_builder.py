from app.rag.retriever import Retriever
from app.rag.prompt_builder import PromptBuilder

retriever = Retriever()

results = retriever.search(
    "¿Qué cursos ofrece IA-GEN?"
)

builder = PromptBuilder()

prompt = builder.build(
    "¿Qué cursos ofrece IA-GEN?",
    results
)

print(prompt)