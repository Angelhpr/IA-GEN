from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
)


class DocumentChunker:

    def __init__(
        self,
        chunk_size: int = 500,
        chunk_overlap: int = 100,
    ):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

    def split(self, document):

        chunks = self.splitter.split_documents(
            [document]
        )

        for index, chunk in enumerate(chunks):
            chunk.metadata = {
                **chunk.metadata,
                "chunk_index": index,
            }

        return chunks