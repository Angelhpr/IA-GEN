from app.rag.embedding import EmbeddingGenerator

generator = EmbeddingGenerator()

vector = generator.generate(
    "Bienvenido al Instituto IA-GEN."
)

print(type(vector))
print(len(vector))
print(vector[:10])