from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest

from app.rag.embedding import EmbeddingGenerator


def embedding_response(
    vectors: list[list[float]],
):
    return SimpleNamespace(
        embeddings=[
            SimpleNamespace(values=vector)
            for vector in vectors
        ]
    )


def create_generator():
    generator = EmbeddingGenerator.__new__(
        EmbeddingGenerator
    )
    generator.client = MagicMock()

    return generator


def test_generate_batch_preserves_order():
    generator = create_generator()

    generator.client.models.embed_content.side_effect = [
        embedding_response(
            [
                [1.0, 1.1],
                [2.0, 2.1],
            ]
        ),
        embedding_response(
            [
                [3.0, 3.1],
            ]
        ),
    ]

    result = generator.generate_batch(
        ["primero", "segundo", "tercero"],
        batch_size=2,
    )

    assert result == [
        [1.0, 1.1],
        [2.0, 2.1],
        [3.0, 3.1],
    ]

    calls = (
        generator.client.models.embed_content
        .call_args_list
    )

    assert len(calls) == 2

    assert calls[0].kwargs["model"] == (
        "models/gemini-embedding-2"
    )
    assert calls[1].kwargs["model"] == (
        "models/gemini-embedding-2"
    )

    first_batch = calls[0].kwargs["contents"]
    second_batch = calls[1].kwargs["contents"]

    assert [
        content.parts[0].text
        for content in first_batch
    ] == [
        "primero",
        "segundo",
    ]

    assert [
        content.parts[0].text
        for content in second_batch
    ] == [
        "tercero",
    ]

    assert all(
        content.role == "user"
        for content in first_batch + second_batch
    )


def test_generate_batch_skips_empty_input():
    generator = create_generator()

    result = generator.generate_batch([])

    assert result == []
    generator.client.models.embed_content.assert_not_called()


def test_generate_batch_rejects_invalid_size():
    generator = create_generator()

    with pytest.raises(
        ValueError,
        match="mayor que cero",
    ):
        generator.generate_batch(
            ["contenido"],
            batch_size=0,
        )


def test_generate_batch_validates_response_count():
    generator = create_generator()

    generator.client.models.embed_content.return_value = (
        embedding_response([[1.0]])
    )

    with pytest.raises(
        ValueError,
        match="cantidad inesperada",
    ):
        generator.generate_batch(
            ["primero", "segundo"],
        )