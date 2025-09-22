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

### 1. Clone the Repository
- Download the project to your local machine using Git.
```bash
git clone https://github.com/username/Medical-Chat-Bot.git

cd Medical-Chat-Bot
```

---

### 2. Set Up a Virtual Environment
- Create and activate a Python virtual environment to manage dependencies.
```
python -m venv env #Create Environment

source env\Scripts\activate   #Activate Environment
```
 
---

### 3. Install Required Packages
- Install all necessary Python packages listed in `requirements.txt` to ensure the project runs smoothly.
```
 pip install --upgrade pip
 pip install -r requirements.txt
```
---

### 4. Configure Environment Variables
- Create a `.env` file in the project root.
- Add your API keys for Pinecone, Groq, and any other services the project uses.
```
  
PINECONE_API_KEY=*****
PINECONE_INDEX_NAME=****
GROQ_API_KEY=****
```
---

### 5. Verify Installation
- Make sure all dependencies are installed correctly.
- Check that the environment variables are accessible from your Python scripts.

---
## Usage

### 1. Prepare Your Documents
- Split your documents into smaller chunks to make embedding generation more efficient.

---

### 2. Initialize Embeddings
- Set up a text embedding model to convert document chunks into vector representations.

---

### 3. Connect to Pinecone
- Initialize the Pinecone client using your API key and environment.
- Connect to the existing index or create a new one for storing vectors.

---

### 4. Store Embeddings in Pinecone
- Add the vectorized document chunks to the Pinecone index for fast similarity search.

---

### 5. Ask Questions with the LLM
- Initialize the Groq LLM or another language model.
- Set up a retrieval-based question-answering system that queries the Pinecone index.
- Input your question to get answers along with optional source documents.



