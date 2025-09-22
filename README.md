# Medical Chat Bot

A conversational AI assistant designed to answer medical-related queries. This project leverages **vector embeddings**, **retrieval-augmented generation (RAG)**, and **large language models** (LLMs) to provide accurate, context-aware responses from medical documents.

---

## Features

- **Document ingestion**: Load PDFs, text, and other medical documents.
- **Vector embeddings**: Convert text chunks into vectors for semantic search.
- **Semantic search**: Quickly find relevant information from your document database.
- **Conversational AI**: Ask questions naturally, get context-aware answers.
- **Supports multiple backends**: 
  - Pinecone for vector database
  - Groq LLM (or HuggingFace embeddings)

---

## Tech Stack

- **Python 3.11+**
- **LangChain**: For LLM and RAG integration
- **Pinecone**: Vector database for semantic search
- **Groq / HuggingFace**: Embeddings and LLM inference
- **PDF/Text loaders**: For document processing
- **Jupyter Notebook**: Interactive experimentation
- **Flask**: Optional API for serving the chatbot

---

## Installation

1. Clone the repository:

```bash
git clone 
cd Medical-Chat-Bot

```


2. Create a virtual environment and activate it:

```bash
   python -m venv env
   source env\Scripts\activate         

```bash
   pip install -r requirements.txt

```
3. Create a .env file for your API keys:
   GROQ_API_KEY
   PINECONE_API_KEY
   PINECONE_INDEX_NAME



