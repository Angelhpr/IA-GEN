from app.rag.retriever import Retriever

retriever = Retriever()

results = retriever.search(
    "¿Qué cursos ofrece IA-GEN?"
)

print("\n===== RESULTADOS =====\n")

print(results)