# Tamil Nadu 12th Standard Botany RAG Chatbot

## Overview

This project is a **Retrieval-Augmented Generation (RAG)** based academic chatbot built using **LangChain, Pinecone, Groq LLM, and Streamlit**.

The chatbot is trained on the **Tamil Nadu State Board 12th Standard Botany textbook** and is designed to help students ask questions in natural language and receive context-aware answers directly from the textbook content.

The system retrieves relevant textbook passages using vector similarity search and generates accurate educational responses using a Large Language Model (LLM).

link :- https://12th-standard-botany-rag-chatbot-iggthk8zidgcbwcxphesrj.streamlit.app/#answer

# Features

* Ask questions from 12th Standard Botany syllabus
* Context-aware answers from textbook content
* Vector search using Pinecone
* Fast inference using Groq LLM
* Streamlit web interface
* RAG (Retrieval-Augmented Generation) pipeline
* Semantic search using embeddings
* Educational response formatting


# Tech Stack

* **Python**
* **Streamlit**
* **LangChain**
* **Pinecone Vector Database**
* **Groq API**
* **HuggingFace Embeddings**
* **PDF Text Extraction**


# Project Structure

```text
medibot/
│
├── app.py
├── requirements.txt
├── .env
│
├── data/
│   └── botany_textbooks.pdf
│
├── src/
│   ├── data_loader.py
│   ├── embedding.py
│   ├── vector_store.py
│   └── retriever.py
│
└── README.md
```


# How RAG Works in This Project

## Step 1 — Load Textbook Data

The textbook PDFs are loaded and converted into text documents.

```text
PDF Textbook
      ↓
Document Loader
```


## Step 2 — Document Cleaning & Filtering

The extracted text is cleaned and filtered to remove unwanted content.

```text
Raw Text
    ↓
Cleaned Documents
```


## Step 3 — Text Chunking

Large textbook content is divided into smaller chunks for efficient retrieval.

```text
Large Text
     ↓
Small Chunks
```


## Step 4 — Create Embeddings

Each chunk is converted into numerical vector embeddings using embedding models.

```text
Text Chunks
      ↓
Embeddings
```


## Step 5 — Store in Pinecone Vector Database

The embeddings are stored in Pinecone for semantic similarity search.

```text
Embeddings
     ↓
Pinecone Vector DB
```


## Step 6 — Student Asks a Question

The student enters a query through the Streamlit interface.

Example:

```text
"What is double fertilization?"
```


## Step 7 — Semantic Retrieval

The query is converted into embeddings and matched against the most relevant textbook chunks.

```text
Student Query
      ↓
Vector Search
      ↓
Relevant Textbook Context
```


## Step 8 — LLM Generates Answer

The retrieved context is passed to the Groq LLM which generates a final answer.

```text
Retrieved Context
        +
Student Question
        ↓
Groq LLM
        ↓
Final Answer
```


# RAG Pipeline Flow

```text
Student Question
        ↓
Embedding Model
        ↓
Pinecone Similarity Search
        ↓
Relevant Textbook Chunks
        ↓
Groq LLM
        ↓
Generated Educational Answer
```

# Installation

## Clone Repository

```bash
git clone https://github.com/your-username/botany-rag-chatbot.git
cd botany-rag-chatbot
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
PINECONE_API_KEY=your_pinecone_api_key
GROQ_API_KEY=your_groq_api_key
```

---

# Run the Project

```bash
streamlit run app.py
```

# Example Questions

* What is photosynthesis?
* Explain double fertilization.
* What are plant hormones?
* Define transpiration.
* Explain Mendelian inheritance.
* What is glycolysis?

# Educational Objective

The purpose of this project is to help students:

* Learn Botany interactively
* Understand textbook concepts easily
* Ask doubts in natural language
* Improve conceptual understanding
* Access textbook knowledge instantly

# Future Improvements

* Multi-language support (Tamil + English)
* Voice-based interaction
* Chapter-wise filtering
* Image-based diagram explanation
* Quiz generation
* Memory-enabled conversations
* Teacher analytics dashboard
