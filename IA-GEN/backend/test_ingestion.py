from app.rag.ingestion import IngestionPipeline

pipeline = IngestionPipeline()

chunks, embeddings = pipeline.run("data/documentos/bienvenida.txt")

print()
print("========== RESULTADOS ==========")
print()

print("Chunks:", len(chunks))
print("Embeddings:", len(embeddings))

print()
print("Primer chunk:")
print(chunks[0].page_content)

print()
print("Dimensión del embedding:")
print(len(embeddings[0]))