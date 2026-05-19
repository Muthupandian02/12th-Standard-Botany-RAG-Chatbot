import streamlit as st
import os
from src.data_loader import doc_loader,doc_filter
from src.embedding import ChunkingPipeine

from src.vector_store import VectorStore
from src.retriever import RagPipeline

st.set_page_config(page_title="Academic QA", layout="centered")
st.title("STUDENT'S BOT")

query = st.text_input("Ask a question:")

col1, col2 = st.columns([1,1])
with col1:
    if st.button("Process"):
        st.write("Processing your file...")

if query:
    chunker=ChunkingPipeine()
    vector_store=VectorStore()
    rag=RagPipeline()

    document=doc_loader('./data')
    new_doc=doc_filter(document)
    chunks=chunker.chunk_doc(new_doc)
    embeddings=chunker.embedding_doc()
    vector = vector_store.pinecone_db(chunks, embeddings)

    retriever = vector.as_retriever(
        search_type='mmr',
        search_kwargs={'k': 5}
    )

    rag_chain = rag.retriver(retriever)
    response=rag_chain.invoke({'input': query})
    
    st.write("### Answer")
    st.write(response['answer'])
