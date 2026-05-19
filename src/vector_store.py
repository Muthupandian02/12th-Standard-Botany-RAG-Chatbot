import pinecone
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os
from langchain_core.documents import Document
from typing import List

load_dotenv(override=True)


PINECONE_API_KEY=os.getenv('PINECONE_API_KEY')
GROQ_API_KEY=os.getenv('GROQ_API_KEY')

pinecone_api_key=PINECONE_API_KEY
pc=Pinecone(api_key=pinecone_api_key.strip())

class VectorStore:
    def __init__(self, index_name: str='studentbot', dimension: int=512):
        self.index_name=index_name
        self.dimension=dimension

    def pinecone_db(self, chunk, embedding):

        if not pc.has_index(self.index_name):

            pc.create_index(
                name=self.index_name,
                dimension=self.dimension,
                metric='cosine',
                spec=ServerlessSpec(
                    cloud='aws',
                    region='us-east-1'
                )
            )

            doc_search = PineconeVectorStore.from_documents(
                documents=chunk,
                embedding=embedding,
                index_name=self.index_name
            )

        else:

            doc_search = PineconeVectorStore.from_existing_index(
                embedding=embedding,
                index_name=self.index_name
            )

        return doc_search