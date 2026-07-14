from app.rag.loader import Loader
from app.rag.chunker import Chunker

loader = Loader()
chunker = Chunker()

text = loader.load_txt("data/bienvenida.txt")

chunks = chunker.split(text)

for i, chunk in enumerate(chunks, start=1):
    print("=" * 50)
    print(f"CHUNK {i}")
    print("=" * 50)
    print(chunk)