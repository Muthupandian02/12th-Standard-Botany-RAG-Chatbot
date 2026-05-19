from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from typing import List
from src.data_loader import doc_loader,doc_filter

class ChunkingPipeine:
    def __init__(self,chunk_size: int=1000, chunk_overlap: int =100):
        self.chunk_size=chunk_size
        self.chunk_overlap=chunk_overlap

    def chunk_doc(self, document: List[Document]) -> List[Document]:
        try:
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=self.chunk_size,
                chunk_overlap=self.chunk_overlap,
                separators=["\n\n", "\n", " ", ""]
            )

            chunks = splitter.split_documents(document)
            return chunks
        except:
            pass

    def embedding_doc(self):
        model=HuggingFaceEmbeddings(model_name='jinaai/jina-embeddings-v2-small-en')
        return model
    
