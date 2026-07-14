from app.rag.loader import DocumentLoader

loader = DocumentLoader()

texto = loader.load("data/documentos/bienvenida.txt")

print(texto)