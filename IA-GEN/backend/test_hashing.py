from app.core.hashing import calculate_file_hash

hash_value = calculate_file_hash(
    "data/documentos/bienvenida.txt"
)

print(hash_value)