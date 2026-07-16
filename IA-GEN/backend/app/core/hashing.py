import hashlib
from pathlib import Path


def calculate_file_hash(file_path: str) -> str:
    """
    Calcula el hash SHA256 del contenido de un archivo.
    """

    path = Path(file_path)

    sha256 = hashlib.sha256()

    with path.open("rb") as file:

        while chunk := file.read(8192):
            sha256.update(chunk)

    return sha256.hexdigest()